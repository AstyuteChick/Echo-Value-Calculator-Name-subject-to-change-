# Echo-Value-Calculator-Name-subject-to-change-


A software that calculates the value of your echos and builds in Wuthering Waves.


Reddit Post:

Download Link [once you open the webpage, click on code - download zip - extract it anywhere you want and run the exe]: Echo Value Calculator (Name Subject to Change)


FEATURES:

1. Put a number on your Echos and Builds
2. Get an analysis for your Echos and Builds
3. The program fairly values and considers all your character's specific and relevant stats, including ER!
4.  Includes all the characters upto and including Roccia, with the exception of Jianxin.


How it works:

There are two processes that comprise this program:
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

From the above mentioned method, if you guessed that it's possible to score above 100, you'd be right! 

But I highly doubt even 1% of the player-base will reach Extreme builds. And while I'm of the "never say never" mindset - there's just no chance even a single player reaches that "Godly" bracket. A singular echo - MAYBE... But a full build? Nope. Not happening. Good luck tho. 


Future Plans: 

The version has a clear meaning. The first number represents a Major update. The next two represent the number of minor changes and updates, and the last 6 represent the date of the update.
Minor changes will help keep the program up to date with the newest character releases, new found data and discoveries, bug-fixes and things of that nature.
Major updates are the long-term future goals for this program. They include major changes in the code's engine, looks and functionality, and scope. For version 3, for example, I aim to graduate from this text-based look to a proper interactive GUI with windows and buttons and color and convenience and a LOT of QoL etc. For version 4, I plan to do a major content update - with the whole program acting more closer to a full fledged WuWa guide with interactive thoughts and advice for specific characters, adjusting your echo-scores by factoring in stuff like your crit ratio, weapon rarity, echo setup (ele-ele or ele-atk, or 44111?) and more that I will keep secret for now. 


Special Thanks to: Maygi (u/Maygii on reddit, Maygi on YouTube) and prydwen.gg

Maygi: This program would quite literally be IMPOSSIBLE without her mathematical guides. The reason: Gains from median substat rolls - bar graphs! Studying her data made me realize that there's a generic pattern to the relative value of substats for a general atk scaling character: on a scale where an avg crit roll increases your dmg by 1, atk% will do so by 0.5, flat atk by 0.25 and, here's the main part I discovered, the basic/heavy/skill/liberation bonus% will increase your damage on this scale by 0.5*(ratio of this type of damage to overall damage) (or maybe even more accurately: relative value of atk% * ratio of damage type in damage profile). Confirming that last part with a high degree of accuracy using Maygi's amazing guides on reddit and youtube, and cross-checking them with countless other sources made me confident that this program would at least be practical. I highly recommend checking her content out - even if you're not into the mathy stuff. Very entertaining and educational guides! https://www.youtube.com/@Maygi

Prydwen.gg : I just have to applaud their commitment to making up-to-date guides, providing info in a easy to consume manner, representing their data beautifully and just a 10/10 presentation. There's only so much research I can do under the guise of procrastination - and without Prydwen.gg , I'm not sure how long much longer I would have taken to finish the first version of this program - if ever!
Additionally: I also want to acknowledge that I went through a LOT of other guides and websites and videos as well to do my due diligence and make sure mains of any and all characters are happy with the program.


Final Notes:

I'm especially proud of how my program handles ER requirements in such a thorough way. For example, it handles it differently for Carlotta (and characters who rely on Liberation being up for most of their damage - other examples: Jiyan, Zhezhi), Jinhsi (and characters who aren't reliant on liberation to deal damage but having it up means free damage - other examples, Yinlin, Camellya) and Sanhua (and characters who either have no ER requirements or don't rely on their burst in any substantial way - other examples: Danjin, Yangyang). 
And it isn't limited to these cases. Any other weird cases (like characters who do rely on their burst for optimal rotations but don't have ER requirements anyway because of low ER costs, and any character specific cases you can think of) are also handled appropiately (unless there is a lack of knowledge about the character on my part).
Thanks for reading all the way. Any and all feedback on reddit and github is much appreciated!
