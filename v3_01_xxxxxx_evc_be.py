

import heapq
import sys


class Character:

    available = {
        "Aalto" :                                  [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.50, 0, 0.5 * 0.25, 0.5 * 0.15, - 135, - 0.65 / 0.9, 0, - 150, - 1],
        "Baizhi" :                                 [0, 0, 0, 0, 1, 0.5, 0, 0, 0, 0, 0, 0, - 215, - 1, 0, - 175, 0],
        "Brant (sub DPS, ER/ER 3 cost setup)" :    [1, 1, 0.3, 0.2, 0, 0, 0, 0, 0.55, 0, 0, 0.0375, - 285, - 0.6, 0, - 175, - 1],
        "Calcharo" :                               [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.25, 0, 0, 0.5 * 0.55, - 125, - 1, 0, - 125, - 1],
        "Camellya" :                               [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.7, 0, 0, 0.5 * 0.15, - 120, - 0.15 / 0.85, 0, - 125, - 1],
        "Carlotta" :                               [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0, 0.5 * 0.85, 0, - 125, - 1, 0, - 125, - 1],
        "Changli" :                                [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.05, 0, 0.5 * 0.6, 0.5 * 0.25, - 125, - 0.25/0.9, 0, - 125, - 1],
        "Chixia" :                                 [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0, 0.5 * 0.5, 0.5 * 0.3, - 150, - 0.3 / 0.8, 0, -150, -1],
        "Danjin" :                                 [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.05, 0.5 * 0.25, 0.5 * 0.25, 0.5 * 0.3, 0, 0, 0, - 100, - 1],
        "Encore (Hypercarry)":                     [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.5, 0, 0.5 * 0.2, 0.5 * 0.1, - 125, - 1, 0, - 125, - 1],
        "Jianxin (DPS/sub DPS)":                   [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.25, 0.5 * 0.4, 0, 0.5 * 0.3, - 130, - 0.3 / 0.95, 0, - 150, - 1],
        "Jinhsi":                                  [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0, 0.5 * 0.75, 0.5 * 0.2, - 115, - 0.2 / 0.95, 0, - 150, - 1],
        "Jiyan":                                   [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0.5 * 0.7, 0.5 * 0.15, 0, - 130, - 1, 0, - 125, - 1],
        "Lingyang":                                [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.35, 0, 0.5 * 0.3, 0.5 * 0.05, - 125, - 1, 0, - 125, - 1],
        "Lumi":                                    [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.35, 0, 0.5 * 0.25, 0.5 * 0.3, - 165, - 1, 0, - 125, - 1],
        "Mortefi":                                 [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.1, 0, 0.5 * 0.15, 0.5 * 0.7, - 125, - 1, 0, - 125, - 1],
        "Phoebe":                                  [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.15, 0.5 * 0.45, 0, 0.5 * 0.15, 0, - 0.15 / 0.75, 0, - 125, -1],
        "Roccia":                                  [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.05, 0.5 * 0.6, 0.5 * 0.15, 0, - 135, - 1, 0, - 125, - 1],
        "Spectro Rover":                           [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.05, 0.5 * 0.1, 0.5 * 0.3, 0.5 * 0.35, 0, - 0.35 / 0.8, 0, - 125, -1],
        "Havoc Rover":                             [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.3, 0, 0.5 * 0.2, 0.5 * 0.25, - 125, - 0.25 / 0.75, 0, - 125, - 1],
        "Sanhua":                                  [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0.5 * 0.3, 0.5 * 0.3, 0.5 * 0.3, 0, 0, 0, - 100, - 1],
        "Taoqi (sub DPS)":                         [1, 1, 0, 0, 0, 0, 0.5, 0.25, 0.5*0.5, 0, 0, 0.5*0.5, - 120, - 0.5, 0, - 125, -1],
        "Taoqi (sup)":                             [0, 0, 0, 0, 0, 0, 1, 0.5, 0, 0, 0, 0, - 170, - 1, 0, - 125, 0],
        "The Shorekeeper":                         [0, 1, 0, 0, 0.5, 0.25, 0, 0, 0.5 * 0.1, 0, 0, 0.5 * 0.85, - 240, - 1, 0, - 175, 0],
        "Verina":                                  [0, 0, 1, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, - 200, - 1, 0, - 175, 0],
        "Xiangli Yao":                             [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.1, 0, 0.5 * 0.2, 0.5 * 0.55, - 120, - 0.55 / 0.85, 0, - 125, - 1],
        "Yangyang":                                [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.3, 0, 0.5 * 0.15, 0.5 * 0.45, 0, 0, 0, - 100, - 1],
        "Yinlin":                                  [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.1, 0.5 * 0.1, 0.5 * 0.55, 0.5 * 0.2, - 135, - 0.2 / 0.95, 0, - 125, - 1],
        "Youhu":                                   [0, 0, 1, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, - 165, - 1, 0, - 100, 0],
        "Yuanwu":                                  [1, 1, 0, 0, 0, 0, 0.5, 0.25, 0, 0, 0.5 * 0.5, 0.5 * 0.4, - 140, - 1, 0, - 125, - 1],
        "Zhezhi":                                  [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.8, 0.5 * 0.05, 0.5 * 0.05, 0, - 135, - 1, 0, - 125, - 1]
        }
    not_available = ["Cantarella", "Zani"]

    assumptions = {
        "Aalto": None, "Baizhi": None, "Brant (sub DPS, ER/ER 3 cost setup)": "ER/ER 3 cost setup is optimal when Brant's ER is above 130% and less than 282% "
        "(source: Maygi). ", "Calcharo": None, "Camellya": None, "Carlotta": None, "Changli": None, "Chixia": None, "Danjin": None, "Encore (Hypercarry)": "As the "
        "damage profile in quickswap and hypercarry teams is different, the relative value of substats will change as well. This data set is for Hypercarry Encore. ", 
        "Jianxin (DPS/sub DPS)": "Full Forte Circuit is channeled and Liberation is cast every rotation. ", "Jinhsi": None, "Jiyan": None, "Lingyang": None, "Lumi": 
        "Built as sub DPS. ", "Mortefi": None, "Phoebe": None, "Roccia": None, "Spectro Rover": None, "Havoc Rover": None, "Sanhua": None, "Taoqi (sub DPS)": "S5 is "
        "unlocked. Assuming two liberation casts and two sets of timed-counters per rotation", "Taoqi (sup)": "S4 or below. Not built for any damage. One liberation "
        "cast and one set of timed-counters per rotation. ", "The Shorekeeper": None, "Verina": None, "Xiangli Yao": None, "Yangyang": None, "Yinlin": None, 
        "Youhu": None, "Yuanwu": None, "Zhezhi": None
        }

    def __init__(self, name_in: str) -> None:

        self.name = name_in
        self.data = Character.available[self.name]
        self.ass: str = Character.assumptions[self.name]
        self.net_er = 0.0

    @property
    def data(self) -> dict : return self._data

    @data.setter
    def data(self, rel_substat_val: list) -> None:
        
        if len(rel_substat_val) != 17: raise CorruptData
        for stat_index in range(12, 17):
            if rel_substat_val[stat_index] > 0: raise CorruptData
        dict_rel_substat_val: GameData = GameData.get("Potential")
        dict_rel_substat_val.data = [rel_substat_val, "Potential"]
        self._data: dict = dict_rel_substat_val.data

    @classmethod
    def get(cls, name_in):
        
        try: return cls(name_in)
        except DataError: print("Character Data unavailable. Please select a different character. ")
        except ValueError: print("Character name not recognized. Please try again. ")
        except CorruptData: print("Character Data is corrupt. If possible, please report this to AstyuteChick via reddit or github. ")


