class Node {
  constructor(value = "") {
    this.value = value
    this.child = new Map()
  }
}

class Trie {
  constructor() {
    this.root = new Node()
  }

  insert(directory) {
    let curRoot = this.root

    for (let d = 0; d < directory.length; d++) {
      if (!curRoot.child.has(directory[d])) {
        curRoot.child.set(directory[d], new Node(directory[d]))
      }
      curRoot = curRoot.child.get(directory[d])
    }
  }

  printTree() {
    const root = this.root
    this._printTree(root, 0)
  }

  _printTree(curRoot, depth) {
    const sortedChilds = [...curRoot.child].sort((a, b) => a[0].localeCompare(b[0]))
    for (let s = 0; s < sortedChilds.length; s++) {
      results.push(" ".repeat(depth) + sortedChilds[s][0])
      this._printTree(sortedChilds[s][1], depth + 1)
    }
  }
}

// --------------------------------------------------------------------------------------------

const fs = require("fs")
const input = fs.readFileSync("/dev/stdin").toString().trim().replaceAll("\r", "").split("\n")

const N = Number(input[0])
const trieTree = new Trie()

for (let n = 1; n <= N; n++) {
  const directory = input[n].split("\\")
  trieTree.insert(directory)
}

const results = []
trieTree.printTree()

console.log(results.join("\n"))
