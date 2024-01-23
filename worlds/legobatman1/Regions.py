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
        "The Face-Off":                    LegoBatman1RegionData([], ["Status Screen"]),
        "There She Goes Again":            LegoBatman1RegionData([], ["Status Screen"]),
        "Batboat Battle":                  LegoBatman1RegionData([], ["Status Screen"]),
        "Under the City":                  LegoBatman1RegionData([], ["Status Screen"]),
        "Zoo's Company":                   LegoBatman1RegionData([], ["Status Screen"]),
        "Penguin's Lair":                  LegoBatman1RegionData([], ["Status Screen"]),
        "Joker's Home Turf":               LegoBatman1RegionData([], ["Status Screen"]),
        "Little Fun at Big Top":           LegoBatman1RegionData([], ["Status Screen"]),
        "Flight of the Bat":               LegoBatman1RegionData([], ["Status Screen"]),
        "In the Dark Night":               LegoBatman1RegionData([], ["Status Screen"]),
        "To the Top of the Tower":         LegoBatman1RegionData([], ["Status Screen"]),
        "The Riddler Makes a Withdrawl":   LegoBatman1RegionData([], ["Status Screen"]),
        "On the Rocks":                    LegoBatman1RegionData([], ["Status Screen"]),
        "Green Fingers":                   LegoBatman1RegionData([], ["Status Screen"]),
        "An Enterprising Theft":           LegoBatman1RegionData([], ["Status Screen"]),
        "Breaking Blocks":                 LegoBatman1RegionData([], ["Status Screen"]),
        "Rockin' the Docks":               LegoBatman1RegionData([], ["Status Screen"]),
        "Stealing the Show":               LegoBatman1RegionData([], ["Status Screen"]),
        "Harboring a Grudge":              LegoBatman1RegionData([], ["Status Screen"]),
        "A Daring Rescue":                 LegoBatman1RegionData([], ["Status Screen"]),
        "Artic World":                     LegoBatman1RegionData([], ["Status Screen"]),
        "A Surpise for the Commissioner":  LegoBatman1RegionData([], ["Status Screen"]),
        "Biplane Blast":                   LegoBatman1RegionData([], ["Status Screen"]),
        "The Joker's Masterpiece":         LegoBatman1RegionData([], ["Status Screen"]),
        "The Lure of the Night":           LegoBatman1RegionData([], ["Status Screen"]),
        "Dying of Laughter":               LegoBatman1RegionData([], ["Status Screen"]),
        "Status Screen":                   LegoBatman1RegionData([], ["Batcave", "Arkham Asylum"]),
    }

    regions["You Can Bank on Batman"].locations.append("Status Screen - You Can Bank on Batman Completed"),
    regions["An Icy Reception"].locations.append("Status Screen - An Icy Reception Completed"),    
    regions["Two-Face Chase"].locations.append("Status Screen - Two-Face Chase Completed"),
    regions["A Poisonous Appointment"].locations.append("Status Screen - A Poisonous Appointment Completed"),
    regions["The Face-Off"].locations.append("Status Screen - The Face-Off Completed"),    
    regions["There She Goes Again"].locations.append("Status Screen - There She Goes Again Completed"),
    regions["Batboat Battle"].locations.append("Status Screen - Batboat Battle Completed"),    
    regions["Under the City"].locations.append("Status Screen - Under the City Completed"),
    regions["Zoo's Company"].locations.append("Status Screen - Zoo's Company Completed"),
    regions["Penguin's Lair"].locations.append("Status Screen - Penguin's Lair Completed"),    
    regions["Joker's Home Turf"].locations.append("Status Screen - Joker's Home Turf Completed"),
    regions["Little Fun at Big Top"].locations.append("Status Screen - Little Fun at Big Top Completed"),    
    regions["Flight of the Bat"].locations.append("Status Screen - Flight of the Bat Completed"),
    regions["In the Dark Night"].locations.append("Status Screen - In the Dark Night Completed"),
    regions["To the Top of the Tower"].locations.append("Status Screen - To the Top of the Tower Completed"),
    regions["The Ridler Makes a Withdrawal"].locations.append("Status Screen - The Ridler Makes a Withdrawal Completed"),
    regions["On the Rocks"].locations.append("Status Screen - On the Rocks Completed"),
    regions["Green Fingers"].locations.append("Status Screen - Green Fingers Completed"),
    regions["An Enterprising Theft"].locations.append("Status Screen - An Enterprising Theft Completed"),
    regions["Breaking Blocks"].locations.append("Status Screen - Breaking Blocks Completed"),
    regions["Rockin' the Docks"].locations.append("Status Screen - Rockin' the Docks Completed"),
    regions["Stealing the Show"].locations.append("Status Screen - Stealing the Show Completed"),
    regions["Harboring a Grudge"].locations.append("Status Screen - Harboring a Grudge Completed"),
    regions["A Daring Rescue"].locations.append("Status Screen - A Daring Rescue Completed"),
    regions["Arctic World"].locations.append("Status Screen - Arctic World Completed"),
    regions["A Surprise for the Commissioner"].locations.append("Status Screen - A Surprise for the Commissioner Completed"),
    regions["Biplane Blast"].locations.append("Status Screen - Biplane Blast Completed"),
    regions["The Joker's Masterpiece"].locations.append("Status Screen - The Joker's Masterpiece Completed"),
    regions["The Lure of the Night"].locations.append("Status Screen - The Lure of the Night Completed"),
    regions["Dying of Laughter"].locations.append("Status Screen - Dying of Laughter Completed"),
    regions["Shop"].locations.append("Buy Beep Beep"),
    regions["Shop"].locations.append("Buy Silhouettes"),
    regions["Shop"].locations.append("Buy Extra Toggle"),
    regions["Shop"].locations.append("Buy Disguise"),
    regions["Shop"].locations.append("Buy Ice Rink"),
    regions["You Can Bank On Batman"].locations.append("TRR Hero #1 - Boss Room, Break the bank darwer"),
    regions["An Icy Reception"].locations.append("TRR Hero #2 - Room 2, Press on switch while other character goes in cage"),
    regions["Two-Face Chase"].locations.append("TRR Hero #3 - Room 3, Destroy trash can in the far back left cornor"),
    regions["A Poisonous Appointment"].locations.append("TRR Hero #4 - Room 4, Use the switch, blow up the silver object and use the generator"),
    regions["The Face-Off"].locations.append("TRR Hero #5 - Room 2, After Two Face Fight, Push Colored Buttons on left side"),
    regions["There She Goes Again"].locations.append("PCP Hero #1 - Boss Room, Break glass wall near entrance"),
    regions["Batboat Battle"].locations.append("PCP Hero #2 - Boss Room, Submerge and shoot targets"),
    regions["Under The City"].locations.append("PCP Hero #3 - Room 1, Use Tech Pannel and run over bouys"),
    regions["Zoo's Company"].locations.append("PCP Hero #4 - Room 2, Break Silver grate and go in water"),
    regions["Penguin's Lair"].locations.append("PCP Hero #5 - Boss Room, Break glass near treadmil, graple and jump to rail and run on tredmil then push button"),
    regions["Joker's Home Turf"].locations.append("TJR Hero #1 - Room 3, Freeze water near entrance then double jump up, then break glass and solve puzzle"),
    regions["Little Fun at the Big Top"].locations.append("TJR Hero #2 - Room 1, Use Tech Pannel on Crane Game, grab and break all 3 pink prizes"),
    regions["Flight of the Bat"].locations.append("TJR Hero #3 - Room 2, Go through toxic gas and shoot turnstiles"),
    regions["In the Dark Night"].locations.append("TJR Hero #4 - Room 3, Build heated ladder then climb, glide and double jump"),
    regions["To the Top of the Tower"].locations.append("TJR Hero #5 - Room 2, Push organ out of hiding, then play it"),

