function solution(arr) {
  const r = arr.length;
  const c = arr[0].length;

  if (r > c) {
    for (let i = 0; i < r; i++) {
      while (arr[i].length < r) arr[i].push(0);
    }
  } else if (r < c) {
    for (let i = 0; i < c - r; i++) {
      arr.push(new Array(c).fill(0));
    }
  }

  return arr;
}