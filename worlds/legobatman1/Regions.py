from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region, Entrance
from .Locations import RLLocation, location_table, get_locations_by_category


class LegoBatman1RegionData(NamedTuple):
    locations: Optional[List[str]]
    region_exits: Optional[List[str]]

regions: Dict[str, LegoBatman1RegionData] = {
        "Menu":                            LegoBatman1RegionData(None, ["Batcave"]),
        "Batcave":                         LegoBatman1RegionData(None, ["Arkham Asylum", "Shop", "You Can Bank on Batman","An Icy Reception","Two-Face Chase","A Poisonous Appointment","The Face-Off","There She Goes Again","Batboat Battle","Under the City","Zoo's Company","Penguin's Lair","Joker's Home Turf","Little Fun at Big Top","Flight of the Bat","In the Dark Night","To the Top of the Tower"]),
        "Shop":                            LegoBatman1RegionData([], ["Batcave", "Arkham Asylum"]),
        "Arkham Asylum":                   LegoBatman1RegionData([], ["Batcave","Shop","The Riddler Makes a Withdrawl","On the Rocks","Green Fingers","An Enterprising Theft", "Breaking Blocks","Rocking the Docks","Stealing the Show","Harboring a Grudge","A Daring Rescue","Artic World","A Surpise for the Commissioner","Biplane Blast","The Joker's Masterpiece","The Lure of the Night","Dying of Laughter"]),
        "You Can Bank on Batman":          LegoBatman1RegionData([], ["Status Screen"]),
        "An Icy Reception":                LegoBatman1RegionData([], ["Status Screen"]),
        "Two-Face Chase":                  LegoBatman1RegionData([], ["Status Screen"]),
        "A Poisonous Appointment":         LegoBatman1RegionData([], ["Status Screen"]),
        "The Face-Off":                    LegoBatman1RegionData(None, ["Status Screen"]),
        "There She Goes Again":            LegoBatman1RegionData(None, ["Status Screen"]),
        "Batboat Battle":                  LegoBatman1RegionData(None, ["Status Screen"]),
        "Under the City":                  {"Status Screen"},
        "Zoo's Company":                   {"Status Screen"},
        "Penguin's Lair":                  {"Status Screen"},
        "Joker's Home Turf":               {"Status Screen"},
        "Little Fun at Big Top":           {"Status Screen"},
        "Flight of the Bat":               {"Status Screen"},
        "In the Dark Night":               {"Status Screen"},
        "To the Top of the Tower":         {"Status Screen"},
        "The Riddler Makes a Withdrawl":   {"Status Screen"},
        "On the Rocks":                    {"Status Screen"},
        "Green Fingers":                   {"Status Screen"},
        "An Enterprising Theft":           {"Status Screen"},
        "Breaking Blocks":                 {"Status Screen"},
        "Rockin' the Docks":               {"Status Screen"},
        "Stealing the Show":               {"Status Screen"},
        "Harboring a Grudge":              {"Status Screen"},
        "A Daring Rescue":                 {"Status Screen"},
        "Artic World":                     {"Status Screen"},
        "A Surpise for the Commissioner":  {"Status Screen"},
        "Biplane Blast":                   {"Status Screen"},
        "The Joker's Masterpiece":         {"Status Screen"},
        "The Lure of the Night":           {"Status Screen"},
        "Dying of Laughter":               {"Status Screen"},
        "Status Screen":                   {"Batcave", "Arkham Asylum"},
    }
