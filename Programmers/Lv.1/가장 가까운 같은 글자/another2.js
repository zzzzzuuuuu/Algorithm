function solution(s) {
  [...s].map((v, i) => {
    const count = s.slice(0, i).lastIndexOf(v);
    return count < 0 ? count : i - count;
  })
}