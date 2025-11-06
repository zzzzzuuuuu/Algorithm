-- 테이블 생성
CREATE TABLE 부서 (
  부서코드 INT PRIMARY KEY,
  부서명 VARCHAR(20)
);

CREATE TABLE 직원 (
  직원코드 INT PRIMARY KEY,
  부서코드 INT,
  직원명 VARCHAR(20),
  FOREIGN KEY (부서코드) REFERENCES 부서(부서코드)
    ON DELETE CASCADE
);

-- 데이터 삽입
INSERT INTO 부서 VALUES (10, '영업부');
INSERT INTO 부서 VALUES (20, '기획부');
INSERT INTO 부서 VALUES (30, '개발부');

INSERT INTO 직원 VALUES (1001, 10, '이진수');
INSERT INTO 직원 VALUES (1002, 10, '곽연정');
INSERT INTO 직원 VALUES (1003, 20, '김설진');
INSERT INTO 직원 VALUES (1004, 20, '최민수');
INSERT INTO 직원 VALUES (1005, 20, '이문주');
INSERT INTO 직원 VALUES (1006, 30, '박종미');
INSERT INTO 직원 VALUES (1007, 30, '박미경');

-- 삭제 전 부서코드 20의 직원 수 확인
SELECT DISTINCT COUNT(부서코드) FROM 직원 WHERE 부서코드 = 20;

-- 부서 삭제 (ON DELETE CASCADE 작동)
DELETE FROM 부서 WHERE 부서코드 = 20;

-- 삭제 후 부서코드 수 확인
SELECT DISTINCT COUNT(부서코드) FROM 직원;
