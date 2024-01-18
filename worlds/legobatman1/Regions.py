from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region, Entrance
from .Locations import LegoBatman1Location, location_table, get_locations_by_category


class LegoBatman1Data(NamedTuple):
    locations: Optional[List[str]]
    region_exits: Optional[List[str]]


def create_regions(multiworld: MultiWorld, player: int):
    regions: Dict[str, LegoBatman1Data] = {
        "Menu":                            LegoBatman1RegionData(None, ["Batcave"]),
        "Batcave":                         LegoBatman1RegionData(None,   ["Arkham Asylum", "Shop", "You Can Bank on Batman","An Icy Reception","Two-Face Chase","A Poisonous Appointment","The Face-Off","There She Goes Again","Batboat Battle","Under the City","Zoo's Company","Penguin's Lair","Joker's Home Turf","Little Fun at Big Top","Flight of the Bat","In the Dark Night","To the Top of the Tower"]),
        "Shop":                            LegoBatman1RegionData([],   ["Batcave", "Arkham Asylum"]),
        "Arkham Asylum":                   LegoBatman1RegionData(None,   ["The Riddler Makes a Withdrawl","On the Rocks","Green Fingers","An Enterprising Theft", "Breaking Blocks","Rocking the Docks","Stealing the Show","Harboring a Grudge","A Daring Rescue","Artic World","A Surpise for the Commissioner","Biplane Blast","The Joker's Masterpiece","The Lure of the Night","Dying of Laughter"]),
        "You Can Bank on Batman":          LegoBatman1RegionData([],   ["Status Screen"]),
        "An Icy Reception":                LegoBatman1RegionData([],   ["Status Screen"]),
        "Two-Face Chase":                  LegoBatman1RegionData([],   ["Status Screen"]),
        "A Poisonous Appointment":         LegoBatman1RegionData([],   ["Status Screen"]),
        "The Face-Off":                    LegoBatman1RegionData([],   ["Status Screen"]),
        "There She Goes Again":            LegoBatman1RegionData([],   ["Status Screen"]),
        "Batboat Battle":                  LegoBatman1RegionData([],   ["Status Screen"]),
        "Under the City":                  LegoBatman1RegionData([],   ["Status Screen"]),
        "Zoo's Company":                   LegoBatman1RegionData([],   ["Status Screen"]),
        "Penguin's Lair":                  LegoBatman1RegionData([],   ["Status Screen"]),
        "Joker's Home Turf":               LegoBatman1RegionData([],   ["Status Screen"]),
        "Little Fun at Big Top":           LegoBatman1RegionData([],   ["Status Screen"]),
        "Flight of the Bat":               LegoBatman1RegionData([],   ["Status Screen"]),
        "In the Dark Night":               LegoBatman1RegionData([],   ["Status Screen"]),
        "To the Top of the Tower":         LegoBatman1RegionData([],   ["Status Screen"]),
        "The Riddler Makes a Withdrawl":   LegoBatman1RegionData([],   ["Status Screen"]),
        "On the Rocks":                    LegoBatman1RegionData([],   ["Status Screen"]),
        "Green Fingers":                   LegoBatman1RegionData([],   ["Status Screen"]),
        "An Enterprising Theft":           LegoBatman1RegionData([],   ["Status Screen"]),
        "Breaking Blocks":                 LegoBatman1RegionData([],   ["Status Screen"]),
        "Rockin' the Docks":               LegoBatman1RegionData([],   ["Status Screen"]),
        "Stealing the Show":               LegoBatman1RegionData([],   ["Status Screen"]),
        "Harboring a Grudge":              LegoBatman1RegionData([],   ["Status Screen"]),
        "A Daring Rescue":                 LegoBatman1RegionData([],   ["Status Screen"]),
        "Artic World":                     LegoBatman1RegionData([],   ["Status Screen"]),
        "A Surpise for the Commissioner":  LegoBatman1RegionData([],   ["Status Screen"]),
        "Biplane Blast":                   LegoBatman1RegionData([],   ["Status Screen"]),
        "The Joker's Masterpiece":         LegoBatman1RegionData([],   ["Status Screen"]),
        "The Lure of the Night":           LegoBatman1RegionData([],   ["Status Screen"]),
        "Dying of Laughter":               LegoBatman1RegionData([],   ["Status Screen"]),
        "Status Screen":                   LegoBatman1RegionData([],   ["Batcave", "Arkham Asylum"]),
    }

