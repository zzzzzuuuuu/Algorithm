const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input = [];

rl.on('line', function (line) {
  input = [line];
}).on('close',function(){
  str = input[0].split('');
  let result = '';
  for (let i=0; i<str.length; i++) {
    const char = str[i]
    if (str[i] === char.toUpperCase()) {
      result += char.toLowerCase();
    } else {
      result += char.toUpperCase();
    }
  }
  console.log(result);
});