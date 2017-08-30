-- TODO: Use variables to fill up the template easier

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
           ,[start_row]
           ,[target_schema]
           ,[target_table]
           ,[email_sender]
           ,[email_recipient]
           ,[email_cc]
           ,[last_update_uid]
           ,[last_update])
     VALUES
           ('uploader-name'
           ,'File upload of ...'
           ,'\pg_bizops\FILE_UPLOADER\[SOURCE FOLDER NAME]'
           ,'16.179.110.132'
           ,'Data'
           ,'.xlsx'
           ,'Sheet1'
           , 0
           ,'FPD'
           ,'TMP_TARGET_TABLE'
           ,'pg_bizopssupport@hpe.com'
           ,'pg_bizopssupport@hpe.com'
           ,'pg_bizopssupport@hpe.com'
           ,'username@hpe.com'
           ,GETDATE())
GO

INSERT INTO [dbo].[mtdta_uploader_params]
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
           ((select uploader from [dbo].[mtdta_uploader] where name = 'uploader-name')
           ,'period date'
           ,'description'
           ,'datetime'
           ,'Y'
           ,'01-01-2017'
           ,'mm-dd-yyyy'
           ,'username@hpe.com'
           ,GETDATE())
GO

INSERT INTO [dbo].[mtdta_uploader_cols]
           ([uploader_id]
           ,[name]
           ,[description]
           ,[is_required]
           ,[max_length]
           ,[default]
           ,[format]
           ,[last_update_uid]
           ,[last_update])
     VALUES
           ((select uploader from [dbo].[mtdta_uploader] where name = 'uploader-name')    '',   '',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
GO



