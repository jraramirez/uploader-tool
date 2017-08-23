from manager.models import MTDTA_UPLOADER
from manager.models import MTDTA_UPLOADER_PARAMS
from manager.models import MTDTA_UPLOADER_COLS
import sys

from manager.spreadsheet import SpreadSheetLogic

from django.apps import apps
from django.contrib.contenttypes.models import ContentType 

import csv
import codecs
from openpyxl import load_workbook
from django.db import transaction
from shutil import copyfile
import contextlib
import datetime
import ast
import os
import re
import fileinput
import subprocess
from io import TextIOWrapper

class UploadLogic:

    # Get the uploader metadata from database
    def getUploaderMetadata(self, uploader_name):
        valid = True
        returned = []
        errors = []
        uploaderMetadata = []
        if(MTDTA_UPLOADER.objects.all().exists()):
            uploaderMetadata = MTDTA_UPLOADER.objects.filter(name=uploader_name)
            if(uploaderMetadata):
                uploaderMetadata = [
                    uploaderMetadata[0].uploader, 
                    uploaderMetadata[0].name, 
                    uploaderMetadata[0].description, 
                    uploaderMetadata[0].source_path,
                    uploaderMetadata[0].file_name,
                    uploaderMetadata[0].file_type,
                    uploaderMetadata[0].sheet_name,    
                    uploaderMetadata[0].target_schema, 
                    uploaderMetadata[0].target_table,
                    uploaderMetadata[0].last_update_uid, 
                    uploaderMetadata[0].last_update, 
                    uploaderMetadata[0].server,
                    uploaderMetadata[0].email_sender,
                    uploaderMetadata[0].email_recipient,
                    uploaderMetadata[0].email_cc,
                    uploaderMetadata[0].start_row,
                ]
            else:
                errors.append("Uploader name not found: '" + uploader_name + "'.")
                valid = False
        else:
            errors.append("Uploader is not set up properly.")
            valid = False
        returned.append(uploaderMetadata)
        returned.append(valid)
        returned.append(errors)
        return returned

    # Get the uploader metadata labels from database
    def getUploaderMetadataLabels(self):
        labels = [
            'Uploader ID', 
            'Uploader Name', 
            'Description', 
            'Source Path', 
            'File Name', 
            'File Type', 
            'Sheet Name', 
            'Target Schema', 
            'Target Table',
            'Last Updated By', 
            'Last Updated',
            'Server',
            'Email Sender',
            'Email Recipient',
            'Email CC',
            'Start Row',
        ]
        return labels

    # Get the uploader metadata parameters from database
    def getUploaderMetadataParameters(self, uploader_name):
        valid = True
        returned = []
        errors = []
        uploaderMetadata = []
        uploaderMetadataParameters = []
        if(MTDTA_UPLOADER_PARAMS.objects.all().exists()):
            uploader_id = MTDTA_UPLOADER.objects.filter(name=uploader_name)[0].uploader
            meta_set = MTDTA_UPLOADER_PARAMS.objects.filter(uploader_id=uploader_id)
            for meta in meta_set.iterator():
                uploaderMetadataParameters.append([
                    meta.uploader_id, 
                    meta.parameter, 
                    meta.name, 
                    meta.description,
                    meta.data_type,
                    meta.is_required,
                    meta.default_value,
                    meta.format,
                    meta.last_update_uid,
                    meta.last_update,
                ])
        else:
            errors.append("Uploader parameters is not set up properly.")
            valid = False
        returned.append(uploaderMetadataParameters)
        returned.append(valid)
        returned.append(errors)
        return returned

    # Get the uploader metadata parameter labels from database
    def getUploaderMetadataParameterLabels(self):
        labels = [
            'Uploader ID', 
            'Parameter ID',
            'Parameter Name', 
            'Description', 
            'Data Type', 
            'Required',
            'Default Value',
            'Format',
            'Last Updated By', 
            'Last Updated',
        ]
        return labels

    # Get the uploader metadata columns from database
    def getUploaderMetadataColumns(self, uploader_name):
        valid = True
        returned = []
        errors = []
        uploaderMetadata = []
        uploaderMetadataColumns = []
        if(MTDTA_UPLOADER_COLS.objects.all().exists()):
            uploader_id = MTDTA_UPLOADER.objects.filter(name=uploader_name)[0].uploader
            meta_set = MTDTA_UPLOADER_COLS.objects.filter(uploader_id=uploader_id)
            for meta in meta_set.iterator():
                uploaderMetadataColumns.append([
                    meta.uploader_id, 
                    meta.column, 
                    meta.name, 
                    meta.description,
                    meta.is_required,
                    meta.default,
                    meta.format,
                    meta.max_length,
                    meta.last_update_uid,
                    meta.last_update,
                ])            
        else:
            errors.append("Uploader columns is not set up properly.")
            valid = False
        returned.append(uploaderMetadataColumns)
        returned.append(valid)
        returned.append(errors)
        return returned

    # Get the uploader metadata column labels from database
    def getUploaderMetadataColumnLabels(self):
        labels = [
            'Uploader ID', 
            'Column ID',
            'Column Name', 
            'Description', 
            'Required',
            'Default Value',
            'Format',
            'Max Length',
            'Last Updated By', 
            'Last Updated',
        ]
        return labels

    #  Validate folder and file existence
    def validateFile(self, uploaderMetadata):
        valid = True    
        errors = []
        returned = []
        
        # Check if folder is valid
        folderPath = "\\\%s%s\\New" % (uploaderMetadata[11], uploaderMetadata[3])
        if(os.path.exists(folderPath)):
            files = [f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))]
            if(files):
                if(len(files) > 1):
                    valid = False
                    errors.append("More than one file was found in the source folder.")
            else:
                valid = False
                errors.append("No files were found in the source folder.")            
        else:
            valid = False
            errors.append("Invalid source folder: " + "Expected: '" + folderPath + "'.")

        returned.append(None)
        returned.append(valid)
        returned.append(errors)
        return returned

    # Get the file from the source path
    def getInputFile(self, uploaderMetadata):
        folderPath = "\\\%s%s\\New" % (uploaderMetadata[11], uploaderMetadata[3])
        files = [f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))]
        fullPath = folderPath + "\\" + files[0]
        if(uploaderMetadata[5] == '.csv'):
            f = open(fullPath, 'rt')
        else:
            f = open(fullPath, 'rb')
        return f

    #  Validate the metadata of the file
    def validateFileMetadata(self, inputFile, uploaderMetadata, uploaderMetadataColumns):
        valid = True    
        errors = []
        returned = []
        sheetIndex = 0
        sheetFound = False
        readSuccess = False
        
        # Validate uploader metadata

        colNames = []
        nCols = 0
        fileName, fileExtension = os.path.splitext(inputFile.name)
        # File type validation
        if(not fileExtension.lower() == uploaderMetadata[5].lower()):
            valid = False
            errors.append("Invalid file type. " + "Expected: '" + str(uploaderMetadata[5]) + "', Found: " + str(fileExtension) + "'.")

        # File name validation
        if(uploaderMetadata[4].lower() not in fileName.lower()):
            valid = False
            errors.append("Invalid file name format. " + "Expected: '" + str(uploaderMetadata[4]) + "'.")
        
        # Sheet name validation
        if(valid):
            startRow = uploaderMetadata[15]
            i = 0
            if(fileExtension == '.csv'):
                paramFile =TextIOWrapper(inputFile.file)
                ws = csv.reader(paramFile)
                for row in ws:
                    if(i == startRow):
                        for cell in row:
                            colNames.append(cell)
                            nCols = nCols + 1
                        break
                    i = i + 1
                readSuccess = True
                paramFile.detach()
            else:
                wb = load_workbook(inputFile, read_only=True)
                sheetNames = wb.get_sheet_names()       # Sheet Names
                for s in sheetNames:
                    if(str(s) == uploaderMetadata[6]):
                        sheetFound = True
                        break
                    sheetIndex = sheetIndex + 1

                if(sheetFound):
                    ws = wb[sheetNames[sheetIndex]]
                    for row in ws.rows:
                        if(i == startRow):
                            for cell in row:
                                colNames.append(cell.value)
                                nCols = nCols + 1
                            break
                        i = i + 1
                    readSuccess = True
                else:
                    valid = False
                    errors.append("Invalid file sheet name. " + "Expected: '" + str(uploaderMetadata[6]) + "', Found: " + str(sheetNames[0]) + "'.")

        # Validate File Metadata Columns
        if(readSuccess):
            # Number of columns validation
            metaColNames = []
            for metaCol in uploaderMetadataColumns:
                metaColNames.append(metaCol[2])
            if(not len(uploaderMetadataColumns) == nCols):
                valid = False
                errors.append("Invalid file number of columns. " + "Expected: '" + str(len(uploaderMetadataColumns)) + "', Found: '" + str(nCols) + "'.")
                if(len(uploaderMetadataColumns) > nCols):
                    for metaCol in metaColNames:
                        if(metaCol not in colNames):
                            errors.append("Invalid file. Column not found in file: '" + str(metaCol) + "'.")
                if(len(uploaderMetadataColumns) < nCols):
                    for fileCol in colNames:
                        if(fileCol not in metaColNames):
                            errors.append("Invalid file. Extra column found in file: '" + str(fileCol) + "'.")
            else:
                # Column names validation
                nMismatch = 0
                for metaCol, fileCol in zip(uploaderMetadataColumns, colNames):
                    if(not metaCol[2] == fileCol):
                        valid = False
                        errors.append("File column name mismatch found. " + "Expected: '" + str(metaCol[2]) + "', Found: '" + str(fileCol) + "'.")
                        nMismatch = nMismatch + 1
                if(nMismatch > 0):
                    errors.append("Too many column name mismatch. Check if the start row is correct. Check if columns are in proper ordering. ")
                
                # Format validation
                # TODO: If needed

        # Validate Target Table
        targetSchemaName = uploaderMetadata[7]
        targetTableName = re.sub(r'[\W_]', '', uploaderMetadata[8])
        targetTable = None
        try:
            targetTable = apps.get_model('file_loader', targetTableName)
        except():
            valid = False
            errors.append("Invalid target table: " + "Found: '" + str(uploaderMetadata[8]) + "'.")
        
        # Validate Target Schema
        targetSchemaName = uploaderMetadata[7]
        if(targetTable):
            try:
                print(targetTable.objects.using(targetSchemaName).all())
            except:
                valid = False
                errors.append("Invalid target schema: " + "Found: '" + str(uploaderMetadata[7]) + "'.")

        returned.append(None)
        returned.append(valid)
        returned.append(errors)
        return returned

    # Move file 
    def moveFile(self, valid, uploaderMetadata):    
        returned = []
        errors = []
        canMove = True

        errorFolderPath = "\\\%s%s\\Error" % (uploaderMetadata[11], uploaderMetadata[3])

        # Determine if the destination directory is Archive or Error
        if(valid):
            destinationPath = "\\\%s%s\\Archive" % (uploaderMetadata[11], uploaderMetadata[3])
        else:
            if(not os.path.exists(errorFolderPath)):
                errors.append("Cannot move file to Error folder due to invalid source path.")
                canMove = False
            else:
                destinationPath = errorFolderPath
        if(canMove):
            folderPath = "\\\%s%s\\New" % (uploaderMetadata[11], uploaderMetadata[3])
            files = [f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))]
            if(files):
                destinationPath = destinationPath + "\\" + datetime.datetime.now().strftime("%Y%m%d%H%M%S - ") + files[0]
                sourcePath = folderPath + "\\" + files[0]
                copyfile(sourcePath, destinationPath)
                os.remove(sourcePath)
                with contextlib.suppress(OSError):
                    os.unlink(sourcePath)

        returned.append(None)
        returned.append(valid)
        returned.append(errors)
        return returned

    # Get all target schema and target tables
    def getAllTargetTablesAndSchemas(self):
        valid = True
        returned = {}
        errors = []
        data = {}

        if(MTDTA_UPLOADER.objects.all().exists()):
            uploaderMetadata = MTDTA_UPLOADER.objects.all()
            for meta in uploaderMetadata:
                data.setdefault(str(meta.target_schema), []).append(meta.target_table)
        else:
            errors.append("Uploader is not set up properly.")
            valid = False
        returned = {
            'valid' : valid,
            'errors' : errors,
            'data' : data,
        }
        return returned

    # Put target tables to models
    def putTargetTablesToModels(self, data):
        open('../maintenance/models.py', 'w').close()
        models = open('../maintenance/models.py', 'a')
        for schema in data:
            tables = ""       
            for table in data[schema]:
                tables = tables + " " + table
            command = "python manage.py inspectdb" + tables + " --database=" + schema
            p = subprocess.call(command, stdout=models)

        models.close()
        phrase = 'from __future__ import unicode_literals'
        for line in fileinput.input('../maintenance/models.py', inplace=True):
            if phrase in line:
                continue
            print(line, end='')
        
        models.close()
        copyfile('../maintenance/models.py', 'file_loader/models.py')

    # Get all uploader names
    def getAllUploaderNames(self):
        valid = True
        returned = {}
        errors = []
        data = {'names':[]}

        if(MTDTA_UPLOADER.objects.all().exists()):
            uploaderMetadata = MTDTA_UPLOADER.objects.all()
            for meta in uploaderMetadata:
                data['names'].append(meta.name)
        else:
            errors.append("Uploader is not set up properly.")
            valid = False
        returned = {
            'valid' : valid,
            'errors' : errors,
            'data' : data,
        }
        return returned