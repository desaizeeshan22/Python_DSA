class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        if head is not None:
            self.size = 1

    def insert(self, value):
        if not self.head:
            self.head = Node(value)
            return self.head
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(value)
        self.size += 1

    def removeByValue(self, value):
        Dummy = Node(-1)
        Dummy.next = self.head
        prev, curr = Dummy, self.head
        while curr:
            if curr.value == value:
                temp = curr.next
                prev.next = temp
                curr = temp
                self.size -= 1
            else:
                prev = curr
                curr = curr.next
        return Dummy.next

    def removeKthNode(self, k):
        i = 0
        if self.size > k:
            return self.head
        Dummy = Node(-1)
        Dummy.next = self.head
        prev = Dummy
        while i < k:
            prev = prev.next
            i += 1
        prev.next = prev.next.next
        return Dummy.next
