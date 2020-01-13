class Node:
    def __init__(self,key):
        self.data = key
        self.left_child = None
        self.right_child = None

class BST:

    def __init__(self):
        self.root = None

    def insert(self,key):
        if not isinstance(key,Node):
            key = Node(key)

        if self.root == None:
            self.root = key
        else:
            self._insert(self.root,key)

    def _insert(self,curr,key):## it is private method(only use within class)
        if curr.data < key.data:
            if curr.right_child == None:
                    curr.right_child = key
            else:
                self._insert(curr.right_child,key)
        elif curr.data > key.data:
            if curr.left_child == None:
                curr.left_child = key
            else:
                self._insert(curr.left_child,key)

    def in_order_traverse(self):
        self._in_order_traverse(self.root)
        print("")
    def _in_order_traverse(self,curr):###root,left,right
        if curr:
            self._in_order_traverse(curr.left_child)
            print(curr.data,end = " ")
            self._in_order_traverse(curr.right_child)

    def pre_order(self):
        self._pre_order(self.root)
        print("")
    def _pre_order(self,curr):
        if curr:
            print(curr.data,end = " ")
            self._pre_order(curr.left_child)
            self._pre_order(curr.right_child)

    def post_order(self):
        self._post_order(self.root)
        print("")
    def _post_order(self,curr):
        if curr:
            self._post_order(curr.left_child)
            self._post_order(curr.right_child)
            print(curr.data,end = " ")

    def search_val(self,key):
        self._search_val(self.root,key)
    def _search_val(self,curr,key):
        if curr != None:
            if curr.data == key:
                return print("found")
            elif curr.data < key:
                return self._search_val(curr.right_child,key)
            else:
                return self._search_val(curr.left_child,key)
        return print("not found")

    def min_right_tree(self,curr):
        if curr.left_child == None:
            return curr
        else:
            return self.min_right_tree(curr.left_child)

    def delete(self,key):
        self._delete(self.root,None,None,key)
    def _delete(self,curr,prev,is_left,key):
        if curr:
            if curr.data == key:
                if curr.left_child and curr.right_child:
                    min_right_child = self.min_right_tree(curr.right_child)
                    curr.data = min_right_child.data
                    self._delete(curr.right_child,curr,False,min_right_child.data)
                elif curr.left_child == None and curr.right_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = None
                        else:
                            prev.right_child = None
                    else:
                        self.root = None
                elif curr.left_child==None:
                    if prev:
                        if is_left:
                            prev.left_child = curr.right_child
                        else:
                            prev.right_child = curr.right_child
                    else:
                        self.root = curr.right_child
                elif curr.right_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = curr.left_child
                        else:
                            prev.right_child = curr.left_child
                    else:
                        self.root = curr.left_child
            elif curr.data >key:
                self._delete(curr.left_child,curr,True,key)
            elif curr.data <key:
                self._delete(curr.right_child,curr,False,key)
        else:
            print("key not found")


#testing

tree = BST()



# print(tree.root.data)
# print(tree.root.left_child.data)
# print(tree.root.right_child.data)
# print(tree.root.left_child.left_child.data)
# print(tree.root.left_child.left_child.right_child.data)
# print(tree.root.right_child.right_child.data)



tree.insert("F")
tree.insert("C")
tree.insert("I")
tree.insert("M")
tree.insert("J")
tree.insert("L")
tree.insert("F")
tree.insert("C")
tree.insert("G")
tree.insert("A")
tree.insert("B")
tree.insert("K")
tree.insert("E")

# tree.in_order_traverse()
# tree.pre_order()
# tree.post_order()
#
# tree.search_val('I')

tree.in_order_traverse()
tree.delete("C")
tree.in_order_traverse()
