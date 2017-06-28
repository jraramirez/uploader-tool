USE [PG_BIZOPS_DEV]
GO

-- truncate table [dbo].[manager_mtdta_uploader_params]
-- truncate table [dbo].[manager_mtdta_uploader_cols]
-- truncate table [dbo].[manager_mtdta_uploader]

INSERT INTO [dbo].[manager_mtdta_uploader]
           ([uploader]
           ,[name]
           ,[description]
           ,[target_schema]
           ,[target_table]
           ,[date_created])
     VALUES
           (1
	      ,'shift'
           ,'File upload of monthly shift'
           ,'pg_bizops_dev'
           ,'tempfin005raw'
           ,CAST('6-21-2017' as date))
GO

INSERT INTO [dbo].[manager_mtdta_uploader_params]
           ([parameter]
           ,[name]
           ,[description]
           ,[dataType]
           ,[isRequired]
           ,[default]
           ,[format]
           ,[date_created]
           ,[uploader_id])
     VALUES
           (1
           ,'period date'
           ,'description'
           ,'datetime'
           ,'Y'
           ,'6-21-2017'
           ,'yyyy-mm-dd'
           ,CAST('6-21-2017' as date)
           ,1)
GO

INSERT INTO [dbo].[manager_mtdta_uploader_cols]
           ([column]
           ,[name]
           ,[description]
           ,[dataType]
           ,[isRequired]
           ,[default]
           ,[format]
           ,[date_created]
           ,[uploader_id])
     VALUES
           (1, 'Period', 'period', 'datetime', 'Y', '0000-01-01', 'yyyy-mm-dd', CAST('6-21-2017' as date), 1),
           (2, 'Employee Number', 'EMPLOYEE_NUMBER', 'int', 'Y', '', '', CAST('6-21-2017' as date), 1),
           (3, 'Employee Name', 'EMPLOYEE_NAME', 'str', 'Y', '', '', CAST('6-21-2017' as date), 1),
           (4, 'Supplemental Pay Type', 'SUPPLEMENTAL_PAY_TYPE', 'str', 'Y', '', '', CAST('6-21-2017' as date), 1),
           (5, 'Claim Month', 'CLAIM_MONTH', 'str', 'Y', '', '', CAST('6-21-2017' as date), 1),
           (6, 'Claim Date', 'CLAIM_DATE', 'str', 'Y', '0000-01-01', 'yyyy-mm-dd', CAST('6-21-2017' as date), 1),
           (7, 'Regular Hours', 'REGULAR_HOURS', 'str', 'N', '', '', CAST('6-21-2017' as date), 1),
           (8, 'OT Time In', 'OT_TIME_IN', 'time', 'Y', '0000-01-01', 'yyyy-mm-dd', CAST('6-21-2017' as date), 1),
           (9, 'OT Time Out', 'OT_TIME_OUT', 'time', 'Y', '0000-01-01', 'yyyy-mm-dd', CAST('6-21-2017' as date), 1),
           (10, 'Total OT Hours', 'period', 'float', 'N', '', '', CAST('6-21-2017' as date), 1),
           (11, 'Overtime Time Amt Pay', 'period', 'float', 'N', '', '', CAST('6-21-2017' as date), 1),
           (12, 'Standby Hours', 'period', 'float', 'N', '', '', CAST('6-21-2017' as date), 1),
           (13, 'Stndby Amt', 'period', 'float', 'N', '', '', CAST('6-21-2017' as date), 1),
           (14, 'Shift Hours', 'period', 'float', 'N', '', '', CAST('6-21-2017' as date), 1),
           (15, 'Shift Amt', 'period', 'float', 'N', '', '', CAST('6-21-2017' as date), 1),
           (16, 'Total Payout - PHP', 'period', 'float', 'Y', '', '', CAST('6-21-2017' as date), 1),
           (17, 'Total Payout - USD', 'period', 'float', 'Y', '', '', CAST('6-21-2017' as date), 1),
           (18, 'Total Payout Percent', 'period', 'int', 'N', '', '', CAST('6-21-2017' as date), 1),
           (19, 'Comments', 'period', 'str', 'N', '', '', CAST('6-21-2017' as date), 1),
           (20, 'PRJ Customer', 'period', 'str', 'Y', '', '', CAST('6-21-2017' as date), 1),
           (21, 'PRJ Customer2', 'period', 'str', 'Y', '', '', CAST('6-21-2017' as date), 1),
           (22, 'Project', 'period', 'str', 'Y', '', '', CAST('6-21-2017' as date), 1),
           (23, 'Project2', 'period', 'str', 'Y', '', '', CAST('6-21-2017' as date), 1),
           (24, 'WBS', 'period', 'str', 'Y', '', '', CAST('6-21-2017' as date), 1),
           (25, 'WBS Description', 'period', 'str', 'N', '', '', CAST('6-21-2017' as date), 1),
           (26, 'DCL Final', 'period', 'str', 'Y', '', '', CAST('6-21-2017' as date), 1),
           (27, 'Location Code', 'period', 'str', 'N', '', '', CAST('6-21-2017' as date), 1),
           (28, 'Manager ID', 'period', 'int', 'Y', '', '', CAST('6-21-2017' as date), 1),
           (29, 'Manager Name', 'period', 'str', 'Y', '', '', CAST('6-21-2017' as date), 1),
           (30, 'Modified', 'period', 'str', 'N', '', '', CAST('6-21-2017' as date), 1)
GO



