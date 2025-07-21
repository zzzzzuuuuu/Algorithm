function solution(arr, queries) {
  queries.forEach(([s, e]) => {
    [arr[s], arr[e]] = [arr[e], arr[s]];
  });
  return arr;
}