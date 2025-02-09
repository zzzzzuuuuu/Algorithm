function solution(arr1, arr2) {
  if (arr1.length === arr2.length) {
    result1 = arr1.reduce((a, b) => a + b, 0);
    result2 = arr2.reduce((a, b) => a + b, 0);
    return result1 === result2 ? 0 : result1 > result2 ? 1 : -1;
  } else return arr1.length > arr2.length ? 1 : -1;
}