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
  str.forEach((s, i) => {
    if (s === s.toUpperCase()) {
      str[i] = s.toLowerCase();
    } else {
      str[i] = s.toUpperCase();
    }
  });
  console.log(str.join(''));
});