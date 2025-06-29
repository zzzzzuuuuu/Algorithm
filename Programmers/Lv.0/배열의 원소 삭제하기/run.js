function solution(arr, delete_list) {
  const result = [];
  arr.forEach(n => {
    if (!delete_list.includes(n)) result.push(n);
  });
  return result;
}