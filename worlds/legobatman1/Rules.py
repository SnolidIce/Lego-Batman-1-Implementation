from worlds.generic.Rules import add_rule, set_rule, forbid_item, add_item_rule
from .items import get_item_type
#varibles that make my life better
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

ch1h = if self.options.glitched or self.options.story_pickups: state.has_all("The Face-Off","You Can Bank on Batman", "Demolition Suit","An Icy Reception", "Glide Suit","Two-Face Chase","A Poisonous Appointment")
else: state.has_all("The Face-Off","You Can Bank on Batman", "Demolition Suit", "Technology Suit","An Icy Reception", "Glide Suit", "Magnet Suit","Two-Face Chase","A Poisonous Appointment", "Sonic Suit", "Heat Protection Suit", "Attract Suit")

ch2h = if self.options.glitched or self.options.story_pickups: state.has_all("Penguin's Lair","There She Goes Again", "Glide Suit","Batboat Battle","Under the City","Zoo's Company", "Demolition Suit", "Sonic Suit")
else: state.has_all( "Penguin's Lair","Water Suit","There She Goes Again", "Magnet Suit", "Glide Suit","Batboat Battle","Under the City", "Magnet Suit", "Water Suit", "Demolition Suit","Zoo's Company",  "Sonic Suit", "Technology Suit")

ch3h = if self.options.glitched or self.options.story_pickups: state.has_all("Joker's Home Turf","To the Top of the Tower", "Glide Suit","In the Dark Night", "Technology Suit", "Demolition Suit","Flight of the Bat","Little Fun at the Big Top")
else: state.has_all("To the Top of the Tower", "Glide Suit", "Demolition Suit", "Magnet Suit","In the Dark Night", "Technology Suit","Flight of the Bat","Little Fun at the Big Top", "Sonic Suit", "Joker's Home Turf","Attract Suit")

has_batarang = state.has_any("Penguin's Lair","There She Goes Again","To the Top of the Tower","The Face-Off","You Can Bank on Batman","In the Dark Night", "An Icy Reception","Little Fun at the Big Top", "A Poisonous Appointment", "Joker's Home Turf","Zoo's Company","Under the City")

any_hero = state.has_any(ch3h, ch2h, ch1h)

all_hero = state.has_all (ch1h, ch2h, ch3h)
#rules
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
  tjrh1_red_brick.access_rule = lambda state: state.has_all(player, "Joker's Home Turf", "Glide Suit", "Attract Suit", "On the Rocks", "Sonic Suit", "Magnet Suit", has_doublejump)

tjrh1_win = multiworld.get_location("Status Screen - Joker's Home Turf Completed", player)
if self.options.glitched or self.options.story_pickups:
  tjrh1_win.access_rule = lambda state: state.has_all(player, "Joker's Home Turf", "Glide Suit")
else:
  tjrh1_win.access_rule = lambda state: state.has_all(player, "Joker's Home Turf", "Glide Suit", "Magnet Suit", "Attract Suit")

tjrh1_status = multiworld.get_location("Status Screen - Joker's Home Turf True Status", player)
if self.options.glitched or self.options.story_pickups:
  tjrh1_status.access_rule = lambda state: state.has_all(player, "Joker's Home Turf", "Glide Suit")
else:
  tjrh1_status.access_rule = lambda state: state.has_all(player, "Joker's Home Turf", "Glide Suit", "Magnet Suit", "Attract Suit")

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

tjrh3_red_brick = multiworld.get_location("TJR Hero #3 - Room 2, Go through toxic gas and shoot turnstiles", player)
if self.options.story_pickups:
  tjrh3_red_brick.access_rule = lambda state: state.has_all(player, "Flight of the Bat")
else:
  tjrh3_red_brick.access_rule = lambda state: state.has_all(player, "Flight of the Bat", "Biplane Blast")

multiworld.get_location("Status Screen - Flight of the Bat True Status", player).access_rule = lambda state: state.has_all(player, "Flight of the Bat")
multiworld.get_location("Status Screen - Flight of the Bat Completed", player).access_rule = lambda state: state.has_all(player, "Flight of the Bat")

tjrh4_red_brick = multiworld.get_location("TJR Hero #4 - Room 3, Build heated ladder then climb, glide and double jump", player)
if self.options.story_pickups:
  tjrh4_red_brick.access_rule = lambda state: state.has_all(player, "In the Dark Night", "Technology Suit", "Demolition Suit")
