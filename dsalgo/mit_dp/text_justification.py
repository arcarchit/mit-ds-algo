import heapq

def get_children(x):
    return [x*y for y in ll]

ans = []
frontier = all()
visited = set()

while(frontier):
    new_frontier = []
    for x in frontier:
        if x not in visited:
            visited.add(x)
            new_frontier.extend(get_children(x))
    cond1 = len(visited) > D
    min_new = min(new_frontier)
    max_old = max(frontier)
    cond2 = min_new >= max_old
    if cond1 == cond2:
        break


    heapq.heappush(ans, x)
    heapq._nsmallest(D)

    heapq.