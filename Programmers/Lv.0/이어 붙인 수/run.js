function solution(num_list) {
  let even = '';
  let odd = '';
  num_list.forEach(n => {
    if (n % 2 === 0) {
      even += String(n);
    } else {
      odd += String(n);
    }
  })
  return Number(even) + Number(odd);
}