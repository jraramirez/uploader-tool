from manager.models import MTDTA_UPLOADER
from manager.models import MTDTA_UPLOADER_PARAMS
from manager.models import MTDTA_UPLOADER_COLS

from shift.models import TempFIN005Raw
from shift.models import TestFIN005Raw

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
        # TODO: Assumes that the first sheet is read
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
                uploaderMetadata[0].source_path,
                uploaderMetadata[0].file_name,
                uploaderMetadata[0].file_type,
                uploaderMetadata[0].sheet_name,    
                uploaderMetadata[0].target_schema, 
                uploaderMetadata[0].target_table,
                uploaderMetadata[0].last_update_uid, 
                uploaderMetadata[0].last_update
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
                    meta.data_type,
                    meta.is_required,
                    meta.default_value,
                    meta.format,
                    meta.last_update_uid,
                    meta.last_update,
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
            'Last Updated By', 
            'Last Updated',
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
                    meta.data_type,
                    meta.is_required,
                    meta.default,
                    meta.format,
                    meta.last_update_uid,
                    meta.last_update,
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
            'Last Updated By', 
            'Last Updated',
        ]
        return labels


    #  Validate the metadata of the file
    def validateFileMetadata(self, inputFile):
        valid = True
        errors = []
        
        # TODO: Check if there is no saved metadata
        
        wb = load_workbook(inputFile)
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
        
        # Validate uploader metadata
        metadata = self.getUploaderMetadata(self)

        # File type validation
        if(not fileType == metadata[5]):
            valid = False
            errors.append("Invalid file type: " + "Expected: '" + str(metadata[5]) + "'. Found: " + str(fileType) + "'")

        # Sheet name validation
        if(not str(sheetNames[0]) == metadata[6]):
            valid = False
            errors.append("Invalid sheet name: " + "Expected: '" + str(metadata[6]) + "'. Found: " + str(sheetNames[0]) + "'")
          
        # Validate File Metadata Columns
        metadataColumns = self.getUploaderMetadataColumns(self)

        # Number of columns validation
        if(not len(metadataColumns) == nCols):
            valid = False
            errors.append("Invalid number of columns: " + "Expected: '" + str(len(metadataColumns)) + "'. Found: " + str(nCols) + "'." + "")
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
            # formats = []
            # for metaCol in metadataColumns:
            #     formats.append(metaCol[7])
            # for columnNumber in range(1, nCols+1):
            #     if(formats[columnNumber-1]):
            #         isValidFormat = True
            #         columnLetter = SpreadSheetLogic.getColumnLetter(columnNumber)
            #         temp = columnLetter + '{}:' + columnLetter + '{}'
            #         for row in ws.iter_rows(temp.format(ws.min_row+1,ws.max_row)):
            #             for cell in row:
            #                 # TODO: Check format
            #                 # print("Value found: " + cell.value + " Expected format: " + formats[columnNumber-1])
            #                 formats[columnNumber-1] = formats[columnNumber-1]
            #             if(not isValidFormat):
            #                 errors.append("Column does not follow expected format: '" + colNames[columnNumber-1] + "'. Expected: "+ formats[columnNumber-1] + ".")
            #                 break
                                        
            # Data type validation
            # TODO: Do this during upload
            # TODO: Do this in the temp table, not in the file
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
                        if(typeFound == 'datetime' and types[columnNumber-1] == 'time'):
                            isValidType = True
                        if(typeFound == 'time' and types[columnNumber-1] == 'datetime'):
                            isValidType = True
                        if(typeFound == 'int' and types[columnNumber-1] == 'float'):
                            isValidType = True
                        if(typeFound == 'float' and types[columnNumber-1] == 'int'):
                            isValidType = True
                        if(not isValidType):
                            errors.append("Column '" + colNames[columnNumber-1] + "' does not follow expected data type. Expected: '" + types[columnNumber-1] + "'. Found: '" + typeFound + "'")
                            break
        errors.insert(0, valid)
        return errors


    # Insert data into database
    def properInsert(inputFile):
        responses = []
        warnings = []
        
        # Upload data from file to the database
        TestFIN005Raw.objects.all().delete()
        with transaction.atomic():
            wb = load_workbook(inputFile)
            sheetNames = wb.get_sheet_names()
            ws = wb[sheetNames[0]]

            nCols = MTDTA_UPLOADER_COLS.objects.all().count()
            startRow = 0

            i = 0
            for row in ws.iter_rows():
                r = []
                j = 0
                for cell in row:
                    if(cell.value != None):
                        r.append(str(cell.value))
                    else:
                        r.append(None)
                for j in range(len(row), nCols):
                    r.append(None)
                if(len(r) > 0):
                    if(i > startRow):
                        print(r)
                        r.insert(0, i)
                        t = TestFIN005Raw(
                            r[0],r[1],r[2],r[3],r[4],r[5],
                            r[6],r[7],r[8],r[9],r[10],r[11],
                            r[12],r[13],r[14],r[15],r[16],
                            r[17],r[18],r[19],r[20],r[21],
                            r[22],r[23],r[24],r[25],r[26],
                            r[27],r[28],r[29],
                        )
                        t.save()
                    i = i + 1
                    
        # Blank values per required column validation
        # TODO: Do this during upload
        # TODO: Do this in the temp table, not in the file
        metadataColumns = self.getUploaderMetadataColumns(self)
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