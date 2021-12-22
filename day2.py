# Linked list operations in Python


# Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    # Insert after a node
    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Insert at the end
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    # Deleting a node
    def deleteNode(self, position):

        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        # Find the key to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If the key is not present
        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None

        temp.next = next

    # Search an element
    def search(self, key):

        current = self.head

        while current is not None:
            if current.data == key:
                return True

            current = current.next

        return False

    # Sort the linked list
    def sortLinkedList(self, head):
        current = head
        index = Node(None)

        if head is None:
            return
        else:
            while current is not None:
                # index points to the node next to current
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data

                    index = index.next
                current = current.next

    # Print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next


if __name__ == '__main__':

    llist = LinkedList()
    llist.insertAtEnd(5)
    llist.insertAtBeginning(1)
    llist.insertAtBeginning(2)
    llist.insertAtEnd(4)
    llist.insertAfter(llist.head.next, 3)

    print('linked list:')
    llist.printList()

    print("\nAfter deleting an element:")
    llist.deleteNode(3)
    llist.printList()

    print()
    item_to_find = 3
    if llist.search(item_to_find):
        print(str(item_to_find) + " is found")
    else:
        print(str(item_to_find) + " is not found")

    llist.sortLinkedList(llist.head)
    print("Sorted List: ")
    llist.printList()
    # Python program to swap two given nodes of a linked list
class LinkedList(object):
	def __init__(self):
		self.head = None

	# head of list
	class Node(object):
		def __init__(self, d):
			self.data = d
			self.next = None

	# Function to swap Nodes x and y in linked list by
	# changing links
	def swapNodes(self, x, y):

		# Nothing to do if x and y are same
		if x == y:
			return

		# Search for x (keep track of prevX and CurrX)
		prevX = None
		currX = self.head
		while currX != None and currX.data != x:
			prevX = currX
			currX = currX.next

		# Search for y (keep track of prevY and currY)
		prevY = None
		currY = self.head
		while currY != None and currY.data != y:
			prevY = currY
			currY = currY.next

		# If either x or y is not present, nothing to do
		if currX == None or currY == None:
			return
		# If x is not head of linked list
		if prevX != None:
			prevX.next = currY
		else: # make y the new head
			self.head = currY

		# If y is not head of linked list
		if prevY != None:
			prevY.next = currX
		else: # make x the new head
			self.head = currX

		# Swap next pointers
		temp = currX.next
		currX.next = currY.next
		currY.next = temp

	# Function to add Node at beginning of list.
	def push(self, new_data):

		# 1. alloc the Node and put the data
		new_Node = self.Node(new_data)

		# 2. Make next of new Node as head
		new_Node.next = self.head

		# 3. Move the head to point to new Node
		self.head = new_Node

	# This function prints contents of linked list starting
	# from the given Node
	def printList(self):
		tNode = self.head
		while tNode != None:
			print (tNode.data),
			tNode = tNode.next


# Driver program to test above function
llist = LinkedList()

# The constructed linked list is:
# 1->2->3->4->5->6->7
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
print ("Linked list before calling swapNodes() ")
llist.printList()
llist.swapNodes(4, 3)
print ("\nLinked list after calling swapNodes() ")
llist.printList()

# This code is contributed by BHAVYA JAIN
