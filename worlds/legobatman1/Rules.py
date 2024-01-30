from worlds.generic.Rules import add_rule, set_rule, forbid_item, add_item_rule
from .items import get_item_type

has_sink(state.has_any("A Daring Rescue","Water Suit")) 

toxic = state.has_any(["A Surpise for the Commissioner", "On the Rocks","Green Fingers","An Enterprising Theft", "Breaking Blocks","The Joker's Masterpiece","Rockin' the Docks", "A Daring Rescue"])
has_toxic(toxic or "Joker (Tropical)")

mindcontrol = state.has_any(["The Riddler Makes a Withdrawl", "On the Rocks","Green Fingers","An Enterprising Theft", "Breaking Blocks","The Joker's Masterpiece"])
has_mindcontrol(mindcontrol or "Mad Hatter")

woman = state.has_any(["A Surpise for the Commissioner", "Stealing the Show", "Artic World","Dying of Laughter","Green Fingers"])
has_woman(woman or "Catwoman (Classic)")

doublejump = state.has_any(["A Surpise for the Commissioner", "Stealing the Show", "Artic World", "The Riddler Makes a Withdrawl","Dying of Laughter","Green Fingers"])
has_doublejump(doublejump or "Mad Hatter" or "Catwoman (Classic)")

joker = state.has_any(["A Surpise for the Commissioner", "The Joker's Masterpiece", "The Lure of the Night", "Dying of Laughter"])
has_joker(joker or "Joker (Tropical)")

glide = state.has_any(["Glide Suit", "Rockin' the Docks", "Stealing the Show", "A Daring Rescue", "Artic World", "The Lure of the Night"])
has_gliding(glide or "Man-Bat")

strong = state.has_any(["The Riddler Makes a Withdrawl", "Rockin' the Docks", "On the Rocks", "A Daring Rescue"])
has_strong(strong or "Man-Bat")

has_penguin(state.has_any(["Rockin' the Docks", "Stealing the Show", "A Daring Rescue", "Artic World"]))

has_bomb(state.has_any(["Rockin' the Docks", "Stealing the Show", "A Daring Rescue", "Artic World","Demolition Suit"]))

def set_rules(multiworld: MultiWorld, player: int, bool):

