import heapq
import sys

#Add List
#Rel_ER_Imp
#Better more efficient Code
#

def calc_route():
    char_name=str(input("\nPlease enter your character, or enter q to quit: ")).lower()
    stat_name, stat_med, char_name2, char_stats=game_data(char_name)
    calc_type=str(input("\nCharacter stats loaded. Please select from one of the following options: "
                        "\n    1) Full evaluation (enter data iteratievely per echo) [Recommended]. "
                        "\n    2) Build evaluation (enter COMBINED stats from echos ONLY). "
                        "\n    3) Echo evaluation. [Recommended]"
                        "\n    4) About this program and the scoring method. "
                        "\n    5) Brackets/Build Tiers explanation. "
                        "\n    6) Display game and character data. "
                        "\n    7) Pick a different character. "
                        "\n    8) Quit the program. "
                        "\n\nEnter the option number here: ")).lower()
    if calc_type=="8":
        quit_calc()
    elif calc_type=="7":
        calc_route()
    elif calc_type=="6":
        disp_char_data(stat_name, stat_med, char_name2, char_stats)
    elif calc_type=="5":
        print("\n---------- ---------- Echo/Build Value brackets ---------- ----------"
              "\n\nThis program calculates the value of your echos and produces a build value based on their average."
              "\nYour score lands your build into one of the following catagories: "
              "\n\nUnbuilt Tier [0<=Score<44]: \nInvesting waveplates into Echos highly optimal"
              "\n\nBase Tier [44<=Score<55]: \nInvesting waveplates into Echos only optimal after getting Character Level to 80/80, Weapon Level to 90 and relevant Fortes to level 8 "
              "with full Forte tree unlocked."
              "\n\nDecent Tier [55<=Score<66]: \nGiven that you have the upgrades mentioned in the previous tier, your character now approximately meets the minimum requirements "
              "to acheive max stars on the hardest ToA Hazard zone level. "
              "\nHighly recommened to secure guaranteed upgrades from ascending and levelling characters and maxing out talents."
              "\n\nWell Built Tier [66<=Score<77]: \nYour character can now be considered well built. If not already done, leveling talents to level 9 or 10 will be the optimal use of "
              "waveplates."
              "\nIf you have more characters to build, now is a great time to move on to the next character in your roster."
              "\n\nHigh Investment Tier [77<=Score<88]: \nYou've given this character build special treatment. Or you got very lucky."
              "\nRoI of time and/or waveplates to seek further improvements is very low there's a massive skew between individual echos. "
              "\n\nExtreme Tier [88<=Score<99]: \nYou are obsessed with this character. Or they're obsessed with you. "
              "This build should easily rank you very high on global echo leaderboards, if we had them."
              "\n\nGod Tier [Score>=99]: \nYou've entered the stats incorrectly or there is an error with this code or logic on my part. "
              "\nThe alternative, that there's no error on either sides, means you've got yourself a build worthy of worship. You can start a religion out of this. "
              "\n\nAdditional info: the max achievable points does not equal 100. But forget ever reaching 3 digits muhahahaha (idk why I'm laughing I'm literally in the same boat). ")
    elif calc_type=="4":
        print("\n---------- ---------- About the Echo Value Calculator (name subject to change) and the Scoring Method ---------- ----------"
              "\n\nThe goal here is to put a value on your ECHOS. NOT your overall character. "
              "\nSo Character sequences, weapons, character level, talent level etc. don't matter whatsoever... well..."
              "\nIf any of the above mentioned things affect your character's ER (and assuming that ER is, in fact, something that your character cares about) then, and only then, will it matter. "
              "\n\nTo start: different characters use different stats and value these stats differently. "
              "\n[If you're confident in your ability to grasp stuff fast or you're the 'learn by doing' type, jump directly to the second last paragraph and come back if you feel lost]."
              "\n\nIn a nutshell, each echo is evaluated with the following simple formula: "
              "\n[Value of your stats with respect to median rolls/Reletive median substat roll values of the best possible stats]*100%."
              "\nThe average of the 5 echo scores calculated as above determines your build value. "
              "\n\nFormula for 'Value of your stats with respect to median rolls': (stat amount/stat median)*(reletive value) "
              "\nFormula for 'Reletive Median substat roll values for the best possible stats': Sum of top 5 (reletive value) "
              "\n\nTo translate this jargon into understandable explanation, we will consider the following example: "
              "\n1. Carlotta: \nLet's start with the 'Reletive median substat roll values for the best possible stats': "
              "\nDespite how it sounds, it's actually a very simple concept. "
              "\nWe want to know how good a stat is (to increase dps and/or playability) vs other stats: aka figure out its reletive value. "
              "\nHere I would like to thank Maygi (reddit name 'Maygii', YouTube name 'Maygi'), for her excellent, incredible and valuable mathematical insights across multiple characters. "
              "\nIn her Carlotta guide, a median roll of crit will increase Carlotta's damage by around 6.16%, median atk% roll will increase her damage by 3.07%, flat attack by 1.49% and resonance skill damage by 2.5%."
              "\nComparing it with other stats to align on a scale where crit gets 100% points, we have the relative values: "
              "\nCrit: 100%, Atk%: 49.84%, Resonance Skill dmg bonus%: 40.58%, Flat Atk: 24.19%"
              "\n\nMany characters show something very similar. Let's take a look at Jinhsi: "
              "\nCrit: 100%, Atk%: 52.72%, Resonance Skill dmg bonus%: 30.19%, Resonance Liberation dmg bonus%: 8.95%, Flat Atk: 30.51%"
              "\n\nFor Roccia: \nCrit: 100%, Atk%: 47.52%, Basic atk dmg bonus%: 4.62%, Heavy atk dmg bonus%: 44.55%, Skill dmg bonus%: 12.21%, Flat Atk: 23.60%. "
              "\n\nVery important to remember here is that these values fluctuate the more you build or unbuild your character based on things such as diminishing returns, base values, and what values are additive and multiplicative together, etc. \nFurthermore, these are also dependent on your character weapon, level and other factors. "
              "\nHowever, in games like these (Wuwa, Genshin etc), the stat balance doesn't usually change reletive to other stats. "
              "\n\nAnd sure enough, after a close inspection of the character's damage profile I figured out that the following general principle applies for all the character's relative value of median stats(attack scaling): "
              "\nCrit: 100%, Atk%: 50%, Flat Atk: 25%, Basic/Heavy/Skill/Liberation dmg bonus%: 50% times %of total damage profile. "
              "\nTo make the last one explicity clear, look at any of the above mentioned character's relative ability dmg bonus% value and times it by 2 to get the %of damage they do as this type and you'll find that it always checks out to a very acceptable degree of accuracy. (To be even more accurate, times it by 1/reletive value of atk%)"
              "\n\nThe above mentioned character specific values are NOT used in this calculator, in favor of the general values mentioned later."
              "\nThe goal, again, is not to EXACTLY determine how good an echo is for your character - to do that would require info about basically everything about your character. \nTo give a very solid and highly accurate value for your echos, however, is an entirely different matter requiring me to only know about the character you're building and the echo in question itself."
              "\nAnother important point to note is that even a 5 to 10% differences in the above mentioned values will have very little impact to be exact, and no impact to be practical. The base idea of the calculator is so easy that with little effort you can verify the results you get from the calculator by yourself. So if you have any doubts, try the values you think a characters *should* have and compare the results!"
              "\n\nWhat's not so easy, however, is to determine the value of ER. I won't dwell on just how based of a solution I found for handling ER here, but I will give a full outline for this either in the reddit post or in a document where I will note the exact logic of the program. I will upload this as soon as possible (if it's not already up). "
              "\nI will say this much: Until you have a comfortable amount of ER for characters requiring ER, it will be valued! Its relative value can be anywhere between 0 to 100% of crit, depending on exactly how far under you are from this value."
              "\nIf you are over this value, the program will ignore the EXCESS ER but not let a single % of ER you have go to waste as long as it's contributing even just for comfort purposes. "
              "\n\nThe amount of lines of code I needed to handle ER related calculations is about 20 TIMES as much as ALL other stats COMBINED."
              "\nAnd this ratio is nothing compared to the effort I had to spend on getting ER right vs all other stats combined as well. "
              "\nThere are very minor 'anomalities' that you should note - for example - 1) when ER is relevant to a character, changing the order in which you enter your echos VERY slightly affects the build score. "
              " 2) The same build entered via option 1 or 2 gets very slightly different scores. Of course, whether you're changing the order in which you enter your echos or whether you're using options 1 or 2 should be irrelevant, and it IS for characters without ER considerations - but expect VERY slight deviations in the score for characters requiring significant ER. "
              "\nI suspect the reason for the first problem is a mathematical reason that HAS to happen for this program to work. In a nutshell, even if a+b=K, a constant, (x+a)/p + (y+b)/q =/= (x+K)/p + (y/q), AND p and q themselves vary depending on whether your character needs ALL of the ER, on the echo, SOME of the ER, or NONE at all. "
              "\nFor those interested in the inner workings, this will become very clear once I post the full logic of the code. The disadvantage of not having this, however, is that my program doesn't consider ER whatsoever. I would rather have (hopefully only) insignificant deviations rather than not consider a stat that's as important as crit. "
              "\nThe reason for the second problem is similar - but the formula for why it happens differently is different. "
              "\n\nWhat this means practically for you, dear users, is that the changes due to these factors should be VERY small (<1 point difference) and shouldn't in any way affect the practicality of this tool. "
              "\nThe reason why I say 'shouldn't' instead of 'doesn't': this whole program is a one-man effort. There's just no way I can test my program thoroughly enough to say with certainty that logic errors aren't the reason for these anamolities, it's just unavoidable math stuff. "
              "\nSo - to that end, I will highly appreciate any reports and comments highlighting major anamolies or things you just find weird. Of course, any suggestions for updates, balances, options for different playstyles or teammates for characters when the requirements for your characters change, and any other suggestions and additions are highly, highly welcome! "              
              "\n\nFinally, let's try calculating an echo's worth ourselves and see if it checks out with the calculator's output. "
              "\nA max value echo for Carlotta will have the 5 highest value substats. Ranking in order of relative value, she wants crit rate, crit damage, atk%, resonance skill dmg, flat atk and ER. "
              "\nAssuming Carlotta has enough ER, she happens to have exactly 5 other substats she cares about. For characters with more or less number of viable substats, the program chooses the best 5 at most and however many they have if less than 5. "
              "\nAdding up the relative values of the 5 best Carlotta substats results in: 100+100+50+(85*0.5)+25=317.5. "
              "\nLet's say you rolled an echo with 7.5 crit rate, 15 crit damage, 10.1% attack and 9.6% resonance skill damage bonus (u freakin highroller!). So, (7.5/8.4)*100+(15/16.8)*100+(10.1/9)*50+(9.6/9)*(0.5*85)=280.016. "
              "\nSo the value of the echo should be 280.016/317.5=88.19%. The calculator output is: 88.19%. "
              "\n\nFinal notes: \nI'm a novice programer and I'm no theory crafter either. "
              "\nThis program is built as a way to translate all the hard work many creators and guides have put into something that can be used regularly with ease. "
              "\nI plan to do constant updates as new characters are released, and more and better data is found for old ones. But I also plan to do two MAJOR updates to this program. "
              "\nThe first one will be a UI update. I want my program to have a window and buttons and look more like a virtual calculator rather than one of those text based games from 1900s (nothing against them btw). "
              "\nThe second one will be a major content update - where the echo values will be adjusted to also consider and reflect good vs garbage crit ratios, equipped weapons, but also an in-built quick character guide, suggestions for further improvements, character specific comments and other stuff that I'll keep secret for now!"
              "\nTo repeat, this is a one-man effort, I can only go so far with bug-testing and getting things right. "
              "\nI'm still quite proud of this program and would like to emphasize that it's quite efficient and easy to make balance changes to this code. "
              "Adding a new character, for example, is simply a matter of basically adding 1 line of code with an array (a vector variable) consisting of numbers, most of which are 0. "
              "\nPoint being - fire away any critiques! Any feedback on any of the things mentioned above is much appreciated. Hope you enjoy using this program and keep a lookout for the next versions with hopefully an actual UI instead of just text!"
              "\n---------- ---------- ---------- ---------- ----------")
        calc_route()
    elif calc_type!="1" and calc_type!="2" and calc_type!="3":
        print("\n\nYou have picked an incorrect option. \nPlease try again. \n")
        calc_route()
    if char_stats[12]!=0:
        ver_char_er=0
        while ver_char_er!=1:
            try:
                net_er=float(input("\n---------- ---------- ---------- ---------- ----------"
                                    "\n\nEnter "+char_name+"'s Energy Regen% from the stat page."
                                    "\nMake sure you've equipped the build you're evaluating and they're on the correct weapons.\nEnergy Regen%: "))+char_stats[12]
                ver_char_er=1
            except:
                print("Error: Input is not a number. Please try again. ")
    else:
        net_er=0
    if calc_type=="1":
        echo_val=0
        for echo_no in range (0,5):
            print("\n---------- ---------- Echo "+str(echo_no+1)+" ---------- ----------")
            cur_echo_val, net_er=player_data(stat_name, stat_med, char_name, char_stats, net_er, 0)
            echo_eval(cur_echo_val, 0, 0)
            echo_val=echo_val+cur_echo_val
        echo_eval(echo_val/5, 1, 2)
    elif calc_type=="2":
        fb_val, net_er=player_data(stat_name, stat_med, char_name, char_stats, net_er, 1)
        echo_eval(fb_val, 1, 2)
    elif calc_type=="3":
        echo_val, net_er=player_data(stat_name, stat_med, char_name, char_stats, net_er, 0)
        echo_eval(echo_val, 0, 1)
    calc_route()

