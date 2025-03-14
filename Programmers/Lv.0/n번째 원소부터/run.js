function solution(num_list, n) {
  return num_list.slice(n-1, num_list.length); // 시작 인덱스만 적으면 자동으로 끝까지 설정 됨
}