class GameData:

    norm_stat_meds = [8.4, 16.8, 9, 45, 9, 450, 11.4, 55, 9, 9, 9, 9, 9.6]
    od_stat_meds = [10.5, 21, 11.6, 60, 11.6, 580, 14.7, 70, 11.6, 11.6, 11.6, 11.6, 12.4]
    substat_val = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    potential_val = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    stat_keys = ["Crit Rate (%)", "Crit Damage (%)", "Atk (%)", "Flat Atk", "HP (%)", "Flat HP", "Def (%)", "Flat Def", "Basic Atk bonus (%)", "Heavy Atk Bonus (%)", 
                 "Skill bonus (%)", "Liberation bonus (%)", "ER (%)", "_Liberation_Impact_", "_ER%_rel_val_", "Resonance Cost", "_Analysis?_"]
    mainstats = [{"Crit Rate (%)": 22, "Crit Damage (%)": 44, "Atk (%)": 33, "Flat Atk": 150, "HP (%)": 33, "Def (%)": 41.5},
                 {"Atk (%)": 30, "Flat Atk": 100, "HP (%)": 30, "Def (%)": 38, "ER (%)": 32},
                 {"Atk (%)": 18, "HP (%)": 22.8, "Flat HP": 2280, "Def (%)": 18}]

    def __init__(self, data_array: list, data_struct: str) -> None:
        
        self.data = [data_array, data_struct]

    @property
    def data(self) -> dict: return self._data

    @data.setter
    def data(self, data_vals: list) -> None:
        data_dict = {}
        match data_vals[1]:
            case "Medians" | "Value":
                if len(data_vals[0]) != 13: raise CorruptData(data_vals[0] + "Array Length array has incorrect size. ")
            case "Potential":
                if len(data_vals[0]) != 17: raise CorruptData("Potential Array has incorrect size. ")
            case _:
                raise CorruptData("Data couldn't be set. ")
        for index in range(len(data_vals[0])):
            data_dict[GameData.stat_keys[index]] = data_vals[0][index]
        self._data:dict = data_dict

    @classmethod
    def get(cls, data_type: str):

        if data_type == "Normal Stat Medians": return cls(cls.norm_stat_meds, "Medians")
        elif data_type == "OverDrive Stat Medians": return cls(cls.od_stat_meds, "Medians")
        elif data_type == "Value": return cls(cls.substat_val, "Value")
        elif data_type == "Potential": return cls(cls.potential_val, "Potential")
        else: raise CorruptData("Data Type not recognized. ")        


