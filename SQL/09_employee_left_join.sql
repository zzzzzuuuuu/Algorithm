SELECT a.코드, 이름, 동아리명
FROM 사원 a
LEFT JOIN 동아리 b ON a.코드 = b.코드;