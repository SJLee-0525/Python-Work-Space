let fs = require("fs")
const input = fs.readFileSync("/dev/stdin").toString().trim().split("")

class Node {
  constructor(value) {
    this.value = value
    this.next = null
    this.prev = null
  }
}

class Deque {
  constructor() {
    this.init()
  }

  init() {
    this.count = 0
    this.front = null
    this.rear = null
  }

  appendLeft(value) {
    const node = new Node(value)

    if (!this.front) {
      this.front = node
      this.rear = node
    } else {
      const cachedPrevFront = this.front
      cachedPrevFront.prev = node
      this.front = node
      node.next = cachedPrevFront
    }
    this.count++
    return this.count
  }

  popleft() {
    if (this.count === 0) {
      return null
    }

    const value = this.front.value
    if (this.count === 1) {
      this.init()
    } else {
      this.front = this.front.next
      this.front.prev = null
      this.count--
    }
    return value
  }

  append(value) {
    const node = new Node(value)

    if (this.count === 0) {
      this.front = node
      this.rear = node
    } else {
      const cachedPrevRear = this.rear
      cachedPrevRear.next = node
      node.prev = cachedPrevRear
      this.rear = node
    }
    this.count++
    return this.count
  }

  pop() {
    if (this.count === 0) {
      return null
    }

    const value = this.rear.value
    if (this.count === 1) {
      this.init()
    } else {
      this.rear = this.rear.prev
      this.rear.next = null
      this.count--
    }
    return value
  }

  size() {
    return this.count
  }

  getValue(index) {
    if (index < 0 || index >= this.count) {
      return -1
    }

    let node = this.front
    for (let i = 0; i < index; i++) {
      node = node.next
    }
    return node.value
  }
}
