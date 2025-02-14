#A LOT of QoLs
#No need to repeat selecting character or changing their teammates unless user wishes
#Now only provides ratings for supports and correctly skips evaluations intended for dps characters.
#Better about page, scoring method example, and improvements to display formatting
#Now waits for input from users at points where users may get lost
#Added assumptions checklist and sequential character building steps
#Overdrive mode is now a toggle


import heapq
import sys


def welcome():
    print("\n========== ========== ========== ========== ==========\n\n"
          "Welcome to the Echo Value Calculator (name subject to change) v2.02.000000\n\n")
    main()


def main():
    
    while True:
        
        character_name = input("Please enter your character, or enter q to quit: \n").lower().strip()
        if character_name == "q":
            calculator_quit()
            continue
        stat_names, stat_medians, character_name_main, character_data = game_data(character_name)        
        if character_name_main[0] == "No selection": continue
        print("\n---------- ---------- ---------- ---------- ----------\nYou have selected " + character_name_main[0] + ".\n---------- ---------- ---------- ---------- ----------\n\n")
        
        if character_data[12] != 0:
            er_consider = input("Press enter key to continue normally [RECOMMENDED]. \nEnter y to IGNORE character ER requirements [NOT recommended]. \n: ").lower()
            if er_consider == "y": character_data[12] = 0
            else:
                er_gained_outro = input("Enter 'y' if you're using Zhezhi or Yangyang as team mates for " + character_name_main[0] + ". Else press enter to continue. \n: ").lower()
                if er_gained_outro == "y":
                    character_data[12] = (1 + (20 / character_data[15])) * character_data[12]
                    if character_data[12] > - 100: character_data[12] = 0
                    
        character_change = 0
        while character_change != 1:
            
            if stat_med[0] == 10.5: calc_mode = "!!!OVERDRIVE MODE!!!"
            else: calc_mode = "Normal Mode"
            calc_type = input("\nEcho Value Calculator - " + calc_mode + "\nPlease select from one of the following options: "
                                  "\n    01) Full evaluation (enter data iteratively per echo) [Recommended]. "
                                  "\n    02) Build evaluation (enter COMBINED stats from all echos (ONLY)). "
                                  "\n    03) Echo evaluation [Recommended]. \n"
                                  "\n    04) About this program and the scoring method. "
                                  "\n    05) Bracket/Build tier explanation. "
                                  "\n    06) General assumptions and Sequence for fast character building. "
                                  "\n    07) Display game and character data. \n"
                                  "\n    08) Pick a different character. \n"
                                  "\n    09) Quit the program. \n"
                                  "\n    10) Toggle Overdrive Mode. \n"
                                  "\nEnter the option number below: \n").lower().strip()
            if calc_type == "9" or calc_type == "09":# Phase 1 handling - actions not requiring character stats
                quit_calc()
                char_change = 1
                continue
            elif calc_type == "8" or calc_type == "08":
                char_change = 1
                continue
            elif calc_type == "6" or calc_type == "06":
                ass_test = input("\n---------- ---------- List of general assumptions about your character ---------- ----------\n\n"
                                 "1. Sensible echo set: Self-explanatory. Usually a character only really has one best-in-slot set, so use that. \n\n"
                                 "2. Sensible echo main stats: The program can't help you if you're running defense% and HP% 3 cost and 1 cost echoes on your Jiyan. \n\n"
                                 "3. Sensible weapon: Again, the program can't help you if you're running Dauntless Evernight on Jinhsi. Look up guides. \n\n"
                                 "4. Sensible crit ratio: 1.5 < (Crit Damage - 100) / Crit Rate <= 2.2. [Enter 4 to test your crit ratio]. \n"
                                 "NOTE: It's completely okay if you don't fall in this sweet-spot, as long as there is a full attempt without sacrificing feasability. \n"
                                 "If your character has a crit damage weapon and you're running a crit rate 4 cost and trying to get at least crit rate on all pieces, that's enough. \n"
                                 "\n---------- ---------- Seequence flowchart to make your character ready ASAP ---------- ----------\n\n"
                                 "It doesn't matter what your standards are for building a character, there is a process you can follow that will make your character 'ready' or "
                                 "'playable' in the shortest amount of time. If you follow the following steps, you can rest assured that at ANY given time - THIS is the BEST your "
                                 "chararacter could have been given the waveplates and/or time invested (always keep the above assumptions in mind): \n\n"
                                 "1. Upgrade and ascend your character, weapon and relavent fortes at this moment in time as much as possible. \n"
                                 "2. Farm an Echo Set with correct main stats and reach the 'Base Level Tier' build rating. \n"
                                 "3. Upgrade Character to level 80/80, Weapon to 90/90, unlock FULL Forte tree and get relavent fortes to level 8. \n"
                                 "4. Improve Echoes until 'Decent' tier. \n"
                                 "5. Ascend Character to level 80/90, then level relavent Fortes to level 9. At this point your character should DEFINITELY be ToA Ready. \n"
                                 "6. Improve Echoes until 'Well Built' tier. \n"
                                 "(7. Level relavent Fortes to level 10, and character to level 90/90. )\n"
                                 "(8. Improve Echoes beyond 'Well Built' tier, depending on your goals. )\n"
                                 "9. Switch to the next character. \n"
                                 "Steps in brackets are OPTIONAL and may be skipped or only partially completed before moving to the next step. \n\n"
                                 "Select available options or enter anything else to continue: \n").strip()
                if ass_test == "4":
                    ver_cs = 0
                    while ver_cs != 1:
                        try:
                            char_cr = float(input("Enter " + char_name + "'s Crit Rate% (Give the exact amount even if it exceeds 100%): ").strip())
                            char_cd = float(input("Enter " + char_name + "'s Crit Damage%: ").strip())
                            ver_cs = 1
                        except:
                            print("Invalid input. \nPlease try again. ")
                    char_r = (char_cd - 100) / char_cr
                    input(char_name + "'s Crit Ratio is: " + str(round(char_r, 3)) + " \nPress Enter to continue. \n")
                continue
            elif calc_type == "5" or calc_type == "05":
                input("\n---------- ---------- Echo/Build Value brackets ---------- ----------\n\n"
                      "Your echoes/builds are rated on a scale where 100 points are assigned to a theoretical build which has all the best stats rolled exactly to their median value. \n\n"
                      "Your rating lands your echo/build into one of the following catagories: \n\n"
                      "Unbuilt Tier [0<=Score<44]: \nInvesting waveplates into Echos highly optimal. \n\n"
                      "Base Level Tier [44<=Score<55]: \nInvesting waveplates into Echoes only optimal after getting Character Level to 80/80, Weapon Level to 90, unlocking the full Forte"
                      " tree and leveling relavant Fortes to level 8. \n\n"
                      "Decent Tier [55<=Score<66]: \nAssuming previous targets are met, your character now approximately meets the minimum requirements to achieve max stars on the "
                      "hardest ToA Hazard zone levels. \n"
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
            elif calc_type == "4" or calc_type == "04":
                input("\n---------- ---------- About the Echo Value Calculator (name subject to change) and the Scoring Method ---------- ----------\n\n"
                      "The goal here is to put a value on your ECHOES. \nThe ratings reflect an echo/build's VALUE to YOUR SITUATION. THIS is what makes this "
                      "calculator so powerful. Here 'Value' does not merely mean damage output potential - the calculator DIRECTLY considers the benefit of a substat to your SPECIFIC "
                      "character and situation. \nIt simply asks 'How valueable is this stat to this character in relation to other stats this character finds valuable, in a specific "
                      "situation? '\nIt is for this reason why the ratings work JUST AS WELL for support characters as for DPS or sub-DPS characters, WITHOUT changing the logic behind "
                      "its mechanisms. \n\n"
                      "Character sequences, weapon level, character level, forte level etc. don't matter whatsoever! (unless they affect this character's ER requirements AND they are "
                      "reflected on the stat page. \n\n"
                      "Scoring Method: \nThe full theory of the calculator and the full logic of this program will be made available in a word document on the GitHub page (unless "
                      "already availabe). The following example is PURPOSELY chosen to be very simple and uncomplicated. For the users who can follow, this gives a VERY BASIC IDEA "
                      "behind this program (for a detailed explanation of the full nitty-gritty, please check the word document). \n\n"
                      "Carlotta uses the following stats: Crit Rate%, Crit Damage%, Atk%, Flat Atk, Resonance Skill% and ER%. \nThese are the relative median substat roll values, "
                      "respectively: 1, 1, 0.5, 0.25, 0.425. For ER% there are 4 different values that the program may require (depending on a variety of factors - please refer to the "
                      "word document): ER% target (without team mates like Zhezhi or Yangyang) (intermediate value used to determine, store and update net surplus/deficit - VERY "
                      "important REGARDLESS of whether the ER% target is low or high) (WILL cause FLUCTUATIONS in the third ER parameter based on updates), Liberation impact (just how "
                      "much a character relies on pressing the liberation button in a rotation, VERY important multiplier), ER% relative median substat roll value (obtained from "
                      "processing and combining the previous two values), Resonance Cost (used to modify ER% targets in presence of Zhezhi or Yangyang). \n"
                      "Assume you've rolled an Echo with the substats: Crit Rate 7.5%, Crit Damage 16.2%, Atk 7.9% and Atk 40. Here is how the Echo rating is determined in general: \n"
                      "[Sum of ([substat value / substat median value] * character specific relative median substat roll value) for all good substats] \n"
                      "Divided by: [Sum of best 5 relative median substat roll values at the time of considering this Echo. The result is then multiplied by 100. \n"
                      "For this Echo evaluated for Carlotta: [(7.5 / 8.4) * 1] + [(16.2 / 16.8) * 1] + [(7.9 / 9) * 0.5] + [(40 / 45) * 0.25] = 2.518... \n"
                      "1 + 1 + 0.5 + 0.425 + 0.25 = 3.175. Dividing the previous number with this one, then multiplying by 100 results in: 79.315 - High Investment Tier. This matches "
                      "exactly with the output of the calculator. \n\n"
                      "Notice that Carlotta happens to have exactly 5 values (ignoring ER) that are good. For characters with more (or less) substats they can make use of, top 5 (or less)"
                      " values are considered. In fact, even for Carlotta - in actuality - ER will play a big roll here as well. \n\n"
                      "Why consider ER? \nImagine a player got the exact Echo mentioned above, except the 5th stat is ER 10% instead of some other dead stat. Additionally this player "
                      "is an S0R1 Carlotta and is not using Zhezhi or Yangyang as team mates. Is it really fair to give this Echo exactly the same rating as the previous? \n"
                      "'Well okay maybe the value will increase slightly' - by how much? why? Without going into specifics (outlined in the document), I am confident that ER% is handled "
                      "and valued exactly as much as it should. For example, the output of the calculator for the SECOND Echo, will change based on whether the total ER% (value on the "
                      "stat-page) is more or less (AND EXACTLY how much more or less) than the target. A total ER% of 100, 120, 125, 130 and 140 will all give the appropiate results of: "
                      "90.699, 90.699, 90.699, 88.196, 79.315. But WAIT! Can you guess what happens to the first Echo's value when this Carlotta has 100 total ER% (as in no ER% substats)"
                      "? \nThe value of the Echo in this circumstance is now 64.159. Look again at the general formula for ratings! Not only is the first part, but ALSO the second part, "
                      " is being influenced by ER%. ER%'s relative median substat roll value FLUCTUATES to enter the top 5 best stats! Let's consider the first Echo's ratings for the "
                      "five ER values that we considered above: 64.159, 73.018, 79.315, 79.315, 79.315. Try to look at both of these sets of results, see where they're the same and where "
                      "they're different, and try to answer why this is the case. This will, in my opinion, make you understand the sheer coolness of this calculator! \n\n"
                      "'Sure, it's great that this is such a thorough handling, but why go to such lengths? ' - Remember that the sets of values we've calculated above are JUST for two "
                      "different Echos, and they're ONLY different with respect to the ER they have! 64.159 falls in the 'Decent' bracket and 90.699 falls in the 'Extreme' bracket. \n"
                      "Do you really think a program where the potential values based on circumstances can vary this much provide any value to anyone? \n\n"
                      "I, hereby, assert that you MUST have ALL these considerations for ANY Program that seeks to evaluate Echoes and provide ANY value whatsoever (in terms of "
                      "satisfaction, trust, reliability, informativeness, fun etc.) to the users. Without this thorough treatment, you would stop using, relying and enjoying this "
                      "program simply for the fact that most characters in this game will have SOME ER requirements, so you'll NEVER be able to make decisions or measure build strenghts "
                      "(or whatever else you wish to do) with ease and without doubts. You would stop using that program soon. I know I would. And so I've went through extra lengths to "
                      "make sure that never happens. I am, first and foremost, a user of this calculator just as much as the creator - and as a user I am confident that this program is "
                      "fun, reliable, trustworthy, informative and correct. I enjoy this program very much, and I hope everyone else finds the same enjoyment with the EVC(nstc) as I do. "
                      "\n---------- ---------- ---------- ---------- ----------\n\nPress enter to continue: \n")
                continue
            elif (calc_type != "1" and calc_type != "2" and calc_type != "3" and calc_type != "7" and calc_type != "10" and calc_type != "01" and calc_type != "02" and calc_type != "03"
                  and calc_type != "07"):
                input("\n\nYou have picked an incorrect option. \nPress enter to try again. \n")
                continue
            if calc_type == "10":# Phase 2 handling - loading correct stat presets
                if stat_med[0] == 8.4:
                    print("!!!WARNING!!!: On this scale - 100 points are awarded to the absolute theoretical maximum a character can ever achieve. Max rolls, Best Relevant stats."
                          " All builds will score low on this scale. \nAdditionally, your build will NOT receive any feedback or evaluation. ")
                    why_tho = input("It is highly NOT recommended to use this scale other than for amusement purposes. "
                                    "Continue anyway? (enter 'y' to continue, anything else to go back) : \n").lower()
                    if why_tho != "y": continue
                    stat_med = [10.5, 21, 11.6, 60, 11.6, 580, 14.7, 70, 11.6, 11.6, 11.6, 11.6, 12.4]
                    char_stats[16] = 0
                else:
                    stat_med, char_stats[16] = game_data(char_name)[1], game_data(char_name)[3][16]
                continue
            if calc_type == "7" or calc_type == "07":# Phase 3 handling - stat related
                disp_char_data(stat_name, stat_med, char_name2, char_stats)
                continue
            if char_stats[12] != 0:
                ver_char_er = 0
                while ver_char_er != 1:
                    try:
                        net_er = (float(input("\n---------- ---------- ---------- ---------- ----------"
                                             "\n\nEnter " + char_name + "'s Energy Regen% from the stat page (please do NOT modify this because other source of ER have been concidered). "
                                             "\n!!!Make sure you've equipped the build you're evaluating and they're on the correct weapons!!!\nEnergy Regen%: \n").strip())
                                  + char_stats[12])
                        ver_char_er = 1
                    except:
                        print("Error: Input is not a number. Please try again. ")
            else:
                net_er = 0            
            if calc_type == "1" or calc_type == "01":
                echo_val = 0            
                for echo_no in range (0,5):
                    print("\n---------- ---------- Echo " + str(echo_no+1) + " ---------- ----------")
                    cur_echo_val, net_er = player_data(stat_name, stat_med, char_name, char_stats, net_er, 1)
                    echo_eval(cur_echo_val, 0, 0, char_stats[16])
                    echo_val = echo_val + cur_echo_val                
                echo_eval(echo_val/5, 1, 2, char_stats[16])
            elif calc_type == "2" or calc_type == "02":
                fb_val, net_er = player_data(stat_name, stat_med, char_name, char_stats, net_er, 5)            
                echo_eval(fb_val, 1, 2, char_stats[16])
            elif calc_type == "3" or calc_type == "03":
                echo_val, net_er = player_data(stat_name, stat_med, char_name, char_stats, net_er, 1)
                echo_eval(echo_val, 0, 1, char_stats[16])
            input("Press enter to continue: \n")


def calculator_quit():
    confirm_exit = input("Are you sure you want to quit? (Enter y to confirm): \n").lower()
    if confirm_exit == "y":
        input("Thank you for using Echo Value Calculator (name subject to change). \nPress enter to exit (intentional): ")
        sys.exit()


def game_data(character_name_gd):
    
    stat_names_gd = (["Crit Rate%", "Crit Damage%", "Attack%", "Flat Attack", "HP%", "Flat HP", "Defense%", "Flat Defense", "Basic Attack Damage Bonus%", "Heavy Attack Damage Bonus%",
                  "Resonance Skill Damage Bonus%", "Resonance Liberation Damage Bonus%", "Energy Regen%", "Liberation Impact", "_Energy_Regen%_", "Resonance Energy", "_Analysis?_"])
    stat_medians_gd = [8.4, 16.8, 9, 45, 9, 450, 11.4, 55, 9, 9, 9, 9, 9.6]
    character_name_main_gd = ["No selection"]
    character_data_gd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    if (character_name_gd == "carlotta" or character_name_gd == "glass girl" or character_name_gd == "small car lotta damage. wait... what?"
        or character_name_gd == "in the name of the montellis." or character_name_gd == "rin tohsaka" or character_name_gd == "best girl"):
        character_name_main_gd = ["Carlotta"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0, 0.5 * 0.85, 0, - 125, - 1, 0, - 125, - 1]
        
    elif character_name_gd == "jinhsi" or character_name_gd == "madam magistrate" or character_name_gd == "sacred light!" or character_name_gd == "snow girl":
        character_name_main_gd = ["Jinhsi"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0, 0.5 * 0.75, 0.5 * 0.2, - 115, - 0.2 / 0.95, 0, - 150, - 1]
        
    elif (character_name_gd == "encore"  or character_name_gd == "leave... me... alone!" or character_name_gd == "annie" or character_name_gd == "klee" or character_name_gd == "maygi"
          or character_name_gd == "pink gremlin"):
        character_name_main_gd = ["Encore (Hypercarry)"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.5, 0, 0.5 * 0.2, 0.5 * 0.1, - 125, - 1, 0, - 125, - 1]
        
    elif (character_name_gd == "yinlin" or character_name_gd == "hmph... now you'll behave." or character_name_gd == "bdsm" or character_name_gd == "dominatrix"
          or character_name_gd == "puppet girl"):
        character_name_main_gd = ["Yinlin"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.1, 0.5 * 0.1, 0.5 * 0.55, 0.5 * 0.2, - 135, - 0.2 / 0.95, 0, - 125, - 1]
        
    elif (character_name_gd == "sanhua" or character_name_gd == "jinhsi's bodyguard" or character_name_gd == "goth girl #3" or character_name_gd == "goth girl 3"
          or character_name_gd == "shackles begone!"):
        character_name_main_gd = ["Sanhua"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0.5 * 0.3, 0.5 * 0.3, 0.5 * 0.3, 0, 0, 0, - 100, - 1]
        
    elif character_name_gd == "zhezhi" or character_name_gd == "shy girl" or character_name_gd == "painter girl" or character_name_gd == "art unveiled":
        character_name_main_gd = ["Zhezhi"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.8, 0.5 * 0.05, 0.5 * 0.05, 0, - 135, - 1, 0, - 125, - 1]
        
    elif character_name_gd == "aalto" or character_name_gd == "cool shades" or character_name_gd == "thanks for watching!":
        character_name_main_gd = ["Aalto"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.50, 0, 0.5 * 0.25, 0.5 * 0.15, - 135, - 0.65 / 0.9, 0, - 150, - 1]
        
    elif (character_name_gd == "baizhi" or character_name_gd == "goth girl #2" or character_name_gd == "goth girl 2" or character_name_gd == "verina at home"
          or character_name_gd == "better than verina" or character_name_gd == "endless reverberation."):
        character_name_main_gd = ["Baizhi"]
        character_data_gd = [0, 0, 0, 0, 1, 0.5, 0, 0, 0, 0, 0, 0, - 215, - 1, 0, - 175, 0]
        
    elif character_name_gd == "brant":
        input("Brant's stats are currently unavailable. Please check the next version. \nPress enter to continue: \n")
        
    elif (character_name_gd == "cucumber" or character_name_gd == "calculator" or character_name_gd == "vergil" or character_name_gd == "kurapika" or character_name_gd == "kukaracha"
          or character_name_gd == "calcium" or character_name_gd == "carpaccio" or character_name_gd == "cactus" or character_name_gd == "calculus" or character_name_gd == "calzone"
          or character_name_gd == "misery follows!"):
        character_name_main_gd = ["Calcharo"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.25, 0, 0, 0.5 * 0.55, - 125, - 1, 0, - 125, - 1]
        
    elif (character_name_gd == "camellya" or character_name_gd == "zyra" or character_name_gd == "yuno gasai" or character_name_gd == "yandere girl"
          or character_name_gd == "she wants my seed?" or character_name_gd == "i can fix her" or character_name_gd == "spin to win" or character_name_gd == "gymnasts girl"
          or character_name_gd == "i will do gymnastics with her but ancient greek style" or character_name_gd == "struggle harder, entertain me!"):
        character_name_main_gd = ["Camellya"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.7, 0, 0, 0.5 * 0.15, - 120, - 0.15 / 0.85, 0, - 125, - 1]
        
    elif (character_name_gd == "changli" or character_name_gd == "fox girl" or character_name_gd == "ahri" or character_name_gd == "nine-tailed fox" or character_name_gd == "yae miko"
          or character_name_gd == "feathers incinerate."):
        character_name_main_gd = ["Changli"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.05, 0, 0.5 * 0.6, 0.5 * 0.25, - 125, - 0.25/0.9, 0, - 125, - 1]
        
    elif (character_name_gd == "chixia" or character_name_gd == "amber" or character_name_gd == "finger pistol" or character_name_gd == "ma xiaofang"
          or character_name_gd == "boom! headshot!" or character_name_gd == "pew pew pew!" or character_name_gd == "one shot, one kill!"
          or character_name_gd == "easy peasy. lemon squeezy!" or character_name_gd == "dakka dakka dakka dakka dakka!"):
        character_name_main_gd = ["Chixia"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0, 0.5 * 0.5, 0.5 * 0.3, - 150, - 0.3 / 0.8, 0, -150, -1]
        
    elif character_name_gd == "danjin" or character_name_gd == "darkness falls...":
        character_name_main_gd = ["Danjin"]
        charater_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.05, 0.5 * 0.25, 0.5 * 0.25, 0.5 * 0.3, 0, 0, 0, - 100, - 1]
        
    elif character_name_gd == "jianxin" or character_name_gd == "sage girl" or character_name_gd == "small-town girl" or character_name_gd == "universe in my psyche!":
        character_name_main_gd = ["Jianxin (DPS)"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.25, 0.5 * 0.4, 0, 0.5 * 0.3, - 130, - 0.3 / 0.95, 0, - 150, - 1]
        
    elif character_name_gd == "jiyan" or character_name_gd == "dragon boy" or character_name_gd == "teal general" or character_name_gd == "windrider!":
        character_name_main_gd = ["Jiyan"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0.5 * 0.7, 0.5 * 0.15, 0, - 130, - 1, 0, - 125, - 1]
        
    elif character_name_gd == "lingyang" or character_name_gd == "who..." or character_name_gd == "cares." or character_name_gd == "gaming" or character_name_gd == "this might hurt.":
        character_name_main_gd = ["Lingyang"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.35, 0, 0.5 * 0.3, 0.5 * 0.05, - 125, - 1, 0, - 125, - 1]
        
    elif character_name_gd == "lumi" or character_name_gd == "delivery girl" or character_name_gd == "bunny girl" or character_name_gd == "squeakie, protect the cargo!":
        character_name_main_gd = ["Lumi"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.35, 0, 0.5 * 0.25, 0.5 * 0.3, - 165, - 1, 0, - 125, - 1]
        
    elif (character_name_gd == "mortefi" or character_name_gd == "xingqiu" or character_name_gd == "four-eyes" or character_name_gd == "roy mustang"
          or character_name_gd == "fuel my wrath!"):
        character_name_main_gd = ["Mortefi"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.1, 0, 0.5 * 0.15, 0.5 * 0.7, - 125, - 1, 0, - 125, - 1]
        
    elif character_name_gd == "phoebe" or character_name_gd == "sister" or character_name_gd == "church girl" or character_name_gd == "lux":
        input("Phoebe's stats are unavailable right now. Please check future updates. \nPress enter to continue: \n")
        
    elif character_name_gd == "roccia" or character_name_gd == "mamma mia!" or character_name_gd == "pero":
        character_name_main_gd = ["Roccia"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.05, 0.5 * 0.6, 0.5 * 0.15, 0, - 135, - 1, 0, - 125, - 1]
        
    elif (character_name_gd == "rover" or character_name_gd == "goth girl #1" or character_name_gd == "goth girl 1" or character_name_gd == "goth guy" or character_name_gd == "rizzler"
          or character_name_gd == "mc"):
        
        ver_rov_ele = 0
        while ver_rov_ele != 1:
            try:
                mc_element = int(input("\nEnter 1 for Spectro Rover, Enter 2 for Havoc Rover: \n").strip())
                if mc_element < 1 or mc_element > 2:
                    print("Please select a valid option. ")
                    continue
                else: ver_rov_ele = 1
            except:
                print("Please enter a valid input. ")
                
        if mc_element == 1:
            input("Due to insufficient data for Spectro Rover, please wait until the next version until more data from the TCs is available. \nPress enter to continue: \n")
        elif mc_element == 2:
            character_name_main_gd = ["Havoc Rover"]
            character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.3, 0, 0.5 * 0.2, 0.5 * 0.25, - 125, - 0.25 / 0.75, 0, - 125, - 1]
            
    elif character_name_gd == "taoqi" or character_name_gd == "personalities" or character_name_gd == "two reasons" or character_name_gd == "attack is the best defense.":
        character_name_main_gd = ["Taoqi (quick concerto focus)"]
        character_data_gd = [0, 0, 0, 0, 0, 0, 1, 0.5, 0, 0, 0, 0, - 170, - 1, 0, - 125, 0]
        
    elif (character_name_gd == "the shorekeeper" or character_name_gd == "shorekeeper" or character_name_gd == "best waifu" or character_name_gd == "must protect"
          or character_name_gd == "vow from the soul." or character_name_gd == "in war with time." or character_name_gd == "i engraft you new."
          or character_name_gd == "astral modulation." or character_name_gd == "ordained."):
        character_name_main_gd = ["The Shorekeeper"]
        character_data_gd = [0, 1, 0, 0, 0.5, 0.25, 0, 0, 0.5 * 0.1, 0, 0, 0.5 * 0.85, - 240, - 1, 0, - 175, 0]
        
    elif character_name_gd == "verina" or character_name_gd == "flower girl" or character_name_gd == "life is in everything.":
        character_name_main_gd = ["Verina"]
        character_data_gd = [0, 0, 1, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, - 200, - 1, 0, - 175, 0]
        
    elif character_name_gd == "xiangli yao" or character_name_gd == "xiangling" or character_name_gd == "reconfiguration!":
        character_name_main_gd = ["Xiangli yao"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.1, 0, 0.5 * 0.2, 0.5 * 0.55, - 120, - 0.55 / 0.85, 0, - 125, - 1]
        
    elif character_name_gd == "yangyang" or character_name_gd == "coolest animations" or character_name_gd == "tempest." or character_name_gd == "i think she likes us":
        character_name_main_gd = ["Yangyang"]
        character_data_gd = [1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5 * 0.3, 0, 0.5 * 0.15, 0.5 * 0.45, 0, 0, 0, - 100, - 1]
        
    elif character_name_gd == "youhu" or character_name_gd == "you who" or character_name_gd == "noice!":
        character_name_main_gd = ["Youhu"]
        character_data_gd = [0, 0, 1, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, - 165, - 1, 0, - 100, 0]
        
    elif character_name_gd == "yuanwu" or character_name_gd == "you and who" or character_name_gd == "maximum voltage.":
        character_name_main_gd = ["Yuanwu"]
        character_data_gd = [1, 1, 0, 0, 0, 0, 0.5, 0.25, 0, 0, 0.5 * 0.5, 0.5 * 0.4, - 140, - 1, 0, - 125, - 1]
        
    elif character_name_gd == "zani" or character_name_gd == "that button is the real body guard":
        input("Zani stats currently unavailable. Please come back later. \nPress enter to continue: \n")
        
    else:
        print ("Character not found or character name not recognized. \nPress enter to continue: \n")
        
    return stat_names_gd, stat_medians_gd, character_name_main_gd, character_data_gd


