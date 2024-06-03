-- Stop USE because In VIEW

-- SELECT
-- 	StuInfo.StuNum,
-- 	StuInfo.StuName,
-- 	StuInfo.StuClass,
-- 	Course.CourseName,
-- 	StuSelInfo.StuScoreS
-- FROM
-- 	StuSelInfo
-- 	JOIN StuInfo ON StuSelInfo.StuNum = StuInfo.StuNum
-- 	JOIN Course ON StuSelInfo.CourseNo = Course.CourseNo
-- 	JOIN Rank ON StuSelInfo.StuNum = Rank.StuNum
EXEC sp_refreshview 'Student_Score_View'
SELECT
	*
FROM
	Student_Score_View
WHERE
	StuNum LIKE ?
	OR StuName LIKE ?
	OR StuClass LIKE ?
	OR CourseName LIKE ?
	OR CourseNo LIKE ?
	OR StuScoreS LIKE ?