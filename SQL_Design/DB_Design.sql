/*
 Navicat Premium Data Transfer

 Source Server         : SQL
 Source Server Type    : SQL Server
 Source Server Version : 16004120 (16.00.4120)
 Source Host           : localhost:1433
 Source Catalog        : Big_HW
 Source Schema         : dbo

 Target Server Type    : SQL Server
 Target Server Version : 16004120 (16.00.4120)
 File Encoding         : 65001

 Date: 15/06/2024 23:29:37
*/


-- ----------------------------
-- Table structure for Course
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[Course]') AND type IN ('U'))
	DROP TABLE [dbo].[Course]
GO

CREATE TABLE [dbo].[Course] (
  [CourseNo] char(10) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [CourseName] char(40) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NULL,
  [Score] int  NULL
)
GO

ALTER TABLE [dbo].[Course] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of Course
-- ----------------------------
BEGIN TRANSACTION
GO

INSERT INTO [dbo].[Course] ([CourseNo], [CourseName], [Score]) VALUES (N'001       ', N'线形代数                            ', N'1'), (N'002       ', N'政治经济原理                      ', N'2'), (N'003       ', N'数据结构                            ', N'5'), (N'004       ', N'英语                                  ', N'4'), (N'005       ', N'C++                                     ', N'4'), (N'006       ', N'电子技术                            ', N'6'), (N'007       ', N'计算机组成原理                   ', N'5'), (N'008       ', N'计算机网络                         ', N'6'), (N'009       ', N'哲学原理                            ', N'3'), (N'010       ', N'数值分析                            ', N'3'), (N'011       ', N'体育                                  ', N'2')
GO

COMMIT
GO


-- ----------------------------
-- Table structure for Login
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[Login]') AND type IN ('U'))
	DROP TABLE [dbo].[Login]
GO

CREATE TABLE [dbo].[Login] (
  [UserName] varchar(255) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [Password] varchar(255) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [Type] bit  NOT NULL
)
GO

ALTER TABLE [dbo].[Login] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of Login
-- ----------------------------
BEGIN TRANSACTION
GO

INSERT INTO [dbo].[Login] ([UserName], [Password], [Type]) VALUES (N'1', N'260bbdc781c0a23c1504d34923baf7db', N'1'), (N'2001140101', N'c4ca4238a0b923820dcc509a6f75849b', N'0'), (N'root', N'c4ca4238a0b923820dcc509a6f75849b', N'1'), (N'root1', N'1033b10f2929052f0eeda1c60ae677d7', N'0')
GO

COMMIT
GO


-- ----------------------------
-- Table structure for Rank
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[Rank]') AND type IN ('U'))
	DROP TABLE [dbo].[Rank]
GO

CREATE TABLE [dbo].[Rank] (
  [StuNum] char(10) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [StuName] varchar(10) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [StuClass] varchar(20) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [StuScoreA] int  NULL,
  [StuRank] int  NULL
)
GO

ALTER TABLE [dbo].[Rank] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of Rank
-- ----------------------------
BEGIN TRANSACTION
GO