class DataError(Exception):
    pass


class CorruptData(Exception):
    pass


def load_data(name: str):

    stat_medians_ld = GameData.get("Normal Stat Medians")
    echo_mainstats_ld = GameData.get("Value")
    character_pick_ld = Character.get(name)

    return stat_medians_ld, echo_mainstats_ld, character_pick_ld


def adjust_er(energy_reqs: float, liberation_cost: float, energy_cons_ae: str) -> float:

    if energy_cons_ae == "y": 
        energy_reqs = (1 + (20 / liberation_cost)) * energy_reqs
        if energy_reqs >= -100: energy_reqs = 0
    elif energy_cons_ae == "x": energy_reqs = 0

    return energy_reqs


def display_menu(calc_mode: str, char_name: str) -> str:

    return (
        "Echo Value Calculator - " + calc_mode + "\nBreif description of all the tabs: \n\n"
        "    01) COMPLETE evaluation: \n"
        "        Rate and analyze every Echo and the overall Echo Set. \n\n"
        "    02) ECHO SET evaluation: \n"
        "        Rate and analyze the full Echo Set directly with the help of Echo presets. \n\n"
        "    03) ECHO evaluation. \n"
        "        Rate and analyze a particular Echo. \n\n"
        "    04) About EVC (nstc) and the scoring method. \n"
        "    05) About Ratings and Brackets. \n"
        "    06) General and character specific (" + char_name + ") assumptions and data. \n\n"
    )
    


def quit_calc() -> None:
    sys.exit()


def general_ass() -> str:

    return (
        "\n---------- ---------- List of general assumptions about your character ---------- ----------\n\n"
        "1. Sensible echo set: Self-explanatory. Usually a character only really has one best-in-slot set, so use that. \n\n"
        "2. Sensible echo main stats: The program can't help you if you're running Defense% and HP% 3 cost and 1 cost echoes on your Jiyan. \n\n"
        "3. Sensible weapon: Again, the program can't help you if you're running Dauntless Evernight on Jinhsi. Look up guides. \n\n"
        "4. Sensible crit ratio: 1.5 < (Crit Damage - 100) / Crit Rate <= 2.2. (Pick option 5 to test crit ratio). \n"
        "NOTE: It's completely okay if you don't fall in this sweet-spot, as long as there is a full attempt without sacrificing feasability. \n"
        "If your character has a crit damage weapon and you're running a crit rate 4 cost and trying to get at least crit rate on all pieces, that's enough. \n"
        "Press enter to continue: \n"
    )


def character_ass(character_pick_ca: Character) -> str:

    if character_pick_ca.ass == None: return character_pick_ca.name + "has no assumptions or they've yet to be populated. "
    else: return character_pick_ca.name + "'s assumptions: \n" + character_pick_ca.ass


def disp_general_data(stat_medians_data: dict) -> str:
    
    dgd_str = "The stat median values currently in use are: \n"
    for stat_name, stat_med in stat_medians_data.items():
        dgd_str = dgd_str + (stat_name + ": " + str(stat_med) + "\n")
    return dgd_str


def disp_character_data(character_pick_dpd: Character) -> str:

    dcd_str = "Following are the relative substat values for " + character_pick_dpd.name + ": \n"
    for substat_name, rel_substat_val in character_pick_dpd.data.items():
        dcd_str = dcd_str + (substat_name + ": " + str(rel_substat_val)+ "\n")
    return dcd_str


def test_crit_ratio(cr: float, cd: float) -> float:

    return (cd - 100) / cr