def game_data(char_name):
    stat_name=["Crit Rate%", "Crit Damage%", "Attack%", "Flat Attack", "HP%", "Flat HP", "Defense%", "Flat Defense", "Basic Attack Damage Bonus%", "Heavy Attack Damage Bonus%", "Resonance Skill Damage Bonus%", "Resonance Liberation Damage Bonus%", "Energy Regen%", "ER_Rel_Imp", "ER_Rel_Val"]
    stat_med=[8.4, 16.8, 9, 50, 9, 450, 11.39, 50, 9, 9, 9, 9, 10.25, 0, 0]
    if char_name=="carlotta" or char_name=="glass girl" or char_name=="small car lotta damage. wait... what?" or char_name=="in the name of the montellis." or char_name=="rin tohsaka" or char_name=="best girl":
        char_name2=["Carlotta"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0, 0.5*0.85, 0, -125, -1, 0]
    elif char_name=="jinhsi" or char_name=="madam magistrate" or char_name=="sacred light!" or char_name=="snow girl":
        char_name2=["Jinhsi", "her"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0, 0.5*0.75, 0.5*0.2, -115, -0.2/0.95, 0]
    elif char_name=="encore"  or char_name=="leave... me... alone!" or char_name=="annie" or char_name=="klee" or char_name=="maygi" or char_name=="pink gremlin":
        char_name2=["Encore (Hypercarry)", "her"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5*0.5, 0, 0.5*0.2, 0.5*0.1, -125, -1, 0]
    elif char_name=="yinlin" or char_name=="hmph... now you'll behave." or char_name=="bdsm" or char_name=="dominatrix" or char_name=="puppet girl":
        char_name2=["Yinlin", "her"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5*0.1, 0.5*0.1, 0.5*0.55, 0.5*0.2, -135, -0.2/0.95, 0]
    elif char_name=="sanhua" or char_name=="jinhsi's bodyguard" or char_name=="goth girl #3" or char_name=="goth girl 3" or char_name=="shackles begone!":
        char_name2=["Sanhua", "her"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0.5*0.3, 0.5*0.3, 0.5*0.3, 0, 0, 0]
    elif char_name=="zhezhi" or char_name=="shy girl" or char_name=="painter girl" or char_name=="art unveiled":
        char_name2=["Zhezhi", "her"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5*0.8, 0.5*0.05, 0.5*0.05, 0, -135, -1, 0]
    elif char_name=="aalto" or char_name=="cool shades" or char_name=="thanks for watching!":
        char_name2=["Aalto", "his"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5*0.50, 0, 0.5*0.25, 0.5*0.15, -135, -0.65/0.9, 0]
    elif char_name=="baizhi" or char_name=="goth girl #2" or char_name=="goth girl 2" or char_name=="verina at home" or char_name=="better than verina" or char_name=="endless reverberation.":
        char_name2=["Baizhi", "her"]
        char_stats=[0, 0, 0, 0, 1, 0.5, 0, 0, 0, 0, 0, 0, -215, -1, 0]
    elif char_name=="brant":
        print("Brant's stats are currently unavailable. Please check the next version.\n")
        calc_route()
    elif char_name=="cucumber" or char_name=="calculator" or char_name=="vergil" or char_name=="kurapika" or char_name=="kukaracha" or char_name=="calcium" or char_name=="carpaccio" or char_name=="cactus" or char_name=="calculus" or char_name=="calzone" or char_name=="misery follows!":
        char_name2=["Calcharo", "his"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5*0.25, 0, 0, 0.5*0.55, -125, -1, 0]
    elif char_name=="camellya" or char_name=="zyra" or char_name=="yuno gasai" or char_name=="yandere girl" or char_name=="she wants my seed?" or  char_name=="i can fix her" or char_name=="spin to win" or char_name=="gymnasts girl" or char_name=="i will do gymnastics with her but ancient greek style" or char_name=="struggle harder, entertain me!":
        char_name2=["Camellya", "her"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5*0.7, 0, 0, 0.5*0.15, -120, -0.15/0.85, 0]
    elif char_name=="changli" or char_name=="fox girl" or char_name=="ahri" or char_name=="nine-tailed fox" or char_name=="yae miko" or char_name=="feathers incinerate.":
        char_name2=["Changli", "her"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5*0.05, 0, 0.5*0.6, 0.5*0.25, -125, -0.25/0.9, 0]
    elif char_name=="chixia" or char_name=="amber" or char_name=="finger pistol" or char_name=="ma xiaofang" or char_name=="boom! headshot!" or char_name=="pew pew pew!" or char_name=="one shot, one kill!" or char_name=="easy peasy. lemon squeezy!" or char_name=="dakka dakka dakka dakka dakka!":
        char_name2=["Chixia", "her"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0, 0.5*0.5, 0.5*0.3, -150, -0.3/0.8, 0]
    elif char_name=="danjin" or char_name=="darkness falls...":
        char_name2=["Danjin", "her"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5*0.05, 0.5*0.25, 0.5*0.25, 0.5*0.3, 0, 0, 0]
    elif char_name=="jianxin" or char_name=="sage girl" or char_name=="small-town girl" or char_name=="universe in my psyche!":
        print("Jianxin's data is currently unavailable. Please check in later.\n")
        calc_route()
    elif char_name=="jiyan" or char_name=="dragon boy" or char_name=="teal general" or char_name=="windrider!":
        char_name2=["Jiyan", "his"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0, 0.5*0.7, 0.5*0.15, 0, -130, -1, 0]
    elif char_name=="lingyang" or char_name=="who..." or char_name=="cares." or char_name=="gaming" or char_name=="this might hurt.":
        char_name2=["Lingyang", "his"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5*0.35, 0, 0.5*0.3, 0.5*0.05, -125, -1, 0]
    elif char_name=="lumi" or char_name=="delivery girl" or char_name=="bunny girl" or char_name=="squeakie, protect the cargo!":
        char_name2=["Lumi", "her"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5*0.35, 0, 0.5*0.25, 0.5*0.3, -165, -1, 0]
    elif char_name=="mortefi" or char_name=="xingqiu" or char_name=="four-eyes" or char_name=="roy mustang" or char_name=="fuel my wrath!":
        char_name2=["Mortefi", "his"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5*0.1, 0, 0.5*0.15, 0.5*0.7, -125, -1, 0]
    elif char_name=="phoebe" or char_name=="sister" or char_name=="church girl":
        print("Phoebe's stats are unavailable right now. Please check future updates.\n")
        calc_route()
    elif char_name=="roccia" or char_name=="mamma mia!" or char_name=="pero":
        char_name2=["Roccia", "her"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5*0.05, 0.5*0.6, 0.5*0.15, 0, -135, -1, 0]
    elif char_name=="havoc rover" or char_name=="goth girl #1" or char_name=="goth girl 1" or char_name=="goth guy" or char_name=="rizzler" or char_name=="havoc mc":
        char_name2=["Havoc Rover", "their"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5*0.3, 0, 0.5*0.2, 0.5*0.25, -125, -0.25/0.75, 0]
    elif char_name=="taoqi" or char_name=="personalities" or char_name=="two reasons" or char_name=="attack is the best defense.":
        char_name2=["Taoqi", "her"]
        char_stats=[0, 0, 0, 0, 0, 0, 1, 0.5, 0, 0, 0, 0, -170, -1, 0]
    elif char_name=="the shorekeeper" or char_name=="best waifu" or char_name=="must protect" or char_name=="vow from the soul." or char_name=="in war with time." or char_name=="i engraft you new." or char_name=="astral modulation." or char_name=="ordained.":
        char_name2=["The Shorekeeper", "her"]
        char_stats=[0, 1, 0, 0, 0.5, 0.25, 0, 0, 0.5*0.1, 0, 0, 0.5*0.85, -240, -1, 0]
    elif char_name=="verina" or char_name=="flower girl" or char_name=="life is in everything.":
        char_name2=["Verina", "her"]
        char_stats=[0, 0, 1, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, -200, -1, 0]
    elif char_name=="xiangli yao" or char_name=="xiangling" or char_name=="reconfiguration!":
        char_name2=["Xiangli yao", "his"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5*0.1, 0, 0.5*0.2, 0.5*0.55, -120, -0.55/0.85, 0]
    elif char_name=="yangyang" or char_name=="coolest animations" or char_name=="tempest." or char_name=="i think she likes us":
        char_name2=["Yangyang", "her"]
        char_stats=[1, 1, 0.5, 0.25, 0, 0, 0, 0, 0.5*0.3, 0, 0.5*0.15, 0.5*0.45, 0, 0, 0]
    elif char_name=="youhu" or char_name=="you who" or char_name=="noice!":
        char_name2=["Youhu", "her"]
        char_stats=[0, 0, 1, 0.5, 0, 0, 0, 0, 0, 0, 0, 0, -165, -1, 0]
    elif char_name=="yuanwu" or char_name=="you and who" or char_name=="maximum voltage.":
        char_name2=["Yuanwu", "his"]
        char_stats=[1, 1, 0, 0, 0, 0, 0.5, 0.25, 0, 0, 0.5*0.5, 0.5*0.4, -140, -1, 0]
    elif char_name=="zani" or char_name=="that button is the real body guard":
        print("Zani stats currently unavailable. Please come back later.\n")
        calc_route()
    elif char_name=="q":  
        quit_calc()
    else:
        print ("\nCharacter not found or character name not recognized. Please try again.\nRestarting Program...\n\n")
        calc_route()
    print("\n---------- ---------- ---------- ---------- ----------\nYou have selected "+char_name2[0]+".\n---------- ---------- ---------- ---------- ----------")
    cons_er=input(char_name2[0]+" has a comfortable ER target value of "+str(-char_stats[12])+"% with a relative substat value multiplier of "+str(-char_stats[13]*100)+"%. \n"
                  "Would you like to IGNORE this character's ER requirements? Enter y for 'yes', Enter any other key for 'no'. \n"
                  "!!!WARNING!!!: Chosing to IGNORE a character's ER requirements may lead to highly inflated OR deflated ratings. \n"
                  "Whether ER requirements are present or absent, it is highly recommeneded to pick 'no' and enter any key other than 1 to continue: \n")
    if cons_er=="y":
        char_stats[12]=0
    return stat_name, stat_med, char_name2, char_stats

