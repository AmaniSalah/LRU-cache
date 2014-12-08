
class QNode(object):
	value = None
	next = None
	prev = None


	def __init__(self,value,next=None,prev=None):
		self.value = value
		self.next = next
		self.prev = prev


