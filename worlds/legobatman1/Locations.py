from typing import Dict, NamedTuple, Optional

from BaseClasses import Location


class LegoBatman1Location(Location):
    game: str = "Lego Batman: The Video Game"


class LegoBatman1LocationData(NamedTuple):
    category: str
    code: Optional[int] = None

def get_locations_by_category(category: str) -> Dict[str, LegoBatman1LocationData]:
    location_dict: Dict[str, LegoBatman1LocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict

# NEXT ID IS 45035996274 and 45035996328
location_table: Dict[str, LegoBatman1LocationData] = {


    # You Can Bank On Batman
    "TRR Hero #1 - Boss Room, Break the bank darwer":                                       LegoBatman1LocationData("You Can Bank On Batman",   45035996011),

    # An Icy Reception
    "TRR Hero #2 - Room 2, Press on switch while other character goes in cage":            LegoBatman1LocationData("An Icy Reception",   45035996020),
    
    # Two-Face Chase
    "TRR Hero #3 - Room 3, Destroy trash can in the far back left cornor":                  LegoBatman1LocationData("Two-Face Chase",   45035996031),
    
    # A Poisonous Appointment
    "TRR Hero #4 - Room 4, Use the switch, blow up the silver object and use the generator":LegoBatman1LocationData("A Poisonous Appointment",   45035996044),

    # The Face-Off
    "TRR Hero #5 - Room 2, After Two Face Fight, Push Colored Buttons on left side":        LegoBatman1LocationData("The Face-Off",   45035996053),

    # There She Goes Again
    "PCP Hero #1 - Boss Room, Break glass wall near entrance":                               LegoBatman1LocationData("There She Goes Again",   45035996070),
    
    # Batboat Battle
    "PCP Hero #2 - Boss Room, Submerge and shoot targets":                                  LegoBatman1LocationData("Batboat Battle",   45035996079),
    
    # Under The City
    "PCP Hero #3 - Room 1, Use Tech Pannel and run over bouys":                             LegoBatman1LocationData("Under The City",   45035996082),
    
    # Zoo's Company
    "PCP Hero #4 - Room 2, Break Silver grate and go in water":                             LegoBatman1LocationData("Zoo's Company",   45035996099),
    
    # Penguin's Lair
    "PCP Hero #5 - Boss Room, Break glass near treadmil, graple and jump to rail and run on tredmil then push button":LegoBatman1LocationData("Penguin's Lair",   45035996116),
    
    # Joker's Home Turf
    "TJR Hero #1 - Room 3, Freeze water near entrance then double jump up, then break glass and solve puzzle":LegoBatman1LocationData("Joker's Home Turf",   45035996126),

    # Little Fun at the Big Top
    "TJR Hero #2 - Room 1, Use Tech Pannel on Crane Game, grab and break all 3 pink prizes":LegoBatman1LocationData("Little Fun at the Big Top",   45035996134),

    # Flight of the Bat
    "TJR Hero #3 - Room 2, Go through toxic gas and shoot turnstiles":                      LegoBatman1LocationData("Flight of the Bat",   45035996147),

    # In the Dark Night
    "TJR Hero #4 - Room 3, Build heated ladder then climb, glide and double jump":         LegoBatman1LocationData("In the Dark Night",   45035996162),

    # To the Top of the Tower
    "TJR Hero #5 - Room 2, Push organ out of hiding, then press button to get guy to play it":LegoBatman1LocationData("To the Top of the Tower",   45035996174),

    # The Ridler Makes a Withdrawal
    "TRR Villian #1 - Room 2, Climb magnet wall then double jump and bring down green sign, build it and bring it to crusher in sub room":LegoBatman1LocationData("The Ridler Makes a Withdrawal",   45035996184),

    # On the Rocks
    "TRR Villian #2 - Room 2, Break silver handle then go inside, break object, build switch, go across and build object":LegoBatman1LocationData("On the Rocks",   45035996193),

    # Green Fingers
    "TRR Villian #3 - Room 2, Bomb silver door, then go in and use attract machine, use tech pannel to bake cake":LegoBatman1LocationData("Green Fingers",   45035996205),    

    # An Enterprising Theft
    "TRR Villian #4 - Room 3, Blow up silver door, then build movie player, go in door and solve puzzle":LegoBatman1LocationData("An Enterprising Theft",   45035996223),

    # Breaking Blocks
    "TRR Villian #5 - Room 3, Break silver door then build and push gold block, break glass, break pannel, then blow up silver door":LegoBatman1LocationData("Breaking Blocks",   45035996241),
   
    # Rockin' the Docks
    "PCP Villian #1 - Room 2, Use female door pannel and solve puzzle":                        LegoBatman1LocationData("Rockin' the Docks",   45035996252),

    # Stealing the Show
    "PCP Villian #2 - Room 2, Use attract machine then build helicopter then push buttons and blow up silver object":LegoBatman1LocationData("Stealing the Show",   45035996267),

    # Harboring a Grudge
    "PCP Villian #3 - Boss Room, Use Robin Torpedo on colored wall and drive to left corner":  LegoBatman1LocationData("Harboring a Grudge",   45035996281),

    # A Daring Rescue
    "PCP Villian #4 - Room 5, Build canon to enter sub room, strong push platform, use tech suit to make another platform, jump across":LegoBatman1LocationData("A Daring Rescue",   45035996289),

    # Arctic World
    "PCP Villian #5 - Room 1, Use attract machine and play fishing mini game":                 LegoBatman1LocationData("Arctic World",   45035996294),

    # A Surprise for the Commissioner
    "TJR Villian #1 - Room 2, Glide across from near generator then grapple up and blow up silver object":LegoBatman1LocationData("A Surprise for the Commissioner",   45035996313),

    # Biplane Blast
    "TJR Villian #2 - Destroy 5 police copters throughout the level":                            LegoBatman1LocationData("Biplane Blast",   45035996318),

    # The Joker's Masterpiece
    "TJR Villian #3 - Room 1, Bomb silver door, then go in heated room and solve puzzle":      LegoBatman1LocationData("The Joker's Masterpiece",   45035996332),

    # The Lure of the Night
    "TJR Villian #4 - Room 2, Use attract machine in playground and grow plants":              LegoBatman1LocationData("The Lure of the Night",   45035996350),

    # Dying of Laughter
    "TJR Villian #5 - Room 1, Batarang chandelures then build sweeper and clean church":       LegoBatman1LocationData("Dying of Laughter",   45035996355),
}


basic_locations = {
   # Status Screen, suit unlocks then true status
    "Status Screen - Unlock Detonation Suit":                                                               LegoBatman1LocationData("Status Screen",    45035996365),
    "Status Screen - Unlock Sonic Suit":                                                                    LegoBatman1LocationData("Status Screen",    45035996366),
    "Status Screen - Unlock Heat Protection Suit":                                                          LegoBatman1LocationData("Status Screen",    45035996367),
    "Status Screen - Unlock Glide Suit":                                                                    LegoBatman1LocationData("Status Screen",    45035996368),
    "Status Screen - Unlock Technology Suit":                                                               LegoBatman1LocationData("Status Screen",    45035996369),
    "Status Screen - Unlock Attraction Suit":                                                               LegoBatman1LocationData("Status Screen",    45035996370),
    "Status Screen - Unlock Magnet Suit":                                                                   LegoBatman1LocationData("Status Screen",    45035996371),
    "Status Screen - Unlock Water Suit":                                                                    LegoBatman1LocationData("Status Screen",    45035996372),    
    "Status Screen - You Can Bank On Batman True Status":                                                   LegoBatman1LocationData("Status Screen",    45035996373),
    "Status Screen - An Icy Reception True Status":                                                         LegoBatman1LocationData("Status Screen",    45035996374),
    "Status Screen - Two-Face Chase True Status":                                                           LegoBatman1LocationData("Status Screen",    45035996375),
    "Status Screen - A Poisonous Appointment True Status":                                                  LegoBatman1LocationData("Status Screen",    45035996376),
    "Status Screen - The Face-Off True Status":                                                             LegoBatman1LocationData("Status Screen",    45035996377),
    "Status Screen - There She Goes Again True Status":                                                     LegoBatman1LocationData("Status Screen",    45035996378),
    "Status Screen - Batboat Battle True Status":                                                           LegoBatman1LocationData("Status Screen",    45035996379),
    "Status Screen - Under the City True Status":                                                           LegoBatman1LocationData("Status Screen",    45035996380),
    "Status Screen - Zoo's Company True Status":                                                            LegoBatman1LocationData("Status Screen",    45035996381),
    "Status Screen - Penguin's Lair True Status":                                                           LegoBatman1LocationData("Status Screen",    45035996382),
    "Status Screen - Joker's Home Turf True Status":                                                        LegoBatman1LocationData("Status Screen",    45035996383),
    "Status Screen - Little Fun at the Big Top True Status":                                                LegoBatman1LocationData("Status Screen",    45035996384),
    "Status Screen - Flight of the Bat True Status":                                                        LegoBatman1LocationData("Status Screen",    45035996385),
    "Status Screen - In the Dark Night True Status":                                                        LegoBatman1LocationData("Status Screen",    45035996386),
    "Status Screen - To the Top of the Tower True Status":                                                  LegoBatman1LocationData("Status Screen",    45035996387),
    "Status Screen - The Ridler Makes a Withdrawal True Status":                                            LegoBatman1LocationData("Status Screen",    45035996388),
    "Status Screen - On the Rocks True Status":                                                             LegoBatman1LocationData("Status Screen",    45035996389),
    "Status Screen - Green Fingers True Status":                                                            LegoBatman1LocationData("Status Screen",    45035996390),
    "Status Screen - An Enterprising Theft True Status":                                                    LegoBatman1LocationData("Status Screen",    45035996391),
    "Status Screen - Breaking Blocks True Status":                                                          LegoBatman1LocationData("Status Screen",    45035996392),
    "Status Screen - Rockin' the Docks True Status":                                                        LegoBatman1LocationData("Status Screen",    45035996393),
    "Status Screen - Stealing the Show True Status":                                                        LegoBatman1LocationData("Status Screen",    45035996394),
    "Status Screen - Harboring a Grudge True Status":                                                       LegoBatman1LocationData("Status Screen",    45035996395),
    "Status Screen - A Daring Rescue True Status":                                                          LegoBatman1LocationData("Status Screen",    45035996396),
    "Status Screen - Arctic World True Status":                                                             LegoBatman1LocationData("Status Screen",    45035996397),
    "Status Screen - A Surprise for the Commissioner True Status":                                          LegoBatman1LocationData("Status Screen",    45035996398),
    "Status Screen - Biplane Blast True Status":                                                            LegoBatman1LocationData("Status Screen",    45035996399),
    "Status Screen - The Joker's Masterpiece True Status":                                                  LegoBatman1LocationData("Status Screen",    45035996400),
    "Status Screen - The Lure of the Night True Status":                                                    LegoBatman1LocationData("Status Screen",    45035996401),
    "Status Screen - Dying of Laughter True Status":                                                        LegoBatman1LocationData("Status Screen",    45035996402),
    "Status Screen - You Can Bank On Batman Completed":                                                     LegoBatman1LocationData("Status Screen",    45035996403),
    "Status Screen - An Icy Reception Completed":                                                           LegoBatman1LocationData("Status Screen",    45035996404),
    "Status Screen - Two-Face Chase Completed":                                                             LegoBatman1LocationData("Status Screen",    45035996405),
    "Status Screen - A Poisonous Appointment Completed":                                                    LegoBatman1LocationData("Status Screen",    45035996406),
    "Status Screen - The Face-Off Completed":                                                               LegoBatman1LocationData("Status Screen",    45035996407),
    "Status Screen - There She Goes Again Completed":                                                       LegoBatman1LocationData("Status Screen",    45035996408),
    "Status Screen - Batboat Battle Completed":                                                             LegoBatman1LocationData("Status Screen",    45035996409),
    "Status Screen - Under the City Completed":                                                             LegoBatman1LocationData("Status Screen",    45035996410),
    "Status Screen - Zoo's Company Completed":                                                              LegoBatman1LocationData("Status Screen",    45035996411),
    "Status Screen - Penguin's Lair Completed":                                                             LegoBatman1LocationData("Status Screen",    45035996412),
    "Status Screen - Joker's Home Turf Completed":                                                          LegoBatman1LocationData("Status Screen",    45035996413),
    "Status Screen - Little Fun at the Big Top Completed":                                                  LegoBatman1LocationData("Status Screen",    45035996414),
    "Status Screen - Flight of the Bat Completed":                                                          LegoBatman1LocationData("Status Screen",    45035996415),
    "Status Screen - In the Dark Night Completed":                                                          LegoBatman1LocationData("Status Screen",    45035996416),
    "Status Screen - To the Top of the Tower Completed":                                                    LegoBatman1LocationData("Status Screen",    45035996417),
    "Status Screen - The Ridler Makes a Withdrawal Completed":                                              LegoBatman1LocationData("Status Screen",    45035996418),
    "Status Screen - On the Rocks Completed":                                                               LegoBatman1LocationData("Status Screen",    45035996419),
    "Status Screen - Green Fingers Completed":                                                              LegoBatman1LocationData("Status Screen",    45035996420),
    "Status Screen - An Enterprising Theft Completed":                                                      LegoBatman1LocationData("Status Screen",    45035996421),
    "Status Screen - Breaking Blocks Completed":                                                            LegoBatman1LocationData("Status Screen",    45035996422),
    "Status Screen - Rockin' the Docks Completed":                                                          LegoBatman1LocationData("Status Screen",    45035996423),
    "Status Screen - Stealing the Show Completed":                                                          LegoBatman1LocationData("Status Screen",    45035996424),
    "Status Screen - Harboring a Grudge Completed":                                                         LegoBatman1LocationData("Status Screen",    45035996425),
    "Status Screen - A Daring Rescue Completed":                                                            LegoBatman1LocationData("Status Screen",    45035996426),
    "Status Screen - Arctic World Completed":                                                               LegoBatman1LocationData("Status Screen",    45035996427),
    "Status Screen - A Surprise for the Commissioner Completed":                                            LegoBatman1LocationData("Status Screen",    45035996428),
    "Status Screen - Biplane Blast Completed":                                                              LegoBatman1LocationData("Status Screen",    45035996429),
    "Status Screen - The Joker's Masterpiece Completed":                                                    LegoBatman1LocationData("Status Screen",    45035996430),
    "Status Screen - The Lure of the Night Completed":                                                      LegoBatman1LocationData("Status Screen",    45035996431),
    "Status Screen - Dying of Laughter Completed":                                                          LegoBatman1LocationData("Status Screen",    45035996432),

    # Shop
    "Buy Beep Beep":                                LegoBatman1LocationData("Shop", 45035996433),
    "Buy Silhouettes":                              LegoBatman1LocationData("Shop", 45035996434),
    "Buy Extra Toggle":                             LegoBatman1LocationData("Shop", 45035996435),
    "Buy Disguise":                                 LegoBatman1LocationData("Shop", 45035996436),
    "Buy Ice Rink":                                 LegoBatman1LocationData("Shop", 45035996437), 
}

charshopsanity_locations = {
    "Buy Bruce Wayne":                              LegoBatman1LocationData("Shop", 45035996438),
    "Buy Alfred":                                   LegoBatman1LocationData("Shop", 45035996439),
    "Buy Batgirl":                                  LegoBatman1LocationData("Shop", 45035996440),
    "Buy Nightwing":                                LegoBatman1LocationData("Shop", 45035996441),
    "Buy Commissioner Gordon":                      LegoBatman1LocationData("Shop", 45035996442),
    "Buy Mad Hatter":                               LegoBatman1LocationData("Shop", 45035996443),
    "Buy Fishmonger":                               LegoBatman1LocationData("Shop", 45035996444),
    "Buy Scientist":                                LegoBatman1LocationData("Shop", 45035996445),
    "Buy Security Guard":                           LegoBatman1LocationData("Shop", 45035996446),
    "Buy Police Marksman":                          LegoBatman1LocationData("Shop", 45035996447),
    "Buy Police Officer":                           LegoBatman1LocationData("Shop", 45035996448),
    "Buy S.W.A.T.":                                 LegoBatman1LocationData("Shop", 45035996449),
    "Buy Sailor":                                   LegoBatman1LocationData("Shop", 45035996450),
    "Buy Miltary Police":                           LegoBatman1LocationData("Shop", 45035996451),
    "Buy Yeti":                                     LegoBatman1LocationData("Shop", 45035996452),
    "Buy Penguin Minion":                           LegoBatman1LocationData("Shop", 45035996453),
    "Buy Catwoman (Classic)":                       LegoBatman1LocationData("Shop", 45035996454),
    "Buy Man-Bat":                                  LegoBatman1LocationData("Shop", 45035996455),
    "Buy Joker (Tropical)":                         LegoBatman1LocationData("Shop", 45035996456),
    "Buy Poison Ivy Goon":                          LegoBatman1LocationData("Shop", 45035996457),
    "Buy Freeze Girl":                              LegoBatman1LocationData("Shop", 45035996458),
    "Buy Zoo Sweeper":                              LegoBatman1LocationData("Shop", 45035996459),
    "Buy Riddler Goon":                             LegoBatman1LocationData("Shop", 45035996460),
    "Buy Riddler Henchman":                         LegoBatman1LocationData("Shop", 45035996461),
    "Buy Penguin Goon":                             LegoBatman1LocationData("Shop", 45035996462),
    "Buy Penguin Henchman":                         LegoBatman1LocationData("Shop", 45035996463),
    "Buy Joker Goon":                               LegoBatman1LocationData("Shop", 45035996464),
    "Buy Clown Goon":                               LegoBatman1LocationData("Shop", 45035996465),
    "Buy Joker Henchman":                           LegoBatman1LocationData("Shop", 45035996466),
    "Buy Police Car":                               LegoBatman1LocationData("Shop", 45035996467),
    "Buy Police Bike":                              LegoBatman1LocationData("Shop", 45035996468),
    "Buy Police Van":                               LegoBatman1LocationData("Shop", 45035996469),
    "Buy Bat-Tank":                                 LegoBatman1LocationData("Shop", 45035996470),
    "Buy Two-Face's Armored Truck":                 LegoBatman1LocationData("Shop", 45035996471),
    "Buy Garbage Truck":                            LegoBatman1LocationData("Shop", 45035996472),
    "Buy Catwoman's Motorcycle":                    LegoBatman1LocationData("Shop", 45035996473),
    "Buy Mr.Freeze's Kart":                         LegoBatman1LocationData("Shop", 45035996474),
    "Buy Police Watercraft":                        LegoBatman1LocationData("Shop", 45035996475),
    "Buy Police Boat":                              LegoBatman1LocationData("Shop", 45035996476),
    "Buy Penguin Goon Submarine":                   LegoBatman1LocationData("Shop", 45035996478),
    "Buy Mad Hatter's Steamboat":                   LegoBatman1LocationData("Shop", 45035996477),
    "Buy Robin's Submarine":                        LegoBatman1LocationData("Shop", 45035996479),
    "Buy Mr.Freeze's Iceberg":                      LegoBatman1LocationData("Shop", 45035996480),               
    "Buy The Joker Van":                            LegoBatman1LocationData("Shop", 45035996481),
    "Buy Harley Quinn's Hammer Truck":              LegoBatman1LocationData("Shop", 45035996482),
    "Buy Police Helicopter":                        LegoBatman1LocationData("Shop", 45035996483),
    "Buy Bruce Wayne's Private Jet":                LegoBatman1LocationData("Shop", 45035996484),
    "Buy Goon Helicopter":                          LegoBatman1LocationData("Shop", 45035996485),
    "Buy Mad Hatter's Glider":                      LegoBatman1LocationData("Shop", 45035996485),
    "Buy Riddler Jet":                              LegoBatman1LocationData("Shop", 45035996486),
    "Buy Harbor Helicopter":                        LegoBatman1LocationData("Shop", 45035996487),
}

hostagesanity_locations = {
    "TRR Hero #1 - Room 1, Break window near spawn and defeat enemeies":                    LegoBatman1LocationData("You Can Bank On Batman",   45035996003),
    "TRR Hero #2 - Room 1, Inside Mind Control Door left of spawn, defeat enemies":         LegoBatman1LocationData("An Icy Reception",   45035996015),
    "TRR Hero #4 - Room 2, Break glass wall and defeat enemies":                            LegoBatman1LocationData("A Poisonous Appointment",   45035996038),
    "TRR Hero #5 - Room 1, Use Attract Machine and Double Jump on Leaves, defeat enemies":  LegoBatman1LocationData("The Face-Off",   45035996051),
    "PCP Hero #1 - Room 2, Fall down rails and defeat enemies, after first Catwoman fight": LegoBatman1LocationData("There She Goes Again",   45035996067),
    "PCP Hero #3 - Room 1, Far Right of room, defeat enemy":                                LegoBatman1LocationData("Under The City",   45035996083),
    "PCP Hero #4 - Room 2, Near batman suit in glass wall, defeat enemies":                 LegoBatman1LocationData("Zoo's Company",   45035996102),
    "PCP Hero #5 - Room 1, On the far right side of room, defeat enemies":                  LegoBatman1LocationData("Penguin's Lair",   45035996109),
    "TJR Hero #1 - Room 3, Use generator far right of room and use elevator and defeat enemies":LegoBatman1LocationData("Joker's Home Turf",   45035996127),
    "TJR Hero #2 - Room 2, Defeat enemies top right of tea cups":                           LegoBatman1LocationData("Little Fun at the Big Top",   45035996136),
    "TJR Hero #4 - Room 3, Defeat enemies south of spawn":                                  LegoBatman1LocationData("In the Dark Night",   45035996159),
    "TJR Hero #5 - Room 1, Bottom left of spawn, defeat enemies":                           LegoBatman1LocationData("To the Top of the Tower",   45035996165),
    "TRR Villian #1 - Room 2, Break Glass and defeat enemies":                              LegoBatman1LocationData("The Ridler Makes a Withdrawal",   45035996180),
    "TRR Villian #2 - Room 2, Break silver handle then go inside and defeat enemies":       LegoBatman1LocationData("On the Rocks",   45035996191),
    "TRR Villian #3 - Room 2, Bomb silver door, then go in and defeat enemy":               LegoBatman1LocationData("Green Fingers",   45035996204),
    "TRR Villian #4 - Room 1, Break glass door to meeting room then defeat enemy":          LegoBatman1LocationData("An Enterprising Theft",   45035996214),
    "TRR Villian #5 - Room 3, Break silver door then defeat enemy in sub room":             LegoBatman1LocationData("Breaking Blocks",   45035996239),
    "PCP Villian #1 - Room 1, Break glass window and defeat enemy":                         LegoBatman1LocationData("Rockin' the Docks",   45035996246),
    "PCP Villian #2 - Room 1, Break strength box, then build magnet wall, break window and defeat enemy":LegoBatman1LocationData("Stealing the Show",   45035996258),
    "PCP Villian #4 - Room 2, Use generator and go in sub room, then defeat enemies":       LegoBatman1LocationData("A Daring Rescue",   45035996283),
    "PCP Villian #5 - Room 1, Swim across toxic water and defeat enemies":                  LegoBatman1LocationData("Arctic World",   45035996293),
    "TJR Villian #1 - Room 1, Blow up silver gate and defeat enemies":                      LegoBatman1LocationData("A Surprise for the Commissioner",   45035996308),
    "TJR Villian #3 - Room 1, Bomb silver door, then go in heated room, and defeat enemies":LegoBatman1LocationData("The Joker's Masterpiece",   45035996331),
    "TJR Villian #4 - Room 1, Build rails, then double jump up and defeat enemies":         LegoBatman1LocationData("The Lure of the Night",   45035996342),
    "TJR Villian #5 - Room 2, Glide from cage and defeat enemy":                            LegoBatman1LocationData("Dying of Laughter",   45035996359),
}

kitsanity_locations = {
    # You Can Bank On Batman
    "TRR Hero #1 - Room 1, Top Of ladder near switch and grapple":                          LegoBatman1LocationData("You Can Bank On Batman",   45035996000),
    "TRR Hero #1 - Room 1, Garage Door from switch near grapple and ladder":                LegoBatman1LocationData("You Can Bank On Batman",   45035996001),
    "TRR Hero #1 - Break 5 Telephone Booths through out level":                             LegoBatman1LocationData("You Can Bank On Batman",   45035996002),
    "TRR Hero #1 - Room 1, Glass Window near spawn":                                        LegoBatman1LocationData("You Can Bank On Batman",   45035996004),
    "TRR Hero #1 - Room 1, Mind Control pannel near toxins":                                LegoBatman1LocationData("You Can Bank On Batman",   45035996005),
    "TRR Hero #1 - Room 1, In the sewer lid with garbage can on it":                        LegoBatman1LocationData("You Can Bank On Batman",   45035996006),
    "TRR Hero #1 - Room 1, Grapple under garbage can to silver window":                     LegoBatman1LocationData("You Can Bank On Batman",   45035996007),
    "TRR Hero #1 - Room 2, Pull window to stairs and walk in":                              LegoBatman1LocationData("You Can Bank On Batman",   45035996008),
    "TRR Hero #1 - Room 2, 2 cars in the garage near toxins":                               LegoBatman1LocationData("You Can Bank On Batman",   45035996009),
    "TRR Hero #1 - Room 2, Attract Suit machine behind glass wall":                         LegoBatman1LocationData("You Can Bank On Batman",   45035996010),
    # An Icy Reception
    "TRR Hero #2 - Room 1, Build and Climb rails on the right of spawn":                    LegoBatman1LocationData("An Icy Reception",   45035996012),
    "TRR Hero #2 - Room 1, Destroy Wood Barrier right of spawn after climbing rails":       LegoBatman1LocationData("An Icy Reception",   45035996013),
    "TRR Hero #2 - Room 1, Strength behind truck left of spawn":                            LegoBatman1LocationData("An Icy Reception",   45035996014),
    "TRR Hero #2 - Room 1, Climb Rails inside Mind Control Door left of spawn":             LegoBatman1LocationData("An Icy Reception",   45035996016),
    "TRR Hero #2 - Room 1, Silver object above rails behind gate north of spawn":           LegoBatman1LocationData("An Icy Reception",   45035996017),
    "TRR Hero #2 - Room 1, Drive truck to platform by spawn and blow up silver objects":    LegoBatman1LocationData("An Icy Reception",   45035996018),
    "TRR Hero #2 - Room 2, Use female door and blow up silver objects":                     LegoBatman1LocationData("An Icy Reception",   45035996019),
    "TRR Hero #2 - Room 3, Press switch near toxic gas and blow up silver object":          LegoBatman1LocationData("An Icy Reception",   45035996021),
    "TRR Hero #2 - Room 3, Glide across, blow up vent near fan and ride fan":               LegoBatman1LocationData("An Icy Reception",   45035996022),
    "TRR Hero #2 - Room 3, Glide across, mind control guy to pull switch":                  LegoBatman1LocationData("An Icy Reception",   45035996023),
    # Two-Face Chase
    "TRR Hero #3 - Room 1, Destroy 3 dumpsters":                                            LegoBatman1LocationData("Two-Face Chase",   45035996024),
    "TRR Hero #3 - Room 1, Destroy the manhole cover south of spawn":                       LegoBatman1LocationData("Two-Face Chase",   45035996025),
    "TRR Hero #3 - Room 2, Destroy trash dumpster, southwest of entrance":                  LegoBatman1LocationData("Two-Face Chase",   45035996026),
    "TRR Hero #3 - Room 2, Destroy 3 blue cars":                                            LegoBatman1LocationData("Two-Face Chase",   45035996027),
    "TRR Hero #3 - Room 2, Down the ramp, press the pannel with Joker's Van":               LegoBatman1LocationData("Two-Face Chase",   45035996028),
    "TRR Hero #3 - Room 2, Down the ramp, press the pannel with Harley's Truck":            LegoBatman1LocationData("Two-Face Chase",   45035996029),
    "TRR Hero #3 - Room 2, Destroy the north set of supports":                              LegoBatman1LocationData("Two-Face Chase",   45035996030),
    "TRR Hero #3 - Room 2, Destroy the south set of supports":                              LegoBatman1LocationData("Two-Face Chase",   45035996033),
    "TRR Hero #3 - Room 3, Destroy telephon booth in the far back left":                    LegoBatman1LocationData("Two-Face Chase",   45035996034),
    "TRR Hero #3 - Destroy 3 food carts through out level":                                 LegoBatman1LocationData("Two-Face Chase",   45035996035),
    # A Poisonous Appointment
    "TRR Hero #4 - Room 1, Build and destroy all carrots":                                  LegoBatman1LocationData("A Poisonous Appointment",   45035996036),
    "TRR Hero #4 - Room 1, Jump on the tree off of the tractor, jump to the right tree":    LegoBatman1LocationData("A Poisonous Appointment",   45035996036),
    "TRR Hero #4 - Room 2, Go through the heat gas and use the tech pad":                   LegoBatman1LocationData("A Poisonous Appointment",   45035996037),    
    "TRR Hero #4 - Room 2, push the glass box and jump on flowers":                         LegoBatman1LocationData("A Poisonous Appointment",   45035996039),
    "TRR Hero #4 - Room 2, Build potted plant and double jump to rail":                     LegoBatman1LocationData("A Poisonous Appointment",   45035996040),
    "TRR Hero #4 - Build 3 carrots through out level":                                      LegoBatman1LocationData("A Poisonous Appointment",   45035996041),
    "TRR Hero #4 - Room 3, Sink down near entrance":                                        LegoBatman1LocationData("A Poisonous Appointment",   45035996042),
    "TRR Hero #4 - Room 3, Magnet walk up from rail and blow up silver object":             LegoBatman1LocationData("A Poisonous Appointment",   45035996043),    
    "TRR Hero #4 - Room 4, Jump on the back pipe and walk right":                           LegoBatman1LocationData("A Poisonous Appointment",   45035996045),
    "TRR Hero #4 - Room 5, Jump from rail":                                                 LegoBatman1LocationData("A Poisonous Appointment",   45035996046),
    # The Face-Off
    "TRR Hero #5 - Room 1, After gap Jump on all 5 poles":                                  LegoBatman1LocationData("The Face-Off",   45035996047),
    "TRR Hero #5 - Room 1, Far Right side of room grapple":                                 LegoBatman1LocationData("The Face-Off",   45035996048),
    "TRR Hero #5 - Room 1, Use Tech Pad and go through revolving door":                     LegoBatman1LocationData("The Face-Off",   45035996049),
    "TRR Hero #5 - Room 1, Build Neon Giant Dollar Sign":                                   LegoBatman1LocationData("The Face-Off",   45035996050),
    "TRR Hero #5 - Room 1, Use Attract Machine and Double Jump on Leaves and Double jump":  LegoBatman1LocationData("The Face-Off",   45035996052),
    "TRR Hero #5 - Room 2, After Two Face Fight, jump down bridge into toxin":              LegoBatman1LocationData("The Face-Off",   45035996054),
    "TRR Hero #5 - Room 2, After Two Face Fight, right side grow plant":                    LegoBatman1LocationData("The Face-Off",   45035996055),
    "TRR Hero #5 - Room 4, Use the switch, blow up the silver object and use the generator":LegoBatman1LocationData("The Face-Off",   45035996056),
    "TRR Hero #5 - Boss Room, Right side opening":                                          LegoBatman1LocationData("The Face-Off",   45035996057),
    "TRR Hero #5 - Boss Room, Destroy 5 large containers of money":                         LegoBatman1LocationData("The Face-Off",   45035996058),
    # There She Goes Again
    "PCP Hero #1 - Room 1, Inside Female Pannel Door, South Magnet Wall":                   LegoBatman1LocationData("There She Goes Again",   45035996059),
    "PCP Hero #1 - Room 1, Break South Purple Box, build car, drive car in garage by robin suit":LegoBatman1LocationData("There She Goes Again",   45035996060),
    "PCP Hero #1 - Room 1, Blow Up silver barrels then build telephone pole, pull switch and sink":LegoBatman1LocationData("There She Goes Again",   45035996061),
    "PCP Hero #1 - Room 1, Find 3 Carrots":                                                 LegoBatman1LocationData("There She Goes Again",   45035996062),
    "PCP Hero #1 - Room 1, Build Blue Machine near dock and sink":                          LegoBatman1LocationData("There She Goes Again",   45035996063),
    "PCP Hero #1 - Room 2, Build and Destroy flowers near bridge":                          LegoBatman1LocationData("There She Goes Again",   45035996064),
    "PCP Hero #1 - Room 2, Remove Trash Can near bridge and grapple":                       LegoBatman1LocationData("There She Goes Again",   45035996065),
    "PCP Hero #1 - Room 2, Remove Trash Can near fan and go under":                         LegoBatman1LocationData("There She Goes Again",   45035996066),
    "PCP Hero #1 - Room 2, Use tech pad to push buttons, blow up silver, fly to glass pannel up left":LegoBatman1LocationData("There She Goes Again",   45035996068),
    "PCP Hero #1 - Room 2, Use tech pad to push buttons, blow up silver, fly to glass pannel right and sink":LegoBatman1LocationData("There She Goes Again",   45035996069),
    # Batboat Battle
    "PCP Hero #2 - Room 1, Power Light House and use ramp":                                 LegoBatman1LocationData("Batboat Battle",   45035996071),
    "PCP Hero #2 - Room 1, Blow up wall near silver gate, blow bomb into silver box":       LegoBatman1LocationData("Batboat Battle",   45035996072),
    "PCP Hero #2 - Room 1, Submerge and hit 2 buttons, then sink ship with torpedos":       LegoBatman1LocationData("Batboat Battle",   45035996073),
    "PCP Hero #2 - Room 1, Pull pipe near door":                                            LegoBatman1LocationData("Batboat Battle",   45035996074),
    "PCP Hero #2 - Room 2, Submerge under ice":                                             LegoBatman1LocationData("Batboat Battle",   45035996075),
    "PCP Hero #2 - Room 2, Destroy Silver Box on Toxic Water":                              LegoBatman1LocationData("Batboat Battle",   45035996076),
    "PCP Hero #2 - Room 2, Blow Up Silver around pipe":                                     LegoBatman1LocationData("Batboat Battle",   45035996078),
    "PCP Hero #2 - Shoot 3 buoys with torpedo":                                             LegoBatman1LocationData("Batboat Battle",   45035996077),
    "PCP Hero #2 - Boss Room, Submerge under ice again":                                    LegoBatman1LocationData("Batboat Battle",   45035996080),
    "PCP Hero #2 - Boss Room, Destroy Silver Boxes on Toxic Water again":                   LegoBatman1LocationData("Batboat Battle",   45035996081),
    # Under the City
    "PCP Hero #3 - Room 1, Glide from robin suit and use mind control door, open cage":     LegoBatman1LocationData("Under The City",   45035996084),
    "PCP Hero #3 - Room 1, Double Jump from rail near middle of room":                      LegoBatman1LocationData("Under The City",   45035996085),
    "PCP Hero #3 - Room 2, Pull Blue Garbage can and break glass":                          LegoBatman1LocationData("Under The City",   45035996086),
    "PCP Hero #3 - Room 2, Double jump from robin suit to rail and walk left":              LegoBatman1LocationData("Under The City",   45035996087),
    "PCP Hero #3 - Room 2, Use Attract Machine near rails from far right of room, use boat and hit buoys":LegoBatman1LocationData("Under The City",  45035996088),
    "PCP Hero #3 - Room 3, Walk through toxins and pull switch":                            LegoBatman1LocationData("Under The City",   45035996089),
    "PCP Hero #3 - Room 3, Near silver gate, build Toilet and push it, then double jump up":LegoBatman1LocationData("Under The City",   45035996090),
    "PCP Hero #3 - Room 3, Use extention platform to blow up silver object and jump":       LegoBatman1LocationData("Under The City",   45035996091),
    "PCP Hero #3 - Room 3, Sink in sewer water after raising it":                           LegoBatman1LocationData("Under The City",   45035996092),
    "PCP Hero #3 - Room 3, Build Machine and use generator":                                LegoBatman1LocationData("Under The City",   45035996093),
    # Zoo's Company
    "PCP Hero #4 - Room 1, Use Female Pannel, blow up silver objects and run over bouys":   LegoBatman1LocationData("Zoo's Company",   45035996094),
    "PCP Hero #4 - Room 1, Open Strength Gate and cross toxic and double jump up":          LegoBatman1LocationData("Zoo's Company",   45035996095),
    "PCP Hero #4 - Room 1, Use Attract Machine, pieces found across the room":              LegoBatman1LocationData("Zoo's Company",   45035996096),
    "PCP Hero #4 - Room 1, Double Jump from vending machine and blow up silver objects":    LegoBatman1LocationData("Zoo's Company",   45035996097),
    "PCP Hero #4 - Room 2, Build totem then grow plant":                                    LegoBatman1LocationData("Zoo's Company",   45035996098),
    "PCP Hero #4 - Room 2, Break silver rocks in lion enclosure":                           LegoBatman1LocationData("Zoo's Company",   45035996100),
    "PCP Hero #4 - Room 2, Top right cornor of elephant enclosure":                         LegoBatman1LocationData("Zoo's Company",   45035996101),  
    "PCP Hero #4 - Room 3, Jump on big lily pad behind boat":                               LegoBatman1LocationData("Zoo's Company",   45035996103),
    "PCP Hero #4 - Room 3, Freeze water near waterfall and jump up":                        LegoBatman1LocationData("Zoo's Company",   45035996105),
    "PCP Hero #4 - Room 3, Use strength thing near batman suit":                            LegoBatman1LocationData("Zoo's Company",   45035996104),
    # Penguin's Lair
    "PCP Hero #5 - Room 1, Break glass cover near spawn and sink down":                     LegoBatman1LocationData("Penguin's Lair",   45035996106),
    "PCP Hero #5 - Room 1, Freeze water near silver gate and blow it up":                   LegoBatman1LocationData("Penguin's Lair",   45035996107),
    "PCP Hero #5 - Room 1, Double Jump on rails to roof of cabin":                          LegoBatman1LocationData("Penguin's Lair",   45035996108),
    "PCP Hero #5 - Room 1, Grow 3 carrots all in room 1":                                   LegoBatman1LocationData("Penguin's Lair",   45035996110),
    "PCP Hero #5 - Room 1, Right side of room break trees, grapple and glide":              LegoBatman1LocationData("Penguin's Lair",   45035996111),
    "PCP Hero #5 - Boss Room, Glide to ice berg in back of room":                           LegoBatman1LocationData("Penguin's Lair",   45035996112),
    "PCP Hero #5 - Boss Room, Double jump up in right of room":                             LegoBatman1LocationData("Penguin's Lair",   45035996113),
    "PCP Hero #5 - Boss Room, Explode silver object left of room with penguin then walk in toxins":LegoBatman1LocationData("Penguin's Lair",   45035996114),
    "PCP Hero #5 - Boss Room, Break glass near treadmil and build heated object":           LegoBatman1LocationData("Penguin's Lair",   45035996115),
    "PCP Hero #5 - Boss Room, Batarang machines connected during fight after blowing up tredmills":LegoBatman1LocationData("Penguin's Lair",   45035996117),
    # Joker's Home Turf
    "TJR Hero #1 - Room 1, Blow up silver objects and build fan":                           LegoBatman1LocationData("Joker's Home Turf",   45035996118),
    "TJR Hero #1 - Room 1, Suck up all toxins in room and then deposit them in machine far right of room":LegoBatman1LocationData("Joker's Home Turf",   45035996119),
    "TJR Hero #1 - Room 1, Go in to mind control pannel room and solve puzzle":             LegoBatman1LocationData("Joker's Home Turf",   45035996120),
    "TJR Hero #1 - Room 1, Use generator and double jump up to rail":                       LegoBatman1LocationData("Joker's Home Turf",   45035996122),
    "TJR Hero #1 - Room 2, Use Tech Pannel to blow up exhaust pipes then build.":           LegoBatman1LocationData("Joker's Home Turf",   45035996121),
    "TJR Hero #1 - Room 2, Pull switch in toxins":                                          LegoBatman1LocationData("Joker's Home Turf",   45035996123),
    "TJR Hero #1 - Room 2, Use strength and double jump to rails":                          LegoBatman1LocationData("Joker's Home Turf",   45035996124),
    "TJR Hero #1 - Room 2, Swim in toxin waters near the end of the room":                  LegoBatman1LocationData("Joker's Home Turf",   45035996125),
    "TJR Hero #1 - Room 3, Use generator far right of room and use elevator and push turnstile":LegoBatman1LocationData("Joker's Home Turf",   45035996128),
    "TJR Hero #1 - Boss Room, Climb up magnet wall and push ramp down":                      LegoBatman1LocationData("Joker's Home Turf",   45035996129),
    # Little Fun at Big Top
    "TJR Hero #2 - Room 1, Push bus behind spawn then pull trash can, double jump up and build tight rope":LegoBatman1LocationData("Little Fun at the Big Top",   45035996130),
    "TJR Hero #2 - Room 1, Break glass infront of carnival game, break carnival game":      LegoBatman1LocationData("Little Fun at the Big Top",   45035996131),
    "TJR Hero #2 - Room 1, Blow Up silver object above carnival game and sink":             LegoBatman1LocationData("Little Fun at the Big Top",   45035996132),
    "TJR Hero #2 - Room 1, Use Tech Pannel on duck game, then destroy all ducks":           LegoBatman1LocationData("Little Fun at the Big Top",   45035996133),
    "TJR Hero #2 - Room 2, Break glass & silver object, build grapple and grapple up":      LegoBatman1LocationData("Little Fun at the Big Top",   45035996135),
    "TJR Hero #2 - Room 2, Use generator near tea cups, after it spins go in bottom left cup":LegoBatman1LocationData("Little Fun at the Big Top", 45035996137),
    "TJR Hero #2 - Room 2, Ride down spiral slide":                                         LegoBatman1LocationData("Little Fun at the Big Top",   45035996138),
    "TJR Hero #2 - Room 3, Use tech pad to bring colored boats in the correct colored homes":LegoBatman1LocationData("Little Fun at the Big Top",  45035996139),
    "TJR Hero #2 - Room 3, Pull door and ride bumper cars":                                 LegoBatman1LocationData("Little Fun at the Big Top",   45035996140),
    "TJR Hero #2 - Room 3, Go across toxins near boss entrance, grapple and build tightrope":LegoBatman1LocationData("Little Fun at the Big Top",  45035996141),
    # Flight of the Bat
    "TJR Hero #3 - Room 1, Destroy all 6 missle launchers":                                 LegoBatman1LocationData("Flight of the Bat",   45035996142),
    "TJR Hero #3 - Room 1, Fly near silver pipe on the right":                              LegoBatman1LocationData("Flight of the Bat",   45035996143),
    "TJR Hero #3 - Room 1, Fly up on railway":                                              LegoBatman1LocationData("Flight of the Bat",   45035996144),
    "TJR Hero #3 - Room 1, Blow up silver object near hotel sign":                          LegoBatman1LocationData("Flight of the Bat",   45035996145),
    "TJR Hero #3 - Room 2, Shoot grey pipe":                                                LegoBatman1LocationData("Flight of the Bat",   45035996146),
    "TJR Hero #3 - Room 2, Destroy 3 silver valves":                                        LegoBatman1LocationData("Flight of the Bat",   45035996148),
    "TJR Hero #3 - Room 2, Torpedo gray barrel and tow blue barrel to button":              LegoBatman1LocationData("Flight of the Bat",   45035996149),
    "TJR Hero #3 - Boss Room, Go through toxic gas and shoot stuff":                        LegoBatman1LocationData("Flight of the Bat",   45035996150),
    "TJR Hero #3 - Boss Room, Shoot all 3 near toxic gas":                                  LegoBatman1LocationData("Flight of the Bat",   45035996151),
    "TJR Hero #3 - Boss Room, Fly south and grab item":                                     LegoBatman1LocationData("Flight of the Bat",   45035996152),
    # In the Dark Night
    "TJR Hero #4 - Room 1, Use Strength on door and break glass":                           LegoBatman1LocationData("In the Dark Night",   45035996153),
    "TJR Hero #4 - Room 1, Use generator and double jump on ladder, then break glass":      LegoBatman1LocationData("In the Dark Night",   45035996154),
    "TJR Hero #4 - Room 1, Jump on rails and go to grapple, grapple up and go to back left corner":LegoBatman1LocationData("In the Dark Night",   45035996155),
    "TJR Hero #4 - Room 1, Destroy 3 cakes":                                                LegoBatman1LocationData("In the Dark Night",   45035996156),
    "TJR Hero #4 - Room 2, Grow 3 plants then sink in fish tank":                           LegoBatman1LocationData("In the Dark Night",   45035996157),
    "TJR Hero #4 - Room 2, Use attract machine to build helicopter, then use tech pannel to fly helicopter into buttons in center of room":LegoBatman1LocationData("In the Dark Night",   45035996158),
    "TJR Hero #4 - Room 3, Pull truck away from garage and blow up silver obeject":         LegoBatman1LocationData("In the Dark Night",   45035996160),
    "TJR Hero #4 - Room 3, Go across toxins then blow up silver objects, build and walk on magnet wall":LegoBatman1LocationData("In the Dark Night",   45035996161),
    "TJR Hero #4 - Room 3, Blow up 3rd silver sewer lid":                                  LegoBatman1LocationData("In the Dark Night",   45035996163),
    "TJR Hero #4 - Boss Room, Break glass and use generator":                              LegoBatman1LocationData("In the Dark Night",   45035996164),
    # To the Top of the Tower
    "TJR Hero #5 - Room 1, Blow up 3 silver gargoyles":                                     LegoBatman1LocationData("To the Top of the Tower",   45035996166),
    "TJR Hero #5 - Room 1, Left of room, break potted plants and build ladder then press buttons":LegoBatman1LocationData("To the Top of the Tower",   45035996167),
    "TJR Hero #5 - Room 1, Left side of room, build magnet wall, break glass":              LegoBatman1LocationData("To the Top of the Tower",   45035996168),
    "TJR Hero #5 - Room 1, Use attract machine right side of room":                         LegoBatman1LocationData("To the Top of the Tower",   45035996169),
    "TJR Hero #5 - Room 1, Pull switch then jump to platform, near robin suit":             LegoBatman1LocationData("To the Top of the Tower",   45035996170),
    "TJR Hero #5 - Room 1, Use generator on right side":                                    LegoBatman1LocationData("To the Top of the Tower",   45035996171),
    "TJR Hero #5 - Room 2, Climb up magnet wall then walk along edge":                      LegoBatman1LocationData("To the Top of the Tower",   45035996172),
    "TJR Hero #5 - Room 2, Climb up magnet wall then walk a little past switch":            LegoBatman1LocationData("To the Top of the Tower",   45035996173),
    "TJR Hero #5 - Boss Room, Cause train crash from Batman Torpedo in back then blow up silver pipe":LegoBatman1LocationData("To the Top of the Tower",   45035996175),
    "TJR Hero #5 - Boss Room, Blow up silver object right side":                            LegoBatman1LocationData("To the Top of the Tower",   45035996176),
    # The Ridler Makes a Withdrawal
    "TRR Villian #1 - Room 1, Pull garbage cans with strong character":                     LegoBatman1LocationData("The Ridler Makes a Withdrawal",   45035996178),
    "TRR Villian #1 - Room 1, Pull white truck in parking lot then double jump up":         LegoBatman1LocationData("The Ridler Makes a Withdrawal",   45035996177),
    "TRR Villian #1 - Room 1, Drive Blue car to machine in bottom right of parking lot":    LegoBatman1LocationData("The Ridler Makes a Withdrawal",   45035996179),    
    "TRR Villian #1 - Room 2, Break silver window near glass":                              LegoBatman1LocationData("The Ridler Makes a Withdrawal",   45035996181),
    "TRR Villian #1 - Room 2, Batarang window then grapple up to it":                       LegoBatman1LocationData("The Ridler Makes a Withdrawal",   45035996182),
    "TRR Villian #1 - Room 2, Break glass window with tv after silver gate":                LegoBatman1LocationData("The Ridler Makes a Withdrawal",   45035996183),
    "TRR Villian #1 - Room 3, Double jump on rails near entrance":                          LegoBatman1LocationData("The Ridler Makes a Withdrawal",   45035996185),
    "TRR Villian #1 - Room 3, Break barrels left side of bank":                             LegoBatman1LocationData("The Ridler Makes a Withdrawal",   45035996186),
    "TRR Villian #1 - Room 3, Break glass window near ladder":                              LegoBatman1LocationData("The Ridler Makes a Withdrawal",   45035996187),
    "TRR Villian #1 - Room 3, Blow up silver object near police car":                       LegoBatman1LocationData("The Ridler Makes a Withdrawal",   45035996188),
    # On the Rocks
    "TRR Villian #2 - Room 1, Drive Ice Cream truck into garage":                              LegoBatman1LocationData("On the Rocks",   45035996189),
    "TRR Villian #2 - Room 1, Break 3 snowmen (One is in glass door sub room)":                LegoBatman1LocationData("On the Rocks",   45035996200),
    "TRR Villian #2 - Room 1, Pull window near fan":                                           LegoBatman1LocationData("On the Rocks",   45035996190),  
    "TRR Villian #2 - Room 2, Break silver handle then go inside near ladder":                 LegoBatman1LocationData("On the Rocks",   45035996192), 
    "TRR Villian #2 - Room 2, Walk up magnet wall then go down":                               LegoBatman1LocationData("On the Rocks",   45035996194),
    "TRR Villian #2 - Room 3, Go up elevator then go left, jump down rails":                   LegoBatman1LocationData("On the Rocks",   45035996195),
    "TRR Villian #2 - Room 3, Use attract machine":                                            LegoBatman1LocationData("On the Rocks",   45035996196),
    "TRR Villian #2 - Room 3, Blow up silver handle then blow up silver object inside with guy":LegoBatman1LocationData("On the Rocks",  45035996197),
    "TRR Villian #2 - Room 4, Walk up magnet wall then glide":                                 LegoBatman1LocationData("On the Rocks",   45035996198),
    "TRR Villian #2 - Room 4, Mind control guy to the left side":                              LegoBatman1LocationData("On the Rocks",   45035996199),
    # Green Fingers
    "TRR Villian #3 - Room 1, Use tech pannel at spawn then drive car through flags":          LegoBatman1LocationData("Green Fingers",   45035996201),
    "TRR Villian #3 - Room 1, Blow up 2 silver gates, then grapple twice, then double jump":   LegoBatman1LocationData("Green Fingers",   45035996202),
    "TRR Villian #3 - Room 1, Left side jump on rails":                                        LegoBatman1LocationData("Green Fingers",   45035996203),
    "TRR Villian #3 - Room 3, Blow up silver door then solve pushing puzzle":                  LegoBatman1LocationData("Green Fingers",   45035996206),
    "TRR Villian #3 - Room 4, Sink in hole in fountain then break glass and pull switch":      LegoBatman1LocationData("Green Fingers",   45035996207),
    "TRR Villian #3 - Room 5, Break glass then build magnet wall":                             LegoBatman1LocationData("Green Fingers",   45035996208),
    "TRR Villian #3 - Room 6, Blow up silver door, break machine, build magnet wall, push it, walk on wall":LegoBatman1LocationData("Green Fingers",   45035996209),
    "TRR Villian #3 - Room 6, Grapple onto heated pipe, then go in hole near heated pipe":     LegoBatman1LocationData("Green Fingers",   45035996210),
    "TRR Villian #3 - Room 6, Break glass door then sink, walk forward then swim up":          LegoBatman1LocationData("Green Fingers",   45035996211),
    "TRR Villian #3 - Room 7, Blow up silver object left side of room":                        LegoBatman1LocationData("Green Fingers",   45035996112),
    # An Enterprising Theft
    "TRR Villian #4 - Room 1, Break glass, build switches, double jump to item":               LegoBatman1LocationData("An Enterprising Theft",   45035996213),
    "TRR Villian #4 - Room 1, Break glass door to scientist room, build contraptions, ride dog to open door near spawn, use tech suit in sub room":LegoBatman1LocationData("An Enterprising Theft",   45035996215),
    "TRR Villian #4 - Room 1, Blow up silver object then open door":                           LegoBatman1LocationData("An Enterprising Theft",   45035996216),
    "TRR Villian #4 - Room 1, Break glass on top floor":                                       LegoBatman1LocationData("An Enterprising Theft",   45035996217),
    "TRR Villian #4 - Room 2, Blow up silver gate, then build helicopter, use tech suit and fly to middle of room":LegoBatman1LocationData("An Enterprising Theft",   45035996218),
    "TRR Villian #4 - Room 2, Raise toxin level in main room, then mind control guy, pull switch, then jump in capsule":LegoBatman1LocationData("An Enterprising Theft",   45035996219),
    "TRR Villian #4 - Room 3, Use batarang on grate then double jump up":                      LegoBatman1LocationData("An Enterprising Theft",   45035996220),
    "TRR Villian #4 - Room 3, Break glass door then build weight":                             LegoBatman1LocationData("An Enterprising Theft",   45035996221),
    "TRR Villian #4 - Room 3, Walk on heated pipe and ride on fan":                            LegoBatman1LocationData("An Enterprising Theft",   45035996222),
    "TRR Villian #4 - Room 4, Freestanding item by laser canon":                                            LegoBatman1LocationData("An Enterprising Theft",   45035996224),
    # Breaking Blocks
    "TRR Villian #5 - Room 1, Jump down on vine leafs":                                        LegoBatman1LocationData("Breaking Blocks",   45035996225),
    "TRR Villian #5 - Room 1, Shoot 3 cameras with the helicopter":                            LegoBatman1LocationData("Breaking Blocks",   45035996226),
    "TRR Villian #5 - Room 2, Batarang 3 paintings then build and pull switch":                LegoBatman1LocationData("Breaking Blocks",   45035996227),
    "TRR Villian #5 - Room 2, Break glass pane, then use attract machine, then walk up magnet wall":LegoBatman1LocationData("Breaking Blocks",   45035996228),
    "TRR Villian #5 - Room 3, Push bookshelf then break boxes":                                LegoBatman1LocationData("Breaking Blocks",   45035996229),
    "TRR Villian #5 - Room 3, Break silver door then blow up silver cage":                     LegoBatman1LocationData("Breaking Blocks",   45035996240),
    "TRR Villian #5 - Room 4, Destroy 4 gold items":                                           LegoBatman1LocationData("Breaking Blocks",   45035996242),
    "TRR Villian #5 - Room 4, Blow up silver cage near pushable block":                        LegoBatman1LocationData("Breaking Blocks",   45035996243),
    "TRR Villian #5 - Room 5, Break glass, build magnet wall, climb magnet wall, push cage":   LegoBatman1LocationData("Breaking Blocks",   45035996244),
    "TRR Villian #5 - Room 5, Blow up silver door, go up ladder, blow up silver cage":         LegoBatman1LocationData("Breaking Blocks",   45035996245),
    # Rockin' the Docks
    "PCP Villian #1 - Room 1, Break glass window and jump up rails":                           LegoBatman1LocationData("Rockin' the Docks",   45035996247),
    "PCP Villian #1 - Room 1, Grow 3 carrots from breaking red canisters":                     LegoBatman1LocationData("Rockin' the Docks",   45035996248),
    "PCP Villian #1 - Room 1, Drive 2 trucks onto orange buttons":                             LegoBatman1LocationData("Rockin' the Docks",   45035996249),
    "PCP Villian #1 - Room 1, Break open ship":                                                LegoBatman1LocationData("Rockin' the Docks",   45035996250),
    "PCP Villian #1 - Room 2, Grow plant ladder and walk right":                               LegoBatman1LocationData("Rockin' the Docks",   45035996251),
    "PCP Villian #1 - Room 2, Break 5 objects on edge of dock":                                LegoBatman1LocationData("Rockin' the Docks",   45035996253),
    "PCP Villian #1 - Room 3, Use generator then use tech pannel to ride boats through barrels":LegoBatman1LocationData("Rockin' the Docks",  45035996254),
    "PCP Villian #1 - Room 3, Swim in toxic water":                                            LegoBatman1LocationData("Rockin' the Docks",   45035996255),
    "PCP Villian #1 - Room 3, Use Female Door then go in sub room and use attract machine then break jukebox":LegoBatman1LocationData("Rockin' the Docks",   45035996256),
    "PCP Villian #1 - Room 3, Go up elevator then walk left":                                  LegoBatman1LocationData("Rockin' the Docks",   45035996257),
    # Stealing the Show
    "PCP Villian #2 - Room 1, Break strength box, then build magnet wall then go to left side and jump":LegoBatman1LocationData("Stealing the Show",   45035996259),
    "PCP Villian #2 - Room 1, Break 3 neon signs":                                             LegoBatman1LocationData("Stealing the Show",   45035996260),
    "PCP Villian #2 - Room 1, Grow plants and climb up":                                       LegoBatman1LocationData("Stealing the Show",   45035996261),
    "PCP Villian #2 - Room 1, Walk behind glass after helicopter fight":                       LegoBatman1LocationData("Stealing the Show",   45035996262),
    "PCP Villian #2 - Room 1, Jump down near 2 man switch after helicopter fight":             LegoBatman1LocationData("Stealing the Show",   45035996263),
    "PCP Villian #2 - Room 1, Walk up magnet wall near gargoyle statue after helicopter fight":LegoBatman1LocationData("Stealing the Show",   45035996264),
    "PCP Villian #2 - Room 2, Break glass container on left side floor 1":                     LegoBatman1LocationData("Stealing the Show",   45035996265),
    "PCP Villian #2 - Room 2, Break right box in skeleton dinosaurs area":                     LegoBatman1LocationData("Stealing the Show",   45035996266),
    "PCP Villian #2 - Room 2, Break glass continers and build catapult and use it":            LegoBatman1LocationData("Stealing the Show",   45035996268),
    "PCP Villian #2 - Room 2, Pull statue, then double jump to ladder and walk left":          LegoBatman1LocationData("Stealing the Show",   45035996269),
    # Harboring a Grudge
    "PCP Villian #3 - Room 1, Use torpedo on toxic canister":                                  LegoBatman1LocationData("Harboring a Grudge",   45035996270),
    "PCP Villian #3 - Room 1, Destroy 3 brown structures":                                     LegoBatman1LocationData("Harboring a Grudge",   45035996271),
    "PCP Villian #3 - Room 1, Tow 2 bombs into 2 silver objects":                              LegoBatman1LocationData("Harboring a Grudge",   45035996272),
    "PCP Villian #3 - Room 2, Destroy 5 buoys in the water":                                   LegoBatman1LocationData("Harboring a Grudge",   45035996273),
    "PCP Villian #3 - Room 2, Shoot bridges on corner near entrance":                          LegoBatman1LocationData("Harboring a Grudge",   45035996275),
    "PCP Villian #3 - Room 2, Drive off of ramp":                                              LegoBatman1LocationData("Harboring a Grudge",   45035996276),
    "PCP Villian #3 - Room 2, Shoot police boat in toxic water":                               LegoBatman1LocationData("Harboring a Grudge",   45035996277),
    "PCP Villian #3 - Room 2, Tow 2 bombs to 2 silver objects near end of room then shoot crate":LegoBatman1LocationData("Harboring a Grudge", 45035996278),
    "PCP Villian #3 - Boss Room, Submerge and collect item infront of dock infront button on the left side of room":LegoBatman1LocationData("Harboring a Grudge",   45035996279),
    "PCP Villian #3 - Boss Room, Use Robin Torpedo on colored wall":                           LegoBatman1LocationData("Harboring a Grudge",   45035996280),
    # A Daring Rescue
    "PCP Villian #4 - Room 1, Bomb silver sewer lid then walk along toxins":                   LegoBatman1LocationData("A Daring Rescue",   45035996282),
    "PCP Villian #4 - Room 2, Use generator and go in sub room, then build instruments and wait":LegoBatman1LocationData("A Daring Rescue",   45035996284),
    "PCP Villian #4 - Room 2, Go through heat pipe to enter sub room, then solve puzzle":      LegoBatman1LocationData("A Daring Rescue",   45035996285),
    "PCP Villian #4 - Room 3, Destroy 5 TVs during the alligator sequence":                    LegoBatman1LocationData("A Daring Rescue",   45035996286),
    "PCP Villian #4 - Room 3, Break glass door then pull switch, and then go up steps":        LegoBatman1LocationData("A Daring Rescue",   45035996287),
    "PCP Villian #4 - Room 5, Go in top left stall":                                           LegoBatman1LocationData("A Daring Rescue",   45035996288),
    "PCP Villian #4 - Room 6, Use attract machine":                                            LegoBatman1LocationData("A Daring Rescue",   45035996289),
    "PCP Villian #4 - Room 6, Use mind control pannel to enter sub room, then park 3 cars":    LegoBatman1LocationData("A Daring Rescue",   45035996290),
    "PCP Villian #4 - Room 7, Walk up magnet wall bottom left of room":                        LegoBatman1LocationData("A Daring Rescue",   45035996291),
    "PCP Villian #4 - Room 8, Open jail door bottom right of room":                            LegoBatman1LocationData("A Daring Rescue",   45035996292),
    # Artic World
    "PCP Villian #5 - Room 1, Slide on ice, then sink and pull switch":                         LegoBatman1LocationData("Arctic World",   45035996295),
    "PCP Villian #5 - Room 1, Climb up magnet wall, pull gate, use generator, grapple and wait":LegoBatman1LocationData("Arctic World",   45035996296),
    "PCP Villian #5 - Room 1, Break glass next to falling platform":                           LegoBatman1LocationData("Arctic World",   45035996297),
    "PCP Villian #5 - Room 1, Double jump on right side, build gate, use female pannel and ski":LegoBatman1LocationData("Arctic World",   45035996298),
    "PCP Villian #5 - Room 2, Use sonic suit near glass mirror and see shark":                 LegoBatman1LocationData("Arctic World",   45035996299),
    "PCP Villian #5 - Room 2, Cross toxins, pull heavy object on button, press other 2 buttons":LegoBatman1LocationData("Arctic World",   45035996300),
    "PCP Villian #5 - Room 3, Slide through all of the gates":                                 LegoBatman1LocationData("Arctic World",   45035996301),
    "PCP Villian #5 - Room 4, Blow up silver door, left side, then double jump on trampoline": LegoBatman1LocationData("Arctic World",   45035996302),
    "PCP Villian #5 - Room 4, Sink down into ice berg":                                        LegoBatman1LocationData("Arctic World",   45035996303),
    "PCP Villian #5 - Room 4, Freeze ice cube, push it, double jump to switch, blow up silver cage":LegoBatman1LocationData("Arctic World",   45035996304),
    # A Surprise for the Commissioner
    "TJR Villian #1 - Room 1, Push block then double jump up":                                 LegoBatman1LocationData("A Surprise for the Commissioner",   45035996305),
    "TJR Villian #1 - Room 1, Break glass after cooperative puzzle":                           LegoBatman1LocationData("A Surprise for the Commissioner",   45035996306),
    "TJR Villian #1 - Freeze 3 waters into ice cream (2 in room one, 1 in room 3)":            LegoBatman1LocationData("A Surprise for the Commissioner",   45035996307),
    "TJR Villian #1 - Room 1, Blow up silver gate, build switch, pull switch":                 LegoBatman1LocationData("A Surprise for the Commissioner",   45035996309),
    "TJR Villian #1 - Room 1, Walk up magnet wall then pull switchs and grapple":              LegoBatman1LocationData("A Surprise for the Commissioner",   45035996310),
    "TJR Villian #1 - Room 1, Double jump on rollercoaster":                                   LegoBatman1LocationData("A Surprise for the Commissioner",   45035996311),
    "TJR Villian #1 - Room 2, Blow up silver object, build grapple, climb magnet wall":        LegoBatman1LocationData("A Surprise for the Commissioner",   45035996312),
    "TJR Villian #1 - Room 3, Sink in duck pound":                                             LegoBatman1LocationData("A Surprise for the Commissioner",   45035996314),
    "TJR Villian #1 - Room 3, Use attract machine then use tech pannel and race cars":         LegoBatman1LocationData("A Surprise for the Commissioner",   45035996315),
    "TJR Villian #1 - Room 3, Bring ice cream truck to garage":                                LegoBatman1LocationData("A Surprise for the Commissioner",   45035996316),
    # Biplane Blast
    "TJR Villian #2 - Break 10 towers throughout the level":                                   LegoBatman1LocationData("Biplane Blast",   45035996317),
    "TJR Villian #2 - Room 1, Pull top of chapel":                                             LegoBatman1LocationData("Biplane Blast",   45035996319),
    "TJR Villian #2 - Room 1, Break Batman gate with torpedo then activate signal tower":      LegoBatman1LocationData("Biplane Blast",   45035996320),
    "TJR Villian #2 - Room 1, Blow up silver object and pop 3 joker balloons":                 LegoBatman1LocationData("Biplane Blast",   45035996321),
    "TJR Villian #2 - Room 2, Shoot 3 joker faces on shields":                                 LegoBatman1LocationData("Biplane Blast",   45035996322),
    "TJR Villian #2 - Room 2, Blow up silver machine":                                         LegoBatman1LocationData("Biplane Blast",   45035996323),
    "TJR Villian #2 - Room 2, Break billboard with torpedo and fly bottom right":              LegoBatman1LocationData("Biplane Blast",   45035996324),
    "TJR Villian #2 - Room 2, Get Batman torpedos, break box on crane, pull crane":            LegoBatman1LocationData("Biplane Blast",   45035996325),
    "TJR Villian #2 - Boss Room, Use batman torpedo on train then blow up silver tank":        LegoBatman1LocationData("Biplane Blast",   45035996326),
    "TJR Villian #2 - Boss Room, Blow up silver cage infront of batman locked gate":           LegoBatman1LocationData("Biplane Blast",   45035996327),
    # The Joker's Masterpiece
    "TJR Villian #3 - Room 1, Batarang bat statue on pillar and press both buttons":           LegoBatman1LocationData("The Joker's Masterpiece",   45035996329),
    "TJR Villian #3 - Break 3 containers throughout level (2 in room two, 1 in room one)":     LegoBatman1LocationData("The Joker's Masterpiece",   45035996330),
    "TJR Villian #3 - Room 1, Shoot laser generator":                                          LegoBatman1LocationData("The Joker's Masterpiece",   45035996333),
    "TJR Villian #3 - Room 1, Double jump and push, then ball falls down":                     LegoBatman1LocationData("The Joker's Masterpiece",   45035996334),
    "TJR Villian #3 - Room 2, Break glasss container":                                         LegoBatman1LocationData("The Joker's Masterpiece",   45035996335),
    "TJR Villian #3 - Room 3, Push vault open":                                                LegoBatman1LocationData("The Joker's Masterpiece",   45035996336),
    "TJR Villian #3 - Room 3, Pull switch protected by heat, then break silver and glass object and build joker face":LegoBatman1LocationData("The Joker's Masterpiece",   45035996337),
    "TJR Villian #3 - Room 4, Double jump on rail, mind control guy then break box":           LegoBatman1LocationData("The Joker's Masterpiece",   45035996338),
    "TJR Villian #3 - Room 4, Double jump to small opening on right side":                     LegoBatman1LocationData("The Joker's Masterpiece",   45035996339),
    "TJR Villian #3 - Room 4, Pull switch and push box to conver and use generator twice":     LegoBatman1LocationData("The Joker's Masterpiece",   45035996340),
    # The Lure of the Night
    "TJR Villian #4 - Room 1, Mind control guy to push silver object, then blow it up":        LegoBatman1LocationData("The Lure of the Night",   45035996341),
    "TJR Villian #4 - Room 1, Build rails, then double jump up and then blow up silver objects, then build and double jump to switch, break plants then build ?":LegoBatman1LocationData("The Lure of the Night",   45035996343),
    "TJR Villian #4 - Room 1, Build rails, then double jump up then glide, build and push battery":LegoBatman1LocationData("The Lure of the Night",   45035996344),
    "TJR Villian #4 - Room 1, Pull boxes then build turnstile and put boat in sea, then ride boat around 3 times":LegoBatman1LocationData("The Lure of the Night",   45035996345),
    "TJR Villian #4 - Room 2, Blow up silver object and build magnet wall then walk up":       LegoBatman1LocationData("The Lure of the Night",   45035996346),
    "TJR Villian #4 - Room 2, Break 5 fire hydrents":                                          LegoBatman1LocationData("The Lure of the Night",   45035996347),
    "TJR Villian #4 - Room 2, Blow up silver door, then press both buttons and climb ladder":  LegoBatman1LocationData("The Lure of the Night",   45035996348),
    "TJR Villian #4 - Room 2, Behind of left tree in playground":                              LegoBatman1LocationData("The Lure of the Night",   45035996349),
    "TJR Villian #4 - Room 3, Blow up silver door":                                            LegoBatman1LocationData("The Lure of the Night",   45035996351),
    "TJR Villian #4 - Room 3, Blow up silver gate and then sink down and push buttons, break glass":LegoBatman1LocationData("The Lure of the Night",   45035996352),
    # Dying of Laughter
    "TJR Villian #5 - Room 1, Grow plants right side of spawn":                                LegoBatman1LocationData("Dying of Laughter",   45035996353),
    "TJR Villian #5 - Room 1, Double jump from collum then break glass":                       LegoBatman1LocationData("Dying of Laughter",   45035996354),
    "TJR Villian #5 - Room 1, Pull both sides of table":                                       LegoBatman1LocationData("Dying of Laughter",   45035996356),
    "TJR Villian #5 - Room 2, Blow up silver gate, build ladder, then climb up":               LegoBatman1LocationData("Dying of Laughter",   45035996357),
    "TJR Villian #5 - Room 2, Double jump onto 2 man button cage next to elevator":            LegoBatman1LocationData("Dying of Laughter",   45035996358),
    "TJR Villian #5 - Room 2, Glide from cage":                                                LegoBatman1LocationData("Dying of Laughter",   45035996360),
    "TJR Villian #5 - Room 2, Use magnet wall near elevator":                                  LegoBatman1LocationData("Dying of Laughter",   45035996361),
    "TJR Villian #5 - Room 2, Freeze water near bridge, then break ice statue":                LegoBatman1LocationData("Dying of Laughter",   45035996362),
    "TJR Villian #5 - Room 3, Jump repeatly on left 2 man button and hit bell repeatly":       LegoBatman1LocationData("Dying of Laughter",   45035996363),
    "TJR Villian #5 - Room 3, Blow up silver ladders, build both turrets, then shoot bells":   LegoBatman1LocationData("Dying of Laughter",   45035996364),

}
event_location_table: Dict[str, LegoBatman1LocationData] = {
    "Unlocked Wayne Mannor":                    LegoBatman1LocationData("Event"),
    "Unlocked Arkham Asylum":                   LegoBatman1LocationData("Event"),
    "Received All Levels":                      LegoBatman1LocationData("Event"),
    "Buy Ra Sha Guul":                          LegoBatman1LocationData("Event"),
    "Buy Hush":                                 LegoBatman1LocationData("Event"),
    "100%":                                     LegoBatman1LocationData("Event"),

}


def get_locations(world):
    locations_table = basic_locations.copy()
    
    if world.options.char_shop_sanity:
        locations_table.update(charshopsanity_locations)

    if world.options.hostage_sanity:
        locations_table.update(hostagesanity_locations)

    if world.options.kit_sanity:
        locations_table.update(kitsanity_locations)
    
    return locations_table
