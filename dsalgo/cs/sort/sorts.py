# TODO : What do you think about iterative merge sort
# I beleive it is not needed, I have explained in blog post that log depth is awesome, just need to confirm it.

def merge_sort(ll):

    if len(ll) == 1:
        return ll

    mid = len(ll)/2

    left, right = ll[:mid], ll[mid:]

    sorted_left, sorted_right = merge_sort(left), merge_sort(right)

    # Merge

    ans = []
    i, j = 0, 0

    while i<len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] < sorted_right[j]:
            ans.append(sorted_left[i])
            i = i + 1
        else:
            ans.append(sorted_right[j])
            j = j + 1
    while i < len(sorted_left):
        ans.append(sorted_left[i])
        i = i + 1
    while j < len(sorted_right):
        ans.append(sorted_right[j])
        j = j + 1

    return ans



def insertion_sort(ll):
	for i in range(1, len(ll)):
		j = i
		while j > 0:
			if ll[j-1] > ll[j]:
				ll[j], ll[j-1] = ll[j-1], ll[j]
				j = j - 1
			else:
				break
	return ll



def selection_sort(ll):
    for i in range(len(ll)):
        k = i
        for j in range(i, len(ll)):
            if ll[j] < ll[k]:
                k = j
        ll[i], ll[k] = ll[k], ll[i]

    return ll


def quick_sort(ll):
	# We are taking last element as pivot
	# Schemes like random pivot is better. We can first swap it with last element there.
	# Worst case complexity O(N^2), average case O(N log N)

	def parition(left, right):
		pivot = ll[right-1]
		i = left
		for j in range(left, right):
			if ll[j] <= pivot:
				ll[i], ll[j] = ll[j], ll[i]
				i+=1
		return (i-1)

	def sub_sol(left, right):
		if left >= right:
			return
		pivot = parition(left, right)
		sub_sol(left, pivot)
		sub_sol(pivot+1, right)

	sub_sol(0, len(ll))
	return ll


def iterative_mergesort():
	pass


def main():
	ll = [1,3,5,2,7,8,4,9,0,6]
	ss = selection_sort(ll)
	print ss

if __name__=="__main__":
    main()