# 1. Fixed option 2
# 2. Fixed Danjin
# 3. Added Brant


import heapq
import sys


def main():

    print("\n========== ========== ========== ========== ==========\n\nWelcome to the Echo Value Calculator (name subject to change) v2.03.060325\n\n")
    
    while True:
        
        character_name = input("Please enter your character, or enter q to quit: \n").lower().strip()
        if character_name == "q":
            quit_calculator()
            continue
        stat_names, stat_medians, real_character_name, character_data = game_data(character_name)        
        if real_character_name[0] == "No selection": continue
        print("\n---------- ---------- ---------- ---------- ----------\nYou have selected " + real_character_name[0] + ".\n---------- ---------- ---------- ---------- ----------\n\n")
        
        if character_data[12] != 0:
            consider_er = input("Press enter key to continue normally [RECOMMENDED]. \nEnter y to IGNORE character ER requirements [NOT recommended]. \n: ").lower().strip()
            if consider_er == "y":
                character_data[12] = 0
                print(real_character_name[0] + "'s ER requirements removed. \n")
            else:
                outro_er_gain = input("Enter 'y' if you're using Zhezhi or Yangyang as team mates for " + real_character_name[0] + ". Else press enter to continue. \n: ").lower().strip()
                if outro_er_gain == "y":
                    character_data[12] = (1 + (20 / character_data[15])) * character_data[12]
                    if character_data[12] > - 100: character_data[12] = 0
                    print(real_character_name[0] + "'s ER requirements adjusted. \n")
                    
        while True:
            
            if stat_medians[0] == 10.5: calculator_mode = "!!!OVERDRIVE MODE!!!"
            else: calculator_mode = "Normal Mode [Recommended]"
            
            option_selected = input("Echo Value Calculator - " + calculator_mode + "\nPlease select from one of the following options: \n"
                                    "[Note: All options are EASY to use. Instructions will be provided as necessary. ]\n\n"
                                    "    01) COMPLETE evaluation: \n"
                                    "        Rate and analyze every Echo AND the overall Echo Set. \n\n"
                                    "    02) ECHO SET evaluation: \n"
                                    "        Rate and analyze the full Echo Set directly. \n\n"
                                    "    03) ECHO evaluation. \n"
                                    "        Rate and analyze a particular Echo. \n\n"
                                    "    04) About this program and scoring method. \n"
                                    "    05) Tiers explained. \n"
                                    "    06) General assumptions, Guide for fast character building. \n\n"
                                    "    07) Display game and character data. \n"
                                    "    08) Pick a different character. \n\n"
                                    "    09) Toggle Overdrive Mode. \n\n"
                                    "    10) Quit the program. \n\n"
                                    "Enter the option number below: \n").lower().strip()

            if option_selected == "10":
                quit_calculator()
                break
            
            elif option_selected == "8" or option_selected == "08": break
            
            elif option_selected == "6" or option_selected == "06":
                assumption_test = input("\n---------- ---------- List of general assumptions about your character ---------- ----------\n\n"
                                        "1. Sensible echo set: Self-explanatory. Usually a character only really has one best-in-slot set, so use that. \n\n"
                                        "2. Sensible echo main stats: The program can't help you if you're running defense% and HP% 3 cost and 1 cost echoes on your Jiyan. \n\n"
                                        "3. Sensible weapon: Again, the program can't help you if you're running Dauntless Evernight on Jinhsi. Look up guides. \n\n"
                                        "4. Sensible crit ratio: 1.5 < (Crit Damage - 100) / Crit Rate <= 2.2. [Enter 4 to test your crit ratio]. \n"
                                        "NOTE: It's completely okay if you don't fall in this sweet-spot, as long as there is a full attempt without sacrificing feasability. \n"
                                        "If your character has a crit damage weapon and you're running a crit rate 4 cost and trying to get at least crit rate on all pieces, that's "
                                        "enough. \n\n---------- ---------- Sequence flowchart to make your character ready ASAP ---------- ----------\n\n"
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
                                        "Select available options or enter anything else to continue: \n").strip()
                if assumption_test == "4":
                    
                    while True:
                        try:
                            character_cr = float(input("Enter " + character_name + "'s Crit Rate% (Give the exact amount even if it exceeds 100%): ").strip())
                            character_cd = float(input("Enter " + character_name + "'s Crit Damage%: ").strip())
                        except: print("Invalid input. \nPlease try again. ")
                        else: break

                    character_crit_ratio = (character_cd - 100) / character_cr
                    input(character_name + "'s Crit Ratio is: " + str(round(character_crit_ratio, 3)) + " \nPress Enter to continue. \n")
                continue
            
            elif option_selected == "5" or option_selected == "05":
                input("\n---------- ---------- Echo/Build Value brackets ---------- ----------\n\n"
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
                      "Press enter to continue: \n")
                continue
            
            elif option_selected == "4" or option_selected == "04":
                input("\n---------- ---------- About the Echo Value Calculator (name subject to change) and the Scoring Method ---------- ----------\n\n"
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
                      "same enjoyment with the EVC(nstc) as I do. \n---------- ---------- ---------- ---------- ----------\n\nPress enter to continue: \n")
                continue
            
            elif option_selected == "9" or option_selected == "09":
                if stat_medians[0] == 8.4:
                    print("!!!WARNING!!!: On this scale - 100 points are awarded to the absolute theoretical maximum a character can ever achieve. Max rolls, Best Relevant stats. "
                          "All builds will score low on this scale. \nAdditionally, your build will NOT receive any feedback or evaluation. ")
                    confirm_mode_change = input("It is highly NOT recommended to use this scale other than for amusement purposes. "
                                    "Continue anyway? (enter 'y' to continue, anything else to go back) : \n").lower().strip()
                    if confirm_mode_change != "y": continue
                    stat_medians = [10.5, 21, 11.6, 60, 11.6, 580, 14.7, 70, 11.6, 11.6, 11.6, 11.6, 12.4]
                    character_data[16] = 0
                else:
                    stat_medians, character_data[16] = game_data(character_name)[1], game_data(character_name)[3][16]
                continue

            elif option_selected == "7" or option_selected == "07":
                display_character_data(stat_names, stat_medians, real_character_name, character_data)
                continue

            elif option_selected != "1" and option_selected != "2" and option_selected != "3" and option_selected != "01" and option_selected != "02" and option_selected != "03":
                input("\n\nYou have picked an incorrect option. \nPress enter to try again. \n")
                continue
            
            if character_data[12] != 0:
                
                while True:
                    try:
                        net_er = (float(input("\n---------- ---------- ---------- ---------- ----------"
                                             "\n\nEnter " + character_name + "'s Energy Regen% from the stat page (please do NOT modify this because other sources of ER have been "
                                              "concidered). \n!!!Make sure you've equipped the build you're evaluating and they're on the correct weapons!!!\nEnergy Regen%: \n").strip())
                                  + character_data[12])
                    except:
                        print("Error: Input is not a number. Please try again. ")
                    else: break
                    
            else:
                net_er = 0

            main_stats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            if option_selected == "1" or option_selected == "01":
                input("INSTRUCTIONS: \n- Enter the substats on your first Echo, then your second, and so on. \n- If the Echo doesn't have a specific substat, just enter 0. \n\n"
                      "Press enter to start: \n")
                total_echo_value = 0            
                for echo_number in range(5):
                    print("\n---------- ---------- Echo " + str(echo_number + 1) + " ---------- ----------")
                    current_echo_value, net_er = player_data(stat_names, stat_medians, character_name, character_data, net_er, 1, main_stats)
                    echo_analysis(current_echo_value, 0, 0, character_data[16])
                    total_echo_value = total_echo_value + current_echo_value                
                echo_analysis(total_echo_value/5, 1, 2, character_data[16])
                
            elif option_selected == "2" or option_selected == "02":
                input("INSTRUCTIONS: \n- Select the correct Echo Setup (43311 or 44111). Select correct mainstats by using the following Key: \n"
                      "{Crit Rate: cr, Crit Damage: cd, Attack%: atk, HP%: hp, Defense%: def, Healing Bonus%: heal, Energy Regen%: er, ANYTHING else: other} \n"
                      "- Then Enter the stats you see on the 'Echo Presets' (You can find this by going to a character's Echo page and selecting the first option "
                      "at the bottom right of your screen). \n- Then simply enter the stats you see for this build directly. \nPress enter to start: \n")

                echo_mainstats = [{"cr": [0, 22], "cd": [1, 44], "atk": [2, 33], "fatk": [3, 150], "hp": [4, 33], "def": [6, 41.5], "heal": [0, 0]},
                                  {"atk": [2, 30], "fatk": [3, 100], "hp": [4, 30], "def": [6, 38], "er": [12, 32], "other": [0, 0]},
                                  {"atk": [2, 18], "hp": [4, 22.8], "fhp": [5, 2280], "def": [6, 18]}]

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
                        secondary_stat = "fatk"
                    elif echo_cost == 1:
                        display_cost = "3"
                        secondary_stat = "fatk"
                    else:
                        display_cost = "1"
                        secondary_stat = "fhp"
                        
                    while True:
                        try:
                            echo_mainstat = input("Enter Echo " + str(echo_number) + " (" + display_cost + " cost)'s Mainstat (please refer to the key above): ").strip().lower()
                            if (echo_mainstat != "cr" and echo_mainstat != "cd" and echo_mainstat != "atk" and echo_mainstat != "hp" and echo_mainstat != "def" and echo_mainstat != "heal"
                                and echo_mainstat != "er" and echo_mainstat != "other"):
                                print("Please enter a valid option!")
                                continue
                            main_stats[echo_mainstats[echo_cost][echo_mainstat][0]] = main_stats[echo_mainstats[echo_cost][echo_mainstat][0]] + echo_mainstats[echo_cost][echo_mainstat][1]
                        except: print("Invalid Input. Please refer to the key above! \n")
                        else: break
                        
                    main_stats[echo_mainstats[echo_cost][secondary_stat][0]] = main_stats[echo_mainstats[echo_cost][secondary_stat][0]] + echo_mainstats[echo_cost][secondary_stat][1]
                    echo_number += 1
                    
                build_value, net_er = player_data(stat_names, stat_medians, character_name, character_data, net_er, 5, main_stats)            
                echo_analysis(build_value, 1, 2, character_data[16])
                
            elif option_selected == "3" or option_selected == "03":
                input("INSTRUCTIONS: \n- Enter the substats on your Echo. \n- If the Echo doesn't have a specific substat, just enter 0. \nPress enter to start: \n")
                echo_value, net_er = player_data(stat_names, stat_medians, character_name, character_data, net_er, 1, main_stats)
                echo_analysis(echo_value, 0, 1, character_data[16])
                
            input("Press enter to continue: \n")


