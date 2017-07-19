import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailLogic:

    def sendEmailNotification(self, sender, recipient, valid, responses, errors, warnings, uploader_name):

        # SMTP used by the enterprise
        smtp = 'smtp.svcs.entsvcs.com'        

        status = ""
        errorList = ""
        warningList = ""
        responseList = ""

        if(valid):
            status = "Success"
        else:
            status = "Failure"

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "[File Loader Bot] [" + uploader_name + " uploader] [" + status + "] - " + responses[0]
        msg['From'] = sender
        msg['To'] = recipient

        # Create the body of the message (a plain-text and an HTML version).
        for e in errors:
            errorList = errorList + "\n - " + e
        for w in warnings:
            warningList = warningList + "\n - " + w
        for r in responses:
            responseList = responseList + "\n - " + r
        text = "\n[File Loader Bot] [" + uploader_name + " uploader] [" + status + "] - " + responses[0] + \
            "\n\nWarnings: " + \
            warningList + \
            "\n\nErrors: " + \
            errorList + \
            "\n\nOthers: " + \
            responseList
        html = ""

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(text, 'plain')
        # part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        msg.attach(part1)
        # msg.attach(part2)

        # Send the message via SMTP server.
        s = smtplib.SMTP(smtp)
        s.sendmail(sender, recipient, msg.as_string())
        s.quit()