INSERT INTO [dbo].[Rank] ([StuNum], [StuName], [StuClass], [StuScoreA], [StuRank]) VALUES (N'2001140101', N'沈娴    ', N'1', N'825', N'17'), (N'2001140102', N'程佳    ', N'1', N'855', N'14'), (N'2001140103', N'高丽燕 ', N'1', N'926', N'3'), (N'2001140104', N'黄小微 ', N'1', N'912', N'5'), (N'2001140105', N'周非草 ', N'1', N'723', N'22'), (N'2001140106', N'金鑫    ', N'1', N'755', N'20'), (N'2001140107', N'蒋鸿翔 ', N'1', N'837', N'16'), (N'2001140108', N'王秩军 ', N'1', N'842', N'15'), (N'2001140109', N'俞健辉 ', N'1', N'759', N'19'), (N'2001140110', N'章尧丰 ', N'1', N'750', N'21'), (N'2001140111', N'王立明 ', N'1', N'877', N'12'), (N'2001140112', N'张均灿 ', N'1', N'942', N'2'), (N'2001140113', N'叶会华 ', N'1', N'923', N'4'), (N'2001140114', N'吴晓芳 ', N'1', N'897', N'8'), (N'2001140115', N'章刘燕 ', N'1', N'856', N'13'), (N'2001140116', N'韩昕    ', N'1', N'887', N'10'), (N'2001140117', N'王利峰 ', N'1', N'898', N'7'), (N'2001140118', N'梁豪文 ', N'1', N'912', N'5'), (N'2001140119', N'张琛    ', N'1', N'887', N'10'), (N'2001140120', N'汪杰    ', N'1', N'890', N'9'), (N'2001140121', N'许晨    ', N'1', N'0', N'24'), (N'2001140122', N'吉良盛 ', N'1', N'0', N'24'), (N'2001140123', N'经涛    ', N'1', N'0', N'24'), (N'2001140125', N'卢丽珍 ', N'1', N'0', N'24'), (N'2001140126', N'沈宁怡 ', N'1', N'0', N'24'), (N'2001140127', N'周丽君 ', N'1', N'0', N'24'), (N'2001140128', N'王安安 ', N'1', N'0', N'24'), (N'2001140129', N'林晓峰 ', N'1', N'0', N'24'), (N'2001140130', N'林觐民 ', N'1', N'0', N'24'), (N'2001140131', N'吴彦    ', N'1', N'0', N'24'), (N'2001140132', N'韩骏    ', N'1', N'0', N'24'), (N'2001140133', N'周建平 ', N'1', N'0', N'24'), (N'2001140134', N'应雷达 ', N'1', N'0', N'24'), (N'2001140135', N'方涛    ', N'1', N'0', N'24'), (N'2001140201', N'杜旭虹 ', N'2', N'823', N'18'), (N'2001140202', N'罗建红 ', N'2', N'0', N'24'), (N'2001140203', N'叶丹    ', N'2', N'0', N'24'), (N'2001140204', N'梁华萍 ', N'2', N'0', N'24'), (N'2001140205', N'童小成 ', N'2', N'990', N'1'), (N'2001140206', N'厉和    ', N'2', N'0', N'24'), (N'2001140207', N'沈峰    ', N'2', N'0', N'24'), (N'2001140208', N'李东    ', N'2', N'0', N'24'), (N'2001140209', N'朱雪峰 ', N'2', N'0', N'24'), (N'2001140210', N'戚军辉 ', N'2', N'0', N'24'), (N'2001140211', N'潘伟庆 ', N'2', N'0', N'24'), (N'2001140214', N'王晓维 ', N'2', N'0', N'24'), (N'2001140215', N'朱洪燕 ', N'2', N'0', N'24'), (N'2001140216', N'郑菲    ', N'2', N'0', N'24'), (N'2001140217', N'傅斌    ', N'2', N'0', N'24'), (N'2001140218', N'温从喜 ', N'2', N'0', N'24'), (N'2001140219', N'范卫峰 ', N'2', N'0', N'24'), (N'2001140220', N'陈侃    ', N'2', N'0', N'24'), (N'2001140221', N'周世会 ', N'2', N'0', N'24'), (N'2001140222', N'许宏杰 ', N'2', N'0', N'24'), (N'2001140223', N'宣传    ', N'2', N'0', N'24'), (N'2001140224', N'张琳    ', N'2', N'0', N'24'), (N'2001140225', N'周砚芝 ', N'2', N'0', N'24'), (N'2001140226', N'叶玉玲 ', N'2', N'0', N'24'), (N'2001140227', N'张燕燕 ', N'2', N'0', N'24'), (N'2001140228', N'祝金    ', N'2', N'0', N'24'), (N'2001140229', N'樊晓波 ', N'2', N'0', N'24'), (N'2001140230', N'方运健 ', N'2', N'0', N'24'), (N'2001140231', N'方池龙 ', N'2', N'0', N'24'), (N'2001140232', N'张永田 ', N'2', N'0', N'24'), (N'2001140233', N'黄卫敏 ', N'2', N'0', N'24'), (N'2001140234', N'李松平 ', N'2', N'0', N'24'), (N'1000000000', N'n         ', N'2', N'21', N'23')
GO

