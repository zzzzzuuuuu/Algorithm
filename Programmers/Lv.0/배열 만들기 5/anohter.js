function solution2(intStrs, k, s, l) {
  return intStrs.map(v => +v.slice(s, s+l)).filter(v => v > k);
}