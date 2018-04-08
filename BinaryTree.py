class BinaryTree:

	def __init__(self, top_value=None):
		self.top_value = top_value
		self.left_child = None
		self.right_child = None

	def insert(self, new_node):

		top_value = self.top_value

		if new_node < top_value:	
			# Case where new node is < top value
			if self.left_child == None:
				# Case where left side is empty
				self.left_child = BinaryTree(new_node)
			else:
				# Case where left side has children
				self.left_child.insert(new_node)
		else:
			# Case where new node is >= top value
			if self.right_child == None:
				# Case where right side is empty
				self.right_child = BinaryTree(new_node)
			else:
				# Case where right side has children
				self.right_child.insert(new_node)
				
	def search(self, target):

		top_value = self.top_value

		if target == top_value:
			# Case where target is found
			print("Found " + str(target) + "!!!")
		elif target < top_value:	
			# Case where target is < top value
			if self.left_child == None:
				# Case where left side is empty
				print("Unable to find " + str(target))
			else:
				# Case where left side has children
				self.left_child.search(target)
		else:
			# Case where target is >= top value
			if self.right_child == None:
				# Case where right side is empty
				print("Unable to find " + str(target))
			else:
				# Case where right side has children
				self.right_child.search(target)

	def display_tree(self):
		print(self.top_value)
		if self.left_child != None:
			self.left_child.display_tree()
		if self.right_child != None:
			self.right_child.display_tree()
	
if __name__ == '__main__':
	print('This is the BinaryTree module')