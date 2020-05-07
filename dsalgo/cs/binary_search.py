def strickly_less_than(ll, a):

    left, right = 0, len(ll) - 1

    while left < right:
        mid = (left + right + 1) / 2 # bias to right

        if ll[mid] < a:
            left = mid
        else:
            right = mid - 1 # decrease right

    return ll[left] # ans is left




def strickly_greater(ll, a):
    left, right = 0, len(ll) - 1
    # T T T T F F F
    while left < right:

        mid = (left + right) / 2 # bias to left

        if ll[mid] <= a:
            left = mid + 1  # increase left
        else:
            right = mid

    return ll[right]  # ans is right


if __name__ == "__main__":
    ll = [2, 4, 6, 9, 11, 13, 17, 19, 20, 21]
    no = 18
    print strickly_less_than(ll, no)
    print strickly_greater(ll, no)