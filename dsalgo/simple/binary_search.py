ll = [1, 2, 5, 8, 9, 13]
import sys

# 1) Search for 5
# 2) What are no of elements less then 11

def binary_search(A, x):
    i = 0
    j = len(A)-1


    while(i<j):
        mid = (i + j) / 2
        if(x < A[mid]):
            j = mid
        elif(x > A[mid]):
            i = mid + 1
        else:
            return mid

    return None

def no_of_stricylt_greater(A, x):
    minn = 0
    maxx = len(A) - 1
# A = [1, 2, 3, 4, 7, 8, 9, 10, 10, 11, 14]
    while(True):
        mid = (minn + maxx)/2
        if (minn > maxx):
            return len(A) - minn

        if x < A[mid]:
            maxx = mid - 1
        elif x > A[mid]:
            minn = mid + 1
        elif x == A[mid]:
            minn = minn + 1

def no_of_less_equal(A, x):
    minn = 0
    maxx = len(A) - 1

    while (True):
        mid = (minn + maxx) / 2
        if minn > maxx:
            return minn

        if x < A[mid]:
            maxx = mid - 1
        elif x > A[mid]:
            minn = mid + 1
        elif x == A[mid]:
            minn = mid + 1

def no_of_stricylt_less(A, x):
    minn = 0
    maxx = len(A) - 1

    while (True):
        mid = (minn + maxx) / 2
        if minn > maxx:
            return minn

        if x < A[mid]:
            maxx = mid - 1
        elif x > A[mid]:
            minn = mid + 1
        elif x == A[mid]:
            maxx = mid  - 1


def no_ele_less_for_array_with_duplicates(A, x):
    pass
    # TODO


if __name__ == "__main__":
    A = [1, 2, 3, 4, 7, 8, 9, 10, 10, 11, 14]
    print no_of_stricylt_less(A, 9)
    print no_of_less_equal(A, 9)

    minn = -sys.maxint - 1
    maxx = sys.maxint
    print minn, maxx, minn > maxx

    while (True):
        print "inside"
        mid = (minn + maxx) / 2
        ss_count, rr_count = no_strictly_less(mid)
        print ss_count, rr_count
        print minn, maxx, mid
        if (minn > maxx):
            pass

        if rr_count > desired_count:
            maxx = mid - 1
        elif ss_count < desired_count:
            minn = mid + 1
        else:
            minn = mid + 1