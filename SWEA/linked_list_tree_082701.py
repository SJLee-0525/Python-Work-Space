# 연결 리스트를 이용한 이진 트리 코드

from collections import deque

class TreeNode:
    def __init__(self, key):
        self.key = key  # 노드의 값
        self.left = None  # 왼쪽 자식 노드를 가리킴
        self.right = None  # 오른쪽 자식 노드를 가리킴

class BinaryTree:
    def __init__(self): # BinaryTree 객체가 생성될 때 호출
        self.root = None  # 기본적으로 갖는 루트 노드: None으로 설정해 비어있음을 나타냄

    # 새로운 노드를 삽입하는 함수 (레벨 순서 삽입)
    def insert(self, key):
        new_node = TreeNode(key) # TreeNode를 이용해 생성된 새 노드
        if self.root is None:  # 트리가 비어있으면 (self.root가 None인 경우)
            self.root = new_node # new_node를 루트 노드로 설정하고 반환
            return

        # 만약 트리가 비어있지 않은 경우: Deque를 사용해 레벨 순서로 트리를 탐색
        queue = deque([self.root]) # 루트 노드를 큐에 추가

        while queue: # 큐에 자료가 있는 동안
            node = queue.popleft() # 큐에서 노드를 꺼냄

            if node.left is None:    # 왼쪽 자식이 비어있으면
                node.left = new_node # 삽입
                break
            else:                       # 비어있지 않으면
                queue.append(node.left) # 왼쪽 자식을 큐에 추가해 다음 노드를 탐색할 수 있도록 함

            if node.right is None:    # 오른쪽 자식이 비어있으면
                node.right = new_node # 삽입
                break
            else:                        # 비어있지 않으면
                queue.append(node.right) # 오른쪽 자식을 큐에 추가해 다음 노드를 탐색할 수 있도록 함

    def inorder_traversal(self):
        '''중위 순회를 통해 트리의 노드들을 출력하는 함수'''
        return self._inorder_traversal(self.root, []) # (트리의 루트 노드, 결과를 저장할 리스트)

    def _inorder_traversal(self, node, result):
        if node: # 노드가 존재하면
            self._inorder_traversal(node.left, result)  # 왼쪽 서브트리의 노드를 중위 순회
            result.append(D[node.key])                  # 결과 추가
            self._inorder_traversal(node.right, result) # 오른쪽 서브 트리의 노들르 중위 순회
        return result

for tc in range(1, 11):
    N = int(input())
    D = {}
    tree = BinaryTree() # 클래스 호출

    for _ in range(N):
        node, node_v, *adjL = input().split()
        node = int(node)
        D[node] = node_v
        tree.insert(node) # 클래스 매서드

    print(f'#{tc}', ''.join(tree.inorder_traversal()))