def disp_char_data(stat_name_dp, stat_med_dp, char_name2_dp, char_stats_dp):
    print("\nNOTE: The character data used in this program has been highly researched by analyzing multiple sources inlcuding but not limited to: prydwen.gg, Maygi, many YouTube guides "
          "and many websites. \nFor the 'damage profile' stats (basic attacks, heavy attacks, resonance skill, resonance liberation), their relative value should be exactly half of "
          "thier damage profile's ratio. Even a 5 to 10% disagreement with the damage profile will have very little impact on the overall score. \n"
          "However, feel free to report any inconsistency you feel are significant as a comment in the publishing post to improve this program. \n")
    for y in range (0, len(stat_name_dp) - 5):
        if char_stats_dp[y] > 0:
            print("The reletive value of a median roll (" + str(stat_med_dp[y]) + ") of " + stat_name_dp[y] + " for " + char_name2_dp[0] + " is: " + str(round(char_stats_dp[y] * 100, 3))
                  + "%. ")
    if char_stats_dp[12] < 0:
        print("The " + stat_name_dp[12] + " requirements for " + char_name2_dp[0] + " are: " + str( - char_stats_dp[12]) + "% with a relative substat value multiplier of: "
              + str(round( - char_stats_dp[13] * 100, 3)) + " (Resonance Cost: " + str( - char_stats_dp[15]) + ").")
        input("The reletive value of a median roll (" + str(stat_med_dp[12]) + ") of " + stat_name_dp[12] + " is fluctuating based on complex factors, and may not be constant even "
              "during the evaluation of a single build (option 1). \nRest assured: ER is handled very carefully and apporpiately to accurately reflect its true value in the scoring "
              "system. \nCheck out option 4 to get a glimpse of this fact with the aid of examples. For full details on the theory and logic, check out the word document in GitHub. \n"
              "Press enter to continue: \n")


