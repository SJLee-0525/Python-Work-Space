class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, data):
        self.head = ListNode(data)

    def print_list(self):
        cnt = 0
        node = self.head
        while cnt < 10:
            print(node.data, end=' ')
            node = node.next
            cnt += 1
        print()

    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    def append_data(self, data):
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = ListNode(data)

    def delete_data(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index - 1)
        node.next = node.next.next

    def insert_data(self, index, data):
        newNode = ListNode(data)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        node = self.get_node(index - 1)
        nextNode = node.next
        node.next = newNode
        newNode.next = nextNode

#########################################################
from collections import deque

for tc in range(1, 11):
    N = int(input())
    init_input = list(map(int, input().split()))

    linked_list = LinkedList(init_input[0])
    for i in range(1, N):
        linked_list.append_data(init_input[i])

    P = int(input())
    prompt_input = deque(list(input().split()))

    while prompt_input:
        currPrompt = prompt_input.popleft()
        if currPrompt == 'I':
            targetIndex = int(prompt_input.popleft())
            targetCnt = int(prompt_input.popleft())
            for cnt in range(targetCnt):
                linked_list.insert_data(targetIndex, int(prompt_input.popleft()))
                targetIndex += 1

        elif currPrompt == 'D':
            targetIndex = int(prompt_input.popleft())
            targetCnt = int(prompt_input.popleft())
            for cnt in range(targetCnt):
                linked_list.delete_data(targetIndex)

        else: # A
            targetCnt = int(prompt_input.popleft())
            for cnt in range(targetCnt):
                linked_list.append_data(int(prompt_input.popleft()))

    print(f'#{tc}', end=' ')
    linked_list.print_list()
