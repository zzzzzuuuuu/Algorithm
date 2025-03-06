function solution(num_list) {
  let odd = 0;
  let even = 0;

  num_list.map((v, i) => {
    if (i % 2 === 0) odd += v;
    else even += v;
  })

  return odd > even ? odd : even;
}