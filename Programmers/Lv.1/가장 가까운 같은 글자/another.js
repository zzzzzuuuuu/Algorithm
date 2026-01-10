function solution(s) {
  const hash = {};

  return [...s].map((v, i) => {
    let result = hash[v] === undefined ? -1 : i - hash[v];
    hash[v] = i;
    return result;
  })
}