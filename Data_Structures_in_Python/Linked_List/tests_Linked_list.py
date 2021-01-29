from linked_list import LinkedList
from node import Node

def run_tests():
    '''Unit tests for LinkedList class'''
    tests = []
    
    #Test initialization of class
    def test_lList_creation():
        l_lst = LinkedList()   #Initialize linked list
        assert l_lst != None, "Initialized linked list object should not point to None"
        assert l_lst.head == None, "Initialized linked list should have a head equal to None"
    tests.append(test_lList_creation)
    
    #Test append function
    def test_append():
        l_lst = LinkedList()
        node1 = Node(1,Node()) #Note that node1.next != None, but it should become None when added to the list
        
        l_lst.append(node1)
        assert l_lst.head.data == 1, "After appending, data of the head node should be equal to the data of the node appended to the list"
        assert l_lst.head.next == None, "After appending one node to an empty list, the next field of the new node should be None"
        
        node1 = l_lst.head
        node2 = Node(2,Node())
        l_lst.append(node2)
        assert l_lst.head.next == node1, "The node appended to a non-empty list should point at the previous head"
    tests.append(test_append)
    
    #Test remove function
    def test_remove():
        
        #test case: empty list
        l_lst = LinkedList()
        
        try:
            l_lst.remove(1)
        except LookupError:
            pass
        else:
            raise AssertionError("LinkedList.remove(item) should raise exception when given an empty list")
        
        #test case: item does not exist
        l_lst = LinkedList()
        l_lst.append(Node(1))
        
        try:
            l_lst.remove(2)
        except LookupError:
            pass
        else:
            raise AssertionError("LinkedList.remove(item) should raise exception when item does not exist")
        
        #test case: remove head
        l_lst = LinkedList()
        l_lst.append(Node(1))
        l_lst.append(Node(2))
        
        l_lst.remove(2)
        exp_lList = LinkedList()
        exp_lList.append(Node(1))
        
        assert l_lst == exp_lList, "After removing the head, head should be old head's next"
        
        #remove inbetween element
        l_lst = LinkedList()
        l_lst.append(Node(1))
        l_lst.append(Node(2))
        
        exp_lList = LinkedList()
        exp_lList.append(Node(2))
        l_lst.remove(1)
        
        assert l_lst == exp_lList, "Linked list after removal of inbetween element (not head)"
    tests.append(test_remove)
    
    def test_lList_equality():
        
        #test case:different types
        l1 = LinkedList()
        l2 = None
        assert l1 != l2, "Different types should not be equal"
        
        #test case:default initialization
        l1 = LinkedList()
        l2 = LinkedList()
        assert l1 == l2, "Two default initialized linked lists should be equal"
        
        #test case: two non-empty identical lists
        l1 = LinkedList()
        l1.append(Node(1))
        l2 = LinkedList()
        l2.append(Node(1))
        assert l1 == l2, "Two identical lists should be equal"
        
        #test case: two non-empty non-identical lists
        l1 = LinkedList()
        l1.append(Node(1))
        l2 = LinkedList()
        l2.append(Node(2))
        assert l1 != l2, "Two non-identical lists should not be equal"
    tests.append(test_lList_equality)
        
    allTestsPassed = True
    for test in tests:
        try:
            print(f"Running test {test}")
            test()
        except Exception as e:
            print(f"Test {test} failed with error {e})")
            allTestsPassed = False

    return allTestsPassed

if __name__ == "__main__":
    
    if run_tests():
        print("All tests passed.")
    
