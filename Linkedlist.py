class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList: 
    def __init__(self):
        self.head = None


    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def search(self, x):
        current = self.head
        while current != None:
            if current.data == x:
                return True
            current = current.next
        return False


    def display(self):
        temp = self.head
        while temp:
            print(temp.data,'->',  end='')
            temp = temp.next
        print('None')

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def identical(self, llist):
        a = self.head
        b = llist.head
        while a != None and b != None:
            if a.data != b.data:
                return False
            a = a.next
            b = b.next
        return a == None and b == None

    def max(self):
        if self.head is None:
            return None
        max = self.head.data
        current = self.head
        while current:
            if current.data > max:
                max = current.data
            current = current.next
        return max

    def delete_llist(self, x):
        self.head = None
     

llist = LinkedList()


llist.insert(6)
llist.insert(4)
llist.insert(3)
llist.insert(2)
print(llist.search(0)) 

llist.display()

print("Size of the linked list:", llist.size())


