'''
Things to add:

CORE
1. append (Done)
2. prepend
3. insert
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
        res = ""
        while curr:
            res += f"[{curr.data}] -> "
            curr = curr.next

        res += "None"
        return res

    @property
    def head(self):
        return self.__head.data
    
    @property
    def tail(self):
        return self.__tail.data
    
    # appends either a Node or List to the LinkedList chain
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
    ll2 = Linkedlist([1, 2, 3, 4, 5])
    ll2.append(["Hahah", "Hoohoo"])
    ll2.append(Node(Node("Hoohoohoo")))
    print(ll2.head)
    print(ll2.tail)
    print(ll2)
    