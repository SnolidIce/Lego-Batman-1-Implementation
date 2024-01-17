import string

from .items import RiskOfRainItem, item_table, item_pool_weights, offset, filler_table, environment_offset
from .locations import RiskOfRainLocation, item_pickups, get_locations
from .rules import set_rules
from .ror2environments import environment_vanilla_table, environment_vanilla_orderedstages_table, \
    environment_sotv_orderedstages_table, environment_sotv_table, collapse_dict_list_vertical, shift_by_offset

from BaseClasses import Item, ItemClassification, Tutorial
from .options import ItemWeights, ROR2Options
from worlds.AutoWorld import World, WebWorld
from .regions import create_explore_regions, create_classic_regions
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
    total_revivals: int

    def generate_early(self) -> None:
        # figure out how many revivals should exist in the pool
        if self.options.goal == "classic":
            total_locations = self.options.total_locations.value
        else:
            total_locations = len(
                get_locations(
                    chests=self.options.chests_per_stage.value,
                    shrines=self.options.shrines_per_stage.value,
                    scavengers=self.options.scavengers_per_stage.value,
                    scanners=self.options.scanner_per_stage.value,
                    altars=self.options.altars_per_stage.value,
                    dlc_sotv=bool(self.options.dlc_sotv.value)
                )
            )
        self.total_revivals = int(self.options.total_revivals.value / 100 *
                                  total_locations)
        if self.options.start_with_revive:
            self.total_revivals -= 1
        if self.options.victory == "voidling" and not self.options.dlc_sotv:
            self.options.victory.value = self.options.victory.option_any

    def create_regions(self) -> None:

        if self.options.goal == "classic":
            # classic mode
            create_classic_regions(self)
        else:
            # explore mode
            create_explore_regions(self)

        self.create_events()

    def create_items(self) -> None:
        # shortcut for starting_inventory... The start_with_revive option lets you start with a Dio's Best Friend
        if self.options.start_with_revive:
            self.multiworld.push_precollected(self.multiworld.create_item("Dio's Best Friend", self.player))

        environments_pool = {}
        # only mess with the environments if they are set as items
        if self.options.goal == "explore":

            # figure out all available ordered stages for each tier
            environment_available_orderedstages_table = environment_vanilla_orderedstages_table
            if self.options.dlc_sotv:
                environment_available_orderedstages_table = \
                    collapse_dict_list_vertical(environment_available_orderedstages_table,
                                                environment_sotv_orderedstages_table)

            environments_pool = shift_by_offset(environment_vanilla_table, environment_offset)

            if self.options.dlc_sotv:
                environment_offset_table = shift_by_offset(environment_sotv_table, environment_offset)
                environments_pool = {**environments_pool, **environment_offset_table}
            environments_to_precollect = 5 if self.options.begin_with_loop else 1
            # percollect environments for each stage (or just stage 1)
            for i in range(environments_to_precollect):
                unlock = self.random.choices(list(environment_available_orderedstages_table[i].keys()), k=1)
                self.multiworld.push_precollected(self.create_item(unlock[0]))
                environments_pool.pop(unlock[0])

        # Generate item pool
        itempool: List[str] = ["Beads of Fealty", "Radar Scanner"]
        # Add revive items for the player
        itempool += ["Dio's Best Friend"] * self.total_revivals

        for env_name, _ in environments_pool.items():
            itempool += [env_name]

        if self.options.goal == "classic":
            # classic mode
            total_locations = self.options.total_locations.value
        else:
            # explore mode
            # Add Stage items for logic gates
            itempool += ["Stage 1", "Stage 2", "Stage 3", "Stage 4"]
            total_locations = len(
                get_locations(
                    chests=self.options.chests_per_stage.value,
                    shrines=self.options.shrines_per_stage.value,
                    scavengers=self.options.scavengers_per_stage.value,
                    scanners=self.options.scanner_per_stage.value,
                    altars=self.options.altars_per_stage.value,
                    dlc_sotv=bool(self.options.dlc_sotv.value)
                )
            )
        # Create junk items
        junk_pool = self.create_junk_pool()
        # Fill remaining items with randomly generated junk
        filler = self.random.choices(*zip(*junk_pool.items()), k=total_locations - len(itempool))
        itempool.extend(filler)

        # Convert itempool into real items
        self.multiworld.itempool += map(self.create_item, itempool)

    def create_junk_pool(self) -> Dict[str, int]:
        # if presets are enabled generate junk_pool from the selected preset
        pool_option = self.options.item_weights.value
        junk_pool: Dict[str, int] = {}
        if self.options.item_pool_presets:
            # generate chaos weights if the preset is chosen
            if pool_option == ItemWeights.option_chaos:
                for name, max_value in item_pool_weights[pool_option].items():
                    junk_pool[name] = self.random.randint(0, max_value)
            else:
                junk_pool = item_pool_weights[pool_option].copy()
        else:  # generate junk pool from user created presets
            junk_pool = {
                "Item Scrap, Green": self.options.green_scrap.value,
                "Item Scrap, Red": self.options.red_scrap.value,
                "Item Scrap, Yellow": self.options.yellow_scrap.value,
                "Item Scrap, White": self.options.white_scrap.value,
                "Common Item": self.options.common_item.value,
                "Uncommon Item": self.options.uncommon_item.value,
                "Legendary Item": self.options.legendary_item.value,
                "Boss Item": self.options.boss_item.value,
                "Lunar Item": self.options.lunar_item.value,
                "Void Item": self.options.void_item.value,
                "Equipment": self.options.equipment.value,
                "Money": self.options.money.value,
                "Lunar Coin": self.options.lunar_coin.value,
                "1000 Exp": self.options.experience.value,
                "Mountain Trap": self.options.mountain_trap.value,
                "Time Warp Trap": self.options.time_warp_trap.value,
                "Combat Trap": self.options.combat_trap.value,
                "Teleport Trap": self.options.teleport_trap.value,
            }
        # remove trap items from the pool (excluding lunar items)
        if not self.options.enable_trap:
            junk_pool.pop("Mountain Trap")
            junk_pool.pop("Time Warp Trap")
            junk_pool.pop("Combat Trap")
            junk_pool.pop("Teleport Trap")
        # remove lunar items from the pool
        if not (self.options.enable_lunar or pool_option == ItemWeights.option_lunartic):
            junk_pool.pop("Lunar Item")
        # remove void items from the pool
        if not (self.options.dlc_sotv or pool_option == ItemWeights.option_void):
            junk_pool.pop("Void Item")

        return junk_pool

    def create_item(self, name: str) -> Item:
        data = item_table[name]
        return RiskOfRainItem(name, data.item_type, data.code, self.player)

    def set_rules(self) -> None:
        set_rules(self)

    def get_filler_item_name(self) -> str:
        weights = [data.weight for data in filler_table.values()]
        filler = self.multiworld.random.choices([filler for filler in filler_table.keys()], weights,
                                                k=1)[0]
        return filler

    def fill_slot_data(self) -> Dict[str, Any]:
        options_dict = self.options.as_dict("item_pickup_step", "shrine_use_step", "goal", "victory", "total_locations",
                                            "chests_per_stage", "shrines_per_stage", "scavengers_per_stage",
                                            "scanner_per_stage", "altars_per_stage", "total_revivals",
                                            "start_with_revive", "final_stage_death", "death_link",
                                            casing="camel")
        return {
            **options_dict,
            "seed": "".join(self.random.choice(string.digits) for _ in range(16)),
            "offset": offset
        }

    def create_events(self) -> None:
        total_locations = self.options.total_locations.value
        num_of_events = total_locations // 25
        if total_locations / 25 == num_of_events:
            num_of_events -= 1
        world_region = self.multiworld.get_region("Petrichor V", self.player)
        if self.options.goal == "classic":
            # classic mode
            # only setup Pickups when using classic_mode
            for i in range(num_of_events):
                event_loc = RiskOfRainLocation(self.player, f"Pickup{(i + 1) * 25}", None, world_region)
                event_loc.place_locked_item(
                    RiskOfRainItem(f"Pickup{(i + 1) * 25}", ItemClassification.progression, None,
                                   self.player))
                event_loc.access_rule = \
                    lambda state, i=i: state.can_reach(f"ItemPickup{((i + 1) * 25) - 1}", "Location", self.player)
                world_region.locations.append(event_loc)
        else:
            # explore mode
            event_region = self.multiworld.get_region("OrderedStage_5", self.player)
            event_loc = RiskOfRainLocation(self.player, "Stage 5", None, event_region)
            event_loc.place_locked_item(RiskOfRainItem("Stage 5", ItemClassification.progression, None, self.player))
            event_loc.show_in_spoiler = False
            event_region.locations.append(event_loc)
            event_loc.access_rule = lambda state: state.has("Sky Meadow", self.player)

        victory_region = self.multiworld.get_region("Victory", self.player)
        victory_event = RiskOfRainLocation(self.player, "Victory", None, victory_region)
        victory_event.place_locked_item(RiskOfRainItem("Victory", ItemClassification.progression, None, self.player))
        victory_region.locations.append(victory_event)