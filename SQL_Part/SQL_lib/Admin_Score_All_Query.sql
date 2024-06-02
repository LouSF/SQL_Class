SELECT
	StuInfo.StuNum,
	StuInfo.StuName,
	StuInfo.StuClass,
	Course.CourseName,
	StuSelInfo.StuScoreS
FROM
	StuSelInfo
	JOIN StuInfo ON StuSelInfo.StuNum = StuInfo.StuNum
	JOIN Course ON StuSelInfo.CourseNo = Course.CourseNo
	JOIN Rank ON StuSelInfo.StuNum = Rank.StuNum