class Node {
  constructor(value) {
    this.value = value
    this.prev = null
    this.next = null
  }
}

class Deque {
  constructor() {
    this.init()
  }

  init() {
    this.size = 0
    this.start = null
    this.end = null
  }

  append(value) {
    const node = new Node(value)

    if (this.size === 0) {
      this.start = node
      this.end = node
    } else {
      const cachedEnd = this.end
      node.prev = cachedEnd
      cachedEnd.next = node
      this.end = node
    }
    this.size++

    return
  }

  popleft() {
    if (this.size === 0) {
      return -1
    }

    const value = this.start.value

    if (this.size === 1) {
      this.init()
    } else {
      this.start = this.start.next
      this.start.prev = null
      this.size--
    }

    return value
  }

  isEmpty() {
    return this.size === 0
  }
}

function combi(lv, cnt) {
  if (cnt === 3) {
    bfs()
    return
  }

  if (lv >= possible.length) return

  path.push(possible[lv])
  combi(lv + 1, cnt + 1)
  path.pop()
  combi(lv + 1, cnt)
}

function bfs() {
  const newRoom = Room.map((innerRoom) => [...innerRoom])
  for (let p = 0; p < 3; p++) {
    newRoom[path[p][0]][path[p][1]] = 1
  }

  const queue = new Deque()
  const visited = Array.from({ length: N }, () => Array(M).fill(0))
  // Array.from({ length: N })는 N 크기의 배열을 생성,
  // () => Array(M).fill(0)는 각 배열의 요소에 대해 M 크기의 배열을 생성하고, 그 값들을 0으로 채움

  for (let v = 0; v < viruses.length; v++) {
    queue.append(viruses[v])
    visited[viruses[v][0]][viruses[v][1]] = 1
  }

  while (!queue.isEmpty()) {
    const [ci, cj] = queue.popleft()

    for (let k = 0; k < 4; k++) {
      const mi = ci + di[k]
      const mj = cj + dj[k]
      if (0 <= mi && mi < N && 0 <= mj && mj < M && visited[mi][mj] === 0 && newRoom[mi][mj] === 0) {
        visited[mi][mj] = 1
        newRoom[mi][mj] = 1
        queue.append([mi, mj])
      }
    }
  }

  const temp = newRoom.reduce((acc, row) => {
    return acc + row.reduce((rowAcc, cell) => rowAcc + (cell === 0 ? 1 : 0), 0)
  }, 0)

  if (result < temp) result = temp

  return
}

// ------------------------------------------------------------------------------------------

const di = [1, 0, -1, 0]
const dj = [0, 1, 0, -1]

const fs = require("fs")
const input = fs.readFileSync("input.txt").toString().trim().replace("\r", "").split("\n")

const [N, M] = input[0].split(" ").map(Number)

const Room = []
const viruses = []
const possible = []

for (let n = 1; n <= N; n++) {
  const line = input[n].split(" ").map(Number)
  Room.push(line)

  for (let m = 0; m < M; m++) {
    if (line[m] == 0) {
      possible.push([n - 1, m])
    } else if (line[m] === 2) {
      viruses.push([n - 1, m])
    }
  }
}

let result = -1
const path = []
combi(0, 0)

console.log(result)