def quit_calc():
    pls_dont_leave=str(input("Are you sure you want to quit? (Enter y to confirm): ")).lower()
    if pls_dont_leave=="y":
        sys.exit("Thank you for using Echo Value Calculator (name subject to change). Program exiting...")
    else:
        calc_route()

def disp_char_data(stat_name, stat_med, char_name2, char_stats):
    print("\nNOTE: The character data used in this program has been highly researched by analyzing multiple sources inlcuding but not limited to: prydwen.gg, Maygi, many YouTube guides and many websites. "
          "\nWhen in doubt (or when it's hella pain), the character is made unavailable for build analysis until verified information is available. "
          "\nFor the 'damage profile' stats (basic attacks, heavy attacks, resonance skill, resonance liberation), even a 5 to 10% disagreement will have very little impact on the overall score."
          "\nHowever, feel free to report any inconsistency you feel are significant as a comment in the publishing post to improve this program. \n")
    for y in range (0, len(stat_name)-2):
        if char_stats[y]>0:
            print("The reletive value of a median roll ("+str(stat_med[y])+") of "+stat_name[y]+" for "+char_name2[0]+" is: "+str(char_stats[y]*100)+"%")
    if char_stats[12]<0:
        print("The "+stat_name[12]+" requirements for "+char_name2[0]+" are: "+str(-char_stats[12])+"% with a relative substat value multiplier of: "+str(-char_stats[13]*100)+".")
        print("The reletive value of a median roll ("+str(stat_med[12])+") of "+stat_name[12]+" is fluctuating based on complex factors, and may not be constant even during the evaluation of a single build (option 1)."
              "\nRest assured: ER is handled very carefully and apporpiately to accurately reflect its true value in the scoring system. "
              "\nFor further details, please check the original reddit post. ")
    main()

