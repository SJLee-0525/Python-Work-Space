import fs from "fs"

const input = Number(fs.readFileSync("input.txt").toString().trim())
console.log(input / 4)
