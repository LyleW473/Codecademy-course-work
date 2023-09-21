import LinkedList

# Definition for singly-linked list node.
class ListNode:
	def __init__(self, value, next_node=None):
		self.value = value
		self.next_node = next_node

# define remove_node() here
def remove_node(head, i):
		# If i is negative
		if i < 0:
			return head

		# If the item we are trying to remove does not exist
		if head == None:
			return None
	
		# If the item we are trying to remove is the head
		if i == 0:
			return head.next_node

		# Set the next node to be a recursive call of the next node (So the current node's next node will become the recursive call's next node)
		head.next_node = remove_node(head.next_node, i - 1)
		
		return head

# Test code - do not edit
gemstones = LinkedList.LinkedList(["Amber", "Sapphire", "Jade", "Pearl"])
head = remove_node(gemstones.head, 1)
print(head.flatten())