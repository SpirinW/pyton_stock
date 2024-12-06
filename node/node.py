class node_single_linked (object):
	def __init__(self, x=None):
		if type(x) is node_single_linked:
			self.key = x.key
			self.next = x.next
		else:
			self.key=x
			self.next=None
	def add(self, x):
		if self.key == None:
			self.key=x
			self.next=None
		else:
			temp=node_single_linked(x)
			while(self.next):
				self=self.next
			self.next=temp
	def delete(self, x):
		new_self=self
		if(self.key != None):
			prev=None
			while True:
				if(self.key == x):
					if not prev:
						if not self.next:
							new_self=None
						else:
							new_self=self.next
					else:
						prev.next=self.next
						self=self.next
					break
				if(self.next):
					prev=self
					self=self.next
				else:
					break
		return new_self
	def size(self):
		s=0
		while(self):
			self=self.next
			s+=1
		return s
	def l_reverse(head):
		curr=head
		prev=None
		while True:
			temp=curr.next
			curr.next=prev
			prev=curr
			#print(f'curr: {curr}')
			#print(f'temp: {temp}')
			if not temp:
				break
			curr=temp
		return curr
	def reverse(self):
		reversed = node_single_linked(self).l_reverse()
		#print(reversed)
		self.key = reversed.key
		self.next = reversed.next

	def __eq__(self, other):
		if(self.key == None or other.key == None):
			return self.key == other.key
		if(self.size() != other.size()):
			return False
		else:
			while(self and other):
				if(self.key != other.key):
					return False
				self=self.next
				other=other.next
			return True
	def __str__(self):
		ans=''
		if not self.key or not self:
			ans="None"
		else:
			while(self):
				ans+=str(self.key) + ' -> '
				self=self.next 
			ans+="None"
		return ans

class node_double_linked(object):
	def __init__(self, x=None):
		if type(x) is node_double_linked:
			self.key = x.key
			self.next = x.next
			self.prev= x.prev

		else:
			self.key=x
			self.next=None
			self.prev=None
	def size(self):
		s=0
		while(self):
			s+=1
			self=self.next
	def add(self, x):
		if(self.key == None):
			self.key=x
			self.next=None
			self.prev=None
		else:
			temp=node_double_linked(x)
			while(self.next):
				self=self.next
			temp.prev=self
			self.next=temp
	def delete(self, x):
		new_self=self
		if(self.key != None):
			temp=None
			while True:
				if self.key == x:
					if not temp:
						self=self.next
						self.prev=None
						new_self=self
					else:
						temp.next=self.next
						self=self.next
					break
				if self.next:
					temp=self
					self=self.next
				else:
					break
		return new_self
	def l_reverse(self):
		curr=self
		prev=None
		while True:
			temp=curr.next
			curr.next=prev
			prev=curr
			if not temp:
				break
			curr=temp
		return curr
	def reverse(self):
		reversed = node_double_linked(self).l_reverse()
		self.key = reversed.key
		self.prev = reversed.prev
		self.next = reversed.next
	def __str__(self):
		ans="None"
		if(self.key != None):
			ans+=' <-> '
			while(self):
				ans+=str(self.key) + ' <-> '
				self=self.next
			ans+="None"
		return ans
	def __eq__(self, other):
		if(self.key == None or other.key == None):
			return self.key == other.key
		if(self.size() != other.size()):
			return False
		else:
			while(self and other):
				if(self.key != other.key):
					return False
				self=self.next
				other=other.next
			return True