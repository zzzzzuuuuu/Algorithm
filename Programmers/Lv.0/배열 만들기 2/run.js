function solution(l, r) {
  const result = [];

  function dfs(cur) {
    const num = Number(cur);
    if (num > l) return;
    if (num >= l) result.push(num);
    dfs(cur + '0');
    dfs(cur + '5');
  }
  dfs('5');

  return result.length ? result.sort((a, b) => a - b) : [-1];
}