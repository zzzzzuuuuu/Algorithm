function solution(number, limit, power) {
  let power_list = [];

  for (let i = 1; i <= number; i++) {
    let count = 0;
    for (let j = 1; j * j <= i; j++) {
      if (j*j === i) count += 1;
      else if (i % j === 0) count += 2;
    }
    power_list.push(count);
  }

  return power_list.reduce((acc, cur) => acc + (cur > limit ? power : cur), 0);
}