def quit_calculator():
    confirm_exit = input("Are you sure you want to quit? (Enter y to confirm): \n").lower().strip()
    if confirm_exit == "y":
        input("Thank you for using Echo Value Calculator (name subject to change). \nPress enter to exit (intentional): ")
        sys.exit()


def game_data(character_name_gd):
    
    stat_names_gd = (["Crit Rate%", "Crit Damage%", "Attack%", "Flat Attack", "HP%", "Flat HP", "Defense%", "Flat Defense", "Basic Attack Damage Bonus%", "Heavy Attack Damage Bonus%",
                  "Resonance Skill Damage Bonus%", "Resonance Liberation Damage Bonus%", "Energy Regen%", "Liberation Impact", "_ER%_", "Resonance Energy", "_Analysis?_"])
    stat_medians_gd = [8.4, 16.8, 9, 45, 9, 450, 11.4, 55, 9, 9, 9, 9, 9.6]
    real_character_name_gd = ["No selection"]
    character_data_gd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    if (character_name_gd == "carlotta" or character_name_gd == "glass girl" or character_name_gd == "small car lotta damage. wait... what?"
        or character_name_gd == "in the name of the montellis." or character_name_gd == "rin tohsaka" or character_name_gd == "best girl"):
        real_character_name_gd = ["Carlotta"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0, 0.5 * 0.85, 0, - 125, - 1, 0, - 125, - 1]
        
    elif character_name_gd == "jinhsi" or character_name_gd == "madam magistrate" or character_name_gd == "sacred light!" or character_name_gd == "snow girl":
        real_character_name_gd = ["Jinhsi"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0, 0.5 * 0.75, 0.5 * 0.2, - 115, - 0.2 / 0.95, 0, - 150, - 1]
        
    elif (character_name_gd == "encore"  or character_name_gd == "leave... me... alone!" or character_name_gd == "annie" or character_name_gd == "klee" or character_name_gd == "maygi"
          or character_name_gd == "pink gremlin"):
        real_character_name_gd = ["Encore (Hypercarry)"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.5, 0, 0.5 * 0.2, 0.5 * 0.1, - 125, - 1, 0, - 125, - 1]
        
    elif (character_name_gd == "yinlin" or character_name_gd == "hmph... now you'll behave." or character_name_gd == "bdsm" or character_name_gd == "dominatrix"
          or character_name_gd == "puppet girl"):
        real_character_name_gd = ["Yinlin"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.1, 0.5 * 0.1, 0.5 * 0.55, 0.5 * 0.2, - 135, - 0.2 / 0.95, 0, - 125, - 1]
        
    elif (character_name_gd == "sanhua" or character_name_gd == "jinhsi's bodyguard" or character_name_gd == "goth girl #3" or character_name_gd == "goth girl 3"
          or character_name_gd == "shackles begone!"):
        real_character_name_gd = ["Sanhua"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0.5 * 0.3, 0.5 * 0.3, 0.5 * 0.3, 0, 0, 0, - 100, - 1]
        
    elif character_name_gd == "zhezhi" or character_name_gd == "shy girl" or character_name_gd == "painter girl" or character_name_gd == "art unveiled":
        real_character_name_gd = ["Zhezhi"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.8, 0.5 * 0.05, 0.5 * 0.05, 0, - 135, - 1, 0, - 125, - 1]
        
    elif character_name_gd == "aalto" or character_name_gd == "cool shades" or character_name_gd == "thanks for watching!":
        real_character_name_gd = ["Aalto"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.50, 0, 0.5 * 0.25, 0.5 * 0.15, - 135, - 0.65 / 0.9, 0, - 150, - 1]
        
    elif (character_name_gd == "baizhi" or character_name_gd == "goth girl #2" or character_name_gd == "goth girl 2" or character_name_gd == "verina at home"
          or character_name_gd == "better than verina" or character_name_gd == "endless reverberation."):
        real_character_name_gd = ["Baizhi"]
        character_data_gd = [0, 0, 0, 0, 1, 0.5, 0, 0, 0, 0, 0, 0, - 215, - 1, 0, - 175, 0]
        
    elif character_name_gd == "brant" or character_name_gd == "pirate":
        real_character_name_gd = ["Brant - Sub DPS, ER/ER 3 cost setup"]
        character_data_gd = [1, 1, 0.3, 0.2, 0, 0, 0, 0, 0.55, 0, 0, 0.0375, - 285, - 0.6, 0, - 175, - 1]

    elif (character_name_gd == "cucumber" or character_name_gd == "calculator" or character_name_gd == "vergil" or character_name_gd == "kurapika" or character_name_gd == "kukaracha"
          or character_name_gd == "calcium" or character_name_gd == "carpaccio" or character_name_gd == "cactus" or character_name_gd == "calculus" or character_name_gd == "calzone"
          or character_name_gd == "misery follows!"):
        real_character_name_gd = ["Calcharo"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.25, 0, 0, 0.5 * 0.55, - 125, - 1, 0, - 125, - 1]
        
    elif (character_name_gd == "camellya" or character_name_gd == "zyra" or character_name_gd == "yuno gasai" or character_name_gd == "yandere girl"
          or character_name_gd == "she wants my seed?" or character_name_gd == "i can fix her" or character_name_gd == "spin to win" or character_name_gd == "gymnasts girl"
          or character_name_gd == "i will do gymnastics with her but ancient greek style" or character_name_gd == "struggle harder, entertain me!"):
        real_character_name_gd = ["Camellya"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.7, 0, 0, 0.5 * 0.15, - 120, - 0.15 / 0.85, 0, - 125, - 1]
        
    elif (character_name_gd == "changli" or character_name_gd == "fox girl" or character_name_gd == "ahri" or character_name_gd == "nine-tailed fox" or character_name_gd == "yae miko"
          or character_name_gd == "feathers incinerate."):
        real_character_name_gd = ["Changli"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.05, 0, 0.5 * 0.6, 0.5 * 0.25, - 125, - 0.25/0.9, 0, - 125, - 1]
        
    elif (character_name_gd == "chixia" or character_name_gd == "amber" or character_name_gd == "finger pistol" or character_name_gd == "ma xiaofang"
          or character_name_gd == "boom! headshot!" or character_name_gd == "pew pew pew!" or character_name_gd == "one shot, one kill!"
          or character_name_gd == "easy peasy. lemon squeezy!" or character_name_gd == "dakka dakka dakka dakka dakka!"):
        real_character_name_gd = ["Chixia"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0, 0.5 * 0.5, 0.5 * 0.3, - 150, - 0.3 / 0.8, 0, -150, -1]
        
    elif character_name_gd == "danjin" or character_name_gd == "darkness falls...":
        real_character_name_gd = ["Danjin"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.05, 0.5 * 0.25, 0.5 * 0.25, 0.5 * 0.3, 0, 0, 0, - 100, - 1]
        
    elif character_name_gd == "jianxin" or character_name_gd == "sage girl" or character_name_gd == "small-town girl" or character_name_gd == "universe in my psyche!":
        real_character_name_gd = ["Jianxin (DPS)"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.25, 0.5 * 0.4, 0, 0.5 * 0.3, - 130, - 0.3 / 0.95, 0, - 150, - 1]
        
    elif character_name_gd == "jiyan" or character_name_gd == "dragon boy" or character_name_gd == "teal general" or character_name_gd == "windrider!":
        real_character_name_gd = ["Jiyan"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0.5 * 0.7, 0.5 * 0.15, 0, - 130, - 1, 0, - 125, - 1]
        
    elif character_name_gd == "lingyang" or character_name_gd == "who..." or character_name_gd == "cares." or character_name_gd == "gaming" or character_name_gd == "this might hurt.":
        real_character_name_gd = ["Lingyang"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.35, 0, 0.5 * 0.3, 0.5 * 0.05, - 125, - 1, 0, - 125, - 1]
        
    elif character_name_gd == "lumi" or character_name_gd == "delivery girl" or character_name_gd == "bunny girl" or character_name_gd == "squeakie, protect the cargo!":
        real_character_name_gd = ["Lumi"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.35, 0, 0.5 * 0.25, 0.5 * 0.3, - 165, - 1, 0, - 125, - 1]
        
    elif (character_name_gd == "mortefi" or character_name_gd == "xingqiu" or character_name_gd == "four-eyes" or character_name_gd == "roy mustang"
          or character_name_gd == "fuel my wrath!"):
        real_character_name_gd = ["Mortefi"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.1, 0, 0.5 * 0.15, 0.5 * 0.7, - 125, - 1, 0, - 125, - 1]
        
    elif character_name_gd == "phoebe" or character_name_gd == "sister" or character_name_gd == "church girl" or character_name_gd == "lux":
        real_character_name_gd = ["Phoebe"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.15, 0.5 * 0.45, 0, 0.5 * 0.15, 0, - 0.15 / 0.75, 0, - 125, -1]
        
    elif character_name_gd == "roccia" or character_name_gd == "mamma mia!" or character_name_gd == "pero":
        real_character_name_gd = ["Roccia"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.05, 0.5 * 0.6, 0.5 * 0.15, 0, - 135, - 1, 0, - 125, - 1]
        
    elif (character_name_gd == "rover" or character_name_gd == "goth girl #1" or character_name_gd == "goth girl 1" or character_name_gd == "goth guy" or character_name_gd == "rizzler"
          or character_name_gd == "mc"):
        
        while True:
            try:
                mc_element = int(input("\nEnter 1 for Spectro Rover, Enter 2 for Havoc Rover: \n").strip())
                if mc_element < 1 or mc_element > 2:
                    print("Please select a valid option. ")
                    continue
                else: break
            except:
                print("Please enter a valid input. ")
                
        if mc_element == 1:
            real_character_name_gd = ["Spectro Rover"]
            character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.05, 0.5 * 0.1, 0.5 * 0.3, 0.5 * 0.35, 0, - 0.35 / 0.8, 0, - 125, -1]
        else:
            real_character_name_gd = ["Havoc Rover"]
            character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.3, 0, 0.5 * 0.2, 0.5 * 0.25, - 125, - 0.25 / 0.75, 0, - 125, - 1]
            
    elif character_name_gd == "taoqi" or character_name_gd == "personalities" or character_name_gd == "two reasons" or character_name_gd == "attack is the best defense.":
        real_character_name_gd = ["Taoqi (quick concerto focus)"]
        character_data_gd = [0, 0, 0, 0, 0, 0, 1, 0.5, 0, 0, 0, 0, - 170, - 1, 0, - 125, 0]
        
    elif (character_name_gd == "the shorekeeper" or character_name_gd == "shorekeeper" or character_name_gd == "best waifu" or character_name_gd == "must protect"
          or character_name_gd == "vow from the soul." or character_name_gd == "in war with time." or character_name_gd == "i engraft you new."
          or character_name_gd == "astral modulation." or character_name_gd == "ordained."):
        real_character_name_gd = ["The Shorekeeper"]
        character_data_gd = [0, 1, 0, 0, 0.5, 0.25, 0, 0, 0.5 * 0.1, 0, 0, 0.5 * 0.85, - 240, - 1, 0, - 175, 0]
        
    elif character_name_gd == "verina" or character_name_gd == "flower girl" or character_name_gd == "life is in everything.":
        real_character_name_gd = ["Verina"]
        character_data_gd = [0, 0, 1, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, - 200, - 1, 0, - 175, 0]
        
    elif character_name_gd == "xiangli yao" or character_name_gd == "xiangling" or character_name_gd == "reconfiguration!":
        real_character_name_gd = ["Xiangli yao"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.1, 0, 0.5 * 0.2, 0.5 * 0.55, - 120, - 0.55 / 0.85, 0, - 125, - 1]
        
    elif character_name_gd == "yangyang" or character_name_gd == "coolest animations" or character_name_gd == "tempest." or character_name_gd == "i think she likes us":
        real_character_name_gd = ["Yangyang"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.3, 0, 0.5 * 0.15, 0.5 * 0.45, 0, 0, 0, - 100, - 1]
        
    elif character_name_gd == "youhu" or character_name_gd == "you who" or character_name_gd == "noice!":
        real_character_name_gd = ["Youhu"]
        character_data_gd = [0, 0, 1, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, - 165, - 1, 0, - 100, 0]
        
    elif character_name_gd == "yuanwu" or character_name_gd == "you and who" or character_name_gd == "maximum voltage.":
        real_character_name_gd = ["Yuanwu"]
        character_data_gd = [1, 1, 0, 0, 0, 0, 0.5, 0.25, 0, 0, 0.5 * 0.5, 0.5 * 0.4, - 140, - 1, 0, - 125, - 1]
        
    elif character_name_gd == "zani" or character_name_gd == "that button is the real body guard":
        input("Zani stats currently unavailable. Please come back later. \nPress enter to continue: \n")
        
    else:
        print ("Character not found or character name not recognized. \nPress enter to continue: \n")
        
    return stat_names_gd, stat_medians_gd, real_character_name_gd, character_data_gd


