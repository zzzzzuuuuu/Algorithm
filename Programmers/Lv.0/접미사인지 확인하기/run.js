function solution(my_string, is_suffix) {
  let my_list = [];
  for (let i = my_string.length; i > 0; i--) {
    my_list.push(my_string.slice(-i));
  }
  return +my_list.includes(is_suffix);
}