# EIP Book : page no 482

'''
We want to add new high.

Objective : minimize sum of shortest distance between all cities

Proposal : [city1, city2]

floyd warshall allows you add new city

Approach one:
    ==  Run floyd warshall for all proposals
    ==  O(p* N^3)


'''

def all_pairs_shortest_path(matrix):

    n = len(matrix)

    ans = matrix
    for i in range(n):
        ans[i][i] = 0

    for k in range(n):
        for u in range(n):
            for v in range(n):
                if ans[u][v] > ans[u][k] + ans[k][v]:
                    ans[u][v] = ans[u][k] + ans[k][v]







