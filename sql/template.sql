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
           ,[delimiter]
           ,[start_row]
           ,[target_schema]
           ,[target_table]
           ,[email_sender]
           ,[email_recipient]
           ,[email_cc]
           ,[last_update_uid]
           ,[last_update])
     VALUES
           ('uploader-name',
            'File upload of ...',
            '\pg_bizops\FILE_UPLOADER\[FOLDER NAME]',
            '16.179.109.62',
            'FILE NAME',
            '.csv',
            'Sheet1',
            ',',
            0,
            'PG_BIZOPS',
            'STG_TARGET_TABLE_NAME',
            'timetracking_techsupport@hpe.com',
            'timetracking_techsupport@hpe.com',
            'user@hpe.com',
            'user@hpe.com',
            GETDATE())
GO

INSERT INTO [dbo].[mtdta_uploader_cols]
            ([uploader_id],
            [name],
            [description],
            [is_required],
            [max_length],
            [default],
            [format],
            [last_update_uid],
            [last_update])
     VALUES
           ((select uploader from [dbo].[mtdta_uploader] where name = 'uploader-name'),    '',   '',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
GO