def player_data(stat_name_pi, stat_med_pi, char_name_pi, char_stats_pi, net_er_pi, rat_typ_pi):
    player_input = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range (0, len(stat_name_pi) - 5):
        if char_stats_pi[x] > 0:
            ver_stat_val = 0
            while ver_stat_val != 1:
                try:
                    player_input[x] = (float(input("Enter " + char_name_pi + "'s " + stat_name_pi[x] + " from echo substats: ")) / stat_med_pi[x]) * char_stats_pi[x]
                    ver_stat_val = 1
                except:
                    print("Error: Input is not a number. Please try again. ")
    if char_stats_pi[12] < 0:
        ver_stat_val = 0
        while ver_stat_val != 1:
            try:
                player_input[13] = float(input("Enter " + char_name_pi + "'s " + stat_name_pi[12] + " from echo substats: "))
                ver_stat_val = 1
            except:
                print("Error: Input is not a number. Please try again. ")
    if net_er_pi >= 0:
        net_er_pi = net_er_pi - player_input[13]
        if net_er_pi < 0:
            er_bank = - net_er_pi / stat_med_pi[12]
            player_input[12] = er_bank * ( - char_stats_pi[13])
            net_er_pi = 0
        else:
            er_bank = 0
    else:
        er_bank = (player_input[13] - net_er_pi) / stat_med_pi[12]
        player_input[12] = (player_input[13] / stat_med_pi[12]) * ( - char_stats_pi[13])
    useful_stat_val = 0
    mechos = 0
    while mechos < rat_typ_pi:
        if er_bank >= 1:
            char_stats_pi[14] = 1 * ( - char_stats_pi[13])
            er_bank = er_bank - 1
        else:
            char_stats_pi[14] = er_bank * ( - char_stats_pi[13])
            er_bank = 0
        useful_stat_val = useful_stat_val + sum(heapq.nlargest(5, char_stats_pi))
        mechos = mechos + 1
    total_stat_val = sum(player_input[:13])
    tot_rat = (total_stat_val / useful_stat_val) * 100
    return tot_rat, net_er_pi


