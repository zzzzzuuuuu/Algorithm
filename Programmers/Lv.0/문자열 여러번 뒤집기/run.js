function solution(my_string, queries) {
  const arr = my_string.split('');

  for (const [s, e] of queries) {
    let i = s, j = e;
    while (i < j) {
      [arr[i], arr[j]] = [arr[j], arr[i]];
      i++; j--;
    }
  }

  return arr.join('');
}