def char_build_time_optimize() -> str:

    return (
        "\n---------- ---------- Sequence flowchart to make your character ready ASAP ---------- ----------\n\n"
        "It doesn't matter what your standards are for building a character, there is a process you can follow that will make your character 'ready' or "
        "'playable' in the shortest amount of time. If you follow the following steps, you can rest assured that at ANY given time - THIS is the BEST your "
        "chararacter could have been given the waveplates and/or time invested (always keep the above assumptions in mind): \n\n"
        "1. Upgrade and ascend your weapon, character and relevant Fortes (in that order) with ONLY the resources available at THIS moment in time. \n"
        "2. Farm an Echo Set with correct main stats and reach the 'Base Level Tier' build rating. \n"
        "3. Upgrade Weapon to 90/90, Character to 80/80, unlock FULL Forte tree and get relavent fortes to level 8 (in that order). \n"
        "4. Improve Echoes until 'Decent' tier. \n"
        "5. Ascend Character to level 80/90, then level relavent Fortes to level 9. Your character is now built. \n"
        "6. Improve Echoes until 'Well Built' tier. Your character is now well built. \n"
        "(7. Level relavent Fortes to level 10, and character to level 90/90. )\n"
        "(8. Improve Echoes beyond 'Well Built' tier. )\n"
        "9. Switch to the next character. \n"
        "Steps in brackets are OPTIONAL and may be skipped or only partially completed before moving to the next step. \n\n"
        "Press enter to continue: \n"
    )


def abt_ratings_brackets() -> str:

    return(
        "\n---------- ---------- Echo/Build Value brackets ---------- ----------\n\n"
        "Your echoes/builds are rated on a scale where 100 rating means best possible substats are rolled AND they are exactly average rolls. \n\n"
        "Your rating lands your echo/build into one of the following catagories: \n\n"
        "Unbuilt Tier [0<=Score<44]: \nInvesting waveplates into Echos highly optimal. \n\n"
        "Base Level Tier [44<=Score<55]: \nInvesting waveplates into Echoes only optimal after getting Character Level to 80/80, Weapon Level to 90, unlocking the full Forte"
        " tree and leveling relavant Fortes to level 8. \n\n"
        "Decent Tier [55<=Score<66]: \nAssuming previous targets are met, your character now approximately meets the minimum requirements to fully clear the hardest "
        "resetting content and end-game. \n"
        "Highly recommened to secure guaranteed upgrades from ascending and leveling characters and maxing out their fortes. \n\n"
        "Well Built Tier [66<=Score<77]: \nCogratulations, you now have a well built character. Leveling talents to level 9 or 10, if not already done so, will be the "
        "optimal use of waveplates. \nOptimal time to switch focus on the next character. \n\n"
        "High Investment Tier [77<=Score<88]: \nSelf-explanatory: higher amounts of time and/or luck was required to achieve this build. \nRoI of time and/or waveplates"
        "for further echo improvements is very low unless there's a massive skew between individual echos. \n\n"
        "Extreme Tier [88<=Score<99]: \nYou are obsessed with this character. Or they're obsessed with you. \nIf we have leaderboards, you're likely in single digit% (even "
        "top 5%). \n\n"
        "God Tier [Score>=99]: \nStats entered incorrectly, or ER omitted, or some other cheat. \nThe alternative is that you've got yourself a build worthy of worship. You "
        "can start a religion out of this. \n\n"
        "Additional info: Max achievable points is not 100, but forget ever reaching 3 digits muhahaha (idk why I'm laughing I'm literally in the same boat). \n\n"
        "Press enter to continue: \n"
    )


