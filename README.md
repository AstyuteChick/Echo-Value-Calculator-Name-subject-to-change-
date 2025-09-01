# Echo-Value-Calculator-Name-subject-to-change-


A tool that determines the worth of your echoes and Echo-sets (builds) of your characters in Wuthering Waves.


FEATURES:

1. Put a number on your Echos and Builds
2. Get an analysis for your Echos and Builds
3. The program fairly values and considers all your character's specific and relevant stats, including ER!
4.  Includes all the characters upto and including Roccia, with the exception of Jianxin.
5.  It is extremely simple and quick to use. 


How it works:

There are two processes:
1. Echo Value Calculator: This puts a number on your Echos/Builds. For a lack of a better term, this is a "scientific" process. There is an objective and concrete reason why it gives the scores it does to your character's build/echos. The base theory used for this scale is so simple that you'll easily be able to reproduce the results of this program by yourself. 
The scoring system is a scale where an echo that has the 5 best substats a character can have (or less if the character has less than 5 useful substats), when rolled at exactly median values (not actually possible - a theoretical system), scores 100 points. The stat values are RELATIVE to other stats, in the sense that if the median value of a substat (say, 9% Atk) increases your damage half as much as the median value of another substat (8.4% crit rate), then it'll also be valued at half the amount. To check the relative values of substats for the character of your choosing, please pick Option 6 in the program. 
The above paragraph on its own provides almost all the things to start calculating. With ER, while the theory again is simple, actually applying it to the calculator was difficult but it does this correctly and accurately (at least from my, albeit small-scale, testing). For a more detailed explanation and example calculations, please pick option 4 in the program to get a full walkthrough for how to calculate the value for an Echo/Build for Carlotta. For the FULL theory, mathematics and logic of the program, I will be posting a document covering all of those aspects in detail very soon.
2. Echo Value Analyzer: This analyzes the ratings your echos/build has gotten. This is a much more empirical process (Ik technically being empirical has nothing to do with being or not being scientific). This means that what the program actually thinks of your program is to be taken with a HUGE grain of salt. I've tried my best to verify if the ranking system makes sense, and I'm convinced it's spot on - but I'm short on data. I will keep making this (and every other) part of the program better and better in the coming versions. 


Here is the rating bracket: 

[0<=Score<44]: Unbuilt character.

[44<=Score<55]: Base-Level Build

[55<=Score<66]:  Decent Build

[66<=Score<77]: Well-Built Character

[77<=Score<88]: High-Investment Build

[88<=Score<99]: Extreme Build

[Score>=99]: Godly Build


Special Thanks to: Maygi (u/Maygii on reddit, Maygi on YouTube) and prydwen.gg

Maygi: This program's concept would not be possible without her mathematical guides for one main reason: Gains from median substat rolls is the key missing piece that prevented me from attempting a program like this for Wuwa. Her data made me realize that there's a generic pattern to the relative value of substats for a general (atk scaling, in this example) character: on a scale where an avg crit roll increases your dmg by 1, atk% will do so by 0.5, flat atk by 0.25 and the basic/heavy/skill/liberation bonus% will increase your damage on this scale by 0.5*(ratio of this type of damage to overall damage) (or maybe even more accurately: relative value of atk% * ratio of damage type in damage profile). Confirming that last part with a high degree of accuracy using Maygi's amazing guides on reddit and youtube, and cross-checking them with countless other sources made me confident that this program, if made carefully, would at the very least be practical, if not really powerful. I highly recommend checking her content out - even if you're not into the mathy stuff. Very entertaining and educational guides! https://www.youtube.com/@Maygi

Prydwen.gg : Their commitment to making up-to-date guides makes it so much easier to do any project like this. 


Final Notes:

Imo, the lowest expectation when creating a tool like this is that I myself find the tool useful and satisfying.
The useful part is obvious to me: I have constantly used this tool, not only to test and refine it to make sure it behaves as expected in accordance with the theory for any type of characters possible, but also practically in the situations where it is meant to be used in the first place. I use it constantly to determine if my characters are built, or what characters to improve by finding out the build score, or gauge how strong my characters are, and compare that prediction practically in combat zones like ToA. I use it to determine who are my weakest characters, and what are their weakest echoes. I use it to set personal goals: when I have multiple characters to build, I build one up to a "well" build (a build score of 66 and above), move on to the next, and then come back to improve the target build score if I want in a prioritized way, for example. Saving huge amounts of time and waveplates that would otherwise be wasted being stuck on a single character, chasing a random build strength that's never good enough once I reach it (because you can't even tell if you reached it until you've spent too much), which would inturn reduce how many different characters and teams I get to experience. 
The satisfaction part is also obvious: it makes Echo strength obvious. Before, it used to really bother me that I couldn't simply guage Echo's worth by counting substats due to the complexity in WuWa's stats and rolls compared to other games like Genshin. Another point of satisfaction is knowing that the Echo scores produced are accurate. Knowing the test cases and scenarios, I am confident that EVC fairly and justly evaluates the stats according to the theory in any scenario. After all, what's the point of a calculator if you can't trust the number it outputs! 
