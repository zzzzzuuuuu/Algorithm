function solution(strArr) {
  const dict = {};
  strArr.forEach(item => {
    const len = item.length;
    dict[len] = dict[len] ?? [];
    dict[len].push(item);
  })
  // Math.max는 배열을 직접 받지 않고, 개별 숫자 인수를 필요로 하므로 스프레드 연산자를 사용하여 개별요소로 펼쳐야 함
  return Math.max(...Object.values(dict).map(v => v.length));
}