function solution(strArr) {
  let result = [];
  strArr.forEach(s => {
    if (!s.includes('ad')) result.push(s);
  })
  return result;
}