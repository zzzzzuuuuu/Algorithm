function solution(num_list) {
  const list = num_list.slice(-2);
  let n = 0;
  if (list[1] > list[0]) {
    n = list[1] - list[0];
  } else {
    n = list[1] * 2;
  }
  num_list.push(n);
  return num_list;
}