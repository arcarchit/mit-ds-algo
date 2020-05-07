# https://leetcode.com/problems/accounts-merge/

# Break in smaller components
# Once you complete the code, you can refactor it.
# More modular way, make functions


# LEARNING : Dictionary can not be used for connected component. Two components might not be connected intially. But third record connects them.


# THoughts on Union Find vs DFS for connected components.
# In DFS you need to construct entire graph, space complexity would be O(V + E). How many edges ?
# In Union find space complexity is O(V)


# My solution is still text-bookish
# Have a look : https://leetcode.com/problems/accounts-merge/discuss/109161/Python-Simple-DFS-with-explanation!!!
# Good DFS : You visited account, update multiple emails

def wrongSolution(self, records):
    """
    :type accounts: List[List[str]]
    :rtype: List[List[str]]
    """

    output_dic = {}  # Stores output
    inter_dic = {}
    global_key = 0

    def check_if_email_exists(emails):
        """
        Return key if any email is matched, else None
        """
        ans = None
        for e in emails:
            if e in inter_dic:
                ans = inter_dic[e]
                break
        return ans

    def update_dics(key, emails):
        for e in emails:
            inter_dic[e] = key
            output_dic[key][1].add(e)

    def produce_output():
        ans = []
        for key in output_dic:
            val = output_dic[key]
            name = val[0]
            emails = list(val[1])
            emails.sort()
            ll = [name]
            for e in emails: ll.append(e)
            ans.append(ll)
        return ans

    for r in records:
        name = r[0]
        emails = r[1:]

        key = check_if_email_exists(emails)

        if key is None:
            key = global_key
            global_key += 1
            output_dic[key] = [name, set()]

        update_dics(key, emails)

    ans = produce_output()
    return ans


from collections import defaultdict


class UnionFind:
    def __init__(self):
        self.dic = {}  # Space : O(M*N)

    def add(self, key):
        if key not in self.dic:self.dic[key] = key

    def union(self, key1, key2):  # O(1) because of path compression
        if key1 not in self.dic: self.dic[key1] = key1
        if key2 not in self.dic: self.dic[key2] = key2

        parent1 = self.find_parent(key1)
        parent2 = self.find_parent(key2)
        self.dic[parent2] = parent1


    def find_parent(self, key):  # Amortized O(1)
        bkp_key = key
        parent = self.dic[key]
        while parent != key:
            key = parent
            parent = self.dic[key]
        self.dic[bkp_key] = parent  # path compression
        return parent

    def get_connected_components(self):  # O(M*N)
        ans = defaultdict(list)
        for key in self.dic:
            parent = self.find_parent(key)
            ans[parent].append(key)
        return ans




def accountsMerge(records):
    """
    :type accounts: List[List[str]]
    :rtype: List[List[str]]

    Each node in graph is (email,name)
    Nodes are connected
    """

    inter_dic = {}  # Stores each (email,name) node to id
    rev_dic = {}  # Given id return node

    gid = 0

    uf = UnionFind()

    for r in records:
        name = r[0]
        emails = r[1:]

        first_id = None
        for e in emails:
            node = (name, e)
            if node in inter_dic:
                id = inter_dic[node]
            else:
                id = gid
                inter_dic[node] = id
                rev_dic[id] = node
                gid += 1
            if first_id != None:
                uf.union(first_id, id)
            else:
                first_id = id
                uf.add(first_id)

    print uf.dic
    dicc = uf.get_connected_components()

    ans = []
    for key in dicc:
        val = dicc[key]  # list of ids
        name = None
        emails = []
        for id in val:
            node = rev_dic[id]
            name = node[0] if not name else name
            emails.append(node[1])
        emails.sort()
        ll = [name]
        ll.extend(emails)
        ans.append(ll)
    return ans


def main():
    input = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    output = accountsMerge(input)
    print output

if __name__=="__main__":
    main()
