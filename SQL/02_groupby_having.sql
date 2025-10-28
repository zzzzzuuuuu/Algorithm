SELECT 과목, MIN(점수) AS 최소점수, MAX(점수) AS 최대점수
FROM 성적
GROUP BY 과목
HAVING AVG(점수) >= 90;
