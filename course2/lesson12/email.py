#!/usr/bin/env python3
"""
email printer - A program to print an email based on passing a sender, a body and optional files.
"""
import email, datetime
from email.mime.multipart import MIMEMultipart
import mimetypes
import os


def print_email(to, body, *files):
        
    msg = email.message_from_string(body)
    msg['From'] = 'sender@db-network.de'
    msg['To'] = to
    msg['Date'] = datetime.datetime.now().strftime("%d %b %Y %H:%M:%S -0600")
    msg['Subject'] = 'Email printer'
    
    print(msg.as_string())
    print(files)
    
    if not files:
        """Get all files in current directory"""
        files = [f for f in os.listdir('.') if os.path.isfile(f)]

    for fn in files:
        ctype, encoding = mimetypes.guess_type(fn)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        
        if maintype == 'text':
            fp = open(path)
            # Note: we should handle calculating the charset
            msg = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == 'image':
            fp = open(path, 'rb')
            msg = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == 'audio':
            fp = open(path, 'rb')
            msg = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(path, 'rb')
            msg = MIMEBase(maintype, subtype)
            msg.set_payload(fp.read())
            fp.close()
            # Encode the payload using Base64
            encoders.encode_base64(msg)
        # Set the filename parameter
        #msg.add_header('Content-Disposition', 'attachment', filename=filename)
        #outer.attach(msg)
    # Now send or store the message
    #scomposed = outer.as_string()
        
    
print_email("receiver@db-network.de","Email Body")