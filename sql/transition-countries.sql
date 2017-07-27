USE [PG_BIZOPS_DEV]
GO

-- truncate table [dbo].[manager_mtdta_uploader_params]
-- truncate table [dbo].[manager_mtdta_uploader_cols]
-- truncate table [dbo].[manager_mtdta_uploader]

INSERT INTO [dbo].[manager_mtdta_uploader]
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
           ('transition-countries'
           ,'File upload of transition countries'
           ,'\pg_bizops\FILE_UPLOADER\TRANSITION COUNTRIES'
           ,'16.179.110.132'
           ,'20170704 BW Monthly Hours Data.xlsb'
           ,'test'
           ,'BW Hours Data'
           ,'pg_bizops_dev'
           ,'TMP_TRANSITION_COUNTRIES'
           ,'joe-ramir.agn.ramirez@hpe.com'
           ,GETDATE())
GO

INSERT INTO [dbo].[manager_mtdta_uploader_params]
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
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries')
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
           ,[name]
           ,[description]
           ,[data_type]
           ,[is_required]
           ,[default]
           ,[format]
           ,[last_update_uid]
           ,[last_update])
     VALUES
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'Service Month', 		'Service Month', 	      'str',      'Y', 		'', 		'Mmm YYYY', 'joe-ramir.agn.ramirez@hpe.com',          GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'Manager Email', 		'Manager Email', 	      'str',     	'Y', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'Employee ID', 		'Employee ID', 	      'int', 	'Y', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'Employee Name', 		'Employee Name', 	      'str', 	'Y', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'Employee Email', 	'Employee Email',       'str', 	'Y', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'P&G Level', 		'P&G Level', 	      'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'Daily Expected Hours', 'Daily Expected Hours', 'str', 	'Y', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'Employee Type', 		'Employee Type', 		'str', 	'Y', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'Bill to Country', 	'Bill to Country',      'int', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'Geography', 		'Geography', 		'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'HP Level', 		'HP Level', 		'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'Seat Country Code', 	'Seat Country Code',	'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'Seat Country', 		'Seat Country', 		'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'WBS', 		      'WBS',                  'str', 	'Y', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'WBS Description', 	'WBS Description', 	'str', 	'Y', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'AA Type', 		      'AA Type', 		      'int', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'Attribute', 		'Attribute', 		'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'Attribute 2', 		'Attribute 2', 		'str', 	'Y', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'Short Text', 		'Short Text', 		'str', 	'Y', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'HP Labor Rate', 		'HP Labor Rate', 		'float', 	'Y', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'USD / Labor Currency',	'USD / Labor Currency', 'float', 	'Y', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'Hours', 		      'Hours', 		      'float', 	'Y', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE())
GO



