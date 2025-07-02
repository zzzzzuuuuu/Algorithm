function solution(num_list) {
  let count = 0;
  num_list.forEach(n => {
    let r = n;
    while (r !== 1) {
      r = r % 2 === 0 ? r / 2 : (r - 1) / 2;
      count++;
    }
  })
  return count;
}