COMMIT
GO


-- ----------------------------
-- Table structure for StuInfo
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[StuInfo]') AND type IN ('U'))
	DROP TABLE [dbo].[StuInfo]
GO

CREATE TABLE [dbo].[StuInfo] (
  [StuNum] char(10) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [StuName] char(10) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [StuSex] varchar(4) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [StuClass] varchar(20) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [StuAge] int  NOT NULL
)
GO

ALTER TABLE [dbo].[StuInfo] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of StuInfo
-- ----------------------------
BEGIN TRANSACTION
GO

INSERT INTO [dbo].[StuInfo] ([StuNum], [StuName], [StuSex], [StuClass], [StuAge]) VALUES (N'2001140101', N'沈娴    ', N'女', N'1', N'22'), (N'2001140102', N'程佳    ', N'女', N'1', N'21'), (N'2001140103', N'高丽燕 ', N'女', N'1', N'22'), (N'2001140104', N'黄小微 ', N'女', N'1', N'21'), (N'2001140105', N'周非草 ', N'男', N'1', N'22'), (N'2001140106', N'金鑫    ', N'男', N'1', N'23'), (N'2001140107', N'蒋鸿翔 ', N'男', N'1', N'22'), (N'2001140108', N'王秩军 ', N'男', N'1', N'22'), (N'2001140109', N'俞健辉 ', N'男', N'1', N'22'), (N'2001140110', N'章尧丰 ', N'男', N'1', N'22'), (N'2001140111', N'王立明 ', N'男', N'1', N'22'), (N'2001140112', N'张均灿 ', N'女', N'1', N'22'), (N'2001140113', N'叶会华 ', N'女', N'1', N'21'), (N'2001140114', N'吴晓芳 ', N'女', N'1', N'22'), (N'2001140115', N'章刘燕 ', N'女', N'1', N'21'), (N'2001140116', N'韩昕    ', N'女', N'1', N'22'), (N'2001140117', N'王利峰 ', N'男', N'1', N'22'), (N'2001140118', N'梁豪文 ', N'男', N'1', N'21'), (N'2001140119', N'张琛    ', N'男', N'1', N'22'), (N'2001140120', N'汪杰    ', N'男', N'1', N'22'), (N'2001140121', N'许晨    ', N'男', N'1', N'22'), (N'2001140122', N'吉良盛 ', N'男', N'1', N'22'), (N'2001140123', N'经涛    ', N'男', N'1', N'22'), (N'2001140125', N'卢丽珍 ', N'女', N'1', N'20'), (N'2001140126', N'沈宁怡 ', N'女', N'1', N'22'), (N'2001140127', N'周丽君 ', N'女', N'1', N'22'), (N'2001140128', N'王安安 ', N'女', N'1', N'23'), (N'2001140129', N'林晓峰 ', N'男', N'1', N'22'), (N'2001140130', N'林觐民 ', N'男', N'1', N'22'), (N'2001140131', N'吴彦    ', N'男', N'1', N'22'), (N'2001140132', N'韩骏    ', N'男', N'1', N'22'), (N'2001140133', N'周建平 ', N'男', N'1', N'22'), (N'2001140134', N'应雷达 ', N'男', N'1', N'22'), (N'2001140135', N'方涛    ', N'男', N'1', N'22'), (N'2001140201', N'杜旭虹 ', N'女', N'2', N'22'), (N'2001140202', N'罗建红 ', N'女', N'2', N'22'), (N'2001140203', N'叶丹    ', N'女', N'2', N'22'), (N'2001140204', N'梁华萍 ', N'女', N'2', N'22'), (N'2001140205', N'童小成 ', N'男', N'2', N'22'), (N'2001140206', N'厉和    ', N'男', N'2', N'22'), (N'2001140207', N'沈峰    ', N'男', N'2', N'22'), (N'2001140208', N'李东    ', N'男', N'2', N'22'), (N'2001140209', N'朱雪峰 ', N'男', N'2', N'22'), (N'2001140210', N'戚军辉 ', N'男', N'2', N'22'), (N'2001140211', N'潘伟庆 ', N'男', N'2', N'22'), (N'2001140214', N'王晓维 ', N'女', N'2', N'22'), (N'2001140215', N'朱洪燕 ', N'女', N'2', N'22'), (N'2001140216', N'郑菲    ', N'女', N'2', N'22'), (N'2001140217', N'傅斌    ', N'男', N'2', N'22'), (N'2001140218', N'温从喜 ', N'男', N'2', N'22'), (N'2001140219', N'范卫峰 ', N'男', N'2', N'22'), (N'2001140220', N'陈侃    ', N'男', N'2', N'22'), (N'2001140221', N'周世会 ', N'男', N'2', N'22'), (N'2001140222', N'许宏杰 ', N'男', N'2', N'22'), (N'2001140223', N'宣传    ', N'男', N'2', N'22'), (N'2001140224', N'张琳    ', N'女', N'2', N'22'), (N'2001140225', N'周砚芝 ', N'女', N'2', N'22'), (N'2001140226', N'叶玉玲 ', N'女', N'2', N'22'), (N'2001140227', N'张燕燕 ', N'女', N'2', N'22'), (N'2001140228', N'祝金    ', N'男', N'2', N'22'), (N'2001140229', N'樊晓波 ', N'男', N'2', N'22'), (N'2001140230', N'方运健 ', N'男', N'2', N'22'), (N'2001140231', N'方池龙 ', N'男', N'2', N'22'), (N'2001140232', N'张永田 ', N'男', N'2', N'22'), (N'2001140233', N'黄卫敏 ', N'男', N'2', N'22'), (N'2001140234', N'李松平 ', N'男', N'2', N'22'), (N'1000000000', N'n         ', N'男', N'2', N'12')
GO

