from BaseClasses import Item, ItemClassification
import typing


class LegoBatman1temData(NamedTuple):
    category: str
    code: Optional[int] = None
    classification: ItemClassification = ItemClassification.filler
    max_quantity: int = 1
    weight: int = 1

def get_items_by_category(category: str) -> Dict[str, LegoBatman1ItemData]:
return {name: data for name, data in item_table.items() if data.category == category}

class LegoBatman1Item(Item):
    game: str = "Lego Batman: The Video Game"


item_table: Dict[str, LegoBatman1ItemData] = {
basic_item = {
   
    #Suits
    "Demolition Suit":                      LegoBatman1ItemData("Suits",        45035996201, ItemClassification.progression),
    "Glide Suit":                           LegoBatman1ItemData("Suits",        45035996202, ItemClassification.progression),
    "Sonic Suit":                           LegoBatman1ItemData("Suits",        45035996203, ItemClassification.progression),
    "Heat Protection Suit":                 LegoBatman1ItemData("Suits",        45035996204, ItemClassification.progression),
    "Technology Suit":                      LegoBatman1ItemData("Suits",        45035996205, ItemClassification.progression),
    "Magnet Suit":                          LegoBatman1ItemData("Suits",        45035996206, ItemClassification.progression),
    "Attract Suit":                         LegoBatman1ItemData("Suits",        45035996207, ItemClassification.progression),
    "Water Suit":                           LegoBatman1ItemData("Suits",        45035996208, ItemClassification.progression),

    #Suit Upgrades
    "Fast Grapple":                         LegoBatman1ItemData("Suit Upgrades",45035996209, ItemClassification.useful),
    "Fast Batarangs":                       LegoBatman1ItemData("Suit Upgrades",45035996210, ItemClassification.useful),
    "More Batarang Targets":                LegoBatman1ItemData("Suit Upgrades",45035996211, ItemClassification.useful),
    "Flaming Batarang":                     LegoBatman1ItemData("Suit Upgrades",45035996212, ItemClassification.useful),
    "Slam":                                 LegoBatman1ItemData("Suit Upgrades",45035996213, ItemClassification.useful),
    "More Detonators":                      LegoBatman1ItemData("Suit Upgrades",45035996214, ItemClassification.useful),
    "Armour Plating":                       LegoBatman1ItemData("Suit Upgrades",45035996215, ItemClassification.useful),
    "Sonic Pain":                           LegoBatman1ItemData("Suit Upgrades",45035996216, ItemClassification.useful),
    "Bats":                                 LegoBatman1ItemData("Suit Upgrades",45035996217, ItemClassification.useful),
    "Freeze Batarang":                      LegoBatman1ItemData("Suit Upgrades",45035996218, ItemClassification.useful),
    "Decoy":                                LegoBatman1ItemData("Suit Upgrades",45035996219, ItemClassification.useful),
    "Fast Magnet Walk":                     LegoBatman1ItemData("Suit Upgrades",45035996220, ItemClassification.useful),
    "Faster Pieces":                        LegoBatman1ItemData("Suit Upgrades",45035996221, ItemClassification.useful),
    "Piece Detector":                       LegoBatman1ItemData("Suit Upgrades",45035996222, ItemClassification.useful),
    
    #Extras
    "Score x2":                             LegoBatman1ItemData("Extras",       45035996223, ItemClassification.useful),
    "Score x4":                             LegoBatman1ItemData("Extras",       45035996224, ItemClassification.useful),
    "Score x6":                             LegoBatman1ItemData("Extras",       45035996225, ItemClassification.useful),
    "Score x8":                             LegoBatman1ItemData("Extras",       45035996226, ItemClassification.progression),
    "Score x10":                            LegoBatman1ItemData("Extras",       45035996227, ItemClassification.useful),
    "Stud Magnet":                          LegoBatman1ItemData("Extras",       45035996228, ItemClassification.useful),
    "Character Studs":                      LegoBatman1ItemData("Extras",       45035996229, ItemClassification.useful),
    "Silhouettes":                          LegoBatman1ItemData("Extras",       45035996230, ItemClassification.filler),
    "Beep Beep":                            LegoBatman1ItemData("Extras",       45035996231, ItemClassification.filler),
    "Ice Rink":                             LegoBatman1ItemData("Extras",       45035996232, ItemClassification.filler),
    "Disguise":                             LegoBatman1ItemData("Extras",       45035996233, ItemClassification.filler),
    "Minikit Detector":                     LegoBatman1ItemData("Extras",       45035996234, ItemClassification.progression),
    "Power Brick Detector":                 LegoBatman1ItemData("Extras",       45035996235, ItemClassification.progression),
    "Always Score Multiply":                LegoBatman1ItemData("Extras",       45035996236, ItemClassification.useful),
    "Fast Build":                           LegoBatman1ItemData("Extras",       45035996237, ItemClassification.useful),
    "Immune to Freeze":                     LegoBatman1ItemData("Extras",       45035996238, ItemClassification.useful),
    "Regenerate Hearts":                    LegoBatman1ItemData("Extras",       45035996239, ItemClassification.useful),
    "Extra Hearts":                         LegoBatman1ItemData("Extras",       45035996240, ItemClassification.useful),
    "Invincibility":                        LegoBatman1ItemData("Extras",       45035996241, ItemClassification.useful),
    "Extra Toggle":                         LegoBatman1ItemData("Extras",       450359962128, ItemClassification.filler),

    #Levels
    "You Can Bank on Batman":               LegoBatman1ItemData("Levels",       45035996242, ItemClassification.progression),
    "An Icy Reception":                     LegoBatman1ItemData("Levels",       45035996243, ItemClassification.progression),
    "Two-Face Chase":                       LegoBatman1ItemData("Levels",       45035996244, ItemClassification.progression),
    "A Poisonous Appointment":              LegoBatman1ItemData("Levels",       45035996245, ItemClassification.progression),
    "The Face-Off":                         LegoBatman1ItemData("Levels",       45035996246, ItemClassification.progression),
    "There She Goes Again":                 LegoBatman1ItemData("Levels",       45035996247, ItemClassification.progression),
    "Batboat Battle":                       LegoBatman1ItemData("Levels",       45035996248, ItemClassification.progression),
    "Under the City":                       LegoBatman1ItemData("Levels",       45035996249, ItemClassification.progression),
    "Zoo's Company":                        LegoBatman1ItemData("Levels",       45035996250, ItemClassification.progression),
    "Penguin's Lair":                       LegoBatman1ItemData("Levels",       45035996251, ItemClassification.progression),
    "Joker's Home Turf":                    LegoBatman1ItemData("Levels",       45035996252, ItemClassification.progression),
    "Little Fun at Big Top":                LegoBatman1ItemData("Levels",       45035996253, ItemClassification.progression),
    "Flight of the Bat":                    LegoBatman1ItemData("Levels",       45035996254, ItemClassification.progression),
    "In the Dark Night":                    LegoBatman1ItemData("Levels",       45035996255, ItemClassification.progression),
    "To the Top of the Tower":              LegoBatman1ItemData("Levels",       45035996256, ItemClassification.progression),
    "The Riddler Makes a Withdrawl":        LegoBatman1ItemData("Levels",       45035996257, ItemClassification.progression),
    "On the Rocks":                         LegoBatman1ItemData("Levels",       45035996258, ItemClassification.progression),
    "Green Fingers":                        LegoBatman1ItemData("Levels",       45035996259, ItemClassification.progression),
    "An Enterprising Theft":                LegoBatman1ItemData("Levels",       45035996260, ItemClassification.progression),
    "Breaking Blocks":                      LegoBatman1ItemData("Levels",       45035996261, ItemClassification.progression),
    "Rockin' the Docks":                    LegoBatman1ItemData("Levels",       45035996262, ItemClassification.progression),
    "Stealing the Show":                    LegoBatman1ItemData("Levels",       45035996263, ItemClassification.progression),
    "Harboring a Grudge":                   LegoBatman1ItemData("Levels",       45035996264, ItemClassification.progression),
    "A Daring Rescue":                      LegoBatman1ItemData("Levels",       45035996265, ItemClassification.progression),
    "Artic World":                          LegoBatman1ItemData("Levels",       45035996266, ItemClassification.progression),
    "A Surpise for the Commissioner":       LegoBatman1ItemData("Levels",       45035996267, ItemClassification.progression),
    "Biplane Blast":                        LegoBatman1ItemData("Levels",       45035996268, ItemClassification.progression),
    "The Joker's Masterpiece":              LegoBatman1ItemData("Levels",       45035996269, ItemClassification.progression),
    "The Lure of the Night":                LegoBatman1ItemData("Levels",       45035996270, ItemClassification.progression),
    "Dying of Laughter":                    LegoBatman1ItemData("Levels",       45035996271, ItemClassification.progression),



    #True Status
    "True Status":                         LegoBatman1ItemData("True Status",450359962123, ItemClassification.progression_skip_balancing,30),

    #Junk
    "Power Up":                            LegoBatman1ItemData("Junk",       450359962124, ItemClassification.filler,60),
    "Ice Trap":                            LegoBatman1ItemData("Junk",       450359962125, ItemClassification.trap),
    "Ice Rink Trap":                       LegoBatman1ItemData("Junk",       450359962126, ItemClassification.trap),
}

charshopsanity_item = {
    #Shop Chars
    "Bruce Wayne":                          LegoBatman1ItemData("Shop Chars",   45035996272, ItemClassification.filler),
    "Alfred":                               LegoBatman1ItemData("Shop Chars",   45035996273, ItemClassification.filler),
    "Batgirl":                              LegoBatman1ItemData("Shop Chars",   45035996274, ItemClassification.filler),
    "Nightwing":                            LegoBatman1ItemData("Shop Chars",   45035996275, ItemClassification.filler),
    "Commissioner Gordon":                  LegoBatman1ItemData("Shop Chars",   45035996277, ItemClassification.filler),
    "Mad Hatter":                           LegoBatman1ItemData("Shop Chars",   45035996276, ItemClassification.progression),
    "Fishmonger":                           LegoBatman1ItemData("Shop Chars",   45035996278, ItemClassification.filler),
    "Scientist":                            LegoBatman1ItemData("Shop Chars",   45035996279, ItemClassification.filler),
    "Security Guard":                       LegoBatman1ItemData("Shop Chars",   45035996280, ItemClassification.filler),
    "Police Marksman":                      LegoBatman1ItemData("Shop Chars",   45035996281, ItemClassification.filler),
    "Police Officer":                       LegoBatman1ItemData("Shop Chars",   45035996282, ItemClassification.filler),
    "S.W.A.T.":                             LegoBatman1ItemData("Shop Chars",   45035996283, ItemClassification.filler),
    "Sailor":                               LegoBatman1ItemData("Shop Chars",   45035996283, ItemClassification.filler),
    "Miltary Police":                       LegoBatman1ItemData("Shop Chars",   45035996284, ItemClassification.filler),
    "Yeti":                                 LegoBatman1ItemData("Shop Chars",   45035996285, ItemClassification.filler),
    "Penguin Minion":                       LegoBatman1ItemData("Shop Chars",   45035996286, ItemClassification.useful),
    "Catwoman (Classic)":                   LegoBatman1ItemData("Shop Chars",   45035996287, ItemClassification.progression),
    "Man-Bat":                              LegoBatman1ItemData("Shop Chars",   45035996288, ItemClassification.progression),
    "Joker (Tropical)":                     LegoBatman1ItemData("Shop Chars",   45035996289, ItemClassification.progression),
    "Poison Ivy Goon":                      LegoBatman1ItemData("Shop Chars",   45035996290, ItemClassification.filler),
    "Freeze Girl":                          LegoBatman1ItemData("Shop Chars",   45035996291, ItemClassification.filler),
    "Zoo Sweeper":                          LegoBatman1ItemData("Shop Chars",   45035996292, ItemClassification.filler),
    "Riddler Goon":                         LegoBatman1ItemData("Shop Chars",   45035996293, ItemClassification.filler),
    "Riddler Henchman":                     LegoBatman1ItemData("Shop Chars",   45035996294, ItemClassification.filler),
    "Penguin Goon":                         LegoBatman1ItemData("Shop Chars",   45035996295, ItemClassification.filler),
    "Penguin Henchman":                     LegoBatman1ItemData("Shop Chars",   45035996296, ItemClassification.filler), 
    "Joker Goon":                           LegoBatman1ItemData("Shop Chars",   45035996297, ItemClassification.filler),
    "Clown Goon":                           LegoBatman1ItemData("Shop Chars",   45035996298, ItemClassification.filler),    
    "Joker Henchman":                       LegoBatman1ItemData("Shop Chars",   45035996299, ItemClassification.filler),         
    "Police Car":                           LegoBatman1ItemData("Shop Chars",   450359962100, ItemClassification.filler),
    "Police Bike":                          LegoBatman1ItemData("Shop Chars",   450359962101, ItemClassification.filler),    
    "Police Van":                           LegoBatman1ItemData("Shop Chars",   450359962102, ItemClassification.filler),
    "Bat-Tank":                             LegoBatman1ItemData("Shop Chars",   450359962103, ItemClassification.filler),
    "Two-Face's Armored Truck":             LegoBatman1ItemData("Shop Chars",   450359962104, ItemClassification.filler),
    "Garbage Truck":                        LegoBatman1ItemData("Shop Chars",   450359962105, ItemClassification.filler),
    "Catwoman's Motorcycle":                LegoBatman1ItemData("Shop Chars",   450359962106, ItemClassification.filler),
    "Mr.Freeze's Kart":                     LegoBatman1ItemData("Shop Chars",   450359962107, ItemClassification.filler),
    "Police Watercraft":                    LegoBatman1ItemData("Shop Chars",   450359962108, ItemClassification.filler),
    "Police Boat":                          LegoBatman1ItemData("Shop Chars",   450359962109, ItemClassification.filler),
    "Penguin Goon Submarine":               LegoBatman1ItemData("Shop Chars",   450359962110, ItemClassification.progression),
    "Mad Hatter's Steamboat":               LegoBatman1ItemData("Shop Chars",   450359962111, ItemClassification.filler),
    "Robin's Submarine":                    LegoBatman1ItemData("Shop Chars",   450359962112, ItemClassification.progression),
    "Mr.Freeze's Iceberg":                  LegoBatman1ItemData("Shop Chars",   450359962113, ItemClassification.filler),                   
    "The Joker Van":                        LegoBatman1ItemData("Shop Chars",   450359962114, ItemClassification.progression),
    "Harley Quinn's Hammer Truck":          LegoBatman1ItemData("Shop Chars",   450359962115, ItemClassification.progression),
    "Police Helicopter":                    LegoBatman1ItemData("Shop Chars",   450359962116, ItemClassification.filler),
    "Bruce Wayne's Private Jet":            LegoBatman1ItemData("Shop Chars",   450359962117, ItemClassification.filler),
    "Goon Helicopter":                      LegoBatman1ItemData("Shop Chars",   450359962118, ItemClassification.progression),
    "Mad Hatter's Glider":                  LegoBatman1ItemData("Shop Chars",   450359962119, ItemClassification.filler),
    "Riddler Jet":                          LegoBatman1ItemData("Shop Chars",   450359962120, ItemClassification.filler),
    "Harbor Helicopter":                    LegoBatman1ItemData("Shop Chars",   450359962121, ItemClassification.filler),   
}

hostagesanity_item = {
    #Hostages 
    "Hostage":                             LegoBatman1ItemData("Hostage",    450359962127, ItemClassification.progression,25),
}

kitsanity_item = {
    #Kits
    "Mini-Kit":                             LegoBatman1ItemData("Mini-Kits",    45035996200, ItemClassification.progression,300),
}
} 


event_item_table: Dict[str, LegoBatman1ItemData] = {
    "Completed All Levels":     LegoBatman1ItemData("Event", classification=ItemClassification.progression),
    "Completed Arkham Asylum":  LegoBatman1ItemData("Event", classification=ItemClassification.progression),
    "Completed Wayne Mannor":   LegoBatman1ItemData("Event", classification=ItemClassification.progression),
    "Ra Sha Guul":              LegoBatman1ItemData("Event", classification=ItemClassification.progression),
    "Hush":                     LegoBatman1ItemData("Event", classification=ItemClassification.progression),
    "100% Obtained":            LegoBatman1ItemData("Event", classification=ItemClassification.progression),
}

def get_items(world):
    item_table = basic_item.copy()
    
    if world.options.char_shop_sanity:
        item_table.update(charshopsanity_item)

    if world.options.hostage_sanity:
        item_table.update(hostagesanity_item)

    if world.options.kit_sanity:
        item_table.update(kitsanity_item)
    
    return item_table
