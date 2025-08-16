# Logging = output. How you'll figure out whats going wrong
import logging

# Built in AP imports
from BaseClasses import Item, ItemClassification

class BMItem(Item):  # or from Items import MyGameItem
    game = "Blaster Master"  # name of the game/world this item is from


def is_progression(item):
    return item in listA

def create_event(self, event: str) -> BMItem:
    # while we are at it, we can also add a helper to create events
    return BMItem(event, ItemClassification.progression, None, self.player)

listA:list[str] = ["Hyper Beam",
                      "Crusher Beam",
                      "Hover Upgrade",
                      "Key",
                      "Dive Engine",
                      "Wall 1",
                      "Wall 2",
                      "Boss Medal",
                      "Victory"]
listB:list[str] = ["Junk Item #9000",
                     "Item That Does Nothing",
                   "Waste Of Space"]

itemnametoid :dict[str, int] = {name: id+1 for id, name in enumerate([*listA, *listB])}