-- PG Structures

USE [PG_BIZOPS]
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
           ('pg-structures-uploader',
            'File upload of PG Structures',
            '\pg_bizops\FILE_UPLOADER\PG Structures',
            '16.179.109.62',
            'PG Structures',
            '.xlsx',
            'Proj_WBSE',
            ',',
            0,
            'PG_BIZOPS',
            'STG_PG_STRUCTURES',
            'timetracking_techsupport@hpe.com',
            'timetracking_techsupport@hpe.com',
            'joe-ramir.agn.ramirez@hpe.com',
            'joe-ramir.agn.ramirez@hpe.com',
            GETDATE()
           )
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
           ((select uploader from [dbo].[mtdta_uploader] where name = 'pg-structures-uploader'),    'WBS element',   'WBS element',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'pg-structures-uploader'),    'User code 2',   'User code 2',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE())
GO
