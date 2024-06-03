SELECT
	*
FROM
	StuInfo
WHERE
	StuNum LIKE ?
	OR StuName LIKE ?
	OR StuSex LIKE ?
	OR StuClass LIKE ?
	OR StuAge LIKE ?