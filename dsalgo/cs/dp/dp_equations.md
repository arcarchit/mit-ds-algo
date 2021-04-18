#### Subset Sum Problem

Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Example:

```
Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.
```

Equations:
```
isSubsetSum(set, n, sum) = isSubsetSum(set, n-1, sum) || 
                           isSubsetSum(set, n-1, sum-set[n-1])
Base Cases:
isSubsetSum(set, n, sum) = false, if sum > 0 and n == 0
isSubsetSum(set, n, sum) = true, if sum == 0 
```

Key Learning : 
1. DP is not always about sequence, you can do subset by excluding and including elements.
2. DP is not always about multiplying sub problems or taking maximum of subproblem. Logical OR is also fine for binary answers. 
3. Always do the memoization first and then convert it into bottom up.
4. Also if you look at the implementation, choice of taking a candidate or not does not require to create multiple sets. We can use inclusion/exclusion of last element by array length.
4. This is NP-complete problem (like knapsack) and does not have polynomial time complexity. 

####Optimal Strategy for a Game

Problem statement: Consider a row of n coins of values v1 . . . vn, where n is even. We play a game against an opponent by alternating turns. In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin. Determine the maximum possible amount of money we can definitely win if we move first.

Equations :

```
F(i, j)  represents the maximum value the user can collect from 
         i'th coin to j'th coin.

    F(i, j)  = Max(Vi + min(F(i+2, j), F(i+1, j-1) ), 
                   Vj + min(F(i+1, j-1), F(i, j-2) )) 
Base Cases
    F(i, j)  = Vi           If j == i
    F(i, j)  = max(Vi, Vj)  If j == i+1
```

Key Learning :
1. Maximum of minimum 



 