def player_data(stat_name, stat_med, char_name, char_stats, net_er, rat_typ):
    player_input=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if rat_typ==0:
        for x in range (0, len(stat_name)-2):
            if char_stats[x]>0:
                ver_stat_val=0
                while ver_stat_val!=1:
                    try:
                        player_input[x]=(float(input("Enter "+char_name+"'s "+stat_name[x]+" from echo substats: "))/stat_med[x])*char_stats[x]
                        ver_stat_val=1
                    except:
                        print("Error: Input is not a number. Please try again. ")
            elif char_stats[x]<0:
                ver_stat_val=0
                while ver_stat_val!=1:
                    try:
                        player_input[x+1]=float(input("Enter "+char_name+"'s "+stat_name[x]+" from echo substats: "))
                        ver_stat_val=1
                    except:
                        print("Error: Input is not a number. Please try again. ")
        if net_er>=0:
            if (net_er-player_input[13])<0:
                player_input[13]=player_input[13]-net_er
                player_input[12]=player_input[13]/stat_med[12]
                net_er=0
                if (player_input[13]/stat_med[12])>=1: char_stats[14]=1
                else: char_stats[14]=(player_input[13]/stat_med[12])
            else:
                net_er=net_er-player_input[13]
                char_stats[14]=0#Possibly redundant but added for fail safety.
        else:
            player_input[12]=player_input[13]/stat_med[12]
            if (-net_er/stat_med[12])>=1: char_stats[14]=1
            else:
                if (player_input[13]/stat_med[12])>=1: max_stat_val=1
                else: max_stat_val=(player_input[13]/stat_med[12])
                char_stats[14]=max(-net_er/stat_med[12], max_stat_val)
        total_stat_val=sum(player_input[:13])
        useful_stat_val=sum(heapq.nlargest(5, char_stats))
        tot_rat=(total_stat_val/useful_stat_val)*100
    else:
        for x in range (0, len(stat_name)-2):
            if char_stats[x]>0:
                ver_stat_val=0
                while ver_stat_val!=1:
                    try:
                        player_input[x]=(float(input("Enter "+char_name+"'s "+stat_name[x]+" from echo substats: "))/stat_med[x])*char_stats[x]
                        ver_stat_val=1
                    except:
                        print("Error: Input is not a number. Please try again. ")
            elif char_stats[x]<0:
                ver_stat_val=0
                while ver_stat_val!=1:
                    try:
                        player_input[x+1]=float(input("Enter "+char_name+"'s "+stat_name[x]+" from echo substats: "))
                        ver_stat_val=1
                    except:
                        print("Error: Input is not a number. Please try again. ")
        if net_er>=0:
            if (net_er-player_input[13])<0:
                player_input[13]=player_input[13]-net_er
                player_input[12]=player_input[13]/stat_med[12]
                net_er=0
                if (player_input[13]/stat_med[12])>=5: char_stats[14]=1
                else: char_stats[14]=(player_input[13]/stat_med[12])
            else:
                net_er=net_er-player_input[13]
                char_stats[14]=0#Possibly redundant but added for fail safety.
        else:
            player_input[12]=player_input[13]/stat_med[12]
            if (-net_er/stat_med[12])>=1: char_stats[14]=1
            else:
                if (player_input[13]/stat_med[12])>=1: max_stat_val=1
                else: max_stat_val=(player_input[13]/stat_med[12])
                char_stats[14]=max(-net_er/stat_med[12], max_stat_val)

        #
        
        useful_stat_val=0
        mechos=0
        useful_er=0
        while mechos<5:
            if net_er>=5:
                char_stats[14]=1
            elif useful_er>0:
                char_stats[14]=max(useful_er/5, net_er)
            useful_stat_val=useful_stat_val+sum(heapq.nlargest(5, char_stats))
            mechos=mechos+1

        #
            
        total_stat_val=sum(player_input[:13])
        useful_stat_val=sum(heapq.nlargest(5, char_stats))
        tot_rat=(total_stat_val/useful_stat_val)*100


        for x in range (0, len(stat_name)-2):
            if char_stats[x]>0:
                ver_stat_val=0
                while ver_stat_val!=1:
                    try:
                        stat_val=float(input("Enter "+char_name+"'s "+stat_name[x]+" from echo substats: "))/stat_med[x]
                        total_stat_val=total_stat_val+(char_stats[x]*stat_val)
                        ver_stat_val=1
                    except:
                        print("Error - Input is not a number. Please try again. ")
            elif char_stats[x]<0:
                ver_stat_val=0
                while ver_stat_val!=1:
                    try:
                        stat_er=float(input("Enter "+char_name+"'s "+stat_name[x]+" from echo substats: "))
                        ver_stat_val=1
                    except:
                        print("Error - Input is not a number. Please try again. ")
                if net_er>=0:
                    if net_er-stat_val<0:
                        stat_val=stat_val-net_er
                        total_stat_val=total_stat_val+(stat_val/stat_med[x])
                        net_er=0
                        #If this rel_er_val is >= 5, 5 points
                        #Else Same points as itself
                    else:
                        net_er=net_er-stat_val#redundant
                        #0 points
                else:
                    total_stat_val=totat_stat_val+(stat_val/stat_med[x])
                    if (-net_er/stat_med[x])>=5:
                        #5 points
                    else:
                        if (stat_val/stat_med[x])>=5: max_stat_val=5
                        else: max_stat_val=stat_val/stat_med[x]
                        #Points based on max of max_stat_val and -net_er/stat_med[x]
 
                        
                        

    return tot_rat, net_er


