EXEC sp_refreshview 'Student_Score_View'
SELECT
	*
FROM
	Student_Score_View
WHERE
	StuNum = ?
	AND CourseNo = ?