USE [PG_BIZOPS_DEV]
GO

-- truncate table [dbo].[manager_mtdta_uploader_params]
-- truncate table [dbo].[manager_mtdta_uploader_cols]
-- truncate table [dbo].[manager_mtdta_uploader]

INSERT INTO [dbo].[manager_mtdta_uploader]
           ([uploader]
           ,[name]
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
           (1
	      ,'shift'
           ,'File upload of monthly shift'
           ,'\pg_bizops\FILE_UPLOADER\SHIFT'
           ,'a4pgbizopsdev.svcs.entsvcs.net'
           ,'2017_03_EOT_RAW.xlsx'
           ,'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
           ,'P&G Raw'
           ,'pg_bizops_dev'
           ,'tempfin005raw'
           ,'joe-ramir.agn.ramirez@hpe.com'
           ,GETDATE())
GO

INSERT INTO [dbo].[manager_mtdta_uploader_params]
           ([uploader_id]
           ,[parameter]
           ,[name]
           ,[description]
           ,[data_type]
           ,[is_required]
           ,[default_value]
           ,[format]
           ,[last_update_uid]
           ,[last_update])
     VALUES
           (1
           ,1
           ,'period date'
           ,'description'
           ,'datetime'
           ,'Y'
           ,'01-01-2017'
           ,'mm-dd-yyyy'
           ,'joe-ramir.agn.ramirez@hpe.com'
           ,GETDATE())
GO

INSERT INTO [dbo].[manager_mtdta_uploader_cols]
           ([uploader_id]
           ,[column]
           ,[name]
           ,[description]
           ,[data_type]
           ,[is_required]
           ,[default]
           ,[format]
           ,[last_update_uid]
           ,[last_update])
     VALUES
           (1, 1, 'Period', 'period', 'datetime', 'Y', '0000-01-01', 'yyyy-mm-dd', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 2, 'Employee Number', 'EMPLOYEE_NUMBER', 'int', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 3, 'Employee Name', 'EMPLOYEE_NAME', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 4, 'Supplemental Pay Type', 'SUPPLEMENTAL_PAY_TYPE', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 5, 'Claim Month', 'CLAIM_MONTH', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 6, 'Claim Date', 'CLAIM_DATE', 'str', 'Y', '0000-01-01', 'yyyy-mm-dd', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 7, 'Regular Hours', 'REGULAR_HOURS', 'str', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 8, 'OT Time In', 'OT_TIME_IN', 'time', 'Y', '0000-01-01', 'yyyy-mm-dd', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 9, 'OT Time Out', 'OT_TIME_OUT', 'time', 'Y', '0000-01-01', 'yyyy-mm-dd', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 10, 'Total OT Hours', 'period', 'float', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 11, 'Overtime Time Amt Pay', 'period', 'float', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 12, 'Standby Hours', 'period', 'float', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 13, 'Stndby Amt', 'period', 'float', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 14, 'Shift Hours', 'period', 'float', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 15, 'Shift Amt', 'period', 'float', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 16, 'Total Payout - PHP', 'period', 'float', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 17, 'Total Payout - USD', 'period', 'float', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 18, 'Total Payout Percent', 'period', 'int', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 19, 'Comments', 'period', 'str', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 20, 'PRJ Customer', 'period', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 21, 'PRJ Customer2', 'period', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 22, 'Project', 'period', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 23, 'Project2', 'period', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 24, 'WBS', 'period', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 25, 'WBS Description', 'period', 'str', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 26, 'DCL FINAL', 'period', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 27, 'Location Code', 'period', 'str', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 28, 'Manager ID', 'period', 'int', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 29, 'Manager Name', 'period', 'str', 'Y', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE()),
           (1, 30, 'Modified', 'period', 'str', 'N', '', '', 'joe-ramir.agn.ramirez@hpe.com', GETDATE())
GO



