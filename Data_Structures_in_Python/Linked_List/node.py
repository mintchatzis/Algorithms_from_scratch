class Node():
    '''Class representing a Node of a LinkedList'''
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next
        
    def __str__(self):
        return str(self.data)
    
    def __eq__(self,other):
        if type(self) != type(other):
            return False
        if self.data == other.data and self.next == other.next:
            return True
        else:
            return False

if __name__ == "__main__":
    
    tests = []
    
    #test Node initialization
    def test_node_creation():
        node = Node()
        assert node != None, "Initialized node object should not point to None"
        assert node.data == None and node.next == None, "Zero argument initialization of Node should have NoneType next and data instance variables"
        node = Node(1)
        assert node != None, "Initialized node object should not point to None"
        assert node.data == 1 and node.next == None, "1 argument initialization of Node should store the data given and have 'next' variable point to None"
        node = Node(2,Node(1))
        assert node.data == 2 and node.next != None, "2 argument initialization of Node should store the data given and point to next non-None Node object"
    tests.append(test_node_creation)
    
    def test_node_equality_method():
        #test case:different types
        node1 = Node()
        node2 = None
        assert node1 != node2, "Objects of different type should not be perceived as equal"

        #test case:default 0 argument initialization
        node1 = Node()
        node2 = Node()
        assert node1 == node2, "default 0 argument initialization"

        #test case: default 1 argument intialization, same arguments
        node1 = Node(1)
        node2 = Node(1)
        assert node1 == node2, "default 1 argument intialization, same arguments"
        
        #test case: default 1 argument initialization, different data argument
        node1 = Node(1)
        node2 = Node(2)
        assert node1 != node2, "default 1 argument initialization, different data argument"

        #test case: default 2 argument initialization, same arguments
        dummy = Node(5)
        node1 = Node(1,dummy)
        node2 = Node(1,dummy)
        assert node1 == node2, "default 2 argument initialization, same arguments"
        
        #test case: default 2 argument initialization, different and NON-EQUAL 'next' argument object
        dummy = Node(3)
        other_dummy = Node(4)
        node1 = Node(1,dummy)
        node2 = Node(1,other_dummy)
        assert node1 != node2, "default 2 argument initialization, different and NON-EQUAL 'next' argument object"
        
        #test case: default 2 argument initialization, different but EQUAL 'next' argument object (recursive equality check)
        dummy = Node(3)
        other_dummy = Node(3)
        node1 = Node(1,dummy)
        node2 = Node(1,other_dummy)
        assert node1 == node2, "default 2 argument initialization, different but EQUAL 'next' argument object (recursive equality check)"
    tests.append(test_node_equality_method)
    
    
    #Run all tests
    def run_tests():
        allTestsPassed = True
        for test in tests:
            #try:
                print(f"Running test {test}")
                test()

        if allTestsPassed:
            print(f"All {len(tests)} tests passed.")

    
    run_tests()