REGIONS: Dict[str, List[str]] = {
 regions["Status Screen"].locations.append("Status Screen - Flight of the Bat Completed"),
    regions["Status Screen"].locations.append("Status Screen - In the Dark Night Completed"),
    regions["Status Screen"].locations.append("Status Screen - To the Top of the Tower Completed"),
    regions["Status Screen"].locations.append("Status Screen - The Ridler Makes a Withdrawal Completed"),
    regions["Status Screen"].locations.append("Status Screen - On the Rocks Completed"),
    regions["Status Screen"].locations.append("Status Screen - Green Fingers Completed"),
    regions["Status Screen"].locations.append("Status Screen - An Enterprising Theft Completed"),
    regions["Status Screen"].locations.append("Status Screen - Breaking Blocks Completed"),
    regions["Status Screen"].locations.append("Status Screen - Rockin' the Docks Completed"),
    regions["Status Screen"].locations.append("Status Screen - Stealing the Show Completed"),
    regions["Status Screen"].locations.append("Status Screen - Harboring a Grudge Completed"),
    regions["Status Screen"].locations.append("Status Screen - A Daring Rescue Completed"),
    regions["Status Screen"].locations.append("Status Screen - Arctic World Completed"),
    regions["Status Screen"].locations.append("Status Screen - A Surprise for the Commissioner Completed"),
    regions["Status Screen"].locations.append("Status Screen - Biplane Blast Completed"),
    regions["Status Screen"].locations.append("Status Screen - The Joker's Masterpiece Completed"),
    regions["Status Screen"].locations.append("Status Screen - The Lure of the Night Completed"),
    regions["Status Screen"].locations.append("Status Screen - Dying of Laughter Completed"),
    regions["Shop"].locations.append("Buy Beep Beep"),
    regions["Shop"].locations.append("Buy Silhouettes"),
    regions["Shop"].locations.append("Buy Extra Toggle"),
    regions["Shop"].locations.append("Buy Disguise"),
    regions["Shop"].locations.append("Buy Ice Rink"),
    regions["The Face-Off"].locations.append("TRR Hero #5 - Room 2, After Two Face Fight, Push Colored Buttons on left side"),
    regions["Joker's Home Turf"].locations.append("TJR Hero #1 - Room 3, Freeze water near entrance then double jump up, then break glass and solve puzzle"),
    regions["Little Fun at the Big Top"].locations.append("TJR Hero #2 - Room 1, Use Tech Pannel on Crane Game, grab and break all 3 pink prizes"),
    regions["You Can Bank On Batman"].locations.append("TRR Hero #1 - Boss Room, Break the bank darwer"),
    regions["Flight of the Bat"].locations.append("TJR Hero #3 - Room 2, Go through toxic gas and shoot turnstiles"),
    regions["In the Dark Night"].locations.append("TJR Hero #4 - Room 3, Build heated ladder then climb, glide and double jump"),
    regions["To the Top of the Tower"].locations.append("TJR Hero #5 - Room 2, Push organ out of hiding, then play it"),
}

CHAR_SHOP: Dict[str, List[str]] = {
"Shop": {"Buy Bruce Wayne","Buy Alfred","Buy Batgirl","Buy Nightwing","Buy Commissioner Gordon","Buy Mad Hatter","Buy Fishmonger","Buy Scientist","Buy Security Guard","Buy Police Marksman","Buy Police Officer","Buy S.W.A.T.","Buy Sailor","Buy Miltary Police","Buy Yeti","Buy Penguin Minion","Buy Catwoman (Classic)","Buy Man-Bat","Buy Joker (Tropical)","Buy Poison Ivy Goon","Buy Freeze Girl","Buy Zoo Sweeper","Buy Riddler Henchman","Buy Riddler Goon","Buy Penguin Goon","Buy Penguin Henchman","Buy Joker Goon","Buy Clown Goon","Buy Joker Henchman","Buy Police Car","Buy Police Bike","Buy Police Van","Buy Bat-Tank","Buy Two-Face's Armored Truck","Buy Garbage Truck","Buy Catwoman's Motorcycle","Buy Mr.Freeze's Kart","Buy Police Watercraft","Buy Police Boat","Buy Penguin Goon Submarine","Buy Mad Hatter's Steamboat","Buy Robin's Submarine","Buy Mr.Freeze's Iceberg","Buy The Joker Van","Buy Harley Quinn's Hammer Truck","Buy Police Helicopter","Buy Bruce Wayne's Private Jet","Buy Goon Helicopter","Buy Mad Hatter's Glider","Buy Riddler Jet","Buy Harbor Helicopter"},
}