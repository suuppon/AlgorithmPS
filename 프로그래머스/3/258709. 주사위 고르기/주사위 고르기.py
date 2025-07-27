from itertools import combinations

def calc_score_comb(dice):
    from copy import deepcopy
    n = len(dice)
    idx_list = [0] * n
    score_list = []

    while True:
        score = sum(dice[i][idx_list[i]] for i in range(n))
        score_list.append(score)

        for i in reversed(range(n)):
            if idx_list[i] < 5:
                idx_list[i] += 1
                break
            else:
                idx_list[i] = 0
        else:
            break 

    return score_list
            
def calc_win(a_score_list, b_score_list):
    a_score_list.sort()
    b_score_list.sort()

    a_win = 0
    b_idx = 0

    for a in a_score_list:
        while b_idx < len(b_score_list) and b_score_list[b_idx] < a:
            b_idx += 1
        a_win += b_idx

    return a_win
    

def solution(dice):
    answer = []
    n = len(dice)
    dice_dict = {i+1: dice[i] for i in range(n)}
    
    combination = combinations(range(n), n//2)
    maximum = 0
    
    for comb in combination:
        dice_list_a = [dice_dict[c+1] for c in comb]
        dice_list_b = [dice_dict[c+1] for c in range(n) if c not in comb]
        
        a_score_list = calc_score_comb(dice_list_a)
        b_score_list = calc_score_comb(dice_list_b)
        
        a_win = calc_win(a_score_list, b_score_list)
        if maximum <= a_win:
            target = comb
            maximum = a_win
            
    for elt in target:
        answer.append(elt+1)
        
    answer.sort()
    
    return answer
