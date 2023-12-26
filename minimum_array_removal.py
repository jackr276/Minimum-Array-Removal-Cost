"""
Jack Robbins
Minimum Array Removal
"""


def reductionCost(startInd, endInd, num):
    #base condition
    if startInd >= endInd:
        return 0
    
    #super high starting point
    cost = 10000000000000
    
    for k in range(startInd, endInd):

        #left hand side problem
        left_cost = reductionCost(startInd, k, num)

        #right hand side problem
        right_cost = reductionCost(k+1, endInd, num)

        cost = min(cost, right_cost + left_cost + computeCost(num, startInd, endInd))
    
    return cost

def computeCost(num, i, j):
    cost = 0
    for k in range(i, j+1):
        cost += num[k]

    return cost

def main():
    num = [1, 2, 3]
    print(reductionCost(0, len(num)-1, num))


if __name__ == '__main__':
    main()