from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.vertices.update([u, v])

    def topo_sort(self):
        ans_stack = []
        visited = set()

        def sub_sol(n):

            # if n not in visited:
            #     visited.add(n)

            for neighbour in self.graph[n]:
                if neighbour not in visited:
                    sub_sol(neighbour)

            visited.add(n)
            ans_stack.append(n)


        for v in self.vertices:
            if v not in visited:
                sub_sol(v)

        return list(reversed(ans_stack))

    def topo_sort_iter(self):
        visited = set()
        ans_stack = []

        for v in self.vertices:
            if v not in visited:
                st = [v]
                call_stack = []

                while st or call_stack:
                    if st :
                        popped = st.pop()
                        visited.add(popped)
                        unvisited_negihbours = False
                        for neighbour in self.graph[popped]:
                            if neighbour not in visited:
                                st.append(neighbour)
                                unvisited_negihbours = True
                        if not unvisited_negihbours:
                            ans_stack.append(popped)
                        else:
                            call_stack.append(popped)
                    else:
                        st.append(call_stack.pop())

        return list(reversed(ans_stack))








def main():
    g = Graph()
    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);
    g.addEdge(7, 8);

    ll = g.topo_sort()
    print "Topological sort ", ll

    ll = g.topo_sort_iter()
    print "Topological sort ", ll


if __name__=="__main__":
    main()