def abt_evc_score() -> str:

    return(
        "---------- ---------- About the Echo Value Calculator (name subject to change) and the Scoring Method ---------- ----------\n\n"
        "The goal here is to put a value on your ECHOES. \nThe ratings reflect an echo/build's VALUE, to YOUR SITUATION. THIS is what makes this "
        "calculator so powerful. Here 'Value' does not merely mean damage output potential - the calculator DIRECTLY considers the benefit of a substat to your SPECIFIC "
        "character and situation. \nIt simply asks 'How valueable is this stat to this character in relation to other stats this character finds valuable, in a specific "
        "situation? '\nIt is for this reason why the ratings work JUST AS WELL for support characters as for DPS or sub-DPS characters, WITHOUT changing the logic behind "
        "its mechanisms. \n\n"
        "Character sequences, weapon level, character level, forte level etc. don't matter whatsoever! (unless they affect this character's ER requirements AND they are "
        "reflected on the stat page. \n\n"
        "Scoring Method: \nThe full theory of the calculator and the full logic of this program will be made available in a word document on the GitHub page (unless "
        "already availabe). The following example is PURPOSELY chosen to be very simple and uncomplicated. For the users who can follow, this gives a VERY BASIC IDEA "
        "behind this program (for a detailed explanation of the full nitty-gritty, please check the word document). \n\n"
        "Carlotta uses the following stats: Crit Rate%, Crit Damage%, Atk%, Flat Atk, Resonance Skill% and ER%. \nThese are the relative values of median substat rolls, "
        "respectively: 1, 1, 0.5, 0.25, 0.425. \nFor ER% there are 4 different parameters that the program uses (depending on a variety of factors - please refer to the "
        "word document): \nER% target - (WITHOUT team mates like Zhezhi or Yangyang) (intermediate value used to determine, store and update net surplus/deficit. VERY "
        "important REGARDLESS of whether the ER% target is low or high) (WILL cause FLUCTUATIONS in the third ER parameter based on updates), \nLiberation impact - (just how"
        " much a character relies on pressing the liberation button in a rotation, VERY important multiplier), \nER% relative median substat roll value - (obtained from "
        "processing and combining the previous two values), \nResonance Cost - (used to modify ER% targets in presence of Zhezhi or Yangyang). \n\n"
        "Assume you've rolled an Echo with the substats: Crit Rate 7.5%, Crit Damage 16.2%, Atk 7.9% and Atk 40. Here is how the Echo rating is determined in general: \n"
        "[Sum of ([substat value / substat median value] * character specific relative median substat roll value) for all substats] \n"
        "Divided by: [Sum of best 5 relative median substat roll values at the time of considering this Echo. The result is then multiplied by 100. \n"
        "For this Echo evaluated for Carlotta: [(7.5 / 8.4) * 1] + [(16.2 / 16.8) * 1] + [(7.9 / 9) * 0.5] + [(40 / 45) * 0.25] = 2.518... \n"
        "1 + 1 + 0.5 + 0.425 + 0.25 = 3.175. Dividing the previous number with this one, then multiplying by 100 results in: 79.315 - High Investment Tier. This matches "
        "exactly with the output of the calculator. \n\n"
        "Notice that Carlotta happens to have exactly 5 values (ignoring ER) that are good. For characters with more (or less) substats they can make use of, top 5 (or less)"
        " values are considered. In fact, even for Carlotta - in actuality - ER may play a big roll depending on your situation. \n\n"
        "Why consider ER? \nImagine a player got the exact Echo considered above, except the 5th stat is ER 10% instead of some other dead stat. Additionally this player "
        "is an S0R1 Carlotta and is not using Zhezhi or Yangyang as team mates. Is it really fair to give this Echo exactly the same rating as the one calculated above? \n"
        "'Well okay maybe the value will increase slightly' - by how much? why? Without going into specifics (that're in the document), I am confident that ER% is handled "
        "and valued exactly as much as it should. For example, the output of the calculator for the SECOND Echo, will change based on whether the total ER% (value on the "
        "stat-page) is more or less (AND EXACTLY how much more or less) than the target. A total ER% of 100, 120, 125, 130 and 140 will all give the appropiate results of: "
        "90.699, 90.699, 90.699, 88.196, 79.315. But WAIT! Can you guess what happens to the first Echo's value when this Carlotta has 100 total ER% (as in no ER% substats)"
        "? \nThe value of the Echo in this circumstance is now 64.159. Look again at the general formula for ratings! Not only is the first part, but ALSO the second part, "
        "being influenced by ER%. ER%'s relative median substat roll value FLUCTUATES to enter the top 5 best stats! Let's consider the first Echo's ratings for the "
        "five ER values that we considered above: 64.159, 73.018, 79.315, 79.315, 79.315. Try to look at both of these sets of results, see where they're the same and where "
        "they're different, and try to answer why this is the case. This will, in my opinion, make you realize how cool the calculator is! \n\n"
        "'Sure, it's great that this is such a thorough handling, but why go to such lengths? ' - Remember that the sets of values we've calculated above are JUST for two "
        "different Echos, and they're ONLY different with respect to the ER they have! 64.159 falls in the 'Decent' bracket and 90.699 falls in the 'Extreme' bracket. \n"
        "Do you really think a program where the potential values based on circumstances can vary this much, provide any value to anyone? \n\n"
        "I, hereby, assert that you MUST have ALL these considerations for ANY Program that seeks to evaluate Echoes and provide ANY value whatsoever (in terms of "
        "satisfaction, trust, reliability, informativeness, fun etc.) to the users. Without this thorough treatment, you would stop using, relying and enjoying this "
        "program simply for the fact that most characters in this game will have SOME ER requirements, so you'll NEVER be able to make decisions or measure build strenghts "
        "(or whatever else you wish to do) with ease and without doubts. You would stop using that program soon. I know I would. And so I've went through extra lengths to "
        "make sure that this calculator is very practical to use on the daily! I am, first and foremost, a user of this calculator just as much as the creator - and as a "
        "user I am confident that this program is fun, reliable, trustworthy, informative and correct. I enjoy this program very much, and I hope everyone else finds the "
        "same enjoyment with the EVC(nstc) as I do. \n---------- ---------- ---------- ---------- ----------\n\nPress enter to continue: \n"
    )


