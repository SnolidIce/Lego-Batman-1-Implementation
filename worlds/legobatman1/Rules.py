from worlds.generic.Rules import add_rule, set_rule, forbid_item, add_item_rule
from .items import get_item_type

sub = state.has(["Harboring a Grudge"])
has_sub(sub or "Penguin Goon Submarine", "Robin's Submarine")

has_sink(state.has_any(["A Daring Rescue","Water Suit"])) 

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

trrh4_red_brick = multiworld.get_location("TRR Hero #4 - Room 4, Use the switch, blow up the silver object and use the generator", player)
if self.options.glitched or self.options.story_pickups:
  trrh4_red_brick.access_rule = lambda state: state.has_all(player, "A Poisonous Appointment", has_joker, has_bomb)
else:
  trrh4_red_brick.access_rule = lambda state: state.has_all(player, "A Poisonous Appointment", has_joker, has_bomb, "Sonic Suit", "Heat Protection Suit", "Attract Suit")

trrh4_win = multiworld.get_location("Status Screen - A Poisonous Appointment Completed", player)
if self.options.glitched or self.options.story_pickups:
  trrh4_win.access_rule = lambda state: state.has_all(player, "A Poisonous Appointment")
else:
  trrh4_win.access_rule = lambda state: state.has_all(player, "A Poisonous Appointment", "Sonic Suit", "Heat Protection Suit", "Attract Suit")

trrh4_status = multiworld.get_location("Status Screen - A Poisonous Appointment True Status", player)
if self.options.glitched or self.options.story_pickups:
  trrh4_status.access_rule = lambda state: state.has_all(player, "A Poisonous Appointment")
else:
  trrh4_status.access_rule = lambda state: state.has_all(player, "A Poisonous Appointment", "Sonic Suit", "Heat Protection Suit", "Attract Suit")

trrh5_red_brick = multiworld.get_location("TRR Hero #5 - Room 2, After Two Face Fight, Push Colored Buttons on left side", player)
if self.options.story_pickups:
  trrh5_red_brick.access_rule = lambda state: state.has_all(player, "The Face-Off", "Glide Suit")
  if self.options.glitched:
  trrh5_red_brick.access_rule = lambda state: state.has_all(player, "The Face-Off", "Glide Suit", has_toxic)
else:
  trrh5_red_brick.access_rule = lambda state: state.has_all(player, "The Face-Off", "Glide Suit", "Magnet Suit", "Attract Suit", has_toxic)

trrh5_win = multiworld.get_location("Status Screen - The Face-Off Completed", player)
if self.options.glitched or self.options.story_pickups:
  trrh5_win.access_rule = lambda state: state.has_all(player, "The Face-Off", "Glide Suit")
else:
  trrh5_win.access_rule = lambda state: state.has_all(player, "The Face-Off", "Glide Suit", "Magnet Suit", "Attract Suit")

trrh5_status = multiworld.get_location("Status Screen - The Face-Off True Status", player)
if self.options.glitched or self.options.story_pickups:
  trrh5_status.access_rule = lambda state: state.has_all(player, "The Face-Off", "Glide Suit")
else:
  trrh5_status.access_rule = lambda state: state.has_all(player, "The Face-Off", "Glide Suit", "Magnet Suit", "Attract Suit")

pcph1_red_brick = multiworld.get_location("PCP Hero #1 - Boss Room, Break glass wall near entrance", player)
if self.options.glitched or self.options.story_pickups:
  pcph1_red_brick.access_rule = lambda state: state.has_all(player, "There She Goes Again", "Glide Suit")
else:
  pcph1_red_brick.access_rule = lambda state: state.has_all(player, "There She Goes Again", "Sonic Suit", "Magnet Suit", "Glide Suit")

pcph1_win = multiworld.get_location("Status Screen - There She Goes Again Completed", player)
if self.options.glitched or self.options.story_pickups:
  pcph1_win.access_rule = lambda state: state.has_all(player, "There She Goes Again", "Glide Suit")
else:
  pcph1_win.access_rule = lambda state: state.has_all(player, "There She Goes Again", "Magnet Suit", "Glide Suit")

