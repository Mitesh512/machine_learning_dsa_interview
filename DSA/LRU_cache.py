"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

An LRU Cache is a data structure that stores a fixed number of items (with a capacity limit) and ensures that the 
least recently used item is removed when the cache is full and a new item needs to be added. It supports two main operations:
Get(key): Retrieve the value associated with a key if it exists, and mark the key as "recently used."

Put(key, value): Insert or update a key-value pair. If the cache is full, remove the least recently used item before adding the new one.


Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Why Use a Doubly Linked List?
To implement an LRU Cache efficiently, we need:
O(1) time complexity for both get and put operations.

A way to track the order of usage (most recently used to least recently used).

A way to quickly remove or move items (e.g., remove the least recently used item or move an accessed item to the "most recently used" position).


cache:
A hash map to store key-value pairs, where the key maps to a node in the doubly linked list. This gives us O(1) lookups.
Hash Map: Maps keys to their corresponding nodes in the list, e.g., 
{key1: Node1, key2: Node2, key3: Node3}.


A doubly linked list to maintain the order of elements:
    - The head (or front) holds the most recently used item.
    - The tail (or end) holds the least recently used item.

A capacity to limit the number of items in the cache.

[Head] <-> [Node1] <-> [Node2] <-> [Node3] <-> [Tail]

Remove the node before the tail (least recently used).
Add the new node after the head.



"""
# Create a doubly linked list
class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key : DLL
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)

        # add head and tail
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # if this key is used then it becomes most recent used
            self.move_to_head(node)
            return node.val
        else:
            return -1
    
    def add(self,node):
        # TODO : add node next to head
        # head <--> some_node
        # head <--> node <--> some_node
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
    
    def remove(self,node):
        # TODO: remove node from any place in the DLL
        # some_node <--> node <--> some_node <--> tail
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def move_to_head(self,node):
        # TODO : given any node take it from DLL any place put it in from most recently used
        self.remove(node)
        self.add(node)

    def put(self, key: int, value: int) -> None:
        # If key is already there
        # I will first remove the key from whichever location it is there
        # put it in the most recent used from head
        if key in self.cache:
            node = self.cache[key]
            # update with latest value
            node.val = value
            self.move_to_head(node)
        else:
            new_node = Node(key,value)
            self.cache[key] = new_node
            # add node to head linked list
            self.add(new_node)

            # check capacity
            if len(self.cache) > self.capacity:
                # Now I need to remove least recently used node from cache
                lru = self.tail.prev
                self.remove(lru)
                # delete this node lru from cache so it is again in capacity
                del self.cache[lru.key]
            

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)