class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("The given previous node must be in LinkedList.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # If key was not present in linked list
        if temp == None:
            return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Test the LinkedList
if __name__ == '__main__':
    llist = LinkedList()

    # Insertion operations
    llist.insert_at_end(6)
    llist.insert_at_beginning(7)
    llist.insert_at_beginning(1)
    llist.insert_at_end(4)
    llist.insert_after(llist.head.next, 8)

    print("Linked list after insertions:")
    llist.print_list()

    # Deletion operation
    llist.delete_node(8)
    print("\nLinked list after deleting 8:")
    llist.print_list()

    llist.delete_node(1)
    print("\nLinked list after deleting 1 (head):")
    llist.print_list()

    llist.delete_node(4)
    print("\nLinked list after deleting 4 (last node):")
    llist.print_list()

    llist.delete_node(10)  # Try to delete a non-existent node
    print("\nLinked list after trying to delete 10 (non-existent):")
    llist.print_list()