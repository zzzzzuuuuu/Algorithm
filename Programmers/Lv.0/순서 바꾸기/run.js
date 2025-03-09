function solution(num_list, n) {
  const list1 = num_list.slice(0, n);
  const list2 = num_list.slice(n);
  return list2.concat(list1);
}