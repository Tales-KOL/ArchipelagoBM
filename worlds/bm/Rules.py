from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule, add_rule
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import BMWorld

#def apply_location_rules(world, target, rule):
#    add_rule(world.multiworld.get_location(target, world.player), rule)

#    if len(world.options.boss_medal.value) > 0:
#       apply_location_rules(world, "Underworld Lord Defeated", lambda state: state.has("Boss Medal", world.player, world.options.boss_medal.value))

def has_bossmedal(state: CollectionState, player: int) -> bool:
    return state.has("Boss Medal", player, 7)

def can_hyper(state: CollectionState, player: int) -> bool:
    return state.has("Hyper Beam", player)

def can_crusher(state: CollectionState, player: int) -> bool:
    return state.has("Crusher Beam", player)

def can_hover(state: CollectionState, player: int) -> bool:
    return state.has("Hover Upgrade", player)

def can_key(state: CollectionState, player: int) -> bool:
    return state.has("Key", player)

def can_dive(state: CollectionState, player: int) -> bool:
    return state.has("Dive Engine", player)

def can_wall1(state: CollectionState, player: int) -> bool:
    return state.has("Wall 1", player)

def can_wall2(state: CollectionState, player: int) -> bool:
    return state.has("Wall 2", player)


