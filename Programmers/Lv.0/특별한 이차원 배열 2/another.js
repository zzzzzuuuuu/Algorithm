function solution(arr) {
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      if (arr[i][j] !== arr[j][i]) return 0; // 대각선을 기준으로 위쪽 or 아래쪽 절반만 확인하므로 더 효율적
    }
  }
  return 1;

}