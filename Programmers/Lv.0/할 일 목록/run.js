function solution(todo_list, finished) {
  let result = [];
  finished.map((value, index) => {
    if (!value) result.push(todo_list[index]);
  })
  return result;
}