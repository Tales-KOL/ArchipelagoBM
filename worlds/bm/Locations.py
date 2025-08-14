from BaseClasses import Location

class BMLocation(Location):  # or from Locations import MyGameLocation
    game = "Blaster Master"  # name of the game/world this location is in

area1list:list[str] = ["Hyper Beam Pickup", "Mother Brain Defeated", "Underwater Room Pickup", "Underwater H-Missile #1", "Underwater H-Missile #2"]
area1hoverloc:list[str] = ["Cliff Hover-4 #1", "Cliff Hover-4 #2", "Cliff Hover-4 #3"]
area2list:list[str] = ["Crusher Beam Pickup", "Northwest Room Item #1", "Northwest Room Item #2", "Northwest Room Item #3"]
area2boss:list[str] = ["Crabullus Defeated", "Area2Boss Pickup #1", "Area2Boss Pickup #2", "Area2Boss Pickup #3", "Area2Boss Pickup #4", "Area2Boss Pickup #5", "Area2Boss Pickup #6", "Area2Boss Pickup #7" ]
area2pathto7:list[str] = ["Area2-7 H-Missile #1", "Area2-7 H-Missile #2", "Area2-7 Power-4", "Area2-7 Thunder Break"]
area3list:list[str] = ["Hover Upgrade Pickup", "Photophage Defeated"]
area4list:list[str] = ["Key Pickup", "Fred Defeated"]
# area4boss:list[str] = ["Key Pickup", "Fred Defeated"]
area5list:list[str] = ["Dive Engine Pickup", "Hard Shell Defeated"]
area6list:list[str] = ["Wall 1 Pickup", "Frozen Crabullus Defeated"]
area7list:list[str] = ["Wall 2 Pickup", "Solar-Enhanced Fred Defeated"]
area8list:list[str] = ["Plutonium Boss Defeated", "Underworld Lord Defeated"]


as_dict :dict[str, int] = {name: id+1 for id, name in enumerate([*area1list, *area1hoverloc, *area2list, *area2boss, *area3list, *area4list, *area5list, *area6list, *area7list, *area8list])}