else if self.options.glitched:
  tjrh4_red_brick.access_rule = lambda state: state.has_all(player, "In the Dark Night", "Glide Suit", "Slam","Technology Suit", "Demolition Suit")
else:
  tjrh4_red_brick.access_rule = lambda state: state.has_all(player, "In the Dark Night", "Glide Suit", "Magnet Suit", "Technology Suit", "Demolition Suit", "Heat Protection Suit",has_doublejump)

tjrh4_win = multiworld.get_location("Status Screen - In the Dark Night Completed", player)
if self.options.glitched or self.options.story_pickups:
  tjrh4_win.access_rule = lambda state: state.has_all(player, "In the Dark Night","Technology Suit", "Demolition Suit")
else:
  tjrh4_win.access_rule = lambda state: state.has_all(player, "In the Dark Night", "Magnet Suit", "Technology Suit", "Demolition Suit")

tjrh4_status = multiworld.get_location("Status Screen - In the Dark Night True Status", player)
if self.options.glitched or self.options.story_pickups:
  tjrh4_status.access_rule = lambda state: state.has_all(player, "In the Dark Night", "Technology Suit", "Demolition Suit")
else:
  tjrh4_status.access_rule = lambda state: state.has_all(player, "In the Dark Night", "Magnet Suit", "Technology Suit", "Demolition Suit")

tjrh5_red_brick = multiworld.get_location("TJR Hero #5 - Room 2, Push organ out of hiding, then press button to get guy to play it", player)
if self.options.story_pickups or self.options.glitched:
  tjrh5_red_brick.access_rule = lambda state: state.has_all(player, "To the Top of the Tower", "Glide Suit", has_strong)
else:
  tjrh5_red_brick.access_rule = lambda state: state.has_all(player, "To the Top of the Tower", "Glide Suit", "Demolition Suit", "Magnet Suit", has_strong)

tjrh5_win = multiworld.get_location("Status Screen - To the Top of the Tower Completed", player)
if self.options.glitched or self.options.story_pickups:
  tjrh5_win.access_rule = lambda state: state.has_all(player, "To the Top of the Tower", "Glide Suit")
else:
  tjrh5_win.access_rule = lambda state: state.has_all(player, "To the Top of the Tower", "Glide Suit", "Demolition Suit", "Magnet Suit")

tjrh5_status = multiworld.get_location("Status Screen - To the Top of the Tower True Status", player)
if self.options.glitched or self.options.story_pickups:
  tjrh5_status.access_rule = lambda state: state.has_all(player, "To the Top of the Tower", "Glide Suit")
else:
  tjrh5_status.access_rule = lambda state: state.has_all(player, "To the Top of the Tower", "Glide Suit", "Demolition Suit", "Magnet Suit")

trrv1_red_brick = multiworld.get_location("TRR Villian #1 - Room 2, Climb magnet wall then double jump and bring down green sign, build it and bring it to crusher in sub room", player)
if self.options.story_pickups:
  trrv1_red_brick.access_rule = lambda state: state.has_all(player, "The Ridler Makes a Withdrawal")
else if self.options.glitched:  
  trrv1_red_brick.access_rule = lambda state: state.has_all(player, "The Ridler Makes a Withdrawal", "Glide Suit", "Slam", has_batarang)
else:
  trrv1_red_brick.access_rule = lambda state: state.has_all(player, "The Ridler Makes a Withdrawal", "Magnet Suit", has_batarang)

multiworld.get_location("Status Screen - The Ridler Makes a Withdrawal True Status", player).access_rule = lambda state: state.has_all(player, "The Ridler Makes a Withdrawal")
multiworld.get_location("Status Screen - The Ridler Makes a Withdrawal Completed", player).access_rule = lambda state: state.has_all(player, "The Ridler Makes a Withdrawal")

trrv2_red_brick = multiworld.get_location("TRR Villian #2 - Room 2, Break silver handle then go inside, break object, build switch, go across and build object", player)
if self.options.story_pickups:
  trrv2_red_brick.access_rule = lambda state: state.has_all(player, "On the Rocks")
else:
  trrv2_red_brick.access_rule = lambda state: state.has_all(player, "On the Rocks", has_bomb)

multiworld.get_location("Status Screen - On the Rocks True Status", player).access_rule = lambda state: state.has_all(player, "On the Rocks")
multiworld.get_location("Status Screen - On the Rocks Completed", player).access_rule = lambda state: state.has_all(player, "On the Rocks")

