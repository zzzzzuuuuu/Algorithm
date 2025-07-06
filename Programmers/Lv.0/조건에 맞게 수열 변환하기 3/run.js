function solution(arr, k) {
  return k % 2 === 0 ? [...arr.map(n => n+k)] : [...arr.map(n => n*k)]; // spread 없이 그냥 바로 arr.map()도 가능
}