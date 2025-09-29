function solution(picture, k) {
  const result = [];

  for (const line of picture) {
    const width = [...line].map(c => c.repeat(k)).join('');
    for (let i = 0; i < k; i++) {
      result.push(width);
    }
  }

  return result;
}