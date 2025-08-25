'''
Things to add:

CORE
1. append (Done)
2. prepend (Done)
3. insert (Done)
4. remove
5. pop
6. clear
7. to_list (convert LL back to python list)

DUNDER METHODS
1. __len__ (len(ll))
2. __iter__ (for x in ll:)
3. __getitem__ (ll[2])
4. __repr__ (pretty printing in REPL)
5. __contains__ (if x in ll:)

EXTRAS
1. reverse()
2. find(value)
3. copy()

'''

# This would be the item(s) inside a Linkedlist object
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self, value=None):
        if isinstance(value, list):     # if a list is passed
            self.__head, self.__tail = self.__listToLinkedList(value)
        elif value is None:
            self.__head = None
            self.__tail = None
        elif isinstance(value, Node):   # if a Node is passed
            self.__head = value
            self.__tail = value
            value.next = None  # detach chain if any
        else:
            raise TypeError("LinkedList expects a list, Node, or None")

    def __str__(self):
        curr = self.__head
        res = "["
        while curr:
            res += f"{curr.data}, "
            curr = curr.next

        # Replace the last occurrence of ',' with ']'
        if ", " in res:
            parts = res.rsplit(", ", 1)     # this deletes the last occurence of ','
            res = "]".join(parts)
        return res

    @property
    def head(self):
        return self.__head.data
    
    @property
    def tail(self):
        print("After tail -> " + str(self.__tail.next))
        return self.__tail.data
    
    # appends either a Node or List -> LinkedList chain
    def append(self, value: Node | list): 
        if self.__checkIfValidNode(value):
            value.next = None     # detach the appending node from any existing chain

            if self.__head is None:     # if the LinkedList object is empty
                self.__head = value
                self.__tail = value
            else:
                assert self.__tail is not None      # Ensure self.__tail is not None before setting its next.
                self.__tail.next = value
                self.__tail = value
        elif isinstance(value, list):
            head, tail = self.__listToLinkedList(value)
            if self.__head is None:
                self.__head = head
                self.__tail = tail
            else:
                assert self.__tail is not None
                self.__tail.next = head     # Link the old tail to the appending head
                self.__tail = tail
        else:
            raise TypeError("LinkedList.append() expects a Node or list")

    # prepends a Node or List -> LinkedList Chain
    def prepend(self, value: Node | list):
        if self.__checkIfValidNode(value):
            value.next = self.__head  # Link the new node to the current head
            self.__head = value  # Update head to the new node
            if self.__tail is None:  # If the list was empty, update tail as well
                self.__tail = value
        elif isinstance(value, list):
            head, tail = self.__listToLinkedList(value)
            tail.next = self.__head  # Link tail of the new chain to the old head
            self.__head = head  # Update head to the new head
            if self.__tail is None:  # If the list was empty, update tail as well
                self.__tail = tail 
        else:
            raise TypeError("LinkedList.prepend() expects a Node or list")
        
    # inserts a Node or List -> LinkedList Chain
    def insert(self, index: int, value: Node | list):
        if index < 0:
            raise IndexError("Negative index not supported")
        # Prepare the node(s) to insert
        if self.__checkIfValidNode(value):
            insert_head = value
            insert_tail = value
            value.next = None
        elif isinstance(value, list):
            insert_head, insert_tail = self.__listToLinkedList(value)
        else:
            raise TypeError("LinkedList.insert() expects a Node or list")

        # Insert at head
        if index == 0:
            insert_tail.next = self.__head
            self.__head = insert_head
            if self.__tail is None:     # incase that the LinkedList is empty
                self.__tail = insert_tail
            return

        # Traverse to node before insertion point
        # Maximum traversal at the end of the List +1 (prev having a NODE and curr is None)
        curr = self.__head
        prev = None
        curr_index = 0
        while curr and curr_index < index:
            prev = curr
            curr = curr.next
            curr_index += 1

        # prevents out of bounds insertion unless at the end(next to the last Node)
        if (prev is None) or (curr_index != index): 
            raise IndexError("Index out of bounds")

        print(f"{prev} | {curr}")

        # Insert in the middle or end
        prev.next = insert_head
        insert_tail.next = curr
        if curr is None:       # incase of inserting at the end
            self.__tail = insert_tail

    # translates a list into a Linkedlist, returning the head and tail in tuple form
    def __listToLinkedList(self, values: list[any]) -> tuple[Node, Node] | None:

        if not values:  # if values is an empty list
            raise ValueError("Cannot create LinkedList from an empty list")
        
        head = Node(values[0]) # first element becomes the head
        prev = head

        for item in values[1:]: # after the first element, create a chain of nodes
            newNode = Node(item)
            prev.next = newNode
            prev = newNode
        
        return head, prev # return head and tail reference as a tuple

    # validates the argument if its a Node object
    def __checkIfValidNode(self, obj) -> bool:
        return isinstance(obj, Node)


if __name__ == "__main__":
    ll2 = Linkedlist([1, 2, 5])
    print(ll2)
    ll2.insert(3, Node(15))
    print(ll2)