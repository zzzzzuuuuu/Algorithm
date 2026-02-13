function solution(s) {
  return s
    .split(' ')
    .map(v =>
      v.split('')
        .map((c, i) => i % 2 ? c.toLowerCase() : c.toUpperCase())
        .join('')
    )
    .join(' ');
}