"""
Jack Robbins
Minimum Array Removal
"""

"""
Split the array in half at every index, adding the respective costs up
"""
def reductionCost(startInd, endInd, num):
    #base condition
    if startInd >= endInd:
        return 0
    
    #super high starting point
    cost = 10000000000000
    
    for k in range(startInd, endInd):
        #Here, k is the index of the value that will be left over
        #we are computing the cost each time if you had "k" as the last element

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