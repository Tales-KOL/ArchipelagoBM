from typing import TYPE_CHECKING

from BaseClasses import Region, Location
from .Locations import as_dict, area1list, area1hoverloc, area2list, area2boss, area3list, area4list, area5list, area6list, area7list, area8list
from .Items import listA
from . import BMLocation
from .Rules import *

if TYPE_CHECKING:
    from . import BMWorld

def create_regions(self) -> None:
    # Add regions to the multiworld. One of them must use the origin_region_name as its name ("Menu" by default).
    # Arguments to Region() are name, player, multiworld, and optionally hint_text
    menu_region = Region("Menu", self.player, self.multiworld)

    # add main area's locations to main area (all but final boss)
    # or
    # main_region.locations = \
    #   [MyGameLocation(self.player, location_name, self.location_name_to_id[location_name], main_region]
    area1_region = Region("Area 1", self.player, self.multiworld)
    area1_hover = Region("Area 1 Hover Cliffs", self.player, self.multiworld)
    area2_region = Region("Area 2", self.player, self.multiworld)
    area2_boss = Region("Area 2 Boss Room", self.player, self.multiworld)
    area2_boss = Region("Area 2 Boss Room", self.player, self.multiworld)
    area3_region = Region("Area 3", self.player, self.multiworld)
    area4_region = Region("Area 4", self.player, self.multiworld)
    # area4_boss = Region("Area 4 Boss", self.player, self.multiworld)
    area5_region = Region("Area 5", self.player, self.multiworld)
    area6_region = Region("Area 6", self.player, self.multiworld)
    area7_region = Region("Area 7", self.player, self.multiworld)
    area8_region = Region("Area 8", self.player, self.multiworld)

    area1_region.add_locations({name : lid for name, lid in as_dict.items() if name in area1list}, BMLocation)
    area1_hover.add_locations({name : lid for name, lid in as_dict.items() if name in area1hoverloc}, BMLocation)
    area2_region.add_locations({name : lid for name, lid in as_dict.items() if name in area2list}, BMLocation)
    area2_boss.add_locations({name : lid for name, lid in as_dict.items() if name in area2boss}, BMLocation)
    area3_region.add_locations({name : lid for name, lid in as_dict.items() if name in area3list}, BMLocation)
    area4_region.add_locations({name : lid for name, lid in as_dict.items() if name in area4list}, BMLocation)
    # area4_boss.add_locations({name : lid for name, lid in as_dict.items() if name in area4boss}, BMLocation)
    area5_region.add_locations({name : lid for name, lid in as_dict.items() if name in area5list}, BMLocation)
    area6_region.add_locations({name : lid for name, lid in as_dict.items() if name in area6list}, BMLocation)
    area7_region.add_locations({name : lid for name, lid in as_dict.items() if name in area7list}, BMLocation)
    area8_region.add_locations({name : lid for name, lid in as_dict.items() if name in area8list}, BMLocation)
    # add event to Boss Room
    # boss_region.locations.append(BMLocation(self.player, "Final Boss", None, boss_region))

    # if entrances are not randomized, they should be connected here, otherwise they can also be connected at a later stage
    # create Entrances and connect the Regions
    menu_region.connect(area1_region)

    area1_region.connect(area2_region, rule=lambda state : can_hyper(state, self.player))
    area1_region.connect(area1_hover, rule=lambda state : can_hover(state, self.player))
    area1_hover.connect(area4_region, rule=lambda state : can_hover(state, self.player or (can_wall1 and can_wall2)))
    area1_hover.connect(area1_region)

    area2_region.connect(area1_region, rule=lambda state : can_crusher(state, self.player))
    area2_region.connect(area2_boss)
    area2_boss.connect(area2_region)

    area2_region.connect(area3_region, rule=lambda state : can_crusher(state, self.player))
    area2_region.connect(area7_region, rule=lambda state : can_wall1(state, self.player))

    area3_region.connect(area2_region, rule=lambda state : can_crusher(state, self.player))
    area3_region.connect(area8_region, rule=lambda state : can_wall1(state, self.player) and can_wall2(state, self.player) and can_crusher(state, self.player) and can_hover(state, self.player))

    area4_region.connect(area1_hover)
    area4_region.connect(area5_region, rule=lambda state : can_key(state, self.player))

    area5_region.connect(area4_region, rule=lambda state : can_key(state, self.player))
    area5_region.connect(area6_region, rule=lambda state : can_dive(state, self.player))

    area6_region.connect(area5_region, rule=lambda state : can_dive(state, self.player))

    area7_region.connect(area2_region)

    area8_region.connect(area3_region, rule=lambda state : can_wall1(state, self.player) and can_wall2(state, self.player))
    # connects the "Menu" and "Main Area", can also pass a rule
    #Item Placement
    self.multiworld.get_location("Hyper Beam Pickup", self.player).place_locked_item(self.create_item("Hyper Beam"))
    #print(self.multiworld.get_location("Hyper Beam Pickup", self.player).item.code)
    # or
    # main_region.add_exits({"Area 3": "Boss Door"}, {"Area 3": lambda state: state.has("Hyper Beam", self.player)})
    # connects the "Area 1" and "Area 3" regions, and places a rule requiring the "Hyper Beam" item to traverse
    # if setting location access rules from data is easier here, set_rules can possibly be omitted
    self.multiworld.regions.extend([menu_region, area1_region, area8_region])