COMMIT
GO


-- ----------------------------
-- Table structure for StuSelInfo
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[StuSelInfo]') AND type IN ('U'))
	DROP TABLE [dbo].[StuSelInfo]
GO

CREATE TABLE [dbo].[StuSelInfo] (
  [StuNum] char(10) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [CourseNo] char(10) COLLATE Chinese_Simplified_Stroke_Order_100_CI_AI_KS_SC_UTF8  NOT NULL,
  [StuScoreS] int  NOT NULL
)
GO

ALTER TABLE [dbo].[StuSelInfo] SET (LOCK_ESCALATION = TABLE)
GO


-- ----------------------------
-- Records of StuSelInfo
-- ----------------------------
BEGIN TRANSACTION
GO

INSERT INTO [dbo].[StuSelInfo] ([StuNum], [CourseNo], [StuScoreS]) VALUES (N'1000000000', N'002       ', N'21'), (N'2001140101', N'001       ', N'89'), (N'2001140101', N'002       ', N'60'), (N'2001140101', N'003       ', N'76'), (N'2001140101', N'004       ', N'61'), (N'2001140101', N'005       ', N'74'), (N'2001140101', N'006       ', N'78'), (N'2001140101', N'007       ', N'81'), (N'2001140101', N'008       ', N'67'), (N'2001140101', N'009       ', N'76'), (N'2001140101', N'010       ', N'90'), (N'2001140101', N'011       ', N'73'), (N'2001140102', N'001       ', N'86'), (N'2001140102', N'002       ', N'80'), (N'2001140102', N'003       ', N'74'), (N'2001140102', N'004       ', N'83'), (N'2001140102', N'005       ', N'82'), (N'2001140102', N'006       ', N'74'), (N'2001140102', N'007       ', N'75'), (N'2001140102', N'008       ', N'75'), (N'2001140102', N'009       ', N'81'), (N'2001140102', N'010       ', N'85'), (N'2001140102', N'011       ', N'60'), (N'2001140103', N'001       ', N'87'), (N'2001140103', N'002       ', N'82'), (N'2001140103', N'003       ', N'73'), (N'2001140103', N'004       ', N'69'), (N'2001140103', N'005       ', N'94'), (N'2001140103', N'006       ', N'84'), (N'2001140103', N'007       ', N'93'), (N'2001140103', N'008       ', N'79'), (N'2001140103', N'009       ', N'86'), (N'2001140103', N'010       ', N'86'), (N'2001140103', N'011       ', N'93'), (N'2001140104', N'001       ', N'93'), (N'2001140104', N'002       ', N'86'), (N'2001140104', N'003       ', N'80'), (N'2001140104', N'004       ', N'76'), (N'2001140104', N'005       ', N'91'), (N'2001140104', N'006       ', N'77'), (N'2001140104', N'007       ', N'77'), (N'2001140104', N'008       ', N'85'), (N'2001140104', N'009       ', N'82'), (N'2001140104', N'010       ', N'93'), (N'2001140104', N'011       ', N'72'), (N'2001140105', N'001       ', N'68'), (N'2001140105', N'002       ', N'60'), (N'2001140105', N'003       ', N'63'), (N'2001140105', N'004       ', N'71'), (N'2001140105', N'005       ', N'60'), (N'2001140105', N'006       ', N'63'), (N'2001140105', N'007       ', N'60'), (N'2001140105', N'008       ', N'71'), (N'2001140105', N'009       ', N'70'), (N'2001140105', N'010       ', N'68'), (N'2001140105', N'011       ', N'69'), (N'2001140106', N'001       ', N'60'), (N'2001140106', N'002       ', N'60'), (N'2001140106', N'003       ', N'70'), (N'2001140106', N'004       ', N'60'), (N'2001140106', N'005       ', N'85'), (N'2001140106', N'006       ', N'70'), (N'2001140106', N'007       ', N'60'), (N'2001140106', N'008       ', N'70'), (N'2001140106', N'009       ', N'78'), (N'2001140106', N'010       ', N'67'), (N'2001140106', N'011       ', N'75'), (N'2001140107', N'001       ', N'92'), (N'2001140107', N'002       ', N'78'), (N'2001140107', N'003       ', N'75'), (N'2001140107', N'004       ', N'66'), (N'2001140107', N'005       ', N'75'), (N'2001140107', N'006       ', N'78'), (N'2001140107', N'007       ', N'73'), (N'2001140107', N'008       ', N'69'), (N'2001140107', N'009       ', N'73'), (N'2001140107', N'010       ', N'75'), (N'2001140107', N'011       ', N'83'), (N'2001140108', N'001       ', N'89'), (N'2001140108', N'002       ', N'80'), (N'2001140108', N'003       ', N'90'), (N'2001140108', N'004       ', N'60'), (N'2001140108', N'005       ', N'78'), (N'2001140108', N'006       ', N'80'), (N'2001140108', N'007       ', N'69'), (N'2001140108', N'008       ', N'80'), (N'2001140108', N'009       ', N'70'), (N'2001140108', N'010       ', N'81'), (N'2001140108', N'011       ', N'65'), (N'2001140109', N'001       ', N'60'), (N'2001140109', N'002       ', N'60'), (N'2001140109', N'003       ', N'60'), (N'2001140109', N'004       ', N'68'), (N'2001140109', N'005       ', N'75'), (N'2001140109', N'006       ', N'72'), (N'2001140109', N'007       ', N'69'), (N'2001140109', N'008       ', N'70'), (N'2001140109', N'009       ', N'77'), (N'2001140109', N'010       ', N'65'), (N'2001140109', N'011       ', N'83')
GO

