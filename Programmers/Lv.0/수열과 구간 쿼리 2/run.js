function solution(arr, queries) {
  const result = [];

  for (const [s, e, k] of queries) {
    let temp = [];
    for (let i = s; i <= e; i++) {
      if (arr[i] > k) temp.push(arr[i]);
    }
    result.push(temp.length ? Math.min(...temp) : -1)
  }
  return result;
}