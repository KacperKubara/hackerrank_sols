#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores.append(0)
    scores_set = list(set(scores))
    scores_set = sorted(scores_set, reverse = True)


    for score_alice in alice:
        if score_alice > scores_set[0]:
            result.append(1)
        if score_alice < scores_set[-1] :
            result.append(len(scores_set))   

        for i in range(0, len(scores_set)-1):
            if  score_alice == scores_set[i]:
                result.append(i+1)
            if  score_alice < scores_set[i] and score_alice > scores_set[i+1]:
                result.append(i+2) 
    return result

if __name__ == '__main__':
    scores = [100, 100, 50, 40, 40, 20, 10]
    alice  = [5, 25, 50, 120]
    result = climbingLeaderboard(scores, alice)
    print(result)

