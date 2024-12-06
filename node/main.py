from node import *

def reverse(head:node_single_linked):
	curr=head
	prev=None
	while True:
		temp = curr.next
		curr.next=prev
		prev=curr
		if 	temp is None:
			break
		curr=temp
	return curr
a=[5,9,2,1,5,8,2]
a=list(range(1,6))
l=node_double_linked(a[0])
for i in a[1:]:
	l.add(i)
#print(reverse(l))
print(l)
l.reverse()
print(l)
