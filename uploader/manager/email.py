import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailLogic:

    def sendEmailNotification(self, uploaderMetadataRaw, fileFullPath, valid, responses, errors, warnings):

        # SMTP used by the enterprise
        smtp = 'smtp.svcs.entsvcs.com'        

        validEmail = True
        emailErrors = []
        returned = []
        status = ""
        errorList = ""
        errorListHTML = ""
        warningList = ""
        warningListHTML = ""
        responseList = ""
        responseListHTML = ""

        sender = uploaderMetadataRaw[12]
        recipient = uploaderMetadataRaw[13]
        cc = uploaderMetadataRaw[14]

        if(valid):
            status = "Success"
        else:
            status = "Failure"

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "[File Loader Bot] [" + uploaderMetadataRaw[1] + " uploader] [" + status + "] - " + responses[0]
        msg['From'] = sender
        msg['To'] = recipient
        msg['cc'] = cc

        # Create the body of the message (a plain-text and an HTML version).
        for e in errors:
            errorList = errorList + "\n - " + e
        for w in warnings:
            warningList = warningList + "\n - " + w
        for r in responses:
            responseList = responseList + "\n - " + r
        text = responses[0]
        if(warnings):
            text = text + "\n\nWarnings: " + warningList
        if(errors):
            text = text + "\n\nErrors: " + errorList        
            
        for e in errors:
            errorListHTML = errorListHTML + "<li>" + e + "</li>"
        for w in warnings:
            warningListHTML = warningListHTML + "<li>" + w + "</li>"

        html = """<html><head></head><body><font face="Arial">
        """ + \
        "<p><b>Status: </b>" + responses[0] + "</p>"
        
        if(warnings):
            html = html + "<p><b>Warnings:</b></p><ul>" + warningListHTML + "</ul>"
        if(errors):
            html = html + "<p><b>Errors:</b></p><ul style='color:red'>" + errorListHTML + "</ul>"

        html = html + "<p><b>Server: </b>" + uploaderMetadataRaw[11] + "</p>"
        html = html + "<p><b>Schema: </b>" + uploaderMetadataRaw[7] + "</p>"
        html = html + "<p><b>Target Table: </b>" + uploaderMetadataRaw[8] + "</p>"
        html = html + "<p><b>Input File: </b>" + fileFullPath + "</p>"


        html = html + """</font></body></html>"""

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        msg.attach(part1)
        msg.attach(part2)

        # Send the message via SMTP server.
        try:
            s = smtplib.SMTP(smtp)
            recipient = [recipient] + [cc]
            s.sendmail(sender, recipient, msg.as_string())
            s.quit()
        
        except():
            emailErrors.append("Uploader email recipient address rejected. Email notification is not sent.")

        # Always send to file loader bot support
        # s = smtplib.SMTP(smtp)
        # recipient = ['pg_bizopssupport@hpe.com']
        # s.sendmail(sender, recipient, msg.as_string())
        # s.quit()

        returned.append(None)
        returned.append(valid)
        returned.append(emailErrors)
        returned.append(warnings)
        return returned