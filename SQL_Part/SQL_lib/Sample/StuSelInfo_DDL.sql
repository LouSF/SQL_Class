CREATE TABLE [dbo].[StuSelInfo] (
  [StuNum] char(10) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [CourseNo] char(10) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [StuScoreS] int  NOT NULL,
  CONSTRAINT [StuNum_StuSelInfo_F] FOREIGN KEY ([StuNum]) REFERENCES [dbo].[StuInfo] ([StuNum]) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT [CourseNo_StuSelInfo_F] FOREIGN KEY ([CourseNo]) REFERENCES [dbo].[Course] ([CourseNo]) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT [StuScoreS_StuSelInfo_Check] CHECK ([StuScoreS]<=(100) AND [StuScoreS]>=(0))
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[StuSelInfo] SET (LOCK_ESCALATION = TABLE)
GO

CREATE TRIGGER [dbo].[Change_StuSel_TRG]
ON [dbo].[StuSelInfo]
WITH EXECUTE AS CALLER
FOR INSERT, UPDATE, DELETE
AS
BEGIN
    -- 更新总分和其他信息
    MERGE INTO Rank AS target
    USING (
        SELECT
            StuInfo.StuNum,
            SUM(StuSelInfo.StuScoreS) AS total_score,
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