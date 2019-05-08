import heapq


def sky_line(builidings):
	# tuples are (start, end, height)
	# We need to return critical point (x, height)

	pq = []
	current_height = 0
	ans = []

	for x in builidings:
		start, height, end  = x
		start_tuple = (start, 0, height)
		end_tuple = (end, 1, height)
		heapq.heappush(pq, start_tuple)
		heapq.heappush(pq, end_tuple)

	while pq:
		popped = heapq.heappop(pq)
		x, indicator, height = popped
		if indicator == 0:
			if height > current_height:
				critical_point = (x, height)
				current_height = height
				ans.append(critical_point)
		else:
			if height == current_height:
				critical_x = x
				critical_h = pq[0][2] if pq and pq[0][1] == 1 else 0
				critical_point = (critical_x, critical_h)
				ans.append(critical_point)

	return ans





def main():
	buildings = [(1,11,5), (2,6,7), (3,13,9), (12,7,16), (14,3,25),
         (19,18,22), (23,13,29), (24,4,28)]
	points = sky_line(buildings)
	print points


if __name__=="__main__":
	main()