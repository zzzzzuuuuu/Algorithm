function solution(a, b, c, d) {
  const count = {};

  for (const x of [a, b, c, d]) {
    count[x] = (count[x] || 0) + 1;
  }

  const entries = Object.entries(count);
  const len = entries.length;

  if (len === 1) {
    const [[p, _]] = entries;
    return 1111 * Number(p);
  }

  if (len === 2) {
    const [[p1, c1], [p2, c2]] = entries.map(([k, v]) => [Number(k), v]);
    if (c1 === 3 || c2 === 3) {
      const p = c1 === 3 ? p1 : p2;
      const q = c1 === 1 ? p1 : p2;
      return (10 * p + q) ** 2;
    } else {
      return (p1 + p2) * Math.abs(p1 - p2);
    }
  }

  if (len === 3) {
    const one = entries.filter(([_, v]) => v === 1).map(([k, _]) => Number(k));
    return one[0] * one[1];
  }

  if (len === 4) {
    return Math.min(a, b, c, d);
  }
}