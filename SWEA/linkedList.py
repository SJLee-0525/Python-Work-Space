class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, data):
        self.head = ListNode(data)

    def append(self, data):
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = ListNode(data)

    def printAll(self):
        node = self.head
        while node is not None:
            print(node.val, end=' ')
            node = node.next
        print()

    def getNode(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    def addNode(self, index, data):
        newNode = ListNode(data)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        node = self.getNode(index - 1)
        nextNode = node.next
        node.next = newNode
        newNode.next = nextNode

    def deleteNode(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.getNode(index - 1)
        node.next = node.next.next

L = LinkedList(1)
L.printAll()
L.append(2)
L.printAll()
L.append(3)
L.printAll()
L.append(4)
L.printAll()