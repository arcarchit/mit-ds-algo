



class TreeNode:

	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


class Serialize:

	def serialize(self, node):
		first = str(node.val)
		second = self.serialize(node.left) if node.left else "-1"
		third = self.serialize(node.right) if node.right else "-1"
		ans = "("+first + " " + second + " " + third + ")"
		return ans


	def deserialize(self, str):
		if str == '()':
			return None

		bracket = {}
		stack = []
		for i,ch in enumerate(str):
			if ch == '(':
				stack.append(i)
			elif ch == ')':
				start = stack.pop()
				bracket[start] = i+1

		start = 1
		end = start
		while str[end] != ' ':
			end+=1
		val = int(str[start:end])

		start = end + 1
		if str[start] == '(':
			end = bracket[start]
			left = self.deserialize(str[start:end])
		else:
			while str[end] != ' ':
				end += 1
			left = None

		start = end + 1
		print str, start
		if str[start] == '(':
			end = bracket[start]
			right = self.deserialize(str[start:end])
		else:
			while str[end] != ' ':
				end += 1
			right = None

		ans = TreeNode(val)
		ans.left = left
		ans.right = right
		return ans


def main():
	root = TreeNode(1)
	two,three, four, five, seven = TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(7)

	root.left, root.right = two, three
	three.left, three.right = four, five
	five.right = seven

	ss =Serialize()
	ans = ss.serialize(root)
	print ans

	root = ss.deserialize(ans)
	print ss.serialize(root)


if __name__ == '__main__':
    main()