INSERT INTO [dbo].[StuSelInfo] ([StuNum], [CourseNo], [StuScoreS]) VALUES (N'2001140110', N'001       ', N'68'), (N'2001140110', N'002       ', N'80'), (N'2001140110', N'003       ', N'70'), (N'2001140110', N'004       ', N'61'), (N'2001140110', N'005       ', N'70'), (N'2001140110', N'006       ', N'70'), (N'2001140110', N'007       ', N'60'), (N'2001140110', N'008       ', N'62'), (N'2001140110', N'009       ', N'82'), (N'2001140110', N'010       ', N'62'), (N'2001140110', N'011       ', N'65'), (N'2001140111', N'001       ', N'85'), (N'2001140111', N'002       ', N'86'), (N'2001140111', N'003       ', N'78'), (N'2001140111', N'004       ', N'80'), (N'2001140111', N'005       ', N'82'), (N'2001140111', N'006       ', N'88'), (N'2001140111', N'007       ', N'83'), (N'2001140111', N'008       ', N'80'), (N'2001140111', N'009       ', N'70'), (N'2001140111', N'010       ', N'75'), (N'2001140111', N'011       ', N'70'), (N'2001140112', N'001       ', N'80'), (N'2001140112', N'002       ', N'85'), (N'2001140112', N'003       ', N'75'), (N'2001140112', N'004       ', N'78'), (N'2001140112', N'005       ', N'84'), (N'2001140112', N'006       ', N'90'), (N'2001140112', N'007       ', N'92'), (N'2001140112', N'008       ', N'89'), (N'2001140112', N'009       ', N'88'), (N'2001140112', N'010       ', N'91'), (N'2001140112', N'011       ', N'90'), (N'2001140113', N'001       ', N'80'), (N'2001140113', N'002       ', N'82'), (N'2001140113', N'003       ', N'88'), (N'2001140113', N'004       ', N'88'), (N'2001140113', N'005       ', N'84'), (N'2001140113', N'006       ', N'78'), (N'2001140113', N'007       ', N'80'), (N'2001140113', N'008       ', N'86'), (N'2001140113', N'009       ', N'85'), (N'2001140113', N'010       ', N'90'), (N'2001140113', N'011       ', N'82'), (N'2001140114', N'001       ', N'80'), (N'2001140114', N'002       ', N'82'), (N'2001140114', N'003       ', N'85'), (N'2001140114', N'004       ', N'90'), (N'2001140114', N'005       ', N'75'), (N'2001140114', N'006       ', N'78'), (N'2001140114', N'007       ', N'80'), (N'2001140114', N'008       ', N'74'), (N'2001140114', N'009       ', N'89'), (N'2001140114', N'010       ', N'81'), (N'2001140114', N'011       ', N'83'), (N'2001140115', N'001       ', N'80'), (N'2001140115', N'002       ', N'74'), (N'2001140115', N'003       ', N'72'), (N'2001140115', N'004       ', N'75'), (N'2001140115', N'005       ', N'82'), (N'2001140115', N'006       ', N'81'), (N'2001140115', N'007       ', N'85'), (N'2001140115', N'008       ', N'74'), (N'2001140115', N'009       ', N'70'), (N'2001140115', N'010       ', N'80'), (N'2001140115', N'011       ', N'83'), (N'2001140116', N'001       ', N'80'), (N'2001140116', N'002       ', N'82'), (N'2001140116', N'003       ', N'70'), (N'2001140116', N'004       ', N'95'), (N'2001140116', N'005       ', N'90'), (N'2001140116', N'006       ', N'67'), (N'2001140116', N'007       ', N'80'), (N'2001140116', N'008       ', N'86'), (N'2001140116', N'009       ', N'82'), (N'2001140116', N'010       ', N'79'), (N'2001140116', N'011       ', N'76'), (N'2001140117', N'001       ', N'74'), (N'2001140117', N'002       ', N'80'), (N'2001140117', N'003       ', N'92'), (N'2001140117', N'004       ', N'76'), (N'2001140117', N'005       ', N'84'), (N'2001140117', N'006       ', N'85'), (N'2001140117', N'007       ', N'86'), (N'2001140117', N'008       ', N'89'), (N'2001140117', N'009       ', N'80'), (N'2001140117', N'010       ', N'78'), (N'2001140117', N'011       ', N'74'), (N'2001140118', N'001       ', N'80'), (N'2001140118', N'002       ', N'90'), (N'2001140118', N'003       ', N'92'), (N'2001140118', N'004       ', N'88'), (N'2001140118', N'005       ', N'74'), (N'2001140118', N'006       ', N'72'), (N'2001140118', N'007       ', N'86'), (N'2001140118', N'008       ', N'88'), (N'2001140118', N'009       ', N'90'), (N'2001140118', N'010       ', N'70'), (N'2001140118', N'011       ', N'82'), (N'2001140119', N'001       ', N'68')
GO

