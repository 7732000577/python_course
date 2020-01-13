class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self,x):

        if not isinstance(x,Node) :
            x = Node(x)
        if self.head == None:
            self.head = x

        else:
            self.tail.next = x

        self.tail = x

    def add_to_start(self,x):
        if not isinstance(x,Node):
            x = Node(x)
        if self.head ==None:
            self.head = x
            self.tail = x
        else:
            x.next = self.head
            self.head = x

    def search_val(self,x):
        curr = self.head
        index = 0
        while curr is not None:
            if curr.data == x:
                return index
            else:
                curr = curr.next
                print(curr)
                index+=1
        return index

    def len(self):
        curr = self.head
        length = 0
        while curr is not None:
            length+=1
            curr = curr.next
        return length

    def remove_val_by_index(self,x):
        curr = self.head
        num = 0
        while num<x:
            previous = curr
            curr = curr.next
            num+=1
        previous.next = curr.next

    def reverse_iter(self):

        curr = self.head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def reverse_recursive(self,curr,prev):
        if self.head==None:
            return
        elif curr.next == None:##1->2->3->4->5
            self.tail = self.head
            curr.next = prev
            self.head = curr
            print('yes')

        else:
            next = curr.next
            curr.next = prev
            self.reverse_recursive(next,curr)


    def __str__(self):
        to_print = ""
        current = self.head###current is node which contains two info (about data and next info)

        while current is not None:
            to_print+= str(current.data)+"->"
            current = current.next

        if to_print:
            return f'{to_print[:-2]}'
        else:
            return '[]'

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

list1 = LinkedList()
print(list1)

list1.append_val(node1)
list1.append_val(node2)
list1.append_val(node3)
list1.append_val(node4)
list1.append_val(5)
print(list1)

list1.add_to_start(Node(3))
print(list1)

print(list1.search_val(3))
print(list1.len())
print(list1.remove_val_by_index(3))
print(list1)

list1.reverse_recursive(list1.head,None)
print(list1)