# Set up locations
    regions["Status Screen"].locations.append("Status Screen - Unlock Detonation Suit"),
    regions["Status Screen"].locations.append("Status Screen - Unlock Sonic Suit"),
    regions["Status Screen"].locations.append("Status Screen - Unlock Heat Protection Suit"),
    regions["Status Screen"].locations.append("Status Screen - Unlock Glide Suit"),
    regions["Status Screen"].locations.append("Status Screen - Unlock Technology Suit"),
    regions["Status Screen"].locations.append("Status Screen - Unlock Attraction Suit"),
    regions["Status Screen"].locations.append("Status Screen - Unlock Magnet Suit"),
    regions["Status Screen"].locations.append("Status Screen - Unlock Water Suit"),
    regions["Status Screen"].locations.append("Status Screen - You Can Bank On Batman True Status"),
    regions["Status Screen"].locations.append("Status Screen - An Icy Reception True Status"),
    regions["Status Screen"].locations.append("Status Screen - Two-Face Chase True Status"),
    regions["Status Screen"].locations.append("Status Screen - A Poisonous Appointment True Status"),
    regions["Status Screen"].locations.append("Status Screen - The Face-Off True Status"),
    regions["Status Screen"].locations.append("Status Screen - There She Goes Again True Status"),
    regions["Status Screen"].locations.append("Status Screen - Batboat Battle True Status"),
    regions["Status Screen"].locations.append("Status Screen - Under the City True Status"),
    regions["Status Screen"].locations.append("Status Screen - Zoo's Company True Status"),
    regions["Status Screen"].locations.append("Status Screen - Penguin's Lair True Status"),
    regions["Status Screen"].locations.append("Status Screen - Joker's Home Turf True Status"),
    regions["Status Screen"].locations.append("Status Screen - Little Fun at the Big Top True Status"),
    regions["Status Screen"].locations.append("Status Screen - Flight of the Bat True Status"),
    regions["Status Screen"].locations.append("Status Screen - In the Dark Night True Status"),
    regions["Status Screen"].locations.append("Status Screen - To the Top of the Tower True Status"),
    regions["Status Screen"].locations.append("Status Screen - The Ridler Makes a Withdrawal True Status"),
    regions["Status Screen"].locations.append("Status Screen - On the Rocks True Status"),
    regions["Status Screen"].locations.append("Status Screen - Green Fingers True Status"),
    regions["Status Screen"].locations.append("Status Screen - An Enterprising Theft True Status"),
    regions["Status Screen"].locations.append("Status Screen - Breaking Blocks True Status"),
    regions["Status Screen"].locations.append("Status Screen - Rockin' the Docks True Status"),
    regions["Status Screen"].locations.append("Status Screen - Stealing the Show True Status"),
    regions["Status Screen"].locations.append("Status Screen - Harboring a Grudge True Status"),
    regions["Status Screen"].locations.append("Status Screen - A Daring Rescue True Status"),
    regions["Status Screen"].locations.append("Status Screen - Arctic World True Status"),
    regions["Status Screen"].locations.append("Status Screen - A Surprise for the Commissioner True Status"),
    regions["Status Screen"].locations.append("Status Screen - Biplane Blast True Status"),
    regions["Status Screen"].locations.append("Status Screen - The Joker's Masterpiece True Status"),
    regions["Status Screen"].locations.append("Status Screen - The Lure of the Night True Status"),
    regions["Status Screen"].locations.append("Status Screen - Dying of Laughter True Status"),
    regions["Status Screen"].locations.append("Status Screen - You Can Bank On Batman Completed"),
    regions["Status Screen"].locations.append("Status Screen - An Icy Reception Completed"),
    regions["Status Screen"].locations.append("Status Screen - Two-Face Chase Completed"),
    regions["Status Screen"].locations.append("Status Screen - A Poisonous Appointment Completed"),
    regions["Status Screen"].locations.append("Status Screen - The Face-Off Completed"),
    regions["Status Screen"].locations.append("Status Screen - There She Goes Again Completed"),
    regions["Status Screen"].locations.append("Status Screen - Batboat Battle Completed"),
    regions["Status Screen"].locations.append("Status Screen - Under the City Completed"),
    regions["Status Screen"].locations.append("Status Screen - Zoo's Company Completed"),
    regions["Status Screen"].locations.append("Status Screen - Penguin's Lair Completed"),
    regions["Status Screen"].locations.append("Status Screen - Joker's Home Turf Completed"),
    regions["Status Screen"].locations.append("Status Screen - Little Fun at the Big Top Completed"),
    regions["Status Screen"].locations.append("Status Screen - Flight of the Bat Completed"),
    regions["Status Screen"].locations.append("Status Screen - In the Dark Night Completed"),
    regions["Status Screen"].locations.append("Status Screen - To the Top of the Tower Completed"),
    regions["Status Screen"].locations.append("Status Screen - The Ridler Makes a Withdrawal Completed"),
    regions["Status Screen"].locations.append("Status Screen - On the Rocks Completed"),
    regions["Status Screen"].locations.append("Status Screen - Green Fingers Completed"),
    regions["Status Screen"].locations.append("Status Screen - An Enterprising Theft Completed"),
    regions["Status Screen"].locations.append("Status Screen - Breaking Blocks Completed"),
    regions["Deep Jungle"].locations.append("Deep Jungle Tree House Suspended Boat Chest"),
    regions["100 Acre Wood"].locations.append("100 Acre Wood Meadow Inside Log Chest"),
    regions["Agrabah"].locations.append("Agrabah Plaza By Storage Chest"),
    regions["Agrabah"].locations.append("Agrabah Plaza Raised Terrace Chest"),
    regions["Agrabah"].locations.append("Agrabah Plaza Top Corner Chest"),
    regions["Agrabah"].locations.append("Agrabah Alley Chest"),
    regions["Agrabah"].locations.append("Agrabah Bazaar Across Windows Chest"),
    regions["Agrabah"].locations.append("Agrabah Bazaar High Corner Chest"),
    regions["Agrabah"].locations.append("Agrabah Main Street Right Palace Entrance Chest"),
    regions["Agrabah"].locations.append("Agrabah Main Street High Above Alley Entrance Chest"),
    regions["Agrabah"].locations.append("Agrabah Main Street High Above Palace Gates Entrance Chest"),
    regions["Agrabah"].locations.append("Agrabah Palace Gates Low Chest"),
    regions["Agrabah"].locations.append("Agrabah Palace Gates High Opposite Palace Chest"),
    regions["Agrabah"].locations.append("Agrabah Palace Gates High Close to Palace Chest"),
    regions["Agrabah"].locations.append("Agrabah Storage Green Trinity Chest"),
    regions["Agrabah"].locations.append("Agrabah Storage Behind Barrel Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Entrance Left Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Entrance Tall Tower Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Hall High Left Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Hall Near Bottomless Hall Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Bottomless Hall Raised Platform Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Bottomless Hall Pillar Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Bottomless Hall Across Chasm Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Treasure Room Across Platforms Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Treasure Room Small Treasure Pile Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Treasure Room Large Treasure Pile Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Treasure Room Above Fire Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Relic Chamber Jump from Stairs Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Relic Chamber Stairs Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Dark Chamber Abu Gem Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Dark Chamber Across from Relic Chamber Entrance Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Dark Chamber Bridge Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Dark Chamber Near Save Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Silent Chamber Blue Trinity Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Hidden Room Right Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Hidden Room Left Chest"),
    regions["Agrabah"].locations.append("Agrabah Aladdin's House Main Street Entrance Chest"),
    regions["Agrabah"].locations.append("Agrabah Aladdin's House Plaza Entrance Chest"),
    regions["Agrabah"].locations.append("Agrabah Cave of Wonders Entrance White Trinity Chest"),
    regions["Monstro"].locations.append("Monstro Chamber 6 Other Platform Chest"),
    regions["Monstro"].locations.append("Monstro Chamber 6 Platform Near Chamber 5 Entrance Chest"),
    regions["Monstro"].locations.append("Monstro Chamber 6 Raised Area Near Chamber 1 Entrance Chest"),
    regions["Monstro"].locations.append("Monstro Chamber 6 Low Chest"),
    if atlantica or goal == "atlantica":
        regions["Atlantica"].locations.append("Atlantica Sunken Ship In Flipped Boat Chest"),
        regions["Atlantica"].locations.append("Atlantica Sunken Ship Seabed Chest"),
        regions["Atlantica"].locations.append("Atlantica Sunken Ship Inside Ship Chest"),
        regions["Atlantica"].locations.append("Atlantica Ariel's Grotto High Chest"),
        regions["Atlantica"].locations.append("Atlantica Ariel's Grotto Middle Chest"),
        regions["Atlantica"].locations.append("Atlantica Ariel's Grotto Low Chest"),
        regions["Atlantica"].locations.append("Atlantica Ursula's Lair Use Fire on Urchin Chest"),
        regions["Atlantica"].locations.append("Atlantica Undersea Gorge Jammed by Ariel's Grotto Chest"),
        regions["Atlantica"].locations.append("Atlantica Triton's Palace White Trinity Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Moonlight Hill White Trinity Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Bridge Under Bridge"),
    regions["Halloween Town"].locations.append("Halloween Town Boneyard Tombstone Puzzle Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Bridge Right of Gate Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Cemetary Behind Grave Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Cemetary By Cat Shape Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Cemetary Between Graves Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Oogie's Manor Lower Iron Cage Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Oogie's Manor Upper Iron Cage Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Oogie's Manor Hollow Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Oogie's Manor Grounds Red Trinity Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Guillotine Square High Tower Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Guillotine Square Pumpkin Structure Left Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Oogie's Manor Entrance Steps Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Oogie's Manor Inside Entrance Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Bridge Left of Gate Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Cemetary By Striped Grave Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Guillotine Square Under Jack's House Stairs Chest"),
    regions["Halloween Town"].locations.append("Halloween Town Guillotine Square Pumpkin Structure Right Chest"),
    regions["Olympus Coliseum"].locations.append("Olympus Coliseum Coliseum Gates Left Behind Columns Chest"),
    regions["Olympus Coliseum"].locations.append("Olympus Coliseum Coliseum Gates Right Blue Trinity Chest"),
    regions["Olympus Coliseum"].locations.append("Olympus Coliseum Coliseum Gates Left Blue Trinity Chest"),
    regions["Olympus Coliseum"].locations.append("Olympus Coliseum Coliseum Gates White Trinity Chest"),
   #regions["Olympus Coliseum"].locations.append("Olympus Coliseum Coliseum Gates Blizzara Chest"),
    regions["Monstro"].locations.append("Monstro Mouth Boat Deck Chest"),
    regions["Monstro"].locations.append("Monstro Mouth High Platform Boat Side Chest"),
    regions["Monstro"].locations.append("Monstro Mouth High Platform Across from Boat Chest"),
    regions["Monstro"].locations.append("Monstro Mouth Near Ship Chest"),
    regions["Monstro"].locations.append("Monstro Mouth Green Trinity Top of Boat Chest"),
    regions["Monstro"].locations.append("Monstro Chamber 2 Ground Chest"),
    regions["Monstro"].locations.append("Monstro Chamber 2 Platform Chest"),
    regions["Monstro"].locations.append("Monstro Chamber 5 Platform Chest"),
    regions["Monstro"].locations.append("Monstro Chamber 3 Ground Chest"),
    regions["Monstro"].locations.append("Monstro Chamber 3 Platform Above Chamber 2 Entrance Chest"),
    regions["Monstro"].locations.append("Monstro Chamber 3 Near Chamber 6 Entrance Chest"),
    regions["Monstro"].locations.append("Monstro Chamber 3 Platform Near Chamber 6 Entrance Chest"),
    regions["Monstro"].locations.append("Monstro Mouth High Platform Near Teeth Chest"),
    regions["Monstro"].locations.append("Monstro Chamber 5 Atop Barrel Chest"),
    regions["Monstro"].locations.append("Monstro Chamber 5 Low 2nd Chest"),
    regions["Monstro"].locations.append("Monstro Chamber 5 Low 1st Chest"),
    regions["Neverland"].locations.append("Neverland Pirate Ship Deck White Trinity Chest"),
    regions["Neverland"].locations.append("Neverland Pirate Ship Crows Nest Chest"),
    regions["Neverland"].locations.append("Neverland Hold Yellow Trinity Right Blue Chest"),
    regions["Neverland"].locations.append("Neverland Hold Yellow Trinity Left Blue Chest"),
    regions["Neverland"].locations.append("Neverland Galley Chest"),
    regions["Neverland"].locations.append("Neverland Cabin Chest"),
    regions["Neverland"].locations.append("Neverland Hold Flight 1st Chest "),
    regions["Neverland"].locations.append("Neverland Clock Tower Chest"),
    regions["Neverland"].locations.append("Neverland Hold Flight 2nd Chest"),
    regions["Neverland"].locations.append("Neverland Hold Yellow Trinity Green Chest"),
    regions["Neverland"].locations.append("Neverland Captain's Cabin Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Rising Falls Water's Surface Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Rising Falls Under Water 1st Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Rising Falls Under Water 2nd Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Rising Falls Floating Platform Near Save Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Rising Falls Floating Platform Near Bubble Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Rising Falls High Platform Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Castle Gates Gravity Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Castle Gates Freestanding Pillar Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Castle Gates High Pillar Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Great Crest Lower Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Great Crest After Battle Platform Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion High Tower 2nd Gravity Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion High Tower 1st Gravity Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion High Tower Above Sliding Gates Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Library Top of Bookshelf Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Library 1st Floor Turn the Carousel Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Library Top of Bookshelf Turn the Carousel Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Library 2nd Floor Turn the Carousel 1st Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Library 2nd Floor Turn the Carousel 2nd Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Lift Stop Library Node After High Tower Switch Gravity Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Lift Stop Library Node Gravity Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Lift Stop Under High Tower Sliding Blocks Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Lift Stop Outside Library Gravity Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Lift Stop Heartless Sigil Door Gravity Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Base Level Bubble Under the Wall Platform Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Base Level Platform Near Entrance Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Base Level Near Crystal Switch Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Waterway Near Save Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Waterway Blizzard on Bubble Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Waterway Unlock Passage from Base Level Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Dungeon By Candles Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Dungeon Corner Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Grand Hall Steps Right Side Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Grand Hall Oblivion Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Grand Hall Left of Gate Chest"),
   #regions["Hollow Bastion"].locations.append("Hollow Bastion Entrance Hall Push the Statue Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Entrance Hall Left of Emblem Door Chest"),
    regions["Hollow Bastion"].locations.append("Hollow Bastion Rising Falls White Trinity Chest"),
   #regions["End of the World"].locations.append("End of the World Final Dimension 1st Chest"),
   #regions["End of the World"].locations.append("End of the World Final Dimension 2nd Chest"),
   #regions["End of the World"].locations.append("End of the World Final Dimension 3rd Chest"),
   #regions["End of the World"].locations.append("End of the World Final Dimension 4th Chest"),
   #regions["End of the World"].locations.append("End of the World Final Dimension 5th Chest"),
   #regions["End of the World"].locations.append("End of the World Final Dimension 6th Chest"),
   #regions["End of the World"].locations.append("End of the World Final Dimension 10th Chest"),
   #regions["End of the World"].locations.append("End of the World Final Dimension 9th Chest"),
   #regions["End of the World"].locations.append("End of the World Final Dimension 8th Chest"),
   #regions["End of the World"].locations.append("End of the World Final Dimension 7th Chest"),
   #regions["End of the World"].locations.append("End of the World Giant Crevasse 3rd Chest"),
   #regions["End of the World"].locations.append("End of the World Giant Crevasse 1st Chest"),
   #regions["End of the World"].locations.append("End of the World Giant Crevasse 4th Chest"),
   #regions["End of the World"].locations.append("End of the World Giant Crevasse 2nd Chest"),
   #regions["End of the World"].locations.append("End of the World World Terminus Traverse Town Chest"),
   #regions["End of the World"].locations.append("End of the World World Terminus Wonderland Chest"),
   #regions["End of the World"].locations.append("End of the World World Terminus Olympus Coliseum Chest"),
   #regions["End of the World"].locations.append("End of the World World Terminus Deep Jungle Chest"),
   #regions["End of the World"].locations.append("End of the World World Terminus Agrabah Chest"),
   #regions["End of the World"].locations.append("End of the World World Terminus Atlantica Chest"),
   #regions["End of the World"].locations.append("End of the World World Terminus Halloween Town Chest"),
   #regions["End of the World"].locations.append("End of the World World Terminus Neverland Chest"),
    regions["End of the World"].locations.append("End of the World World Terminus 100 Acre Wood Chest"),
    regions["End of the World"].locations.append("End of the World World Terminus Hollow Bastion Chest"),
    regions["End of the World"].locations.append("End of the World Final Rest Chest"),
    regions["Monstro"].locations.append("Monstro Chamber 6 White Trinity Chest"),
   #regions["Awakening"].locations.append("Awakening Chest"), missable
   
   #regions["End of the World"].locations.append("Chronicles Sora's Story")
    if goal in ["final_rest", "unknown"]: #Not possible if HB is complete, could interefere with other win cons if 4 emblems is not go-mode
        regions["Wonderland"].locations.append("Chronicles Wonderland")
    regions["Olympus Coliseum"].locations.append("Chronicles Olympus Coliseum")
    regions["Deep Jungle"].locations.append("Chronicles Deep Jungle")
    regions["Agrabah"].locations.append("Chronicles Agrabah")
    regions["Monstro"].locations.append("Chronicles Monstro")
   #regions["100 Acre Wood"].locations.append("Chronicles 100 Acre Wood")
    if atlantica or goal == "atlantica":
        regions["Atlantica"].locations.append("Chronicles Atlantica")
    regions["Halloween Town"].locations.append("Chronicles Halloween Town")
   #regions["Neverland"].locations.append("Chronicles Neverland")
    
    regions["Agrabah"].locations.append("Ansem's Secret Report 1")
    regions["Hollow Bastion"].locations.append("Ansem's Secret Report 2")
    if atlantica or goal == "atlantica":
        regions["Atlantica"].locations.append("Ansem's Secret Report 3")
    regions["Hollow Bastion"].locations.append("Ansem's Secret Report 4")
    regions["Hollow Bastion"].locations.append("Ansem's Secret Report 5")
    regions["Hollow Bastion"].locations.append("Ansem's Secret Report 6")
    regions["Halloween Town"].locations.append("Ansem's Secret Report 7")
    regions["Olympus Coliseum"].locations.append("Ansem's Secret Report 8")
    regions["Neverland"].locations.append("Ansem's Secret Report 9")
    regions["Hollow Bastion"].locations.append("Ansem's Secret Report 10")
   #regions["Agrabah"].locations.append("Ansem's Secret Report 11")
    if goal == "sephiroth":
        regions["Olympus Coliseum"].locations.append("Ansem's Secret Report 12")
    if goal == "unknown":
        regions["Hollow Bastion"].locations.append("Ansem's Secret Report 13")
   
    for i in range(levels):
        regions["Levels"].locations.append("Level " + str(i+1).rjust(3,'0'))

   
    regions["Olympus Coliseum"].locations.append("Complete Phil Cup")
    regions["Olympus Coliseum"].locations.append("Complete Pegasus Cup")
    regions["Olympus Coliseum"].locations.append("Complete Hercules Cup")
    regions["Olympus Coliseum"].locations.append("Complete Hades Cup")

    # Set up the regions correctly.
    for name, data in regions.items():
        multiworld.regions.append(create_region(multiworld, player, name, data))

    multiworld.get_entrance("Awakening", player).connect(multiworld.get_region("Awakening", player))
    multiworld.get_entrance("Destiny Islands", player).connect(multiworld.get_region("Destiny Islands", player))
    multiworld.get_entrance("Traverse Town", player).connect(multiworld.get_region("Traverse Town", player))
    multiworld.get_entrance("Wonderland", player).connect(multiworld.get_region("Wonderland", player))
    multiworld.get_entrance("Olympus Coliseum", player).connect(multiworld.get_region("Olympus Coliseum", player))
    multiworld.get_entrance("Deep Jungle", player).connect(multiworld.get_region("Deep Jungle", player))
    multiworld.get_entrance("Agrabah", player).connect(multiworld.get_region("Agrabah", player))
    multiworld.get_entrance("Monstro", player).connect(multiworld.get_region("Monstro", player))
    multiworld.get_entrance("Atlantica", player).connect(multiworld.get_region("Atlantica", player))
    multiworld.get_entrance("Halloween Town", player).connect(multiworld.get_region("Halloween Town", player))
    multiworld.get_entrance("Neverland", player).connect(multiworld.get_region("Neverland", player))
    multiworld.get_entrance("Hollow Bastion", player).connect(multiworld.get_region("Hollow Bastion", player))
    multiworld.get_entrance("End of the World", player).connect(multiworld.get_region("End of the World", player))
    multiworld.get_entrance("World Map", player).connect(multiworld.get_region("World Map", player))
    multiworld.get_entrance("Levels", player).connect(multiworld.get_region("Levels", player))

def create_region(multiworld: MultiWorld, player: int, name: str, data: LegoBatman1RegionData):
    region = Region(name, player, multiworld)
    if data.locations:
        for loc_name in data.locations:
            loc_data = location_table.get(loc_name)
            location = LegoBatman1Location(player, loc_name, loc_data.code if loc_data else None, region)
            region.locations.append(location)

    if data.region_exits:
        for exit in data.region_exits:
            entrance = Entrance(player, exit, region)
            region.exits.append(entrance)

    return region