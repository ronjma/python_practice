class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

	def __str__(self):
		return "This is the Node class"

class LinkedList:

	def __init__(self):
		self.head = Node()
		self.prev = Node()
		self.count = 0

	def __str__(self):
		return "This is the LinkedList class"

	def insert_from_head(self, data_node):
		if self.is_empty():
			self.head = data_node
		else:
			data_node.next = self.head
			self.head = data_node
		self.count += 1

	def insert_from_tail(self, data_node):
		if self.is_empty():
			self.head = data_node
		else:
			marker = self.head
			while self.head.next != None:
				self.head = self.head.next
			self.head.next = data_node
			self.head = marker
		self.count += 1

	def insert_in_between(self, index, data_node):

		if index > self.count:
			print("Index is larger than length of Linked List")
			return
		elif index == 0:
			self.insert_from_head(data_node)
		elif index == self.count:
			self.insert_from_tail(data_node)
		else:
			marker = self.head
			target = 0
			while target != index:
				self.prev = self.head
				self.head = self.head.next
				target += 1
			data_node.next = self.head
			self.prev.next = data_node
			self.count += 1
			self.head = marker
		
	def remove_from_head(self):
	
		if self.is_empty():
			return
			
		self.head = self.head.next
		self.count -= 1
		
	def remove_from_tail(self):

		if self.is_empty():
			return

		marker = self.head
		while self.head.next != None:
			self.prev = self.head
			self.head = self.head.next
			
		self.prev.next = None
		self.head = marker
		self.count -= 1
		
	def remove_in_between(self, index):

		if self.is_empty():
			return
		elif index > self.count:
			print("Index is larger than length of Linked List")
			return
		elif index == 0:
			self.remove_from_head()
		elif index == self.count:
			self.remove_from_tail()
		else:
			marker = self.head
			target = 0
			while target != index:
				self.prev = self.head
				self.head = self.head.next
				target += 1
			self.prev.next = self.head.next
			self.count -= 1
			self.head = marker
	
	def is_empty(self):
		return self.count <= 0

	def display_list(self):

		if self.is_empty():
			print("LinkedList is empty!")
			return

		marker = self.head
		while self.head != None:
			print(self.head.data, end=" ")
			self.head = self.head.next
		self.head = marker
		print()
		
	def display_count(self):
		print(self.count)
		
if __name__ == "__main__":
	print("This is the LinkedList module")