function solution(food) {
  const left = food.map((v, i) => String(i).repeat(Math.floor(v / 2))).join('');

  return (left + "0" + [...left].reverse().join(''));
}