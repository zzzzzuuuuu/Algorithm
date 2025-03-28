function solution(my_string, indices) {
  return [...my_string].filter((_, index) => !indices.includes(index)).join('');
}

// my_string의 길이가 100자 제한되어 있어서 includes 사용 가능 (전체 순회, 시간복잡도 O(n*m))
// 크기가 점점 커지면 Set 이용하기 (시간복잡도 O(n))