def display_character_data(stat_names_dp, stat_medians_dp, real_character_name_dp, character_data_dp):
    
    print("\nNOTE: The character data used in this program has been highly researched by analyzing multiple sources inlcuding but not limited to: prydwen.gg, Maygi, many YouTube guides "
          "and many websites. \nFor the 'damage profile' stats (basic attacks, heavy attacks, resonance skill, resonance liberation), their relative value should be exactly half of "
          "thier damage profile's ratio. Even a 5 to 10% disagreement with the damage profile will have very little impact on the overall score. \n"
          "However, feel free to report any inconsistency you feel are significant as a comment in the publishing post to improve this program. \n")
    for _ in range (len(stat_names_dp) - 5):
        if character_data_dp[_] > 0:
            print("The reletive value of a median roll (" + str(stat_medians_dp[_]) + ") of " + stat_names_dp[_] + " for " + real_character_name_dp[0] + " is: "
                  + str(round(character_data_dp[_] * 100, 3)) + "%. ")
    if character_data_dp[12] < 0:
        print("The " + stat_names_dp[12] + " requirements for " + real_character_name_dp[0] + " are: " + str( - character_data_dp[12]) + "% with a relative substat value multiplier of: "
              + str(round( - character_data_dp[13] * 100, 3)) + " (Resonance Cost: " + str( - character_data_dp[15]) + "). \n")
        print("The reletive value of a median roll (" + str(stat_medians_dp[12]) + ") of " + stat_names_dp[12] + " is fluctuating based on complex factors, and may not be constant even "
              "during the evaluation of a single build (option 1). \nRest assured: ER is handled very carefully and apporpiately to accurately reflect its true value in the scoring "
              "system. \nCheck out option 4 to get a glimpse of this fact with the aid of examples. For full details on the theory and logic, check out the word document in GitHub. \n")
    input("Press enter to continue: \n")


