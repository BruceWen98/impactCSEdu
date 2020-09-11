import itertools
def impact_cs_edu(D, array_of_tuples):
    costs = []
    for tup in array_of_tuples:
        costs.append(tup[0])
    cost_combinations = []
    for L in range(0, len(costs)+1):
        for subset in itertools.combinations(costs, L):
            cost_combinations.append(subset)

    valid_cost_combinations = list(filter(lambda tup: sum(list(tup)) <= D, cost_combinations))

    def impactOfCombination (combination):
        impact = 0
        array = array_of_tuples.copy()
        for cost in list(combination):
            for elem in array:
                if cost == elem[0]: 
                    impact += elem[1]
                    array.remove(elem)
        return impact

    impacts = list(map(impactOfCombination, valid_cost_combinations))
    return(max(impacts))

# Test inputs here
test_array = [(1,2),(1,3),(5,4),(1.2,3.8),(10,11.2),(7.5,8),(11,12)]
D = 10
test_array2 = [(50,60),(40,110),(100,160)]
D2 = 100
print(impact_cs_edu(D2,test_array2))