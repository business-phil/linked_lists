class Node(object):
	def __init__(self, data, prev = None, next = None):
		self.data = data
		self.prev_node = prev
		self.next_node = next
	def get_data(self):
		return self.data
	def set_data(self, data):
		self.data = data
	def get_prev(self):
		return self.prev_node
	def set_prev(self, prev):
		self.prev_node = prev
	def get_next(self):
		return self.next_node
	def set_next(self, next):
		self.next_node = next

class DoublyLinkedList(object):
	def __init__(self, head = None, tail = None):
		self.head = head
		self.tail = tail
		self.size = 0
	def add_last(self, data):
		new_node = Node(data, prev = self.tail)
		if self.tail:
			self.tail.set_next(new_node)
		self.tail = new_node
		if not(self.head):
			self.head = new_node
		self.size += 1
	def add_first(self, data):
		new_node = Node(data, next = self.head)
		if self.head:
			self.head.set_prev(new_node)
		self.head = new_node
		if not(self.tail):
			self.tail = new_node
		self.size += 1
	def remove_nth_node(self, n):  # 1-indexed
		#fast fail if n is greater than list size
		if n > self.size:
			return False
		#iterate through list until current_mode points to nth node, which will be removed
		current_node = self.head
		for i in range(n-1):
			current_node = current_node.get_next()
		next_temp = current_node.get_next()
		prev_temp = current_node.get_prev()
		if next_temp:
			next_temp.set_prev(prev_temp)
		else:
			self.tail = prev_temp
		if prev_temp:
			prev_temp.set_next(next_temp)
		else:
			self.head = next_temp
		self.size -= 1
		return True
	def find_first(self, data):  # 1-indexed
		current_node = self.head
		node_count = 1
		while current_node:
			if current_node.get_data() == data:
				return node_count
			else:
				node_count += 1
				current_node = current_node.get_next()
		return -1



# fancylist = DoublyLinkedList()
# fancylist.add_first('phil')
# fancylist.add_last('marco')
# fancylist.add_last('adam')
# fancylist.add_last('sneha')
# fancylist.add_last('kadiatu')
# fancylist.add_last('tim')
# print fancylist.find_first('tim')
# print fancylist.remove_nth_node(1)
# print fancylist.head.data, fancylist.tail.data, fancylist.size