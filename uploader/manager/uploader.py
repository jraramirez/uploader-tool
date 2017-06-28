from manager.models import MTDTA_UPLOADER
from manager.models import MTDTA_UPLOADER_PARAMS
from manager.models import MTDTA_UPLOADER_COLS

from manager.spreadsheet import SpreadSheetLogic

from openpyxl import load_workbook
from django.db import transaction
import ast

class UploadLogic:

    # Read the metadata of the file
    def readFileMetadata(inputFile):
        wb = load_workbook(inputFile)
        contents = []

        sheetNames = wb.get_sheet_names()       # Sheet Names
        fileName = inputFile.name               # File Name
        fileType = inputFile.content_type       # File Type
        colNames = []                           # Column Names and nCols
        nCols = 0
        colNamesLength = 0
        ws = wb[sheetNames[0]]
        for row in ws.rows:
            for cell in row:
                colNames.append(cell.value)
                nCols = nCols + 1
            break

        contents = [sheetNames, colNames, fileName, fileType, nCols]
        return contents

    # Get the uploader metadata from database
    # TODO: Parameterize the upload type
    def getUploaderMetadata(self):
        uploaderMetadata = []
        if(MTDTA_UPLOADER.objects.all().exists()):
            uploaderMetadata = MTDTA_UPLOADER.objects.all()
            uploaderMetadata = [
                uploaderMetadata[0].uploader, 
                uploaderMetadata[0].name, 
                uploaderMetadata[0].description, 
                uploaderMetadata[0].target_schema, 
                uploaderMetadata[0].target_table,
                uploaderMetadata[0].date_created
            ]
        return uploaderMetadata

    # Get the uploader metadata labels from database
    # TODO: Get uploader metadata labels from database
    # TODO: Parameterize the upload type
    def getUploaderMetadataLabels(self):
        labels = [
            'Uploader ID', 
            'Uploader Name', 
            'Description', 
            'Target Schema', 
            'Target Table',
            'Date Created',
        ]
        return labels

    # Get the uploader metadata parameters from database
    # TODO: Parameterize the upload type
    def getUploaderMetadataParameters(self):
        uploaderMetadataParameters = []
        if(MTDTA_UPLOADER_PARAMS.objects.all().exists()):
            meta_set = MTDTA_UPLOADER_PARAMS.objects.all()
            for meta in meta_set.iterator():
                uploaderMetadataParameters.append([
                    meta.uploader_id, 
                    meta.parameter, 
                    meta.name, 
                    meta.description,
                    meta.dataType,
                    meta.isRequired,
                    meta.default,
                    meta.format,
                    meta.date_created,
                ])
        return uploaderMetadataParameters

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
            'Date Created',
        ]
        return labels

    # Get the uploader metadata columns from database
    # TODO: Parameterize the upload type
    def getUploaderMetadataColumns(self):
        uploaderMetadataColumns = []
        if(MTDTA_UPLOADER_COLS.objects.all().exists()):
            meta_set = MTDTA_UPLOADER_COLS.objects.all()
            for meta in meta_set.iterator():
                uploaderMetadataColumns.append([
                    meta.uploader_id, 
                    meta.column, 
                    meta.name, 
                    meta.description,
                    meta.dataType,
                    meta.isRequired,
                    meta.default,
                    meta.format,
                    meta.date_created,
                ])
        return uploaderMetadataColumns

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
            'Date Created',
        ]
        return labels


    #  Validate the metadata of the file
    def validateFileMetadata(self, inputFile):
        valid = True
        errors = []
        
        # TODO: Check if there is no saved metadata

        # TODO: Sheet names
        
        wb = load_workbook(inputFile)
        contents = []
        metadata = []

        sheetNames = wb.get_sheet_names()       # Sheet Names
        fileName = inputFile.name               # File Name
        fileType = inputFile.content_type       # File Type
        colNames = []                           # Column Names and nCols
        nCols = 0
        ws = wb[sheetNames[0]]
        for row in ws.rows:
            for cell in row:
                colNames.append(cell.value)
                nCols = nCols + 1
            break
        
        # TODO: Check if there is no saved metadata

        # TODO: Validate metadata parameters

        # Validate File Metadata Columns
        metadataColumns = self.getUploaderMetadataColumns(self)

        # Number of columns validation
        if(not len(metadataColumns) == nCols):
            valid = False
            errors.append("Invalid number of columns: " + "Expected: '" + str(len(metadataColumns)) + "'. Found: " + str(nCols) + "'")
        
        else:
            # Column names validation
            for metaCol, fileCol in zip(metadataColumns, colNames):
                if(not metaCol[2] == fileCol):
                    valid = False
                    errors.append("Column name mismatch:" + " Expected: '" + metaCol[2] + "'. Found: '" + fileCol + "'")
            
            # Blank values per required column validation
            required = []
            for metaCol in metadataColumns:
                required.append(metaCol[5])
            for columnNumber in range(1, nCols+1):
                if(required[columnNumber-1] == 'Y'):
                    hasBlank = False
                    columnLetter = SpreadSheetLogic.getColumnLetter(columnNumber)
                    temp = columnLetter + '{}:' + columnLetter + '{}'
                    for row in ws.iter_rows(temp.format(ws.min_row+1,ws.max_row)):
                        for cell in row:
                            if(cell.value == None):
                                hasBlank = True
                        if(hasBlank and required[columnNumber-1] == 'Y'):
                            errors.append("Column has blank values: '" + colNames[columnNumber-1] + "'. This column is required.")
                            break
            
            # Format validation 
            formats = []
            for metaCol in metadataColumns:
                formats.append(metaCol[7])
            for columnNumber in range(1, nCols+1):
                if(formats[columnNumber-1]):
                    isValidFormat = True
                    columnLetter = SpreadSheetLogic.getColumnLetter(columnNumber)
                    temp = columnLetter + '{}:' + columnLetter + '{}'
                    for row in ws.iter_rows(temp.format(ws.min_row+1,ws.max_row)):
                        for cell in row:
                            # TODO: Check format
                            # print("Value found: " + cell.value + " Expected format: " + formats[columnNumber-1])
                            formats[columnNumber-1] = formats[columnNumber-1]
                        if(not isValidFormat):
                            errors.append("Column does not follow expected format: '" + colNames[columnNumber-1] + "'. Expected: "+ formats[columnNumber-1] + ".")
                            break
                                        
            # Data type validation 
            types = []
            for metaCol in metadataColumns:
                types.append(metaCol[4])
            for columnNumber in range(1, nCols+1):
                if(types[columnNumber-1]):
                    isValidType = True
                    columnLetter = SpreadSheetLogic.getColumnLetter(columnNumber)
                    temp = columnLetter + '{}:' + columnLetter + '{}'
                    for row in ws.iter_rows(temp.format(ws.min_row+1,ws.max_row)):
                        for cell in row:
                            typeFound = str(type(cell.value).__name__)
                            print("Column Name: " + colNames[columnNumber-1] + " Value: "+ str(cell.value) +"Type found: '" + str(type(cell.value).__name__) + "' Expected: " + types[columnNumber-1])
                            if(not (str(type(cell.value).__name__) == types[columnNumber-1]) and not (cell.value == None)):
                                isValidType = False
                                break
                        if(typeFound == 'datetime' or types[columnNumber-1] == 'time'):
                            isValidType = True
                        if(typeFound == 'time' or types[columnNumber-1] == 'datetime'):
                            isValidType = True
                        if(typeFound == 'int' or types[columnNumber-1] == 'float'):
                            isValidType = True
                        if(typeFound == 'float' or types[columnNumber-1] == 'int'):
                            isValidType = True
                        if(not isValidType):
                            errors.append("Column '" + colNames[columnNumber-1] + "' does not follow expected data type. Expected: '" + types[columnNumber-1] + "'. Found: '" + typeFound + "'")
                            break
        errors.insert(0, valid)
        return errors

    # TODO: Validate the metadata changes from the file

    # TODO: Read and save the metadata of the file

    # TODO: Insert data into database