def toggle_mode(stat_medians_tm: GameData) -> GameData:

    if stat_medians_tm.data["Crit Rate (%)"] == 10.5: stat_medians_tm = GameData.get("Normal Stat Medians")
    else: stat_medians_tm = GameData.get("OverDrive Stat Medians")

    return stat_medians_tm


def get_net_er(character_pick_gne: Character, tot_er: float) -> None:

    if character_pick_gne.data["ER (%)"] != 0:
                
        try: character_pick_gne.net_er = tot_er + character_pick_gne.data["ER (%)"]
        except: raise ValueError("Total ER: invalid input")

    else: character_pick_gne.net_er = 0


def evc_engine(character_pick_ee: Character, echo_mainstats_ee: GameData, stat_medians_ee: GameData, rating_type_ee: int, cur_sub_vals_ee: GameData) -> float:

    achieved_value = GameData.get("Value")

    av_non_er(character_pick_ee, achieved_value, echo_mainstats_ee, stat_medians_ee, cur_sub_vals_ee)
    er_bank: float = av_er(character_pick_ee, echo_mainstats_ee, stat_medians_ee, achieved_value, cur_sub_vals_ee)

    pot_value: float = potential_value(rating_type_ee, er_bank, character_pick_ee.data)

    return ((sum(list(achieved_value.data.values()))) / pot_value) * 100


def av_non_er(character_pick_ane: Character, achieved_value_ane: GameData, echo_mainstats_ane: GameData, stat_medians_ae: GameData, cur_sub_vals: GameData) -> None:

    for substat_name in character_pick_ane.data:
        if character_pick_ane.data[substat_name] > 0:

            try:
                achieved_value_ane.data[substat_name] = (((cur_sub_vals.data[substat_name] - echo_mainstats_ane.data[substat_name]) / 
                                                            stat_medians_ae.data[substat_name]) * character_pick_ane.data[substat_name])
            except: raise ValueError(str(cur_sub_vals.data[substat_name]) + ": Invalid input. ")


def av_er(character_pick_ae: Character, echo_mainstats_ae: GameData, stat_medians_ae: GameData, achieved_value_ae: GameData, cur_sub_vals: GameData) -> float:

    if character_pick_ae.data["ER (%)"] < 0:

        while True:
            try:
                current_er = cur_sub_vals.data["ER (%)"] - echo_mainstats_ae.data["ER (%)"]
            except: print("Error: Input is not a number. Please try again. ")
            else: break
    
    else: current_er = 0

    return calc_er_bank(character_pick_ae, current_er, stat_medians_ae.data["ER (%)"], achieved_value_ae.data)


def calc_er_bank(character_pick_ceb: Character, current_er_ceb: float, energy_regen_med: float, achieved_value_dict: dict) -> float:

    if character_pick_ceb.net_er >= 0:
        character_pick_ceb.net_er = character_pick_ceb.net_er - current_er_ceb
        if character_pick_ceb.net_er < 0:
            er_bank_ceb = - character_pick_ceb.net_er / energy_regen_med
            achieved_value_dict["ER (%)"] = er_bank_ceb * ( - character_pick_ceb.data["_Liberation_Impact_"])
            character_pick_ceb.net_er = 0
        else: er_bank_ceb = 0
        
    else:
        er_bank_ceb = (current_er_ceb - character_pick_ceb.net_er) / energy_regen_med
        achieved_value_dict["ER (%)"] = (current_er_ceb / energy_regen_med) * ( - character_pick_ceb.data["_Liberation_Impact_"])

    return er_bank_ceb


def potential_value(rating_type_pv: int, er_bank_pv: float, character_pick_pv_data: dict) -> float:

    potential_value = 0
    echo_amount = 0
    while echo_amount < rating_type_pv:
        if er_bank_pv >= 1:
            character_pick_pv_data["_ER%_rel_val_"] = 1 * ( - character_pick_pv_data["_Liberation_Impact_"])
            er_bank_pv = er_bank_pv - 1
        else:
            character_pick_pv_data["_ER%_rel_val_"] = er_bank_pv * ( - character_pick_pv_data["_Liberation_Impact_"])
            er_bank_pv = 0
        potential_value = potential_value + sum(heapq.nlargest(5, list(character_pick_pv_data.values())))
        echo_amount = echo_amount + 1
    
    character_pick_pv_data["_ER%_rel_val_"] = 0

    return potential_value


