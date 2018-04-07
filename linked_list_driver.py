from LinkedList import LinkedList
from LinkedList import Node

base_char_idx = 97
offset_1 = 5
offset_2 = 5

LL = LinkedList()
LL.display_count()

for i in range(base_char_idx, base_char_idx+offset_1+1):
	i = chr(i)
	LL.insert_from_head(Node(i))
	LL.display_list()
LL.display_count()

for i in range(base_char_idx+offset_1+1, base_char_idx+offset_1+offset_2+1):
	i = chr(i)
	LL.insert_from_tail(Node(i))
	LL.display_list()
LL.display_count()

LL.insert_in_between(5, Node('x'))
LL.display_list()
LL.insert_in_between(2, Node('y'))
LL.display_list()
LL.remove_in_between(10)
LL.display_list()
LL.display_count()

for i in range(2):
	LL.remove_from_head()
	LL.display_list()
	LL.remove_from_tail()
	LL.display_list()
LL.display_count()
