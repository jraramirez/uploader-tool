USE [FPD]
GO

INSERT INTO [dbo].[mtdta_uploader]
           ([name]
           ,[description]
           ,[source_path]
           ,[server]
           ,[file_name]
           ,[file_type]
           ,[sheet_name]
           ,[target_schema]
           ,[target_table]
           ,[last_update_uid]
           ,[last_update])
     VALUES
           ('shift'
           ,'File upload of monthly shift'
           ,'\pg_bizops\FILE_UPLOADER\SHIFT'
           ,'16.179.110.132'
           ,'EOT_RAW'
           ,'.xlsx'
           ,'P&G Raw'
           ,'PG_BIZOPS_DEV'
           ,'tempfin005raw'
           ,'joe-ramir.agn.ramirez@hpe.com'
           ,GETDATE())
GO

INSERT INTO [dbo].[mtdta_uploader_params]
           ([uploader_id]
           ,[name]
           ,[description]
           ,[data_type]
           ,[is_required]
           ,[default_value]
           ,[format]
           ,[last_update_uid]
           ,[last_update])
     VALUES
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift')
           ,'period date'
           ,'description'
           ,'datetime'
           ,'Y'
           ,'01-01-2017'
           ,'mm-dd-yyyy'
           ,'joe-ramir.agn.ramirez@hpe.com'
           ,GETDATE())
GO

INSERT INTO [dbo].[mtdta_uploader_cols]
           ([uploader_id]
           ,[name]
           ,[description]
           ,[data_type]
           ,[is_required]
           ,[default]
           ,[format]
           ,[last_update_uid]
           ,[last_update])
     VALUES
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Period', 'period', 'datetime', 'Y', '0000-01-01', 'yyyy-mm-dd', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Employee Number', 'EMPLOYEE_NUMBER', 'int', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Employee Name', 'EMPLOYEE_NAME', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Supplemental Pay Type', 'SUPPLEMENTAL_PAY_TYPE', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Claim Month', 'CLAIM_MONTH', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Claim Date', 'CLAIM_DATE', 'str', 'Y', '0000-01-01', 'yyyy-mm-dd', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Regular Hours', 'REGULAR_HOURS', 'str', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'OT Time In', 'OT_TIME_IN', 'time', 'Y', '0000-01-01', 'yyyy-mm-dd', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'OT Time Out', 'OT_TIME_OUT', 'time', 'Y', '0000-01-01', 'yyyy-mm-dd', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Total OT Hours', 'period', 'float', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Overtime Time Amt Pay', 'period', 'float', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Standby Hours', 'period', 'float', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Stndby Amt', 'period', 'float', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Shift Hours', 'period', 'float', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Shift Amt', 'period', 'float', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Total Payout - PHP', 'period', 'float', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Total Payout - USD', 'period', 'float', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Total Payout Percent', 'period', 'int', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Comments', 'period', 'str', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'PRJ Customer', 'period', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'PRJ Customer2', 'period', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Project', 'period', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Project2', 'period', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'WBS', 'period', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'WBS Description', 'period', 'str', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'DCL FINAL', 'period', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Location Code', 'period', 'str', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Manager ID', 'period', 'int', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Manager Name', 'period', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'shift'), 'Modified', 'period', 'str', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE())
GO