def player_data(stat_names_pi, stat_medians_pi, character_name_pi, character_data_pi, net_er_pi, rating_type, main_stats_pi):
    
    achieved_value = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    current_er = 0
    
    for _ in range (len(stat_names_pi) - 5):
        if character_data_pi[_] > 0:
            
            while True:
                try:
                    achieved_value[_] = ((float(input(stat_names_pi[_] + ": ").strip()) - main_stats_pi[_]) / stat_medians_pi[_]) * character_data_pi[_]
                except: print("Error: Input is not a number. Please try again. ")
                else: break
                
    if character_data_pi[12] < 0:

        while True:
            try:
                current_er = float(input(stat_names_pi[12] + ": ").strip()) - main_stats_pi[12]
            except: print("Error: Input is not a number. Please try again. ")
            else: break
            
    if net_er_pi >= 0:
        net_er_pi = net_er_pi - current_er
        if net_er_pi < 0:
            er_bank = - net_er_pi / stat_medians_pi[12]
            achieved_value[12] = er_bank * ( - character_data_pi[13])
            net_er_pi = 0
        else: er_bank = 0
        
    else:
        er_bank = (current_er - net_er_pi) / stat_medians_pi[12]
        achieved_value[12] = (current_er / stat_medians_pi[12]) * ( - character_data_pi[13])
        
    echo_potential = 0
    echo_amount = 0
    while echo_amount < rating_type:
        if er_bank >= 1:
            character_data_pi[14] = 1 * ( - character_data_pi[13])
            er_bank = er_bank - 1
        else:
            character_data_pi[14] = er_bank * ( - character_data_pi[13])
            er_bank = 0
        echo_potential = echo_potential + sum(heapq.nlargest(5, character_data_pi))
        echo_amount = echo_amount + 1
        
    achieved_value_sum = sum(achieved_value)
    rating = (achieved_value_sum / echo_potential) * 100
    return rating, net_er_pi


