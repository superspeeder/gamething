ExampleArea = """
First hand description: You have entered a small clearing in this darkened forest. There are a few rotted stumps and fallen trees along the edges.

Perception:
1-3: You see a mushroom and decide that it is edible so you eat it. You are now sick and lose [calc 4 - $diceroll] hp per turn and cannot fight, walk, or see. {ApplyDiasese mushroom-sickness lvl $diceroll}
4-10: You see nothing.
11-16: You see the slight remnents of a path, but become distracted by the local wildlife and are unable to see it. (Continue if $diceroll > 14 #->) You remember that the path was winding towards the east.
17-19: You are able to see most of the path and discover that it leaves the clearing to the southeast.
20: You see the path so clearly you are suprised nobody else had noticed it yet. You are able to help everyone follow the path if you so choose.

Map:
!Key -
~| # = Forest
~| % = Grass
~| _ = Path
~| + = Hidden Treasure
~| @ = Treasure Tree
!Map -
#############################
##########%%#######@#########
####%%%%%%%%###%%#%##%%##%###
##%%%%%%%%%%%%%%%%%%%%%%%%%##
##%%%%%%%%%%%%%%+%%%%%%%%%%%#
#__________%%%%%%%%%%%%%%%%%#
#%%%%%%%%%__%%%%%%%%%%%%%%%%#
#%%%%%%%%%%__%%%%%%%%%%%%%%%#
#%%%%%%%%%%%___________%%%%##
####%%%%%%%%%%%%%%%%%%____###
###########%%%%%%%%%%%%%_____
####################%%%%%####
#############################

Treasure:
-tree:
~| 1-3 = Nothing
~| 
"""