def echo_eval(echo_val, eval_type, anal_type):
    eval_ui=["Echo", "Build"]
    print("\n\nYour "+eval_ui[eval_type]+" rating is: "+str(echo_val))
    if echo_val>=99:
        print("\nThis "+eval_ui[eval_type]+" falls in the 'Godly' tier.")
    elif echo_val>=88:
        print("\nThis "+eval_ui[eval_type]+" falls in the 'Extreme' tier.")
    elif echo_val>=77:
        print("\nThis "+eval_ui[eval_type]+" falls in the 'High Investment' tier.")
    elif echo_val>=66:
        print("\nThis "+eval_ui[eval_type]+" falls in the 'Well Built' tier.")
    elif echo_val>=55:
        print("\nThis "+eval_ui[eval_type]+" falls in the 'Decent' tier.")
    elif echo_val>=44:
        print("\nThis "+eval_ui[eval_type]+" falls in the 'Base Level' tier.")
    else:
        print("\nThis "+eval_ui[eval_type]+" falls in the 'Unbuit' tier.")
    if anal_type==1:
        if echo_val>=99:
            print("\nOne of the rarest echos. Impractically close to perfect, if not - quite literally perfect. Whitebeard was right afterall... "
                  "\nDelete it immedietly. \n.\n.\n.(Please don't do that it's a joke!) "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val>=88:
            print("\nPractically perfect piece. Congratulations! "
                  "More than just time and effort are required, however, to reach the next category. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val>=77:
            print("\nHigh value piece. Usually only found on builds with lots of dedicated investment. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val>=66:
            print("\nVery solid piece. Recommended to find upgrades for other pieces before trying to find upgrades for this. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val>=55:
            print("\nFine piece. Recommended to find upgrades to other pieces if the goal is to make this character 'ToA-ready'. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val>=44:
            print("\nPassable piece. Good enough until your character is at lvl 80/80, weapon at level 90/90, and relevant talents are at level 8. "
                  "\n---------- ---------- ---------- ---------- ----------")
        else:
            print("\nDiscardable piece. C'mon man have some ambition. "
                  "\n---------- ---------- ---------- ---------- ----------")
    elif anal_type==2:
        if echo_val>=99:
            print("\nYou have entered stats incorrectly. \nThe alternative is that you've actually found a build so perfect - posting this on reddit will lead to the birth of a new religion. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val>=88:
            print("\nYou've shown extreme levels of dedication for this character build. \nIt'll most likely place you very high even on global leaderboards, if we had them. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val>=77:
            print("\nYou've given this build special treatment, or it has given special treatment to you. \nYou'll find clearing ToA easy even WITH skill issues. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val>=66:
            print("\nYour build is looking great! Now is a good time to move on to the next character. \nIf you're having difficulty to get 30/30 in ToA, this character build is certainly not an issue whatsoever. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val>=55:
            print("\nYour character is 'ToA ready'. \nGiven that the rest of the teammates are at or above this level, getting 30/30 should be achievable with enough skill and attempts. \nHighly recommended to get your character talens, levels, weapons and any other guaranteed upgrades at max level (if not, as high as possible) before continuing to improve your echos. "
                  "\n---------- ---------- ---------- ---------- ----------")
        elif echo_val>=44:
            print("\nA passable build that will work great until you bring your character to level 80/80, talents to level 8, and weapon to level 90."
                  "\n---------- ---------- ---------- ---------- ----------")
        else:
            print("\nUnacceptable build. Highly recommended to find better pieces immedietly if you want to build this character. "
                  "\n---------- ---------- ---------- ---------- ----------")

def main():
    print("\n========== ========== ========== ========== =========="
          "\n\nWelcome to the Echo Value Calculator (name subject to change) v1.00.250125")
    calc_route()

main()

"""total_stat_val=0
    if rat_typ==0:
        for x in range (0, len(stat_name)-1):
            if char_stats[x]>0:
                ver_stat_val=0
                while ver_stat_val!=1:
                    try:
                        stat_val=float(input("Enter "+char_name+"'s "+stat_name[x]+" from echo substats: "))/stat_med[x]
                        total_stat_val=total_stat_val+(char_stats[x]*stat_val)
                        ver_stat_val=1
                    except:
                        print("Error: Input is not a number. Please try again. ")
            elif char_stats[x]<0:
                ver_stat_val=0
                while ver_stat_val!=1:
                    try:
                        stat_val=float(input("Enter "+char_name+"'s "+stat_name[x]+" from echo substats: "))
                        ver_stat_val=1
                    except:
                        print("Error: Input is not a number. Please try again. ")
                if char_er/stat_med[x]<=-1:
                    char_stats[13]=1
                    total_stat_val=total_stat_val+(stat_val/stat_med[x])
                elif char_er/stat_med[x]<0:
                    char_stats[13]=max(stat_val/stat_med[x], -(char_er/stat_med[x]))
                    total_stat_val=total_stat_val+(stat_val/stat_med[x])
                elif char_er/stat_med[x]==0:
                    if stat_val/stat_med[x]>=1:
                        char_stats[13]=1
                    else:
                        char_stats[13]=stat_val/stat_med[x]
                    total_stat_val=total_stat_val+(stat_val/stat_med[x])
                else:
                    char_er=char_er-stat_val
                    if char_er<0:
                        char_stats[13]=-(char_er/stat_med[x])
                        total_stat_val=total_stat_val-(char_er/stat_med[x])
                        char_er=0
        useful_stat_val=sum(heapq.nlargest(5, char_stats))
        tot_rat=(total_stat_val/useful_stat_val)*100

    else:
        case1=0
        for x in range (0, len(stat_name)-1):
            if char_stats[x]>0:
                ver_stat_val=0
                while ver_stat_val!=1:
                    try:
                        stat_val=float(input("Enter "+char_name+"'s "+stat_name[x]+" from echo substats: "))/stat_med[x]
                        total_stat_val=total_stat_val+(char_stats[x]*stat_val)
                        ver_stat_val=1
                    except:
                        print("Error - Input is not a number. Please try again. ")
            elif char_stats[x]<0:
                ver_stat_val=0
                while ver_stat_val!=1:
                    try:
                        stat_er=float(input("Enter "+char_name+"'s "+stat_name[x]+" from echo substats: "))
                        ver_stat_val=1
                    except:
                        print("Error - Input is not a number. Please try again. ")
                if char_er/stat_med[x]<=-5:
                    total_stat_val=total_stat_val+(stat_er/stat_med[x])
                    case1=1
                elif char_er/stat_med[x]<0:
                    total_stat_val=total_stat_val+(stat_er/stat_med[x])
                    case1=2
                elif char_er/stat_med[x]==0:
                    total_stat_val=total_stat_val+(stat_er/stat_med[x])
                    case1=3
                else:
                    char_er=char_er-stat_er
                    if char_er<0:
                        stat_er=-char_er
                        total_stat_val=total_stat_val+stat_er/stat_med[x]
                        char_er=0
                        case1=3
                    else:
                        case1=0
        if case1==0:
            useful_stat_val=5*sum(heapq.nlargest(5, char_stats))
        elif case1==1:
            useful_stat_val=5+(sum(heapq.nlargest(4, char_stats))*5)
        elif case1==2:
            useful_stat_val=0
            mechos=0
            er_bank=max(stat_er/stat_med[8], -(char_er/stat_med[8]))
            while er_bank>=1 and mechos<5:
                char_stats[13]=1
                useful_stat_val=useful_stat_val+sum(heapq.nlargest(5, char_stats))
                mechos=mechos+1
                er_bank=er_bank-1
            if mechos<5:
                char_stats[13]=er_bank
                useful_stat_val=useful_stat_val+sum(heapq.nlargest(5, char_stats))
                mechos=mechos+1
                char_stats[13]=0
            while mechos<5:
                useful_stat_value=useful_stat_val+sum(heapq.nlargest(5, char_stats))
                mechos=mechos+1
        elif case1==3:
            useful_stat_val=0
            mechos=0
            er_bank=stat_er/stat_med[8]
            while er_bank>=1 and mechos<5:
                char_stats[13]=1
                useful_stat_val=useful_stat_val+sum(heapq.nlargest(5, char_stats))
                mechos=mechos+1
                er_bank=er_bank-1
            if mechos<5:
                char_stats[13]=er_bank
                useful_stat_val=useful_stat_val+sum(heapq.nlargest(5, char_stats))
                mechos=mechos+1
                char_stats[13]=0
            while mechos<5:
                useful_stat_val=useful_stat_val+sum(heapq.nlargest(5, char_stats))
                mechos=mechos+1
        tot_rat=(total_stat_val/useful_stat_val)*100
"""

