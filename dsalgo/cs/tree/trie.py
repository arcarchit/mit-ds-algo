# Problem : https://leetcode.com/problems/replace-words/


class Trie:
	"""
	Idea is to have '_end' token always.
	This make life easier then trying to end end tree with None.
	"""

	def __init__(self):
		self.root = {}

	def add_word(self, word):
		focus = self.root
		for ch in word:
			if ch in focus:
				focus = focus[ch]
			else:
				focus[ch] = {}
				focus = focus[ch]
		focus['_end'] = None

	def get_prefix(self, word):
		ans = []
		focus = self.root
		for ch in word:
			if '_end' in focus:
				return (''.join(ans), True)
			if ch in focus:
				ans.append(ch)
				focus = focus[ch]
			else:
				return ('', False)
		return ('', False)


