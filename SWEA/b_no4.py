class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, data):
        self.head = ListNode(data)

    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    def append_node(self, data):
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = ListNode(data)

    def insert_node(self, index, data):
        newNode = ListNode(data)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        node = self.get_node(index - 1)
        nextNode = node.next
        node.next = newNode
        newNode.next = nextNode

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        node = self.get_node(index - 1)
        node.next = node.next.next

    def change_node(self, index, data):
        node = self.get_node(index)
        node.data = data

    def print_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index and node is not None:
            cnt += 1
            node = node.next
        if cnt == index:
            print(node.data)
        else:
            print(-1)

    def check_print(self):
        node = self.head
        while node is not None:
            print(node.data, end=' ')
            node = node.next


##################################################################

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    # N 수열의 길이, M 추가 횟수, L 출력할 번호

    arr = list(map(int, input().split()))
    linked_list = LinkedList(arr[0])
    for i in range(1, N):
        linked_list.append_node(arr[i])

    # linked_list.check_print()

    for _ in range(M):
        prompt, *pArr = input().split()
        if prompt == 'I':
            index, data = map(int, pArr)
            linked_list.insert_node(index, data)
        elif prompt == 'D':
            index = int(pArr[0])
            linked_list.delete_node(index)
        else:
            index, data = map(int, pArr)
            linked_list.change_node(index, data)

    print(f'#{tc}', end=' ')
    linked_list.print_node(L)