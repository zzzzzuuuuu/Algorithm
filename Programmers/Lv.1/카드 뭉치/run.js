function solution(cards1, cards2, goal) {
  let idx1 = 0, idx2 = 0;

  for (const g of goal) {
    if (g === cards1[idx1]) idx1++;
    else if (g === cards2[idx2]) idx2++;
    else return "No"
  }

  return "Yes";
}