def echo_eval(echo_val_al, eval_type_al, anal_type_al, eval_al):
    eval_ui = ["Echo", "Build"]
    print("\n\nYour " + eval_ui[eval_type_al] + " rating is: " + str(round(echo_val_al, 3)))
    if eval_al == 0: return
    if echo_val_al >= 99:
        print("\nThis " + eval_ui[eval_type_al] + " falls in the 'Godly' tier.")
    elif echo_val_al >= 88:
        print("\nThis " + eval_ui[eval_type_al] + " falls in the 'Extreme' tier.")
    elif echo_val_al >= 77:
        print("\nThis " + eval_ui[eval_type_al] + " falls in the 'High Investment' tier.")
    elif echo_val_al >= 66:
        print("\nThis " + eval_ui[eval_type_al] + " falls in the 'Well Built' tier.")
    elif echo_val_al >= 55:
        print("\nThis " + eval_ui[eval_type_al] + " falls in the 'Decent' tier.")
    elif echo_val_al >= 44:
        print("\nThis " + eval_ui[eval_type_al] + " falls in the 'Base Level' tier.")
    else:
        print("\nThis " + eval_ui[eval_type_al] + " falls in the 'Unbuit' tier.")
    if anal_type_al == 1:
        if echo_val_al >= 99:
            print("\nOne of the rarest echos. Impractically close to perfect, if not - quite literally perfect. Whitebeard was right afterall... "
                  "\nDelete it immedietly. \n.\n.\n.(Please don't do that it's a joke!) "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val_al>= 88:
            print("\nPractically perfect piece. Congratulations! "
                  "More than just time and effort are required, however, to reach the next category. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val_al >= 77:
            print("\nHigh value piece. Usually only found on builds with lots of dedicated investment. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val_al >= 66:
            print("\nVery solid piece. Recommended to find upgrades for other pieces before trying to find upgrades for this. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val_al >= 55:
            print("\nFine piece. Recommended to find upgrades to other pieces if the goal is to make this character 'ToA-ready'. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val_al >= 44:
            print("\nPassable piece. Good enough until your character is at lvl 80/80, weapon at level 90/90, and relevant talents are at level 8. "
                  "\n---------- ---------- ---------- ---------- ----------")
        else:
            print("\nDiscardable piece. C'mon man have some ambition. "
                  "\n---------- ---------- ---------- ---------- ----------")
    elif anal_type_al == 2:
        if echo_val_al >= 99:
            print("\nYou have entered stats incorrectly. \nThe alternative is that you've actually found a build so perfect - posting this on reddit will lead to the birth of a new religion. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val_al >= 88:
            print("\nYou've shown extreme levels of dedication for this character build. \nIt'll most likely place you very high even on global leaderboards, if we had them. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val_al >= 77:
            print("\nYou've given this build special treatment, or it has given special treatment to you. \nYou'll find clearing ToA easy even WITH skill issues. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val_al >= 66:
            print("\nYour build is looking great! Now is a good time to move on to the next character. \nIf you're having difficulty to get 30/30 in ToA, this character build is certainly not an issue whatsoever. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val_al >= 55:
            print("\nYour character is 'ToA ready'. \nGiven that the rest of the teammates are at or above this level, getting 30/30 should be achievable with enough skill and attempts. \nHighly recommended to get your character talens, levels, weapons and any other guaranteed upgrades at max level (if not, as high as possible) before continuing to improve your echos. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val_al >= 44:
            print("\nA passable build that will work great until you bring your character to level 80/80, talents to level 8, and weapon to level 90."
                  "\n---------- ---------- ---------- ---------- ----------")
        else:
            print("\nUnacceptable build. Highly recommended to find better pieces immedietly if you want to build this character. "
                  "\n---------- ---------- ---------- ---------- ----------")


welcome()

