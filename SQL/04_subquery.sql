SELECT 제품명, 단가, 제조사
FROM 제품
WHERE 단가 > ALL (
  SELECT 단가
  FROM 제품
  WHERE 제조사 = 'C'
);