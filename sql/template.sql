USE [PG_BIZOPS_DEV]
GO

-- truncate table [dbo].[manager_mtdta_uploader_params]
-- truncate table [dbo].[manager_mtdta_uploader_cols]
-- truncate table [dbo].[manager_mtdta_uploader]

-- TODO: Parameterize the values into variables

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
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries') 		'', 	'',     'str',    'N', 		'', 		'',         'joe-ramir.agn.ramirez@hpe.com',          GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'', 	'',     'str',    'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 		'', 	'',     'str',    'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 		'', 	'',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 		'', 	'',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 		'', 	'',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 		'',   '',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 		'', 	'',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 		'', 	'',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),       	'', 	'',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'),		'', 	'',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 	 	'', 	'',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 	 	'', 	'',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 	 	'',   '',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 		'', 	'',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 		'',   '',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 		'', 	'',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 		'', 	'',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 		'', 	'',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 		'', 	'',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 		'',	'',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE()),
           ((select uploader from [dbo].[manager_mtdta_uploader] where name = 'transition-countries'), 		'',   '',     'str', 	'N', 		'', 		'', 		'joe-ramir.agn.ramirez@hpe.com', 		GETDATE())
GO



