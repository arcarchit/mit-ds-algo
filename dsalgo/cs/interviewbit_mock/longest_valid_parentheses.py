# https://leetcode.com/problems/longest-valid-parentheses/

def solution(ss):
    """
    input : string
    return : int


    input : (()
    output : 2

    Brute force : try all parenthesis : O(N^3)

    This was asked by Santhosh. He told me it is good to atleast code brute force after asking interviewer. It should have some score in their template.


    Stack way:
    maintain running length
    ( --- > insert into stack
    ) --- > Check top and pop out. If match increase running length, else set running length to 0

    Example :
    (()))
    (
    (
    ) 2
    ) 4
    ) 0


    DP seems to turn out to be O(N^3). Similar to matix mulitplication.
    We pass two argument to sub_sol. But time per sub-problem is O(n).

    Stack was the way to go. Put index in stack not parenthesis.
    Push in stack only for opening parenthesis, not for closing one.

    Even checking for valid parenthesis can be solved by pushing index instead of '('.
    This can help thinking in more generic way.
    """

    stack = []
    ans = 0
    left_most = -1

    for i,ch in enumerate(ss):
        if ch == '(':
            stack.append(i)
        else:
            if stack:
                popped = stack.pop()
                if stack:
                    temp = i - stack[-1]
                    ans = max(ans, temp)
                else:
                    temp = i - left_most
                    ans = max(ans, temp)
            else:
                left_most = i

    return ans