pcph1_status = multiworld.get_location("Status Screen - There She Goes Again True Status", player)
if self.options.glitched or self.options.story_pickups:
  pcph1_status.access_rule = lambda state: state.has_all(player, "There She Goes Again", "Glide Suit")
else:
  pcph1_status.access_rule = lambda state: state.has_all(player, "There She Goes Again", "Magnet Suit", "Glide Suit")

pcph2_red_brick = multiworld.get_location("PCP Hero #2 - Boss Room, Submerge and shoot targets", player)
if self.options.char_shop_sanity:
  pcph2_red_brick.access_rule = lambda state: state.has_all(player, "Batboat Battle", has_sub)
else:
  pcph2_red_brick.access_rule = lambda state: state.has_all(player, "Batboat Battle")

multiworld.get_location("Status Screen - Batboat Battle True Status", player).access_rule = lambda state: state.has_all(player, "Batboat Battle")
multiworld.get_location("Status Screen - Batboat Battle Completed", player).access_rule = lambda state: state.has_all(player, "Batboat Battle")

pcph3_red_brick = multiworld.get_location("PCP Hero #3 - Room 1, Use Tech Pannel and run over bouys", player)
if self.options.story_pickups:
  pcph3_red_brick.access_rule = lambda state: state.has_all(player, "Under the City")
else if self.options.glitched:
  pcph3_red_brick.access_rule = lambda state: state.has_all(player, "Under the City", "Glide Suit", "Technology Suit")
else:
  pcph3_red_brick.access_rule = lambda state: state.has_all(player, "Under the City", "Glide Suit", "Magnet Suit", "Water Suit", "Technology Suit", "Demolition Suit")

pcph3_win = multiworld.get_location("Status Screen - Under the City Completed", player)
if self.options.glitched or self.options.story_pickups:
  pcph3_win.access_rule = lambda state: state.has_all(player, "Under the City", "Glide Suit")
else:
  pcph3_win.access_rule = lambda state: state.has_all(player, "Under the City", "Glide Suit", "Magnet Suit", "Water Suit", "Demolition Suit")

pcph3_status = multiworld.get_location("Status Screen - Under the City True Status", player)
if self.options.glitched or self.options.story_pickups:
  pcph3_status.access_rule = lambda state: state.has_all(player, "Under the City", "Glide Suit")
else:
  pcph3_status.access_rule = lambda state: state.has_all(player, "Under the City", "Glide Suit", "Magnet Suit", "Water Suit", "Demolition Suit")

pcph4_red_brick = multiworld.get_location("PCP Hero #4 - Room 2, Break Silver grate and go in water", player)
if self.options.story_pickups or self.options.story_pickups:
  pcph4_red_brick.access_rule = lambda state: state.has_all(player, "Zoo's Company", "Sonic Suit", "Demolition Suit")
else:
  pcph4_red_brick.access_rule = lambda state: state.has_all(player, "Zoo's Company", "Glide Suit", "Sonic Suit", "Magnet Suit", "Demolition Suit", "Technology Suit")

pcph4_win = multiworld.get_location("Status Screen - Zoo's Company Completed", player)
if self.options.glitched or self.options.story_pickups:
  pcph4_win.access_rule = lambda state: state.has_all(player, "Zoo's Company", "Demolition Suit", "Sonic Suit")
else:
  pcph4_win.access_rule = lambda state: state.has_all(player, "Zoo's Company", "Glide Suit", "Sonic Suit", "Magnet Suit", "Demolition Suit", "Technology Suit")

pcph4_status = multiworld.get_location("Status Screen - Zoo's Company True Status", player)
if self.options.glitched or self.options.story_pickups:
  pcph4_status.access_rule = lambda state: state.has_all(player, "Zoo's Company", "Demolition Suit", "Sonic Suit")
else:
  pcph4_status.access_rule = lambda state: state.has_all(player, "Zoo's Company", "Glide Suit", "Sonic Suit", "Magnet Suit", "Demolition Suit", "Technology Suit")