multiworld.get_location("TRR Villian #3 - Room 2, Bomb silver door, then go in and use attract machine, use tech pannel to bake cake", player).access_rule = lambda state: state.has_all(player, "Green Fingers", "Attract Suit","Technology Suit", has_bomb)
multiworld.get_location("Status Screen - Green Fingers True Status", player).access_rule = lambda state: state.has_all(player, "Green Fingers")
multiworld.get_location("Status Screen - Green Fingers Completed", player).access_rule = lambda state: state.has_all(player, "Green Fingers")

multiworld.get_location("Status Screen - An Enterprising Theft True Status", player).access_rule = lambda state: state.has_all(player, "An Enterprising Theft")
multiworld.get_location("Status Screen - An Enterprising Theft Completed", player).access_rule = lambda state: state.has_all(player, "An Enterprising Theft")

multiworld.get_location("Status Screen - Breaking Blocks True Status", player).access_rule = lambda state: state.has_all(player, "Breaking Blocks")
multiworld.get_location("Status Screen - Breaking Blocks Completed", player).access_rule = lambda state: state.has_all(player, "Breaking Blocks")

multiworld.get_location("Status Screen - Rockin' the Docks True Status", player).access_rule = lambda state: state.has_all(player, "Rockin' the Docks")
multiworld.get_location("Status Screen - Rockin' the Docks Completed", player).access_rule = lambda state: state.has_all(player, "Rockin' the Docks")

multiworld.get_location("Status Screen - Stealing the Show True Status", player).access_rule = lambda state: state.has_all(player, "Stealing the Show")
multiworld.get_location("Status Screen - Stealing the Show Completed", player).access_rule = lambda state: state.has_all(player, "Stealing the Show")

multiworld.get_location("Status Screen - Harboring a Grudge True Status", player).access_rule = lambda state: state.has_all(player, "Harboring a Grudge")
multiworld.get_location("Status Screen - Harboring a Grudge Completed", player).access_rule = lambda state: state.has_all(player, "Harboring a Grudge")

multiworld.get_location("Status Screen - A Daring Rescue True Status", player).access_rule = lambda state: state.has_all(player, "A Daring Rescue")
multiworld.get_location("Status Screen - A Daring Rescue Completed", player).access_rule = lambda state: state.has_all(player, "A Daring Rescue")

multiworld.get_location("Status Screen - Arctic World True Status", player).access_rule = lambda state: state.has_all(player, "Breaking Blocks")
multiworld.get_location("Status Screen - Arctic World Completed", player).access_rule = lambda state: state.has_all(player, "Breaking Blocks")

multiworld.get_location("Status Screen - A Surprise for the Commissioner True Status", player).access_rule = lambda state: state.has_all(player, "A Surprise for the Commissioner")
multiworld.get_location("Status Screen - A Surprise for the Commissioner Completed", player).access_rule = lambda state: state.has_all(player, "A Surprise for the Commissioner")

multiworld.get_location("Status Screen - Biplane Blast True Status", player).access_rule = lambda state: state.has_all(player, "Biplane Blast")
multiworld.get_location("Status Screen - Biplane Blast Completed", player).access_rule = lambda state: state.has_all(player, "Biplane Blast")

multiworld.get_location("Status Screen - The Joker's Masterpiece True Status", player).access_rule = lambda state: state.has_all(player, "The Joker's Masterpiece")
multiworld.get_location("Status Screen - The Joker's Masterpiece Completed", player).access_rule = lambda state: state.has_all(player, "The Joker's Masterpiece")

multiworld.get_location("Status Screen - The Lure of the Night True Status", player).access_rule = lambda state: state.has_all(player, "The Lure of the Night")
multiworld.get_location("Status Screen - The Lure of the Night Completed", player).access_rule = lambda state: state.has_all(player, "The Lure of the Night")

multiworld.get_location("TJR Villian #5 - Room 1, Batarang chandelures then build sweeper and clean church", player).access_rule = lambda state: state.has_all(player, "Dying of Laughter", has_batarang)
multiworld.get_location("Status Screen - Dying of Laughter True Status", player).access_rule = lambda state: state.has_all(player, "Dying of Laughter")
multiworld.get_location("Status Screen - Dying of Laughter Completed", player).access_rule = lambda state: state.has_all(player, "Dying of Laughter")



multiworld.get_location("TRR Villian #3 - Room 2, Bomb silver door, then go in and defeat enemy", player).access_rule = lambda state: state.has_all(player, "Green Fingers", has_bomb)