function solution(n, m, sections) {
  let count = 0;
  let painted = 0;

  for (let section of sections) {
    if (painted < section) { // if문은 스코프가 아니기 때문에 if문 안에서 바꾼 painted 값은 if문을 나간 후에도 그대로 유지됨.
      count++;
      painted = section + m - 1;
    }
  }

  return count;
}