INSERT INTO [dbo].[StuSelInfo] ([StuNum], [CourseNo], [StuScoreS]) VALUES (N'2001140119', N'002       ', N'74'), (N'2001140119', N'003       ', N'80'), (N'2001140119', N'004       ', N'85'), (N'2001140119', N'005       ', N'92'), (N'2001140119', N'006       ', N'90'), (N'2001140119', N'007       ', N'88'), (N'2001140119', N'008       ', N'84'), (N'2001140119', N'009       ', N'70'), (N'2001140119', N'010       ', N'76'), (N'2001140119', N'011       ', N'80'), (N'2001140120', N'001       ', N'90'), (N'2001140120', N'002       ', N'82'), (N'2001140120', N'003       ', N'64'), (N'2001140120', N'004       ', N'85'), (N'2001140120', N'005       ', N'82'), (N'2001140120', N'006       ', N'75'), (N'2001140120', N'007       ', N'69'), (N'2001140120', N'008       ', N'86'), (N'2001140120', N'009       ', N'87'), (N'2001140120', N'010       ', N'82'), (N'2001140120', N'011       ', N'88'), (N'2001140201', N'001       ', N'85'), (N'2001140201', N'002       ', N'80'), (N'2001140201', N'003       ', N'66'), (N'2001140201', N'004       ', N'71'), (N'2001140201', N'005       ', N'70'), (N'2001140201', N'006       ', N'71'), (N'2001140201', N'007       ', N'84'), (N'2001140201', N'008       ', N'70'), (N'2001140201', N'009       ', N'76'), (N'2001140201', N'010       ', N'84'), (N'2001140201', N'011       ', N'66'), (N'2001140205', N'001       ', N'92'), (N'2001140205', N'002       ', N'91'), (N'2001140205', N'003       ', N'91'), (N'2001140205', N'004       ', N'82'), (N'2001140205', N'005       ', N'97'), (N'2001140205', N'006       ', N'96'), (N'2001140205', N'007       ', N'97'), (N'2001140205', N'008       ', N'95'), (N'2001140205', N'009       ', N'80'), (N'2001140205', N'010       ', N'87'), (N'2001140205', N'011       ', N'82')
GO

