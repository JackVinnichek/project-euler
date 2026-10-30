def main():
    with open("input54.txt") as f:
        p1_wins = 0
        p2_wins = 0
        lines = f.read().splitlines()
        for line in lines:
            values = line.split(" ")
            p1 = values[0:5]
            p2 = values[5:10]
            p1_rank = check(p1)
            p2_rank = check(p2)
            
            if p1_rank[0] > p2_rank[0]:
                p1_wins += 1
            elif p1_rank[0] < p2_rank[0]:
                p2_wins += 1
            if p1_rank[0] == p2_rank[0]:
                if p1_rank[1] > p2_rank[1]:
                    p1_wins += 1
                elif p1_rank[1] < p2_rank[1]:
                    p2_wins+=1
                else:
                    if tieBraker(p1,p2,p1_rank,p2_rank):
                        p1_wins += 1
        print(p1_wins)
            


def check(p):
    map_hands = {"Pair": 0, "Two Pairs": 0, "Three Kind": 0, "Straight": 0, "Flush":0, "Full House": 0, "Four Kind" : 0, "Straight Flush": 0}
    pair_val = pair(p)
    if pair_val != 0 :
        map_hands['Pair'] = pair_val
    is_flush = flush(p)
    if is_flush:
        map_hands['Flush'] = 1
    if pair_val != 0:
        two_pair_val = two_pair(p,pair_val)
        if two_pair_val != 0:
            map_hands["Two Pairs"] = pair_val
        three_four_val = three_or_four(p)
        if three_four_val[1] == 'T':
            map_hands['Three Kind'] = three_four_val[0]
        elif three_four_val[1] == 'F':
            map_hands['Four Kind'] = three_four_val[0]
        
        full_house_val = full_house(two_pair_val,three_four_val)
        if full_house_val != 0:
            map_hands['Full House'] = full_house_val
    else:
        straight_val = straight(p)
        if straight_val != 0:
            if is_flush == True:
                map_hands["Straight Flush"] = straight_val
            else:
                map_hands["Straight"] = straight_val
    rank = 0
    rank_val = 0
    for i, (name, val) in enumerate(map_hands.items()):
        if val != 0:
            rank = i + 1
            rank_val = val
    return (rank, rank_val)
        
def tieBraker(p1,p2,p1_rank,p2_rank):
    rank = p1_rank[0]
    if rank in {0,5}:
        return compare_high(p1,p2,[])
    elif rank in {1,3,7}:
        return compare_high(p1,p2,[p1_rank[1]])
    elif rank == 2:
        high = p1_rank[1]
        low_p1 = two_pair(p1,high)
        low_p2 = two_pair(p2,high)
        if low_p1 != low_p2:
            return low_p1 > low_p2
        return compare_high(p1,p2,[high,low_p1])
    return False

def compare_high(p1, p2, skip):
    h1 = highCard(p1, skip)
    h2 = highCard(p2, skip)

    if h1 > h2:            # base case: P1 wins
        return True
    if h1 < h2:            # base case: P2 wins
        return False
    if h1 == 0:            # base case: no cards left, so a full tie
        return False

    return compare_high(p1, p2, skip + [h1])   # recursive step

def highCard(p,skip):
    map_values = {'T':10,'J':11,'Q':12,'K':13,'A':14}
    high = 0
    for card in p:
        num = card[0]
        if num in ['T','J','Q','K','A']:
            num = map_values[num]
        num = int(num)
        if num > high and num not in skip:
            high = num
    return high




    


def pair(p):
    map_values = {'T':10,'J':11,'Q':12,'K':13,'A':14}
    p_nums = []
    has_pair_highest = 0
    for card in p:
        num = card[0]
        if num in ['T','J','Q','K','A']:
            num = map_values[num]
        num = int(num)
        if num not in p_nums:
            p_nums.append(num)
        else:
            if num > has_pair_highest:
                has_pair_highest = num
            
    return has_pair_highest

def two_pair(p,pair):
    map_values = {'T':10,'J':11,'Q':12,'K':13,'A':14}
    p_nums = []
    has_2nd_pair = 0
    for card in p:
        num = card[0]
        if num in ['T','J','Q','K','A']:
            num = map_values[num]
        num = int(num)
        if num == pair:
            continue  
        if num not in p_nums:
            p_nums.append(num)
        else:
            if num > has_2nd_pair:
                has_2nd_pair  = num
            
    return has_2nd_pair 
    
def three_or_four(p):
    map_values = {'T':10,'J':11,'Q':12,'K':13,'A':14}
    counts = {}
    for card in p:
        num = card[0]
        if num in ['T','J','Q','K','A']:
            num = map_values[num]
        num = int(num)
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for num, count in counts.items():  
        if counts[num] == 3:
            return (num,'T')
        elif counts[num] == 4:
            return(num,'F')
        
    return (0,'0')

def straight(p):
    map_values = {'T':10,'J':11,'Q':12,'K':13,'A':14}
    nums = []
    for card in p:
        num = card[0]
        if num in ['T','J','Q','K','A']:
            num = map_values[num]
        num = int(num)
        nums.append(num)
    nums.sort()
    if nums[4] - nums[0] == 4:
        return nums[-1]
    return 0

def flush(p):
    suit = p[0][1]
    for card in p:
        if card[1] != suit:
            return False
    return True

def full_house(two_pair,three_or_four):
    if three_or_four[1] == 'T':
        if two_pair != 0:
            return three_or_four[0]
    return 0

        


    






        
     
main()

            