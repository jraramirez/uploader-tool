from manager.models import MTDTA_UPLOADER
from manager.models import MTDTA_UPLOADER_PARAMS
from manager.models import MTDTA_UPLOADER_COLS

from file_loader.models import *

from manager.spreadsheet import SpreadSheetLogic
from manager.uploader import UploadLogic

from django.apps import apps

from openpyxl import load_workbook
from django.db import transaction
import ast
import os

class InsertLogic:

    # Insert data into database
    def properInsert(self, inputFile, uploaderMetadata, uploaderMetadataColumns):
        returned = []
        valid = True
        errors = []
        warnings = []
        responses = []
        required = []
        types = []
        names = []

        # TODO: Put these to metadata table
        startRow = 0
        
        uploaderName = uploaderMetadata[1]

        # TODO: Remove underscores of the target table name
        targetTable = apps.get_model('file_loader', uploaderMetadata[8])

        print("Insert to database")
        if(uploaderMetadata):
            targetTable.objects.all().delete()
            with transaction.atomic():
                wb = load_workbook(inputFile, read_only=False)
                sheetNames = wb.get_sheet_names()
                ws = wb[sheetNames[0]]
                
                ulogic = UploadLogic
                nCols = len(uploaderMetadataColumns)

                i = 0
                all = []
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
                            r.insert(0,i)
                            all.append(r)
                            t = targetTable(*r)
                            t.save()
                            print(str(r))
                    i = i + 1

            # TODO: Close file properly after insert

            # Blank values per required column validation
            print("Data type validation")
            for metaCol in uploaderMetadataColumns:
                required.append(metaCol[5])
                names.append(metaCol[2])
                types.append(metaCol[4])
            required.insert(0, 'Y')
            names.insert(0, 'id')
            types.insert(0, 'int')
            
            columnNumber = 0
            for f in targetTable._meta.get_fields():
                print(f.name)
                values = []
                if(required[columnNumber] == 'Y'):
                    hasBlank = False
                    values = targetTable.objects.values_list(f.name, flat=True)
                    for value in values:
                        if(value == None):
                            hasBlank = True
                            break
                    if(hasBlank and required[columnNumber] == 'Y'):
                        warnings.append("Column has blank values: '" + names[columnNumber] + "'. This column is required.")
                columnNumber = columnNumber + 1

            # # Data type validation
            columnNumber = 0
            print("Data type validation")
            for f in targetTable._meta.get_fields():
                print(f.name)
                if(not f.name == 'id'):
                    isValidType = True
                    if(str(types[columnNumber]) == 'str'):
                        isValidType = True
                    else:
                        values = targetTable.objects.values_list(f.name, flat=True)
                        for value in values:
                            typeFound = str(type(value).__name__)
                            if(not (str(typeFound) == str(types[columnNumber])) and not (str(typeFound) == 'NoneType')):
                                isValidType = False
                                break
                        if(typeFound == 'datetime' and types[columnNumber] == 'time'):
                            isValidType = True
                        if(typeFound == 'time' and types[columnNumber] == 'datetime'):
                            isValidType = True
                        if(typeFound == 'int' and types[columnNumber] == 'float'):
                            isValidType = True
                        if(typeFound == 'float' and types[columnNumber] == 'int'):
                            isValidType = True
                        if(typeFound == 'Decimal' and types[columnNumber] == 'int'):
                            isValidType = True
                        if(typeFound == 'Decimal' and types[columnNumber] == 'float'):
                            isValidType = True
                        if(typeFound == 'float' and types[columnNumber] == 'Decimal'):
                            isValidType = True
                    if(not isValidType):
                        warnings.append("Column '" + names[columnNumber] + "' does not follow expected data type. Expected: '" + types[columnNumber] + "'. Found: '" + typeFound + "'")
                    columnNumber = columnNumber + 1
        else:
            valid = False
            responses.append("Uploader name '"+ uploaderName +"' is invalid.")

        if(len(warnings) > 0):
            responses.append("File upload successful with warnings")
        else:
            responses.append("File upload successful.")
        
        returned.append(None)
        returned.append(valid)
        returned.append(errors)
        returned.append(responses)
        returned.append(warnings)
        return returned