function solution(arr) {
  let x = 0;
  let prevArr = [...arr];

  while (true) {
    let newArr = prevArr.map(v => {
      if (v >= 50 && v % 2 === 0) return v / 2;
      else if (v < 50 && v % 2 === 1) return v * 2 + 1;
      else return v;
    });

    if (prevArr.every((v, i) => v === newArr[i])) {
      return x;
    }

    prevArr = newArr;
    x++;
  }
}