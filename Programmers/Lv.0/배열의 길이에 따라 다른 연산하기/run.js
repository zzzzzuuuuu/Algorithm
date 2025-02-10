function solution(arr, n) {
  const startIndex = arr.length % 2 === 0 ? 1 : 0;

  for (let i = startIndex; i < arr.length; i+=2) {
    arr[i] += n;
  }

  return arr;
}