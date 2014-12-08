from QNode import *

class Queue(object):
	head = None
	tail = None
	size = 0
	limit = 0

	def __init__(self,limit=limit,head=None,tail=None):
		self.head = head
		self.tail = tail
		self.size = 0
		self.limit = limit

	def push(self,value):
		if self.size < self.limit:
			n = QNode(value=value,prev=None,next=self.head)
			if self.head == None:
				self.tail = n
			else:	
				self.head.prev = n
			self.head = n
			self.size = self.size + 1
			return 1
		else:
			return 0		

	def pop(self):	
		if self.size != 0:
			t = self.tail
			self.tail = t.prev
			t.prev = None
			self.tail.next = None
			self.size = self.size - 1
			return 1
		else:
			return 0
	
	def remove(self,value):
		n = self.head
		while n != None:
			if n.value == value:
				if self.head == n:
					self.head = n.next
				if self.tail == n:
					self.tail = prev
				next_node = n.next
				if n.prev != None:
					n.prev.next = n.next
				if n.next != None:
					n.next.prev = n.prev
				n.prev = None
				n.next = None
				self.size = self.size - 1
				return 1
			else:
				n = n.next
		return 0

q = Queue(limit=1)
print q.push(5)
print "--"
print "size = ",q.size
print "--"
print q.push(3)
print "--"
print "size = ",q.size
print "--"
print q.remove(3)
print "--"
print "size = ",q.size
print "--"
print "xx\n"
print q.head.value
#print q.head.next.value
print q.tail.value






