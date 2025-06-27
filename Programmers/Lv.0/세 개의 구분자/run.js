function solution(myStr) {
  const result = myStr.split(/[abc]/).filter(Boolean); // filter(str => str);
  return result.length > 0 ? result : ["EMPTY"];
}