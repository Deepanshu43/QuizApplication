USE [master]
GO
/****** Object:  Database [quizapplication]    Script Date: 3/12/2021 9:52:56 PM ******/
CREATE DATABASE [quizapplication]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'quizapplication', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\quizapplication.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'quizapplication_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\quizapplication_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [quizapplication] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [quizapplication].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [quizapplication] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [quizapplication] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [quizapplication] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [quizapplication] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [quizapplication] SET ARITHABORT OFF 
GO
ALTER DATABASE [quizapplication] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [quizapplication] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [quizapplication] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [quizapplication] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [quizapplication] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [quizapplication] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [quizapplication] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [quizapplication] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [quizapplication] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [quizapplication] SET  DISABLE_BROKER 
GO
ALTER DATABASE [quizapplication] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [quizapplication] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [quizapplication] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [quizapplication] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [quizapplication] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [quizapplication] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [quizapplication] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [quizapplication] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [quizapplication] SET  MULTI_USER 
GO
ALTER DATABASE [quizapplication] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [quizapplication] SET DB_CHAINING OFF 
GO
ALTER DATABASE [quizapplication] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [quizapplication] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [quizapplication] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [quizapplication] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [quizapplication] SET QUERY_STORE = OFF
GO
USE [quizapplication]
GO
/****** Object:  Table [dbo].[easy]    Script Date: 3/12/2021 9:52:56 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[easy](
	[Id] [int] NULL,
	[Question] [varchar](50) NULL,
	[Option1] [varchar](50) NULL,
	[Option2] [varchar](50) NULL,
	[Option3] [varchar](50) NULL,
	[option4] [varchar](50) NULL,
	[Answer] [varchar](50) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[hard]    Script Date: 3/12/2021 9:52:56 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[hard](
	[Id] [int] NULL,
	[Question] [varchar](100) NULL,
	[Option1] [varchar](50) NULL,
	[Option2] [varchar](50) NULL,
	[Option3] [varchar](50) NULL,
	[Option4] [varchar](50) NULL,
	[Result] [varchar](50) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[medium]    Script Date: 3/12/2021 9:52:56 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[medium](
	[Id] [int] NULL,
	[Question] [varchar](100) NULL,
	[Option1] [varchar](50) NULL,
	[Option2] [varchar](50) NULL,
	[Option3] [varchar](50) NULL,
	[Option4] [varchar](50) NULL,
	[Result] [varchar](50) NULL
) ON [PRIMARY]
GO
INSERT [dbo].[easy] ([Id], [Question], [Option1], [Option2], [Option3], [option4], [Answer]) VALUES (1, N'The language spoken by the people by India is ?', N'Hindi', N'Palauan', N'Sindhi', N'Nauruan', N'Hindi')
INSERT [dbo].[easy] ([Id], [Question], [Option1], [Option2], [Option3], [option4], [Answer]) VALUES (2, N'The World Largest desert is ?', N'Thar', N'Kalahari', N'Sahara', N'Sonoran', N'Sahara')
INSERT [dbo].[easy] ([Id], [Question], [Option1], [Option2], [Option3], [option4], [Answer]) VALUES (3, N'Country that has the highest in Barley Production?', N'China', N'India', N'Russia', N'France', N'Russia')
INSERT [dbo].[easy] ([Id], [Question], [Option1], [Option2], [Option3], [option4], [Answer]) VALUES (4, N'The metal whose salts are sensitive to light is ?', N'Zinc', N'Silver', N'Copper', N'Aluminium', N'Aluminium')
INSERT [dbo].[easy] ([Id], [Question], [Option1], [Option2], [Option3], [option4], [Answer]) VALUES (5, N'The Central Rice Research Station is situated in ?', N'Chennai', N'Cuttack', N'Bangalore ', N'Quilons', N'Cuttack')
GO
INSERT [dbo].[hard] ([Id], [Question], [Option1], [Option2], [Option3], [Option4], [Result]) VALUES (1, N'Who was the first Indian woman in Space?', N'Kalpana Chawla', N'Sunita Williams', N'Koneru Humpy', N'None of the above', N'Kalpana Chawla')
INSERT [dbo].[hard] ([Id], [Question], [Option1], [Option2], [Option3], [Option4], [Result]) VALUES (2, N'Who was the first Indian in space?', N'Vikram Ambalal', N'Ravish Malhotra', N'Rakesh Sharma', N'Nagapathi Bhat', N'Rakesh Sharma')
INSERT [dbo].[hard] ([Id], [Question], [Option1], [Option2], [Option3], [Option4], [Result]) VALUES (3, N'Who was the first Man to Climb Mount Everest Without Oxygen?', N'Junko Tabei', N'Reinhold Messner', N'Peter Habeler', N'Phu Dorji', N'Reinhold Messner')
INSERT [dbo].[hard] ([Id], [Question], [Option1], [Option2], [Option3], [Option4], [Result]) VALUES (4, N'Who built the Jama Masjid?', N'Jahangir', N'Akbar', N'Imam Bukhari', N'Shah Jahan', N'Shah Jahan')
INSERT [dbo].[hard] ([Id], [Question], [Option1], [Option2], [Option3], [Option4], [Result]) VALUES (5, N'Who wrote the Indian National Anthem?', N'Bakim Chandra Chatterji', N'Rabindranath Tagore', N'Swami Vivekanand', N'None of the above', N'Rabindranath Tagore')
GO
INSERT [dbo].[medium] ([Id], [Question], [Option1], [Option2], [Option3], [Option4], [Result]) VALUES (1, N'Grand Central Terminal, Park Avenue, New York is the world''s', N'largest railway station', N'highest railway station', N'longest railway station', N'None of the above', N'largest railway station')
INSERT [dbo].[medium] ([Id], [Question], [Option1], [Option2], [Option3], [Option4], [Result]) VALUES (2, N'Entomology is the science that studies', N'Behavior of human beings', N'Insects', N'history of technical and scientific terms', N'The formation of rocks', N'Insects')
INSERT [dbo].[medium] ([Id], [Question], [Option1], [Option2], [Option3], [Option4], [Result]) VALUES (3, N'Eritrea, which became the 182nd member of the UN in 1993, is in the continent of', N'Asia', N'Africa', N'Europe', N'Australia', N'Africa')
INSERT [dbo].[medium] ([Id], [Question], [Option1], [Option2], [Option3], [Option4], [Result]) VALUES (4, N'Garampani sanctuary is located at', N'Junagarh', N'Diphu', N'Kohima', N'Gangtok', N'Diphu')
INSERT [dbo].[medium] ([Id], [Question], [Option1], [Option2], [Option3], [Option4], [Result]) VALUES (5, N'For which of the following disciplines is Nobel Prize awarded?', N'Physics and Chemistry', N'Physiology or Medicine', N'Literature,Peace and Economics', N'All of the above', N'All of the above')
GO
USE [master]
GO
ALTER DATABASE [quizapplication] SET  READ_WRITE 
GO
