function solution(s, n) {
  return s.split('').map(c => {
    if (c === ' ') return c;

    const code = c.charCodeAt(0);
    const base = (code >= 65 && code <= 90) ? 65 : 97;
    const newCode = (code - base + n) % 26 + base;

    return String.fromCharCode(newCode);
  }).join('');
}