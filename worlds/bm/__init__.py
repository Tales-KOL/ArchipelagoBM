# world/mygame/__init__.py

import settings, typing, random
from BaseClasses import ItemClassification, Tutorial, MultiWorld
from .Options import BMOptions  # the options we defined earlier
from .Items import itemnametoid, BMItem, is_progression, listA, listB  # data used below to add items to the World
from .Locations import BMLocation, as_dict  # same as above
from .Regions import create_regions
from . import Regions
from worlds.AutoWorld import World, WebWorld


class BMWeb(WebWorld):
    # There's a few different themes so have fun with it
    theme = "Party"
    # You shouldn't have to change much here except the name at the bottom!
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up (the game you are randomizing) for Archipelago. "
        "This guide covers single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Koldes"]
    )]


class BMSettings(settings.Group):
    class RomFile(settings.SNESRomPath):
        """Insert help text for host.yaml here."""

    rom_file: RomFile = RomFile("Blaster Master.nes")


class BMWorld(World):
    """Insert description of the world/game here."""
    game = "Blaster Master"  # name of the game/world
    options_dataclass = BMOptions  # options the player can set
    options: BMOptions  # typing hints for option results
    settings: typing.ClassVar[BMSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    # ID of first item and location, could be hard-coded but code may be easier
    # to read with this as a property.
    # instead of dynamic numbering, IDs could be part of data

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = itemnametoid
    location_name_to_id = as_dict

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    #item_name_groups = {
    #    "upgrades": {"beams", "movement"},
    #}
    def __init__(self, multiworld: MultiWorld, player: int):
        self.itempool = []
        super().__init__(multiworld, player)


    def create_item(self, item: str) -> BMItem:
        # this is called when AP wants to create an item by name (for plando, start inventory, item links) or when you call it from your own code
        classification = ItemClassification.progression if is_progression(item) else ItemClassification.filler
        return BMItem(item, classification, self.item_name_to_id[item], self.player)

    def create_items(self) -> None:
        # Add items to the Multiworld.
        # If there are two of the same item, the item has to be twice in the pool.
        # Which items are added to the pool may depend on player options, e.g. custom win condition like triforce hunt.
        # Having an item in the start inventory won't remove it from the pool.
        # If you want to do that, use start_inventory_from_pool

        for item in map(self.create_item, [x for x in listA if x != "Victory" and x != "Boss Medal"]):
            self.itempool.append(item)
        self.multiworld.itempool.extend(self.itempool)

        # itempool and number of locations should match up.
        # If this is not the case we want to fill the itempool with junk.
        junk = len(self.multiworld.get_unfilled_locations(self.player)) - len(self.itempool) # calculate this based on player options
        self.multiworld.itempool += [self.create_item(random.choice(listB)) for _ in range(junk)]
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def create_regions(self):
        create_regions(self)
        from Utils import visualize_regions
        visualize_regions(self.multiworld.get_region("Menu", self.player), "_region_diagram.puml")