pcph5_red_brick = multiworld.get_location("PCP Hero #5 - Boss Room, Break glass near treadmil, graple and jump to rail and run on tredmil then push button", player)
if self.options.story_pickups:
  pcph5_red_brick.access_rule = lambda state: state.has_all(player, "Penguin's Lair", "Glide Suit")
else if self.options.glitched:
  pcph5_red_brick.access_rule = lambda state: state.has_all(player, "Penguin's Lair", "Glide Suit")
else:
  pcph5_red_brick.access_rule = lambda state: state.has_all(player, "Penguin's Lair", "Glide Suit", "Sonic Suit", "Water Suit")

pcph5_win = multiworld.get_location("Status Screen - Penguin's Lair Completed", player)
if self.options.glitched or self.options.story_pickups:
  pcph5_win.access_rule = lambda state: state.has_all(player, "Penguin's Lair", "Glide Suit")
else:
  pcph5_win.access_rule = lambda state: state.has_all(player, "Penguin's Lair", "Glide Suit", "Water Suit")

pcph5_status = multiworld.get_location("Status Screen - Penguin's Lair True Status", player)
if self.options.glitched or self.options.story_pickups:
  pcph5_status.access_rule = lambda state: state.has_all(player, "Penguin's Lair", "Glide Suit")
else:
  pcph5_status.access_rule = lambda state: state.has_all(player, "Penguin's Lair", "Glide Suit", "Water Suit")

tjrh1_red_brick = multiworld.get_location("TJR Hero #1 - Room 3, Freeze water near entrance then double jump up, then break glass and solve puzzle", player)
if self.options.story_pickups:
  tjrh1_red_brick.access_rule = lambda state: state.has_all(player, "Joker's Home Turf", "Glide Suit", "Magnet Suit")
else if self.options.glitched:
  tjrh1_red_brick.access_rule = lambda state: state.has_all(player, "Joker's Home Turf", "Glide Suit", "Slam")
else:
  tjrh1_red_brick.access_rule = lambda state: state.has_all(player, "Joker's Home Turf", "Glide Suit", "Attract Suit", "On the Rocks", "Sonic Suit", has_doublejump)

tjrh1_win = multiworld.get_location("Status Screen - Joker's Home Turf Completed", player)
if self.options.glitched or self.options.story_pickups:
  tjrh1_win.access_rule = lambda state: state.has_all(player, "Joker's Home Turf", "Glide Suit")
else:
  tjrh1_win.access_rule = lambda state: state.has_all(player, "Joker's Home Turf", "Glide Suit", "Magnet Suit")

tjrh1_status = multiworld.get_location("Status Screen - Joker's Home Turf True Status", player)
if self.options.glitched or self.options.story_pickups:
  tjrh1_status.access_rule = lambda state: state.has_all(player, "Joker's Home Turf", "Glide Suit")
else:
  tjrh1_status.access_rule = lambda state: state.has_all(player, "Joker's Home Turf", "Glide Suit", "Magnet Suit")

tjrh2_red_brick = multiworld.get_location("TJR Hero #2 - Room 1, Use Tech Pannel on Crane Game, grab and break all 3 pink prizes", player)
if self.options.story_pickups or self.options.glitched:
  tjrh2_red_brick.access_rule = lambda state: state.has_all(player, "Little Fun at the Big Top", "Technology Suit")
else:
  tjrh2_red_brick.access_rule = lambda state: state.has_all(player, "Little Fun at the Big Top", "Glide Suit", "Attract Suit", "Technology Suit", "Sonic Suit")

tjrh2_win = multiworld.get_location("Status Screen - Little Fun at the Big Top Completed", player)
if self.options.glitched or self.options.story_pickups:
  tjrh2_win.access_rule = lambda state: state.has_all(player, "Little Fun at the Big Top")
else:
  tjrh2_win.access_rule = lambda state: state.has_all(player, "Little Fun at the Big Top", "Demolition Suit", "Sonic Suit", "Attract Suit")

