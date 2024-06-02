-- Do not use in there. This is a Sample!
CREATE TRIGGER DeleteStudent_TRG
ON StuInfo
FOR DELETE
AS
BEGIN
    DELETE FROM Rank
    WHERE StuNum IN (SELECT StuNum FROM DELETED);

    DELETE FROM StuSel
    WHERE StuNum IN (SELECT StuNum FROM DELETED);
END;