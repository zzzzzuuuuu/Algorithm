function solution(n, m, section) {
  let i = 0, count = 0;

  while (i < section.length) {
    const start = section[i];
    const end = start + m - 1;

    while (i < section.length && section[i] <= end) i++;
    count++;
  }

  return count;
}