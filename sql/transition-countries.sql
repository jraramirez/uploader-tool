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
           ('transition-countries',
            'File upload of transition countries',
            '\pg_bizops\FILE_UPLOADER\TRANSITION COUNTRIES',
            '16.179.109.62',
            'BW Monthly Hours Data',
            '.xlsx',
            'BW Hours Data',
            ',',
            0,
            'PG_BIZOPS',
            'STG_TRANSITIONBW',
            'timetracking_techsupport@hpe.com',
            'timetracking_techsupport@hpe.com',
            'joe-ramir.agn.ramirez@hpe.com',
            'joe-ramir.agn.ramirez@hpe.com',
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
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'Service Month',   'Service Month',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'Manager Email',   'Manager Email',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'Employee ID',   'Employee ID',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'Employee Name',   'Employee Name',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'Employee Email',   'Employee Email',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'P&G Level',   'P&G Level',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'Daily Expected Hours',   'Daily Expected Hours',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'Employee Type',   'Employee Type',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'Bill to Country',   'Bill to Country',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'Geography',   'Geography',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'HP Level',   'HP Level',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'Seat Country Code',   'Seat Country Code',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'Seat Country',   'Seat Country',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'WBS',   'WBS',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'WBS Description',   'WBS Description',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'AA Type',   'AA Type',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'Attribute',   'Attribute',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'Attribute 2',   'Attribute 2',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'Short Text',   'Short Text',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'HP Labor Rate',   'HP Labor Rate',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'USD / Labor Currency',   'USD / Labor Currency',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'transition-countries'),    'Hours',   'Hours',   'N',  255,  'None',     'None',     'user@hpe.com',   GETDATE()),
GO



