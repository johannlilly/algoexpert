# basic solution
# O(n²) time | O(1) space
def twoNumberSum(array, targetSum):
    # Write your code here.
    results = []

    # iterate over dictionary
    for x in array:
        for y in array:
            if array.index(x) != array.index(y):
                if x + y == targetSum:
                    if x not in results:
                        results.append(x)
                    if y not in results:
                        results.append(y)

    return(results)
    
    pass
