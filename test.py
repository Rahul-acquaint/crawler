from typing import List

def combinationSum(list:List[int], target:int) -> List:

    output, cur, n=[], [], len(list)
    list.sort()


    def backtracking(i, target):

        if target == 0 :
            output.append(cur.copy())
            return
        if i == 0 or target < 0 : return 

        output.append()
    
    return output





arr, target=[10,1,2,7,6,1,5], 8
combinationSum(arr, target)