tjrh2_status = multiworld.get_location("Status Screen - Little Fun at the Big Top True Status", player)
if self.options.glitched or self.options.story_pickups:
  tjrh2_status.access_rule = lambda state: state.has_all(player, "Little Fun at the Big Top")
else:
  tjrh2_status.access_rule = lambda state: state.has_all(player, "Little Fun at the Big Top", "Demolition Suit", "Sonic Suit", "Attract Suit")

tjrh3_red_brick = multiworld.get_location("TJR Hero #2 - Room 1, Use Tech Pannel on Crane Game, grab and break all 3 pink prizes", player)
if self.options.story_pickups:
  tjrh3_red_brick.access_rule = lambda state: state.has_all(player, "Flight of the Bat")
else:
  tjrh3_red_brick.access_rule = lambda state: state.has_all(player, "Flight of the Bat", "Biplane Blast")

multiworld.get_location("Status Screen - Flight of the Bat True Status", player).access_rule = lambda state: state.has_all(player, "Flight of the Bat")
multiworld.get_location("Status Screen - Flight of the Bat Completed", player).access_rule = lambda state: state.has_all(player, "Flight of the Bat")

tjrh4_red_brick = multiworld.get_location("TJR Hero #4 - Room 3, Build heated ladder then climb, glide and double jump", player)
if self.options.story_pickups:
  tjrh4_red_brick.access_rule = lambda state: state.has_all(player, "In the Dark Night", "Glide Suit", "Magnet Suit")
else if self.options.glitched:
  tjrh4_red_brick.access_rule = lambda state: state.has_all(player, "In the Dark Night", "Glide Suit", "Slam")
else:
  tjrh4_red_brick.access_rule = lambda state: state.has_all(player, "In the Dark Night", "Glide Suit", "Magnet Suit", "Technology Suit", "Demolition Suit", has_doublejump)

tjrh4_win = multiworld.get_location("Status Screen - In the Dark Night Completed", player)
if self.options.glitched or self.options.story_pickups:
  tjrh4_win.access_rule = lambda state: state.has_all(player, "In the Dark Night", "Glide Suit")
else:
  tjrh4_win.access_rule = lambda state: state.has_all(player, "In the Dark Night", "Glide Suit", "Glide Suit", "Magnet Suit", "Technology Suit", "Demolition Suit")

tjrh4_status = multiworld.get_location("Status Screen - In the Dark Night True Status", player)
if self.options.glitched or self.options.story_pickups:
  tjrh4_status.access_rule = lambda state: state.has_all(player, "In the Dark Night", "Glide Suit")
else:
  tjrh4_status.access_rule = lambda state: state.has_all(player, "In the Dark Night", "Glide Suit", "Magnet Suit", "Technology Suit", "Demolition Suit")

tjrh5_red_brick = multiworld.get_location("TJR Hero #5 - Room 2, Push organ out of hiding, then press button to get guy to play it", player)
if self.options.story_pickups or self.options.glitched:
  tjrh5_red_brick.access_rule = lambda state: state.has_all(player, "To the Top of the Tower", "Glide Suit", has_strong)
else:
  tjrh5_red_brick.access_rule = lambda state: state.has_all(player, "To the Top of the Tower", "Glide Suit", "Attract Suit", "Technology Suit", "Sonic Suit", has_strong)

tjrh5_win = multiworld.get_location("Status Screen - To the Top of the Tower Completed", player)
if self.options.glitched or self.options.story_pickups:
  tjrh5_win.access_rule = lambda state: state.has_all(player, "To the Top of the Tower", "Glide Suit")
else:
  tjrh5_win.access_rule = lambda state: state.has_all(player, "To the Top of the Tower", "Demolition Suit", "Sonic Suit", "Attract Suit")

tjrh5_status = multiworld.get_location("Status Screen - To the Top of the Tower True Status", player)
if self.options.glitched or self.options.story_pickups:
  tjrh5_status.access_rule = lambda state: state.has_all(player, "To the Top of the Tower", "Glide Suit")
else:
  tjrh5_status.access_rule = lambda state: state.has_all(player, "To the Top of the Tower", "Glide Suit", "Demolition Suit", "Sonic Suit", "Attract Suit")