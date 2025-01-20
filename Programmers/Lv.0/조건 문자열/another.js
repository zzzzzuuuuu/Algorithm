const operation = {
  '>=': (n, m) => n >= m,
  '<=': (n, m) => n <= m,
  '>!': (n, m) => n > m,
  '<!': (n, m) => n < m
};

function solution(ineq, eq, n, m) {
  const op = operation[ineq + eq]; // 객체 대괄호 표기법, 객체 프로퍼티에 동적으로 접근
  return Number(op(n, m));
}