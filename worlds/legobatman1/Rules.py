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

trrh1_red_brick = multiworld.get_location("TRR Hero #1 - Boss Room, Break the bank darwer", player)
if self.options.glitched or self.options.story_pickups:
  trrh1_red_brick.access_rule = lambda state: state.has_all(player, "You Can Bank on Batman", "Demolition Suit")
else:
  trrh1_red_brick.access_rule = lambda state: state.has_all(player, "You Can Bank on Batman", "Demolition Suit", "Technology Suit")

trrh1_win = multiworld.get_location("Status Screen - You Can Bank On Batman Completed", player)
if self.options.glitched or self.options.story_pickups:
  trrh1_win.access_rule = lambda state: state.has_all(player, "You Can Bank on Batman", "Demolition Suit")
else:
  trrh1_win.access_rule = lambda state: state.has_all(player, "You Can Bank on Batman", "Demolition Suit", "Technology Suit")

trrh1_status = multiworld.get_location("Status Screen - You Can Bank On Batman True Status", player)
if self.options.glitched or self.options.story_pickups:
  trrh1_status.access_rule = lambda state: state.has_all(player, "You Can Bank on Batman", "Demolition Suit")
else:
  trrh1_status.access_rule = lambda state: state.has_all(player, "You Can Bank on Batman", "Demolition Suit", "Technology Suit")

trrh2_red_brick = multiworld.get_location("TRR Hero #2 - Room 2, Press on switch while other character goes in cage", player)
if self.options.story_pickups:
  trrh2_red_brick.access_rule = lambda state: state.has_all(player, "An Icy Reception", "Glide Suit")
else if self.options.glitched:
  trrh2_red_brick.access_rule = lambda state: state.has_all(player, "An Icy Reception", "Glide Suit", has_strong)
else:
  trrh2_red_brick.access_rule = lambda state: state.has_all(player, "An Icy Reception", "Glide Suit", "Magnet Suit", has_strong)

trrh2_win = multiworld.get_location("Status Screen - An Icy Reception Completed", player)
if self.options.glitched or self.options.story_pickups:
  trrh2_win.access_rule = lambda state: state.has_all(player, "An Icy Reception", "Glide Suit")
else:
  trrh2_win.access_rule = lambda state: state.has_all(player, "An Icy Reception", "Glide Suit", "Magnet Suit")

trrh2_status = multiworld.get_location("Status Screen - An Icy Reception True Status", player)
if self.options.glitched or self.options.story_pickups:
  trrh2_status.access_rule = lambda state: state.has_all(player, "An Icy Reception", "Glide Suit")
else:
  trrh2_status.access_rule = lambda state: state.has_all(player, "An Icy Reception", "Glide Suit", "Magnet Suit")

multiworld.get_location("TRR Hero #3 - Room 3, Destroy trash can in the far back left cornor", player).access_rule = lambda state: state.has_all(player, "Two-Face Chase")
multiworld.get_location("Status Screen - Two-Face Chase True Status", player).access_rule = lambda state: state.has_all(player, "Two-Face Chase")
multiworld.get_location("Status Screen - Two-Face Chase Completed", player).access_rule = lambda state: state.has_all(player, "Two-Face Chase")