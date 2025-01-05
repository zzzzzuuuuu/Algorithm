const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('close', function () {
  console.log("!@#$%^&*(\\'" + '"<>?:;');
});

// 백틱으로 감싸는 게 더 베스트일듯하다