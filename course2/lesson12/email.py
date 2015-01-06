#!/usr/bin/env python3
"""
email printer - A program to print an email based on passing a sender, a body and optional files.
"""
import email, datetime
from email.mime.multipart import MIMEMultipart
import mimetypes
import os


def print_email(to, body, *files):
    
    if not files:
        """Get all files in current directory"""
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        
    msg = email.message_from_string(body)
    msg['From'] = 'sender@db-network.de'
    msg['To'] = to
    msg['Date'] = datetime.datetime.now().strftime("%d %b %Y %H:%M:%S -0600")
    msg['Subject'] = 'Email printer'
    
    print(msg.as_string())
    print(files)
    
    for fn in files:
        print(mimetypes.guess_type(fn))
        
    
print_email("receiver@db-network.de","Email Body")