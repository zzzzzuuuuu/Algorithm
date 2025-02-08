function solution(num_list) {
  return num_list.sort((a, b) => a - b).slice(5); // slice는 원본 변경X, splice는 변경
}