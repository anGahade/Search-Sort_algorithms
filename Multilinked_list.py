class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


first = Node(1)
second = Node(2)
third = Node(3)
first.next = second
second.next = third
second.prev = first
third.next = first
third.prev = second

print(first.next.data)
print(second.next.data)
print(third.next.data)
print(second.prev.data)
print(third.prev.data)