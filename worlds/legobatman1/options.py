from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, DeathLink, Range, Choice, PerGameCommonOptions

class Goal(Choice):
    """
    Hero Levels: Unlock and complete all hero campaigns levels to win.

    Villain Levels: Unlock and complete all hero campaigns levels to win.

    All Levels: Unlock and complete both campaigns to win.

    Mini Kits: Collect all the Mini Kits and beat the two bonus levels to win.
    
    Unlock Hush: Collect all Hostages and buy Hush

    Unlock Ra Sha Guul: Also known as 100%, Almost every single item is needed
    DO NOT do Ra Sha Guul goal in a sync you are an awful person if you do.
    """
    display_name = "Goal"
    option_hero_levels = 0
    option_villain_levels = 1
    option_all_levels = 2
    option_kits = 3
    option_hush = 4
    option_ra_sha_guul = 5
    default = 0


class Logic(Choice):
    """
    Glitchless: Locations are gotten through the normal methods as the game devs intended. 
    You can make minor optimizations but nothing too crazy
    
    Glitched: WARNING VERY HARD AND REQUIRES A LOT OF PRACTICE. Puts all glitches from Lego Batman into logic.
    These glitches require a lot of hard work to be consitant at.

    Story Pickups: A more advanced version of glitched logic, this adds logic for all the glitches you can use to grab items in story. 
    """
    display_name = "Logic"
    option_glitchless = 0
    option_glitched = 1
    option_story_pickups = 2
    default = 0


class MiniKitSanity(Toggle):
    """Puts all 300 Mini-Kits into the pool. 
    This setting is forced on Mini-Kit Goal
    """
    display_name = "Mini-KitSanity"


class HostageSanity(Toggle):
    """Puts all 25 Hostages into the pool. 
    This setting is forced on Unlock Hush Goal
    """
    display_name = "HostageSanity"


class CharacterShopSanity(Toggle):
    """Puts all 49 characters in the shop into the pool.
    Hush and Ra Sha Guul are never added into the pool due to being potineal goals
    """
    display_name = "CharacterShopSanity"

class StartingLevels(Choice):
    """What levels you start off with.
    Vanillia: Start with only the first level of hero campaign 
    Withdraw: Start with only the first level of villain campaign
    Bank & Withdraw: Start with the first level of hero and villain Campaign (Gives more in Sphere 1)
    Random Level: Start with a random level from any campaign
    Random Both: Start with 2 random  levels, one from each campaign
    Random Any: Start with 2 random levels
    Random Vehicle: Start with a random vehicle level
    Random Non Vehicle: Start with a random non vehicle level
    Random Both Vechile & Non Vechile: Start with a random vechile level and a random non vechile level
    """
    display_name = "Starting Levels"
    option_vanillia = 0
    option_withdraw = 1
    option_bank_withdraw = 2
    option_random_lvl = 3
    option_random_both = 4
    option_random_any = 5
    option_random_vehicle = 6
    option_random_non_vehicle = 7
    option_random_vechile_non = 8
    default = 0

class DectectorLogic(Toggle):
    """Adds a rule where Mini Kit Dector and Red Brick Dector are required for Mini Kits and Red Bricks to be in logic"""
    display_name = "Dectctors Required?"

class RequireMultipliers(Toggle):
    """Requires atleast a stud multipler for True Statuses and characters in shop to be in logic. 
    The ammount required for true status and purchases are turned up.
    6x Studs becomes progression instead of useful.
    """
    display_name = "Require Stud Multipliers?"


class IncreaseCharSpeed(Toggle):
    """
    Makes the character speed slightly faster. Can help making sync games not as long
    """
    display_name = "Increase Character Movement Speed?"

class Hints(Toggle):
    """
    Hints are in the level loading text, you need to wait for the all the text before you can get your hint and you always get a hint related to that level. Adds 30 hints
    """
    display_name = "Hints?"


class HintItems(Choice):
    """
    Local Item: Hints are only related to your items on your Slot
    Local Location: Hints are only related to your locations on your Slot
    Current Level: Hints are only related to the level you are about to enter
    Anything: Hints can be any item in the multiworld
    """
    display_name = "Hint Locations"
    option_local_item = 0
    option_local_item = 1
    option_current_level = 2
    option_anything = 3
    default = 0


class AllowTrapItems(Toggle):
    """Allows Trap items in the item pool."""
    display_name = "Enable Trap Items"

class TrapPrecentage(Range):
    """The ammount of traps that replace filler items."""
    display_name = "Trap Weight"
    range_start = 1
    range_end = 100
    default = 15

class TrapApperance(Choice):
    """
    What trap items look like. 
    """
    display_name = "Trap Apperance"
    option_important = 0
    option_anything = 1
    option_ap_item_only = 2
    default = 0
    
class DeathLinkAmnesty(Range):
    """Amount of Deaths to take before sending a DeathLink signal, due to how easy it is to die"""
    range_start = 0
    range_end = 15
    default = 4


@dataclass
class LegoBatman1Options(PerGameCommonOptions):
    goal: Goal
    logic: Logic
    kit_sanity: MiniKitSanity
    hostage_sanity: HostageSanity
    char_shop_sanity: CharacterShopSanity
    start_level: StartingLevels
    multipler_req: RequireMultipliers
    dector_req: DectectorLogic
    speed_up: IncreaseCharSpeed
    hints: Hints
    hint_items: HintItems
    enable_trap: AllowTrapItems
    trap_percent: TrapPrecentage
    trap_apperance: TrapApperance
    death_link: DeathLink
    DeathLinkAmnesty: DeathLinkAmnesty

