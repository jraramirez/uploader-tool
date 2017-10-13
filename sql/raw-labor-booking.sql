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
           ('raw-labor-booking-uploader',
            'File upload of Raw Labor Booking',
            '\pg_bizops\FILE_UPLOADER\RAW LABOR BOOKING',
            '16.179.109.62',
            'ANALYSIS_PATTERN',
            '.csv',
            'Sheet1',
            ';',
            0,
            'PG_BIZOPS',
            'STG_RAW_LABOR_BOOKING',
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
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Fiscal year/period',   'Fiscal year/period',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Labor Source 1',   'Labor Source 1',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Labor Source 2',   'Labor Source 2',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Posting Date',   'Posting Date',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Employee Name',   'Employee Name',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Employee',   'Employee',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'E-Mail Address 1',   'E-Mail Address 1',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Activity Type',   'Activity Type',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Legacy Location Code',   'Legacy Location Code',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Master Cost Center',   'Master Cost Center',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Employee Region',   'Employee Region',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Employee Country',   'Employee Country',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'WBS Resp Cost Center',   'WBS Resp Cost Center',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Region',   'Region',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Country',   'Country',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'WBS 1',   'WBS 1',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'WBS 2',   'WBS 2',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Attribute 1',   'Attribute 1',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Short text',   'Short text',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Activity Date',   'Activity Date',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Supervisor 1',   'Supervisor 1',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Supervisor 2',   'Supervisor 2',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'E-Mail Address 2',   'E-Mail Address 2',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'PRJ Customer',   'PRJ Customer',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Cost Element',   'Cost Element',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Currency Code Local',   'Currency Code Local',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Activity Hours 1',   'Activity Hours 1',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Total Cost 1',   'Total Cost 1',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Activity Hours 2',   'Activity Hours 2',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'raw-labor-booking-uploader'),    'Total Cost 2',   'Total Cost 2',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE())
GO



