function solution(board, k) {
  let result = 0;
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) { // board[i] 주의
      if (i + j <= k) result += board[i][j];
    }
  }
  return result;
}