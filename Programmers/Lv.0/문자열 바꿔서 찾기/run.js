function solution(myString, pat) {
  return Number(myString
    .split('')
    .map(c => c === 'A' ? 'B' : c === 'B' ? 'A' : c)
    .join('')
    .includes(pat));
}