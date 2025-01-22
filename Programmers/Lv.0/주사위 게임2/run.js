function solution(a, b, c) {
  const result1 = a + b + c;
  const result2 = a**2 + b**2 + c**2;
  const result3 = a**3 + b**3 + c**3;

  if (a !== b && a !== c && b !== c) {
    return result1;
  } else if (a === b && b === c && a === c) {
    return result1 * result2 * result3;
  } else return result1 * result2;
}