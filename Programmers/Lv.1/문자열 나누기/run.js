function solution(string) {
  let result = 0;
  let i = 0;

  while (i < string.length) {
    let s = string[i];
    let x = 0, y = 0;

    while (i < string.length) {
      if (s === string[i]) x++;
      else y++;

      i++;

      if (x === y) break;
    }

    result++;
  }


  return result;
}