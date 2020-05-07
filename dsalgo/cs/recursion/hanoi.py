
def hanoi(m):

    st1 = [i for i in range(m,0,-1)]
    st2, st3 = [], []

    t1, t2, t3 = ("a", st1), ("b", st2), ("c", st3)
    ans = []

    def sub_sol(t1, t2, t3, n):
        if n == 0: return

        sub_sol(t1, t3, t2, n-1)

        s1, s2 = t1[1], t2[1]
        popped = s1.pop()
        s2.append(popped)
        tt = (t1[0], t2[0], popped)
        ans.append(tt)

        sub_sol(t3, t2, t1, n-1)

    sub_sol(t1, t2, t3, m)
    for x in ans:
        print x



def hanoi_iter(m):

    st1 = [i for i in range(m, 0, -1)]
    st2, st3 = [], []

    t1, t2, t3 = ("a", st1), ("b", st2), ("c", st3)
    ans = []

    stack = []
    task = (t1, t2, t3, m)
    stack.append(task)
    while stack :
        peek_task = stack[-1]
        sub_task = (peek_task[0], peek_task[2], peek_task[1], peek_task[3]-1)

        if sub_task[3] != 0:
            stack.append(sub_task)
        else:
            s1, s2 = t1[1], t2[1]
            popped = s1.pop()
            s2.append(popped)
            tt = (t1[0], t2[0], popped)
            ans.append(tt)





if __name__=="__main__":
    """
    (s1, s2, s3, 2)
        (s1, s3, s2, 1)
            (s1, s2, s3, 0)
            s1 -> s3 [1]
            (s3, s2, s1, 0)
         s1 -> s2   
        (s2, s3, s1, 1)
            (s2, s1, s3, 0)
            s2 -> s3
            (s1, s3, s2, 0)
        
    
    
    
    
    
    
    """
    hanoi(4)