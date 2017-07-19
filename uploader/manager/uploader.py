from manager.models import MTDTA_UPLOADER
from manager.models import MTDTA_UPLOADER_PARAMS
from manager.models import MTDTA_UPLOADER_COLS

from manager.spreadsheet import SpreadSheetLogic

from openpyxl import load_workbook
from django.db import transaction
import ast
import os

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
                    uploaderMetadata[0].server
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
    # TODO: Get uploader metadata labels from database
    # TODO: Parameterize the upload type
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
        ]
        return labels

    # Get the uploader metadata parameters from database
    # TODO: Parameterize the upload type
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
    # TODO: Get uploader metadata parameter labels from database
    # TODO: Parameterize the upload type
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
                    meta.data_type,
                    meta.is_required,
                    meta.default,
                    meta.format,
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
    # TODO: Get uploader metadata column labels from database
    # TODO: Parameterize the upload type
    def getUploaderMetadataColumnLabels(self):
        labels = [
            'Uploader ID', 
            'Column ID',
            'Column Name', 
            'Description', 
            'Data Type', 
            'Required',
            'Default Value',
            'Format',
            'Last Updated By', 
            'Last Updated',
        ]
        return labels

    #  Validate folder and file existence
    def validateFile(self, uploader_name):
        valid = True    
        errors = []
        returned = []

        uploaderMetadata = self.getUploaderMetadata(self, uploader_name)[0]
        
        # Check if folder is valid
        folderPath = "\\\%s%s" % (uploaderMetadata[11], uploaderMetadata[3])
        if(os.path.exists(folderPath)):
            files = [f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))]
            if(len(files) > 1):
                valid = False
                errors.append("More than one file was found in the source folder.")
        else:
            valid = False
            errors.append("Invalid source folder: " + "Expected: '" + folderPath + "'.")

        returned.append(None)
        returned.append(valid)
        returned.append(errors)
        return returned

    # Get the file from the source path
    def getInputFile(self, uploader_name):
        uploaderMetadata = self.getUploaderMetadata(self, uploader_name)[0]
        folderPath = "\\\%s%s" % (uploaderMetadata[11], uploaderMetadata[3])
        files = [f for f in os.listdir(folderPath) if os.path.isfile(os.path.join(folderPath, f))]
        fullPath = folderPath + "\\" + files[0]
        f = open(fullPath, 'rb')
        return f

    #  Validate the metadata of the file
    def validateFileMetadata(self, inputFile, uploader_name):
        valid = True    
        errors = []
        returned = []
        
        wb = load_workbook(inputFile)

        sheetNames = wb.get_sheet_names()       # Sheet Names
        fileName = inputFile.name               # File Name
        # fileType = inputFile.content_type       # File Type
        colNames = []                           # Column Names and nCols
        nCols = 0
        ws = wb[sheetNames[0]]
        for row in ws.rows:
            for cell in row:
                colNames.append(cell.value)
                nCols = nCols + 1
            break
        
        # Validate uploader metadata
        uploaderMetadata = self.getUploaderMetadata(self, uploader_name)[0]

        # File type validation
        # TODO: FIX
        # if(not fileType == uploaderMetadata[5]):
        #     valid = False
        #     errors.append("Invalid file type: " + "Expected: '" + str(uploaderMetadata[5]) + "'. Found: " + str(fileType) + "'")

        # Sheet name validation
        # TODO: Find sheet for multiple sheets
        if(not str(sheetNames[0]) == uploaderMetadata[6]):
            valid = False
            errors.append("Invalid sheet name: " + "Expected: '" + str(uploaderMetadata[6]) + "'. Found: " + str(sheetNames[0]) + "'")
          
        # Validate File Metadata Columns
        metadataColumns = self.getUploaderMetadataColumns(self, uploader_name)[0]

        # Number of columns validation
        if(not len(metadataColumns) == nCols):
            valid = False
            errors.append("Invalid number of columns: " + "Expected: '" + str(len(metadataColumns)) + "'. Found: '" + str(nCols) + "'." + "")
            metaColNames = []
            for metaCol in metadataColumns:
                metaColNames.append(metaCol[2])
            for fileCol in colNames:
                if(fileCol not in metaColNames):
                    errors.append("Column not in metadata: '" + str(fileCol) + "'")
            for metaCol, fileCol in zip(metadataColumns, colNames):
                if(not metaCol[2] == fileCol):
                    errors.append("Possible missing column: '" + metaCol[2] + "'.")
                    break
        
        else:
            # Column names validation
            for metaCol, fileCol in zip(metadataColumns, colNames):
                if(not metaCol[2] == fileCol):
                    valid = False
                    errors.append("Possible column name mismatch or column is missing:" + " Expected: '" + metaCol[2] + "'. Found: '" + fileCol + "'")
            
            # Format validation
            # TODO: If needed

        returned.append(None)
        returned.append(valid)
        returned.append(errors)
        return returned
