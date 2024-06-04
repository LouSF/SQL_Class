CREATE TABLE [dbo].[StuInfo] (
  [StuNum] char(10) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [StuName] char(10) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [StuSex] varchar(4) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [StuClass] varchar(20) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [StuAge] int  NOT NULL,
  CONSTRAINT [PK__StuInfo__D9EEA61697FF3BBB] PRIMARY KEY NONCLUSTERED ([StuNum])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = OFF, ALLOW_PAGE_LOCKS = OFF)
ON [PRIMARY],
  CONSTRAINT [StuAge_StuInfo_Check] CHECK ([StuAge]<(100) AND [StuAge]>(0)),
  CONSTRAINT [StuNum_StuInfo_Check] CHECK ([StuNum] like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[StuInfo] SET (LOCK_ESCALATION = TABLE)
GO

CREATE TRIGGER [dbo].[Change_StuInfo_TRG]
ON [dbo].[StuInfo]
WITH EXECUTE AS CALLER
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