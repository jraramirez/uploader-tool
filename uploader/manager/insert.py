from manager.models import MTDTA_UPLOADER
from manager.models import MTDTA_UPLOADER_PARAMS
from manager.models import MTDTA_UPLOADER_COLS

from file_loader.models import shift_temp_table

from manager.spreadsheet import SpreadSheetLogic
from manager.uploader import UploadLogic


from openpyxl import load_workbook
from django.db import transaction
import ast
import os

class InsertLogic:

    # Insert data into database
    def properInsert(self, inputFile, uploader_name):
        returned = []
        valid = True
        errors = []
        warnings = []
        responses = []
        required = []
        types = []
        names = []
        
        # SHIFT
        # Upload data from file to the database
        if(uploader_name == 'shift'):
            # Specific to shift: use target table shift_temp_table
            shift_temp_table.objects.all().delete()
            with transaction.atomic():
                wb = load_workbook(inputFile)
                sheetNames = wb.get_sheet_names()
                ws = wb[sheetNames[0]]
                
                ulogic = UploadLogic
                metadataColumns = ulogic.getUploaderMetadataColumns(self, uploader_name)[0]
                nCols = len(metadataColumns)

                # Specific to shift: data starts at row 0
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
                    print(i)

                    # Specific to shift: 30 columns
                    if(len(r) > 0):
                        if(i > startRow):
                            r.insert(0, i)
                            t = shift_temp_table(
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
            for metaCol in metadataColumns:
                required.append(metaCol[5])
                names.append(metaCol[2])
                types.append(metaCol[4])
            columnNumber = 0
            for f in shift_temp_table._meta.get_fields():
                if(not f.name == 'id'):
                    values = []
                    if(required[columnNumber] == 'Y'):
                        hasBlank = False
                        values = shift_temp_table.objects.values_list(f.name, flat=True)
                        for value in values:
                            if(value == None):
                                hasBlank = True
                                break
                        if(hasBlank and required[columnNumber] == 'Y'):
                            warnings.append("Column has blank values: '" + names[columnNumber] + "'. This column is required.")
                    columnNumber = columnNumber + 1

            # Data type validation
            columnNumber = 0
            for f in shift_temp_table._meta.get_fields():
                if(not f.name == 'id'):
                    isValidType = True
                    values = shift_temp_table.objects.values_list(f.name, flat=True)
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
                    if(typeFound == 'str'):
                        isValidType = True
                    if(not isValidType):
                        warnings.append("Column '" + names[columnNumber] + "' does not follow expected data type. Expected: '" + types[columnNumber] + "'. Found: '" + typeFound + "'")
                    columnNumber = columnNumber + 1
        
        # SVR
        # elif(uploader_name == 'svr'):

        else:
            valid = False

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