COMMIT
GO


-- ----------------------------
-- View structure for Student_Score_View
-- ----------------------------
IF EXISTS (SELECT * FROM sys.all_objects WHERE object_id = OBJECT_ID(N'[dbo].[Student_Score_View]') AND type IN ('V'))
	DROP VIEW [dbo].[Student_Score_View]
GO

CREATE VIEW [dbo].[Student_Score_View] AS SELECT
	StuInfo.StuNum,
	StuInfo.StuName,
	StuInfo.StuClass,
	Course.CourseName,
	Course.CourseNo,
	StuSelInfo.StuScoreS 
FROM
	StuSelInfo
	JOIN StuInfo ON StuSelInfo.StuNum = StuInfo.StuNum
	JOIN Course ON StuSelInfo.CourseNo = Course.CourseNo
	JOIN Rank ON StuSelInfo.StuNum = Rank.StuNum
GO


-- ----------------------------
-- Primary Key structure for table Course
-- ----------------------------
ALTER TABLE [dbo].[Course] ADD CONSTRAINT [PK__Course__C9D24549873A54EC] PRIMARY KEY NONCLUSTERED ([CourseNo])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = OFF, ALLOW_PAGE_LOCKS = OFF)  
ON [PRIMARY]
GO


-- ----------------------------
-- Primary Key structure for table Login
-- ----------------------------
ALTER TABLE [dbo].[Login] ADD CONSTRAINT [PK__Login__BD20C6F005F5C9AB] PRIMARY KEY CLUSTERED ([UserName])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Primary Key structure for table Rank
-- ----------------------------
ALTER TABLE [dbo].[Rank] ADD CONSTRAINT [PK__Rank__D9EEA6166CA0FBB7] PRIMARY KEY NONCLUSTERED ([StuNum])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = OFF, ALLOW_PAGE_LOCKS = OFF)  
ON [PRIMARY]
GO


