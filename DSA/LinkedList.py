class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
        
    def insert_at_position(self,data,position):
        if position <0:
            # invalid case
            return 

        if position==0:
            self.insert_at_beginning(data)
            return 

        new_node = Node(data)
        
        curr_node = self.head
        curr_pos = 1
        while curr_node and curr_pos<position:
            curr_node = curr_node.next
            curr_pos += 1
        if curr_node is None:
            print("position is out of range")
            return
        
        new_node.next = curr_node.next
        curr_node.next = new_node
    
    
    # def delete_node(self,data):
        
    #     curr_node = self.head
        
    #     while curr_node and curr_node.data==data:
    
    def display(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.val, end="-->")
            curr_node = curr_node.next
        print("None")


my_list = LinkedList()
my_list.insert_at_end(1)
my_list.insert_at_end(2)
my_list.insert_at_beginning(0)
my_list.insert_at_position(3, 2)
my_list.display() # Output: 0 -> 1 -> 3 -> 2 -> None
# my_list.delete_node(3)
# my_list.display() # Output: 0 -> 1 -> 2 -> None  
        
        
        
        
        







"""
You're designing a service dependency visualizer at Google. 
Each service is represented as a node in a linked list, 
and dependencies are represented via the next pointer.
Due to a misconfiguration, 
some services are forming cyclic dependencies. 
You are given the head of a singly linked list. 
Your task is to determine if there's a cycle in the list.
"""




