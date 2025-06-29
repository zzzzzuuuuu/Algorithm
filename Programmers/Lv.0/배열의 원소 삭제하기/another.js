function solution(arr, del)  {
  return arr.filter(n => !del.includes(n));
}