-- ----------------------------
-- Triggers structure for table StuInfo
-- ----------------------------
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
GO


-- ----------------------------
-- Checks structure for table StuInfo
-- ----------------------------
ALTER TABLE [dbo].[StuInfo] ADD CONSTRAINT [StuAge_StuInfo_Check] CHECK ([StuAge]<(100) AND [StuAge]>(0))
GO

ALTER TABLE [dbo].[StuInfo] ADD CONSTRAINT [StuNum_StuInfo_Check] CHECK ([StuNum] like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
GO


-- ----------------------------
-- Primary Key structure for table StuInfo
-- ----------------------------
ALTER TABLE [dbo].[StuInfo] ADD CONSTRAINT [PK__StuInfo__D9EEA61697FF3BBB] PRIMARY KEY NONCLUSTERED ([StuNum])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = OFF, ALLOW_PAGE_LOCKS = OFF)  
ON [PRIMARY]
GO


-- ----------------------------
-- Triggers structure for table StuSelInfo
-- ----------------------------
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
GO


-- ----------------------------
-- Checks structure for table StuSelInfo
-- ----------------------------
ALTER TABLE [dbo].[StuSelInfo] ADD CONSTRAINT [StuScoreS_StuSelInfo_Check] CHECK ([StuScoreS]<=(100) AND [StuScoreS]>=(0))
GO


-- ----------------------------
-- Primary Key structure for table StuSelInfo
-- ----------------------------
ALTER TABLE [dbo].[StuSelInfo] ADD CONSTRAINT [PK__StuSelIn__457382430A4C9613] PRIMARY KEY CLUSTERED ([StuNum], [CourseNo])
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON)  
ON [PRIMARY]
GO


-- ----------------------------
-- Foreign Keys structure for table Rank
-- ----------------------------
ALTER TABLE [dbo].[Rank] ADD CONSTRAINT [StuNum_Rank_F] FOREIGN KEY ([StuNum]) REFERENCES [dbo].[StuInfo] ([StuNum]) ON DELETE CASCADE ON UPDATE CASCADE
GO


-- ----------------------------
-- Foreign Keys structure for table StuSelInfo
-- ----------------------------
ALTER TABLE [dbo].[StuSelInfo] ADD CONSTRAINT [StuNum_StuSelInfo_F] FOREIGN KEY ([StuNum]) REFERENCES [dbo].[StuInfo] ([StuNum]) ON DELETE CASCADE ON UPDATE CASCADE
GO

ALTER TABLE [dbo].[StuSelInfo] ADD CONSTRAINT [CourseNo_StuSelInfo_F] FOREIGN KEY ([CourseNo]) REFERENCES [dbo].[Course] ([CourseNo]) ON DELETE CASCADE ON UPDATE CASCADE
GO