def echo_analysis(rating, analysis_object_index, analysis_type_index, analysis_validity):
    
    type_display = ["Echo", "Build"]
    print("\n\nYour " + type_display[analysis_object_index] + " rating is: " + str(round(rating, 3)))
    
    if analysis_validity == 0: return
    
    if rating >= 99: print("\nThis " + type_display[analysis_object_index] + " falls in the 'Godly' tier.")
        
    elif rating >= 88: print("\nThis " + type_display[analysis_object_index] + " falls in the 'Extreme' tier.")
        
    elif rating >= 77: print("\nThis " + type_display[analysis_object_index] + " falls in the 'High Investment' tier.")
        
    elif rating >= 66: print("\nThis " + type_display[analysis_object_index] + " falls in the 'Well Built' tier.")
        
    elif rating >= 55: print("\nThis " + type_display[analysis_object_index] + " falls in the 'Decent' tier.")
        
    elif rating >= 44: print("\nThis " + type_display[analysis_object_index] + " falls in the 'Base Level' tier.")
        
    else: print("\nThis " + type_display[analysis_object_index] + " falls in the 'Unbuit' tier.")
        
    if analysis_type_index == 1:
        
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
            
    elif analysis_type_index == 2:
        
        if rating >= 99: print("\nYou have entered stats incorrectly. \nThe alternative is that you've actually found a build so perfect - posting this on reddit will lead to the birth "
                               "of a new religion. "
                               "\n---------- ---------- ---------- ---------- ----------")
            
        elif rating >= 88: print("\nYou've shown extreme levels of dedication for this character build. \nIt'll most likely place you very high even on global leaderboards, if we had "
                                 "them. "
                                 "\n---------- ---------- ---------- ---------- ----------")
            
        elif rating >= 77: print("\nYou've given this build special treatment, or it has given special treatment to you. \nYou'll find clearing ToA easy even WITH skill issues. "
                                 "\n---------- ---------- ---------- ---------- ----------")
            
        elif rating >= 66: print("\nYour build is looking great! Now is a good time to move on to the next character. \nIf you're having difficulty to get 30/30 in ToA, this character "
                                 "build is certainly not an issue whatsoever. "
                                 "\n---------- ---------- ---------- ---------- ----------")
            
        elif rating >= 55: print("\nYour character is 'ToA ready'. \nGiven that the rest of the teammates are at or above this level, getting 30/30 should be achievable with enough "
                                 "skill and attempts. \nHighly recommended to get your character talens, levels, weapons and any other guaranteed upgrades at max level (if not, as high "
                                 "as possible) before continuing to improve your echos. "
                                 "\n---------- ---------- ---------- ---------- ----------")
            
        elif rating >= 44: print("\nA passable build that will work great until you bring your character to level 80/80, talents to level 8, and weapon to level 90."
                                 "\n---------- ---------- ---------- ---------- ----------")
            
        else: print("\nUnacceptable build. Highly recommended to find better pieces immedietly if you want to build this character. "
                    "\n---------- ---------- ---------- ---------- ----------")


main()

