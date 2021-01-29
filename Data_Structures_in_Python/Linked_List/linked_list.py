'''Linked List data structure, implements: Iterable'''
from node import Node

class LinkedList():
    '''Class representing a linked list'''
    def __init__(self):
        self.head = None
        self.current_iter = None    #Helper variable for capturing current state
    
    def append(self,node):
        '''Appends node to the end of the list'''
        node.next = self.head
        self.head = node
       
    def remove(self,item):
        '''Removes item from list. Throws exception when empty or item not found'''
        
        #Case 1: empty list
        if self.head == None:
            raise LookupError("Item not in list")

        #Case 2: head deleted
        if self.head.data == item:
            self.head = self.head.next
            return True
        
        #Case 3: rest of nodes
        self.current_iter = self.head
        while self.current_iter.next != None:
            nextNode = self.current_iter.next
            if nextNode.data == item:
                self.current_iter.next = nextNode.next
                return True
            else:
                self.current_iter = self.current_iter.next
        else:
            raise LookupError("Item not in list")
    
    def __eq__(self,other):
        '''Checks if given linked list is equal to caller object'''        
        #case 1: different types
        if type(self) != type(other):
            return False
        
        #fetch head of both lists
        self.current_iter = self.head
        other.current_iter = other.head
        
        #iterate validating all nodes of the lists are identical and in same order
        while self.current_iter != None and other.current_iter != None:
            if self.current_iter != other.current_iter:
                return False
            else:
                self.current_iter = self.current_iter.next
                other.current_iter = other.current_iter.next
        
        if self.current_iter != None and other.current_iter != None:
                return False
        else:
            return True
    
    #Iterable methods '__iter__' and '__next__' are implemented below
    def __iter__(self):
        self.current_iter = self.head
        return self
    
    def __next__(self):
        if self.current_iter != None:
            data = self.current_iter.data
            self.current_iter = self.current_iter.next
            return data
        raise StopIteration
        
    def __str__(self):
        s = "]"
        temp = self.head
        while temp != None:
            s = "," + str(temp.data) + s
            temp = temp.next
        else:
            s = "[" + s
        return s.replace(',' , '' , 1)
    
    def from_iterable(self,iterable):
        '''Converts the given Iterable to a linked list'''
        iterable = iterable.__iter__()
        try:
            while True:
                next = iterable.__next__()
                self.append(Node(next))
        except StopIteration:
            return self
            
if __name__ == "__main__":
    
    from tests_Linked_list import run_tests
    
    if run_tests():
        print("All tests passed.")
    