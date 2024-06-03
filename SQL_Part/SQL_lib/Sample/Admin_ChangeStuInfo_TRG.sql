-- Do not use in there! This is a Sample

CREATE TRIGGER [dbo].[Change_StuInfo_TRG]
ON [dbo].[StuInfo]
FOR INSERT, UPDATE, DELETE
AS
BEGIN
    -- 更新总分和其他信息
    MERGE INTO Rank AS target
    USING (
        SELECT
            StuInfo.StuNum,
            ISNULL(SUM(StuSelInfo.StuScoreS), 0) AS total_score,
            StuInfo.StuName,
            StuInfo.StuClass
        FROM
            StuInfo
        LEFT JOIN
            StuSelInfo ON StuInfo.StuNum = StuSelInfo.StuNum
        GROUP BY
            StuInfo.StuNum, StuInfo.StuName, StuInfo.StuClass
    ) AS source (StuNum, total_score, StuName, StuClass)
    ON (target.StuNum = source.StuNum)
    WHEN MATCHED THEN
        UPDATE SET
            target.StuScoreA = source.total_score,
            target.StuName = source.StuName,
            target.StuClass = source.StuClass
    WHEN NOT MATCHED BY TARGET THEN
        INSERT (StuNum, StuScoreA, StuName, StuClass)
        VALUES (source.StuNum, source.total_score, source.StuName, source.StuClass)
    WHEN NOT MATCHED BY SOURCE THEN
        DELETE;

    -- 初始化排名变量
    DECLARE @rank INT = 0;

    -- 更新所有学生的排名
    WITH RankedScores AS (
        SELECT
            StuNum,
            StuScoreA,
            RANK() OVER (ORDER BY StuScoreA DESC) AS rank
        FROM
            Rank
    )
    UPDATE Rank
    SET StuRank = RankedScores.rank
    FROM Rank
    JOIN RankedScores ON Rank.StuNum = RankedScores.StuNum;
END;