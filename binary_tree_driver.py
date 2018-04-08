from BinaryTree import BinaryTree

r = BinaryTree(50)
value_array = [30, 20, 25, 40, 10, 15, 23, 26, 5, 70, 75, 80, 100, 60, 68, 69, 41, 39]
search_array = [100, 23, 50, 51, 39, 38]

# Populate Binary Tree
for v in value_array:
	r.insert(v)

r.display_tree()

# Perform binary search on tree
for v in search_array:
	r.search(v)

'''
print(r.get_top_value())
print(r.get_left_child())
print(r.get_right_child())
'''