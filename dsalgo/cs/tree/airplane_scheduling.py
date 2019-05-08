# Airplane scheduling problem
# Mainly 2 API
# 1) schedule new arrival
# 2) Get no of arrivals before time t

class TreeNode:
	def __init__(self, name, time):
		self.left, self.right = None, None
		self.name, self.time = name, time
		self.smaller, self.larger = 0, 0


class AirplanScheduler:
	# This will be tree and will have a root

	def __init__(self, diff):
		self.diff = diff
		self.root = None

	def schedule(self, name, time):
		# Return 1 if accepted and scheduled else return 0
		new_node = TreeNode(name, time)

		if not self.root:
			self.root = new_node
			return 1

		current = self.root
		while True:
			if abs(current.time - time) <= self.diff:
				return 0
			if time < current.time:
				current.smaller += 1
				if current.left:
					current = current.left
				else:
					current.left = new_node
					return 1
			else:  # time > current.time
				current.larger += 1
				if current.right:
					current = current.right
				else:
					current.right = new_node
					return 1


	def landed(self, flight):
		# Remove flight from the tr
		pass

	def _print_level_order(self):
		frontier = [self.root]
		ans = []
		while frontier:
			temp, new_frontier = [], []
			for x in frontier:
				temp.append((x.time, x.smaller))
				if x.left:
					new_frontier.append(x.left)
				if x.right:
					new_frontier.append(x.right)
			frontier = new_frontier
			ans.append(temp)
		print ans

	def get_next(self, time):
		# Return next earliest time available
		# Not an officeal API of BST
		if not self.root:
			return time

		st, in_order = [], []
		current = self.root


		while st or current:
			if current:
				st.append(current)
				current = current.left
			else:
				popped = st.pop()
				in_order.append(popped)  # Can be optimized here
				current = popped.right

		in_order_set = set(in_order)

		while True:
			# TODO This may not be part of BST, requires some special ds-algo
			left, right = time - self.diff, time + self.diff
			if left in in_order_set or right <= 0 or right in in_order_set:
				time += 1
				continue
			else:
				return time


	def count_smaller(self, time):
		# How many planes are scheduled at before 'time'
		# Augment tree
		if not self.root:
			return 0
		current = self.root
		ans = 0
		while current:
			if time < current.time:
				current = current.left
			elif time > current.time:
				ans += 1
				ans += current.smaller
				current = current.right
			else:
				ans += current.smaller
				break
		return ans




def main():
	ass = AirplanScheduler(3)

	print "insert"
	print ass.schedule("SG12", 12)
	print ass.schedule("SG14", 8)
	print ass.schedule("SG19", 19)
	print ass.schedule("SG16", 16)
	print ass.schedule("SG15", 15)
	print ass.schedule("SG12", 51)
	print ass.schedule("SG12", 38)
	print ass.schedule("SG12", 68)
	print ass.schedule("SG12", 31)
	print ass.schedule("SG12", 43)
	print ass.schedule("SG12", 61)
	print ass.schedule("SG12", 74)
	print ass._print_level_order()
	print "get smaller"
	print ass.count_smaller(10)
	print ass.count_smaller(12)
	print ass.count_smaller(13)
	print ass.count_smaller(15)
	print ass.count_smaller(21)
	print ""
	print ass.count_smaller(40)
	print ass.count_smaller(50)
	print ass.count_smaller(60)
	print ass.count_smaller(70)
	print ass.count_smaller(80)
	print ass.count_smaller(38)


if __name__=="__main__":
	main()