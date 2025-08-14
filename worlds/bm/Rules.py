from BaseClasses import CollectionState

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
