function solution(my_string) {
  let al = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
  let a = Array(52).fill(0);

  my_string.split("").map(n => {
    a[al.indexOf(n)]++;
  })

  return a;
}