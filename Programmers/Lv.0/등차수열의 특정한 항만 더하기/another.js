/*
* array.reduce(<콜백함수>, <초기값>);
* 콜백함수 4가지 인자 (보통 첫 2개의 인자만 필요)
* acc: 누적 값
* cur: 현재 요소 값
* currentIndex: 현재 요소의 인덱스
* array: reduce() 메서드를 호출하는 배열
 */

function solution(a, d, included) {
  return included.reduce((acc, flag, i) => {
    return flag ? acc + a + d *  i : acc
  }, 0)
}
