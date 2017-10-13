-- MASTER PRJ PORTFOLIO

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
           ('master-prj-portfolio-uploader'
            ,'File upload of master-prj-portfolio'
            ,'\pg_bizops\FILE_UPLOADER\MASTER PRJ PORTFOLIO'
            ,'16.179.109.62'
            ,'Master_Portfolio'
            ,'.xlsx'
            ,'Master_Portfolio'
            , ','
            , 0
            ,'PG_BIZOPS'
            ,'STG_MASTER_PRJ_PORTFOLIO'
            ,'timetracking_techsupport@hpe.com'
            ,'timetracking_techsupport@hpe.com'
            ,'joe-ramir.agn.ramirez@hpe.com'
            ,'joe-ramir.agn.ramirez@hpe.com'
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
           ((select uploader from [dbo].[mtdta_uploader] where name = 'master-prj-portfolio-uploader'),    'HP Project #',   'HP Project #',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'master-prj-portfolio-uploader'),    'Project Name',   'Project Name',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'master-prj-portfolio-uploader'),    'HP Project Manager',   'HP Project Manager',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'master-prj-portfolio-uploader'),    'HP Project Manager Email',   'HP Project Manager Email',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'master-prj-portfolio-uploader'),    'Project Classification',   'Project Classification',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'master-prj-portfolio-uploader'),    'Project Stage',   'Project Stage',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'master-prj-portfolio-uploader'),    'Project Actual Start Date',   'Project Actual Start Date',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'master-prj-portfolio-uploader'),    'Project Actual End Date',   'Project Actual End Date',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'master-prj-portfolio-uploader'),    'SFDC_Estimated Project End Date',   'SFDC_Estimated Project End Date',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'master-prj-portfolio-uploader'),    'COMPASS FMO WBS',   'COMPASS FMO WBS',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'master-prj-portfolio-uploader'),    'COMPASS/WBS ID',   'COMPASS/WBS ID',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE()),
           ((select uploader from [dbo].[mtdta_uploader] where name = 'master-prj-portfolio-uploader'),    'HP Lead Service Category',   'HP Lead Service Category',   'N',  255,  'None',     'None',     'joe-ramir.agn.ramirez@hpe.com',   GETDATE())
GO