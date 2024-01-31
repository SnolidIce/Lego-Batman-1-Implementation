import string

from .items import LegoBatman1Item, item_table, item_pool_weights, offset, filler_table
from .locations import LegoBatman1Location
from .rules import set_rules

from BaseClasses import Item, ItemClassification, Tutorial
from .options import ItemWeights, LegoBatman1Options
from worlds.AutoWorld import World, WebWorld
from .regions 
from typing import List, Dict, Any


class LegoBatman1(WebWorld):
    theme = "stone"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Risk of Rain 2 integration for Archipelago multiworld games.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Ijwu", "Kindasneaki"]
    )]


class LegoBatman1World(World):
    """
     When all the villains in Arkham Asylum team up and break loose, only the dynamic duo is bold enough to take them on to save Gotham City. 
     The fun of LEGO, the drama of Batman and the uniqueness of the combination makes for a comical and exciting adventure in LEGO Batman: The Videogame. 
    """ #Lazy Import
    game = "Lego Batman: The Video Game"
    options_dataclass = LegoBatman1Options
    options: LegoBatman1Options
    topology_present = True

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}

    data_version = 1
    required_client_version = (0, 4, 4)
    web = LegoBatman1Web()
   
