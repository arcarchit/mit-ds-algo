from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, node):
        visited = [False]*len(self.graph)
        q = []
        print node,
        visited[node] = True
        q.append(node)
        while(len(q) != 0):
            current = q.pop(0)
            neighbours = self.graph[current]
            for n in neighbours:
                if not visited[n]:
                    print n,
                    q.append(n)
                    visited[n] = True


    def dfs(self, node):
        visited = [False] * len(self.graph)
        st = []
        st.append(node)

        while (len(st) != 0):
            current = st.pop()
            print current,
            visited[current ] = True
            for n in self.graph[current]:
                if not visited[n]:
                    st.append(n)

    def topologicalSort(self):
        st = []
        ans_st = []
        visited = [False] * len(self.graph)
        node = 2

        st.append(node)

        while (len(st) != 0):
            current = st[-1]
            visited[current] = True
            count = 0
            for n in self.graph[current]:
                if not visited[n]:
                    st.append(n)
                    count = count + 1
            if count == 0:
                print current,
                print st[-1]
                ans_st.append(st.pop())

        print ans_st




def main():
    g = Graph()
    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);

    print "Following is a Topological Sort of the given graph"
    g.topologicalSort()

if __name__=="__main__":
    main()