def full_rating(character_pick_fr: Character, echo_mainstats_fr: GameData, stat_medians_fr: GameData, cur_sub_vals_r: GameData) -> None:

    input("INSTRUCTIONS: \n- Enter the substats on your first Echo, then your second, and so on. \n- If the Echo doesn't have a specific substat, just enter 0. \n\n"
          "Press enter to start: \n")
    total_echo_value = 0            
    for echo_number in range(5):
        print("\n---------- ---------- Echo " + str(echo_number + 1) + " ---------- ----------")
        current_echo_value = evc_engine(character_pick_fr, echo_mainstats_fr, stat_medians_fr, 1, cur_sub_vals_r)
        echo_analysis(current_echo_value, 0, 0, character_pick_fr.data["_Analysis?_"])
        total_echo_value = total_echo_value + current_echo_value                
    echo_analysis(total_echo_value/5, 1, 2, character_pick_fr.data["_Analysis?_"])


def build_rating(echo_mainstats_br: GameData, character_pick_br: Character, stat_medians_br: GameData, cur_sub_vals_r: GameData) -> None:

    input("INSTRUCTIONS: \n- Select the correct Echo Setup (43311 or 44111). Select correct mainstats by using the following Key: \n"
          "{Crit Rate: cr, Crit Damage: cd, Attack%: atk, HP%: hp, Defense%: def, Healing Bonus%: heal, Energy Regen%: er, ANYTHING else: other} \n"
          "- Then Enter the stats you see on the 'Echo Presets' (You can find this by going to a character's Echo page and selecting the first option "
          "at the bottom right of your screen). \n- Then simply enter the stats you see for this build directly. \nPress enter to start: \n")

    get_mainstat_values(echo_mainstats_br)
        
    build_value = evc_engine(character_pick_br, echo_mainstats_br, stat_medians_br, 5, cur_sub_vals_r)            
    echo_analysis(build_value, 1, 2, character_pick_br.data["_Analysis?_"])


def get_mainstat_values(echo_mainstats_gmv: GameData, cur_sub_vals_r: GameData) -> None:
    
    while True:
        try:
            echo_cost_setup = int(input("Select your Echo Cost Setup: \n    1. 43311\n    2. 44111\nEnter option number here: \n").strip())
            if echo_cost_setup != 1 and echo_cost_setup != 2:
                print("Please pick a correct option. \n")
                continue
        except: print("Invalid input - please enter the option number. \n")
        else: break
        
    if echo_cost_setup == 1: echo_costs = [0, 1, 1, 2, 2]
    else: echo_costs = [0, 0, 2, 2, 2]

    echo_number = 1
    for echo_cost in echo_costs:
        if echo_cost == 0:
            display_cost = "4"
            secondary_stat = "Flat Atk"
        elif echo_cost == 1:
            display_cost = "3"
            secondary_stat = "Flat Atk"
        else:
            display_cost = "1"
            secondary_stat = "Flat HP"
            
        while True:
            try:
                echo_mainstat = input("Enter Echo " + str(echo_number) + " (" + display_cost + " cost)'s Mainstat (please refer to the key above): ").strip().lower()
                match echo_mainstat:
                    case "cr": echo_mainstat = "Crit Rate (%)"
                    case "cd": echo_mainstat = "Crit Damage (%)"
                    case "atk": echo_mainstat = "Atk (%)"
                    case "hp": echo_mainstat = "HP (%)"
                    case "def": echo_mainstat = "Def (%)"
                    case "er": echo_mainstat = "ER (%)"
                    case "heal" | "other": break
                    case _:
                        print("Please enter a valid option!")
                        continue
                    
                echo_mainstats_gmv.data[echo_mainstat] = (echo_mainstats_gmv.data[echo_mainstat] + GameData.mainstats[echo_cost][echo_mainstat])
            except: print("Invalid Input. Please refer to the key above! \n")
            else: break
            
        echo_mainstats_gmv.data[echo_mainstat] = echo_mainstats_gmv.data[echo_mainstat] + GameData.mainstats[echo_cost][secondary_stat]
        echo_number += 1


def echo_rating(character_pick_er: Character, echo_mainstats_er: GameData, stat_medians_er: GameData) -> None:

    input("INSTRUCTIONS: \n- Enter the substats on your Echo. \n- If the Echo doesn't have a specific substat, just enter 0. \nPress enter to start: \n")
    echo_value = evc_engine(character_pick_er, echo_mainstats_er, stat_medians_er, 1)
    echo_analysis(echo_value, 0, 1, character_pick_er.data["_Analysis?_"])


