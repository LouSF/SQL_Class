CREATE TABLE [dbo].[Rank] (
  [StuNum] char(10) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [StuName] varchar(10) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [StuClass] varchar(20) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [StuScoreA] int  NULL,
  [StuRank] int  NULL,
  CONSTRAINT [PK__Rank__D9EEA6166CA0FBB7] PRIMARY KEY NONCLUSTERED ([StuNum])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = OFF, ALLOW_PAGE_LOCKS = OFF)
ON [PRIMARY],
  CONSTRAINT [StuNum_Rank_F] FOREIGN KEY ([StuNum]) REFERENCES [dbo].[StuInfo] ([StuNum]) ON DELETE CASCADE ON UPDATE CASCADE
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[Rank] SET (LOCK_ESCALATION = TABLE)