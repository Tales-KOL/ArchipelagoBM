from dataclasses import dataclass

from Options import Toggle, Range, Choice, PerGameCommonOptions


class StartingHover(Toggle):
    """Adds a hover to your starting inventory."""
    display_name = "Start With Hover"  # this is the option name as it's displayed to the user on the webhost and in the spoiler log


class StartingArea(Choice):
    """Sets Starting Area."""
    display_name = "Starting Area"
    option_area1 = 1
    option_area2 = 2
    option_area3 = 3
    default = 1  # default to normal

class BossMedalCount(Range):
    """Sets the amount of Bosses defeated to goal"""
    display_name = "Boss Medals Required"
    range_start = 0
    range_end = 8
    default = 8


@dataclass
class BMOptions(PerGameCommonOptions):
    starting_hover: StartingHover
    starting_area: StartingArea
    boss_medal: BossMedalCount