def echo_analysis(rating: float, analysis_object_index: int, analysis_type_index: int, analysis_validity: int) -> None:
    
    if analysis_validity == 0: return
    
    match analysis_object_index:
        case 0: type_display = "Echo"
        case 1: type_display = "Build"
        case _: raise CorruptData("Analysis object is incorrectly defined")

    match analysis_type_index:
        case 0: analysis = "None"
        case 1: analysis = "Echo"
        case 2: analysis = "Build"
        case _: raise CorruptData("Analysis type is incorrectly defined")

    print("\n\nYour " + type_display + " rating is: " + str(round(rating, 3)))
    
    if rating >= 99: print("\nThis " + type_display + " falls in the 'Godly' tier.")
        
    elif rating >= 88: print("\nThis " + type_display + " falls in the 'Extreme' tier.")
        
    elif rating >= 77: print("\nThis " + type_display + " falls in the 'High Investment' tier.")
        
    elif rating >= 66: print("\nThis " + type_display + " falls in the 'Well Built' tier.")
        
    elif rating >= 55: print("\nThis " + type_display + " falls in the 'Decent' tier.")
        
    elif rating >= 44: print("\nThis " + type_display + " falls in the 'Base Level' tier.")
        
    else: print("\nThis " + type_display + " falls in the 'Unbuit' tier.")
        
    if analysis == "Echo":
        
        if rating >= 99: print("\nOne of the rarest echos. Impractically close to perfect, if not - quite literally perfect. Whitebeard was right afterall... "
                               "\nDelete it immedietly. \n.\n.\n.(Please don't do that it's a joke!) "
                               "\n---------- ---------- ---------- ---------- ----------")
            
        elif rating >= 88: print("\nPractically perfect piece. Congratulations! "
                                 "More than just time and effort are required, however, to reach the next category. "
                                 "\n---------- ---------- ---------- ---------- ----------")
            
        elif rating >= 77: print("\nHigh value piece. Usually only found on builds with lots of dedicated investment. "
                                 "\n---------- ---------- ---------- ---------- ----------")
            
        elif rating >= 66: print("\nVery solid piece. Recommended to find upgrades for other pieces before trying to find upgrades for this. "
                                 "\n---------- ---------- ---------- ---------- ----------")
            
        elif rating >= 55: print("\nFine piece. Recommended to find upgrades to other pieces if the goal is to make this character 'ToA-ready'. "
                                 "\n---------- ---------- ---------- ---------- ----------")
            
        elif rating >= 44: print("\nPassable piece. Good enough until your character is at lvl 80/80, weapon at level 90/90, and relevant talents are at level 8. "
                                 "\n---------- ---------- ---------- ---------- ----------")
            
        else: print("\nDiscardable piece. C'mon man have some ambition. "
                    "\n---------- ---------- ---------- ---------- ----------")
            
    elif analysis == "Build":
        
        if rating >= 99: print("\nYou have entered stats incorrectly. \nThe alternative is that you've actually found a build so perfect - posting this on reddit will lead to the "
                               "birth of a new religion. "
                               "\n---------- ---------- ---------- ---------- ----------")
            
        elif rating >= 88: print("\nYou've shown extreme levels of dedication for this character build. \nIt'll most likely place you very high even on global leaderboards, if we "
                                 "had them. "
                                 "\n---------- ---------- ---------- ---------- ----------")
            
        elif rating >= 77: print("\nYou've given this build special treatment, or it has given special treatment to you. \nYou'll find clearing ToA easy even WITH skill issues. "
                                 "\n---------- ---------- ---------- ---------- ----------")
            
        elif rating >= 66: print("\nYour build is looking great! Now is a good time to move on to the next character. \nIf you're having difficulty to get 30/30 in ToA, this "
                                 "character build is certainly not an issue whatsoever. "
                                 "\n---------- ---------- ---------- ---------- ----------")
            
        elif rating >= 55: print("\nYour character is 'ToA ready'. \nGiven that the rest of the teammates are at or above this level, getting 30/30 should be achievable with enough "
                                 "skill and attempts. \nHighly recommended to get your character talens, levels, weapons and any other guaranteed upgrades at max level (if not, as "
                                 "high as possible) before continuing to improve your echos. "
                                 "\n---------- ---------- ---------- ---------- ----------")
            
        elif rating >= 44: print("\nA passable build that will work great until you bring your character to level 80/80, talents to level 8, and weapon to level 90."
                                 "\n---------- ---------- ---------- ---------- ----------")
            
        else: print("\nUnacceptable build. Highly recommended to find better pieces immedietly if you want to build this character. "
                    "\n---------- ---------- ---------- ---------- ----------")


if __name__ == "__main__":
    main()

