This repository is the resul of a fork command which was executed on a distant-friend's repo. I try to play around with the code and data for a better understanding of the system.

____________________________________________________________________________


Learning to Rank. 

Run it as python learning_to_rank.py

The filename to be be executed is learning_to_rank.py. It does the processing for all folder, runs the test set on all folders and reports the accuracy at the end. The optimal C value has been chosen for each of the folders and has been given in the code.
The C values for each folder correspondingly are 0.04, 8.3 and 0.003

The output looks like,

Folder name is 1

Accuracy of the ranker is  92.6952141058
Accuracy obtained at C =  0.04

Ten most important weights for this folder
feature 23  -  1.40047264106
feature 39  -  1.03949988762
feature 21  -  0.664914678321
feature 37  -  0.470876150788
feature 18  -  -0.411570908321
feature 41  -  0.405503874386
feature 19  -  0.401731727938
feature 28  -  0.349758142295
feature 25  -  0.325244041902
feature 32  -  0.308775368526
______________________________________________________________________________

Folder name is 2

Accuracy of the ranker is  83.5443037975
Accuracy obtained at C =  8.3

Ten most important weights for this folder
feature 15  -  -6.10639586165
feature 11  -  5.78106213255
feature 23  -  5.04276395363
feature 12  -  4.20689093196
feature 2  -  -4.02617990083
feature 1  -  -3.39062305623
feature 14  -  -3.35920738346
feature 34  -  2.54708139356
feature 5  -  2.27835167863
feature 32  -  2.05410363495
______________________________________________________________________________

Folder name is 3

Accuracy of the ranker is  87.8281622912
Accuracy obtained at C =  0.003

Ten most important weights for this folder
feature 23  -  0.452833588959
feature 39  -  0.420800644497
feature 21  -  0.311391171259
feature 37  -  0.300828012578
feature 18  -  -0.197934130512
feature 25  -  0.191275081913
feature 42  -  0.18453302379
feature 38  -  0.1814762876
feature 46  -  -0.173898893559
feature 41  -  0.172284483315
______________________________________________________________________________
