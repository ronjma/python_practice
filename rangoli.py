class Queue:
	def __init__(self):
		self.q = []

	def enqueue(self, data):
		self.q.append(data)
		
	def dequeue(self):
		return self.q.pop()
		
	def is_empty(self):
		return len(self.q) == 0
	
	def show_queue(self):
		print(self.q)

def make_string_pattern(N):
	str = ''
	queue = Queue()

	for i in range(0, N-1):
		data = letter_list[i]
		queue.enqueue(data)
		str += data + '-'
	queue.enqueue(letter_list[N-1])
	
	while not queue.is_empty():
		data = queue.dequeue()
		str += data + '-'

	str = str.rstrip('-')

	return str
	
N=26
letter_list = [chr(i) for i in range(ord('a'), ord('a')+N)][::-1]

for i in range(1, N+1):
	print(make_string_pattern(i).center(N*2-1+(N*2-2), '-'))
for i in range(N-1, 0, -1):
	print(make_string_pattern(i).center(N*2-1+(N*2-2), '-'))