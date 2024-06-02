CREATE TRIGGER DeleteStuSel_TRG
ON StuSel
AFTER DELETE
AS
BEGIN
    -- 计算总分并更新 Rank 表
    DECLARE @StuNum INT, @TotalScore INT;

    -- 获取删除的学生编号
    SELECT @StuNum = StuNum
    FROM DELETED;

    -- 计算该学生的总分
    SELECT @TotalScore = SUM(StuScoreS)
    FROM StuSel
    WHERE StuNum = @StuNum;

    -- 更新 Rank 表
    IF EXISTS (SELECT * FROM Rank WHERE StuNum = @StuNum)
    BEGIN
        UPDATE Rank
        SET TotalScore = @TotalScore
        WHERE StuNum = @StuNum;
    END
    ELSE
    BEGIN
        INSERT INTO Rank (StuNum, TotalScore)
        VALUES (@StuNum, @TotalScore);
    END

    -- 根据总分进行排名
    ;WITH Ranked AS (
        SELECT StuNum,
               TotalScore,
               RANK() OVER (ORDER BY TotalScore DESC) AS Rank
        FROM Rank
    )
    UPDATE Rank
    SET Rank = Ranked.Rank
    FROM Rank
    JOIN Ranked ON Rank.StuNum = Ranked.StuNum;
END;
