from BaseClasses import Location

class BMLocation(Location):  # or from Locations import MyGameLocation
    game = "Blaster Master"  # name of the game/world this location is in

area1list:list[str] = ["Hyper Beam Pickup", "Mother Brain (Boss 1) Defeated", "Underwater Room - Power", "Underwater - H-Missile #1", "Underwater - H-Missile #2"]
area1hoverloc:list[str] = ["Area 1 Cliff - Hover4 #1", "Area 1 Cliff - Hover4 #2", "Area 1 Cliff - Hover4 #3"]
area2list:list[str] = ["Area 2 Northwest Ladder Room - Power4", "Area 2 Northwest Ladder Room - Hover4", "Area 2 Northwest Ladder Room - Thunder Break", "Area 2 Northwest Ladder Room - H-Missile"]
area2hoverloc:list[str] = ["Area 2 Lava Room 1 Hover Top Right - H-Missile", "Area 2 Lava Room 1 Hover Top Right - Thunder Break", "Area 2 Lava Room 1 Hover Top Right - Multi-Missile"]
area2boss:list[str] = ["Crusher Beam Pickup", "Crabullus (Boss 2) Defeated", "Boss 2 Room Spike Area - Power", "Boss 2 Room Above Spike Area - Power", "Boss 2 Room Above Spike Area - Gun",
                       "Boss 2 Room Far Right DeadEnd - Hover4", "Boss 2 Room Far Right DeadEnd - Gun", "Boss 2 Room Before Boss - Power4", "Boss 2 Room Before Boss- Gun4" ]
area2pathto7:list[str] = ["Area 2 to 7 Path - H-Missile #1", "Area 2 to 7 Path - H-Missile #2", "Area 2 to 7 Path - Power4", "Area 2 to 7 Path - Thunder Break"]
area3list:list[str] = ["Hover Upgrade Pickup", "Photophage (Boss 3) Defeated"]
area3wall1crush:list[str] = ["Area 3 Room Behind Crusher Blocks - Gun", "Area 3 Room Behind Crusher Blocks- Hover4",
                             "Area 3 Room Behind Crusher Blocks - Thunder Break", "Area 3 Room Behind Crusher Blocks - H-Missile"]
area4boss: list[str] = ["Key Pickup", "Fred (Boss 4) Defeated", "Boss 4 Room Top Right - Power #1", "Boss 4 Room Top Right - Power #2", "Boss 4 Room Bottom Right - Power4",
                        "Boss 4 Room Bottom Right - Gun #1", "Boss 4 Room Bottom Right - Gun #2", "Boss 4 Room Bottom Right - Power #1", "Boss 4 Room Bottom Right - Power #2",
                        "Boss 4 Room Bottom Right - Power #3", "Boss 4 Room Bottom Right - Power #4", "Boss 4 Room Bottom Left - Power #1", "Boss 4 Room Bottom Left - Hover",
                        "Boss 4 Room Bottom Left - Power #2", "Boss 4 Room Bottom Left - Power #3", "Boss 4 Room Bottom Left - Power4", "Boss 4 Room Bottom Left - Hover4"]
area5list:list[str] = ["Dive Engine Pickup", "Hard Shell (Boss 5) Defeated"]
area6list:list[str] = ["Wall 1 Pickup", "Frozen Crabullus (Boss 6) Defeated", "Area 6 Behind Blocks - H-Missile #1", "Area 6 Behind Blocks - H-Missile #2"]
area7list:list[str] = ["Wall 2 Pickup", "Solar-Enhanced Fred (Boss 7) Defeated", "Area 7 Outside Boss Room - Gun4", "Area 7 4th Section Bottom Right - Power", "Area 7 4th Section Bottom Right - Thunder Break",
                       "Boss 7 Room 1st Walkway - Power4", "Boss 7 Room 1st Walkway - Gun4", "Boss 7 Room 3rd Walkway - Gun4", "Boss 7 Room Before Boss - Power"]
area8list:list[str] = ["Plutonium Boss (Boss 8) Defeated", "Underworld Lord Defeated", "Area 8 Top Right Room End - Thunder Break", "Area 8 Top Right Room End - Hover4 #1", "Area 8 Top Right Room End - Hover4 #2",
                       "Area 8 Top Right Room End - Power4", "Area 8 Top Right Room End - H-Missile #1", "Area 8 Top Right Room End - H-Missile #2", "Area 8 Bottom Right Room End - H-Missile #1",
                       "Area 8 Bottom Right Room End - H-Missile #2", "Area 8 Bottom Right Room End - Hover", "Area 8 Bottom Right Room End - Hover4"]


as_dict :dict[str, int] = {name: id+1 for id, name in enumerate([*area1list, *area1hoverloc, *area2list, *area2boss, *area2pathto7, *area2hoverloc, *area3list, *area3wall1crush, *area4boss, *area5list, *area6list, *area7list, *area8list])}



