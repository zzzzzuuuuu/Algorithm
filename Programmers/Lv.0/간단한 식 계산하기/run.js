function solution(b) {
  const l = b.split(' ');
  const n1 = parseInt(l[0]);
  const op = l[1];
  const n2 = parseInt(l[2])

  let result = 0;
  switch (op) {
    case '+':
      result = n1 + n2;
      break;
    case '-':
      result = n1 - n2;
      break;
    case '*':
      result = n1 * n2;
      break;
  }
  return result;
}