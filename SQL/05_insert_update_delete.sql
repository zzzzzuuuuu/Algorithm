INSERT INTO 사원 (사원번호, 이름, 주소, 부서)
VALUES (32431, '정실기', '서울', '영업');

INSERT INTO 부서 (사원번호, 이름, 주소, 부서)
SELECT 사원번호, 이름, 나이, 23
FROM 사원
WHERE 이름 = '정실기';

UPDATE 사원
SET 부서 = '퇴사'
WHERE 사원번호 = 32431;

SELECT * FROM 사원;
