from operator import itemgetter
wCount = {} #dictionary

sentence = '''With a strong priority move, fantastic 120 base stats across the board, and a wide array of coverage moves, Arceus-Normal makes for an effective late-game sweeper that can easily set up and sweep once its checks and counters have been weakened. However, a huge part of Arceus-Normal's viability also comes from its ability to serve as a very strong revenge killer for its team, taking out weakened offensive threats with its Life Orb Extreme Speed. Arceus-Normal also pairs well with other offensive behemoths such as Primal Groudon, Xerneas, Darkrai, and Mega Salamence, easing its ability to fit onto offensive teams. Arceus-Normal fares well against a variety of offensive threats due to having a strong priority move in Extreme Speed and various coverage options. Arceus-Normal also appreciates the decline of Will-O-Wisp Support Arceus, non-Primal Groudon, and Landorus-T in the generation transition, competent checks in XY. However, a new check in Mega Salamence has been introduced, and old checks such as Mega Gengar are still troublesome.
 
Swords Dance grants Arceus-Normal the ability to double its Attack, allowing it to OHKO various Pokemon such as Mewtwo and offensive Yveltal with little or no prior damage. Extreme Speed allows Arceus-Normal to bypass Speed tiers and Choice Scarf users, and it can and should be used to revenge kill offensive Pokemon such as Darkrai, Xerneas, Mega Mewtwo Y, and Blaziken once they have been even slightly weakened. Earthquake should be used to break through Primal Groudon as well as Steel- and Rock-types, namely Dialga, Arceus-Rock, and Mega Diancie, while Shadow Claw is used to break through Lugia and Ghost-types, namely Arceus-Ghost and Giratina-O. Stone Edge is an equally viable alternate option to Shadow Claw that hit Lugia, defensive Yveltal, Mega Salamence and Ho-Oh with one moveslot.
 
Various other coverage moves can be used in lieu of Shadow Claw or Stone Edge. Ice Beam takes out Mega Salamence after Stealth Rock, OHKOes the albeit rare Landorus-T, and can also 2HKO support Groudon. Overheat or Fire Blast can be used to blow Ferrothorn and Mega Scizor away, with Fire Blast also 2HKOing support Groudon thanks to Drought. Lastly, Shadow Force can be used to OHKO Arceus-Ghost and Giratina-O as well as block Defog, but bear in mind it is easy for the opponent to switch in something that resists or is immune to Ghost during the charge turn, and Lugia is also given a free turn to Roost back to full health and reactivate Multiscale.'''

sentence = sentence.strip().lower()
words = sentence.split()
for w in words:
    if  w in wCount:
       wCount[w] = wCount[w] + 1
    else:
       wCount[w] = 1

#print wCount.items()
#s_list = sorted(wCount.items(), key=lambda t: t[1], reverse = True)
s_list = sorted(wCount.items(),key=itemgetter(1), reverse = True)
for word,count in s_list:
    print ("%-15s %d" % (word, count))