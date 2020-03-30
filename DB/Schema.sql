USE [master]
GO
/****** Object:  Login [WorkDude]    Script Date: 3/30/2020 10:25:47 AM ******/
CREATE LOGIN LinkedIn WITH PASSWORD=N'ni2iLvsQnqMMX5O0CXdSOCLdWzKvN58VoqWgdpSjV9I', DEFAULT_DATABASE=[master], DEFAULT_LANGUAGE=[us_english], CHECK_EXPIRATION=OFF, CHECK_POLICY=ON
GO
USE [LinkedIn]
GO
/****** Object:  Table [dbo].[JodyConfig]    Script Date: 3/30/2020 10:25:48 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[JodyConfig](
	[LastChecked] [datetime] NULL
) ON [PRIMARY]
GO
GRANT DELETE ON [dbo].[JodyConfig] TO [WorkDude] AS [dbo]
GO
GRANT INSERT ON [dbo].[JodyConfig] TO [WorkDude] AS [dbo]
GO
GRANT REFERENCES ON [dbo].[JodyConfig] TO [WorkDude] AS [dbo]
GO
GRANT SELECT ON [dbo].[JodyConfig] TO [WorkDude] AS [dbo]
GO
GRANT UPDATE ON [dbo].[JodyConfig] TO [WorkDude] AS [dbo]
GO
/****** Object:  Table [dbo].[JodyEmployees]    Script Date: 3/30/2020 10:25:48 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[JodyEmployees](
	[intID] [int] IDENTITY(1,1) NOT NULL,
	[Company] [varchar](200) NULL,
	[URL] [varchar](200) NULL,
	[LastNum] [int] NULL,
	[EntryDate] [datetime] NULL
) ON [PRIMARY]
GO
GRANT DELETE ON [dbo].[JodyEmployees] TO [WorkDude] AS [dbo]
GO
GRANT INSERT ON [dbo].[JodyEmployees] TO [WorkDude] AS [dbo]
GO
GRANT REFERENCES ON [dbo].[JodyEmployees] TO [WorkDude] AS [dbo]
GO
GRANT SELECT ON [dbo].[JodyEmployees] TO [WorkDude] AS [dbo]
GO
GRANT UPDATE ON [dbo].[JodyEmployees] TO [WorkDude] AS [dbo]
GO
ALTER TABLE [dbo].[JodyEmployees] ADD  DEFAULT ((0)) FOR [LastNum]
GO
ALTER TABLE [dbo].[JodyEmployees] ADD  DEFAULT (getdate()) FOR [EntryDate]
GO
