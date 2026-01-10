function solution(s) {
  const result = [];
  const last = {};

  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (!(c in last)) {
      result.push(-1);
      last[c] = i;
    } else {
      result.push(i - last[c]);
      last[c] = i;
    }
  }

  return result;

}