#!/usr/bin/env python3
"""
email printer - A program to print an email based on passing a sender, a body and optional files.
"""
import email, datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email import encoders

import mimetypes
import os


def print_email(to, body, *files):
    
    program_dir = os.path.dirname(__file__)
        
    msg = MIMEMultipart()
    msg['From'] = 'sender@db-network.de'
    msg['To'] = to
    msg['Date'] = datetime.datetime.now().strftime("%d %b %Y %H:%M:%S -0600")
    msg['Subject'] = 'Email printer'
    msg.attach(MIMEText(body, 'plain'))
    
    if not files:
        """Get all files in current directory"""
        files = [program_dir + "/" + f for f in os.listdir(program_dir)] # if os.path.isfile(f)
    
    print(msg.as_string())
    
    for fn in files:
        ctype, encoding = mimetypes.guess_type(fn)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        
        if maintype == 'text':
            fp = open(fn)
            # Note: we should handle calculating the charset
            content = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == 'image':
            fp = open(fn, 'rb')
            content = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == 'audio':
            fp = open(fn, 'rb')
            content = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(fn, 'rb')
            content = MIMEBase(maintype, subtype)
            content.set_payload(fp.read())
            fp.close()
            # Encode the payload using Base64
            encoders.encode_base64(content)
        # Set the filename parameter
        msg.add_header('Content-Disposition', 'attachment', filename=fn)
        msg.attach(content)
    print(msg.as_string())
        
    
print_email("receiver@db-network.de","Email Body")