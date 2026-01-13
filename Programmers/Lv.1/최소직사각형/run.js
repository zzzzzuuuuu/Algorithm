function solution(sizes) {
  const size = [...sizes].map(s => {
    return s.sort((a, b) => a - b);
  });

  const result = size.reduce((acc, cur) => {
    acc[0] = Math.max(acc[0], cur[0]);
    acc[1] = Math.max(acc[1], cur[1]);
    return acc;
  }, [0, 0]);

  return result[0] * result[1];
}