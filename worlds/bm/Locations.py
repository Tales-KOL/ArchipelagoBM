from BaseClasses import Location

class BMLocation(Location):  # or from Locations import MyGameLocation
    game = "Blaster Master"  # name of the game/world this location is in

area1list:list[str] = ["Area 1 Hyper Beam Upgrade", "Mother Brain (Boss 1) Defeated", "Area 1 (Underwater Room) - Power Pickup", "Area 1 (Underwater Bottom Right) - H-Missile Pickup #1", "Area 1 (Underwater Bottom Right) - H-Missile Pickup #2"]
area1hoverloc:list[str] = ["Area 1 (Hover Cliffs) - Hover4 Pickup #1", "Area 1 (Hover Cliffs) - Hover4 Pickup #2", "Area 1 (Hover Cliffs) - Hover4 Pickup #3"]
area2list:list[str] = ["Area 2 (Northwest Ladder Room) - Power4 Pickup", "Area 2 (Northwest Ladder Room) - Hover4 Pickup", "Area 2 (Northwest Ladder Room) - Thunder Break Pickup", "Area 2 (Northwest Ladder Room) - H-Missile Pickup"]
area2hoverloc:list[str] = ["Area 2 Lava Pools (Top Right Hover Platform) - H-Missile Pickup", "Area 2 Lava Pools (Top Right Hover Platform) - Thunder Break Pickup", "Area 2 Lava Pools (Top Right Hover Platform) - Multi-Missile"]
area2boss:list[str] = ["Area 2 Crusher Beam Upgrade", "Crabullus (Boss 2) Defeated", "Boss 2 Room (Spike Area) - Power Pickup", "Boss 2 Room (Above Spike Area) - Power Pickup", "Boss 2 Room (Above Spike Area) - Gun Pickup",
                       "Boss 2 Room (Far Right DeadEnd) - Hover4 Pickup", "Boss 2 Room (Far Right DeadEnd) - Gun Pickup", "Boss 2 Room (Right Before Boss) - Power4 Pickup", "Boss 2 Room (Right Before Boss) - Gun4 Pickup" ]
area2pathto7:list[str] = ["Area 2 to 7 Path - H-Missile Pickup #1", "Area 2 to 7 Path - H-Missile Pickup #2", "Area 2 to 7 Path - Power4 Pickup", "Area 2 to 7 Path - Thunder Break Pickup"]
area3list:list[str] = ["Area 3 Hover Upgrade", "Photophage (Boss 3) Defeated"]
area3wall1crush:list[str] = ["Area 3 Room (Behind Crusher Blocks) - Gun Pickup", "Area 3 Room (Behind Crusher Blocks) - Hover4 Pickup",
                             "Area 3 Room (Behind Crusher Blocks) - Thunder Break Pickup", "Area 3 Room (Behind Crusher Blocks) - H-Missile Pickup"]
area4boss: list[str] = ["Area 4 Key Upgrade", "Fred (Boss 4) Defeated", "Boss 4 Room (Top Right) - Power Pickup #1", "Boss 4 Room (Top Right) - Power Pickup #2", "Boss 4 Room (Bottom Right) - Power4 Pickup",
                        "Boss 4 Room (Bottom Right) - Gun Pickup #1", "Boss 4 Room (Bottom Right) - Gun Pickup #2", "Boss 4 Room (Bottom Right) - Power Pickup #1", "Boss 4 Room (Bottom Right) - Power Pickup #2",
                        "Boss 4 Room (Bottom Right) - Power Pickup #3", "Boss 4 Room (Bottom Right) - Power Pickup #4", "Boss 4 Room (Bottom Left) - Power Pickup #1", "Boss 4 Room (Bottom Left) - Hover Pickup",
                        "Boss 4 Room (Bottom Left) - Power Pickup #2", "Boss 4 Room (Bottom Left) - Power Pickup #3", "Boss 4 Room (Bottom Left) - Power4 Pickup", "Boss 4 Room (Bottom Left) - Hover4 Pickup"]
area5list:list[str] = ["Area 5 Dive Upgrade", "Hard Shell (Boss 5) Defeated"]
area6list:list[str] = ["Area 6 Wall 1 Upgrade", "Frozen Crabullus (Boss 6) Defeated", "Area 6 (Behind Blocks) - H-Missile Pickup #1", "Area 6 (Behind Blocks) - H-Missile Pickup #2"]
area7list:list[str] = ["Area 7 Wall 2 Upgrade", "Solar-Enhanced Fred (Boss 7) Defeated", "Area 7 (Outside Boss Room) - Gun4 Pickup", "Area 7 (4th Section Bottom Right) - Power Pickup", "Area 7 (4th Section Bottom Right) - Thunder Break Pickup",
                       "Boss 7 Room (1st Walkway) - Power4 Pickup", "Boss 7 Room (1st Walkway) - Gun4 Pickup", "Boss 7 Room (3rd Walkway) - Gun4 Pickup", "Boss 7 Room (Before Boss) - Power Pickup"]
area8list:list[str] = ["Area 8 (Top Right Room End) - Thunder Break Pickup", "Area 8 (Top Right Room End) - Hover4 Pickup #1", "Area 8 (Top Right Room End) - Hover4 Pickup #2",
                       "Area 8 (Top Right Room End) - Power4 Pickup", "Area 8 (Top Right Room End) - H-Missile Pickup #1", "Area 8 (Top Right Room End) - H-Missile Pickup #2", "Area 8 (Bottom Right Room End) - H-Missile Pickup #1",
                       "Area 8 (Bottom Right Room End) - H-Missile Pickup #2", "Area 8 (Bottom Right Room End) - Hover Pickup", "Area 8 (Bottom Right Room End) - Hover4 Pickup"]
area8bosslist:list[str] = ["Plutonium Boss (Boss 8) Defeated", "Underworld Lord Defeated"]


as_dict :dict[str, int] = {name: id+1 for id, name in enumerate([*area1list, *area1hoverloc, *area2list, *area2boss, *area2pathto7, *area2hoverloc, *area3list, *area3wall1crush, *area4boss, *area5list, *area6list, *area7list, *area8list, *area8bosslist])}



