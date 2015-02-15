#!/usr/bin/env python3
import settings
from datetime import timedelta
from datetime import datetime

from email.mime.text import MIMEText
from email.utils import make_msgid

from database import login_info
import mysql.connector as msc

conn = msc.Connect(**login_info)
conn.autocommit = True
curs = conn.cursor()

def generate_daylist(starttime, daycount):
    """
    Generates a list of timestamps
    """
    daylist = []
    while daycount > 0:
        daycount = daycount - 1
        starttime = starttime + timedelta(days=1)
        daylist.append(starttime)
    return daylist
    
def generate_email(recipient, subject, bodytext):
    """
    Generate and Email based on the settings' "From" and definition arguments
    """
    msg = MIMEText(bodytext)
    msg['subject'] = subject
    msg['from'] = settings.FROM
    msg['to'] = recipient
    msg['message-id'] = make_msgid()
    return msg

def store(msg, sending_datetime):
    """
    Store email in database to prepare sending emails on specific days
    """
    message_body = msg.get_payload()
    message_id = msg['message-id']
    message_to = msg['to']
    message_subject = msg['subject']
    curs.execute("""INSERT INTO message
                    (msgMessageID, msgDate, msgRecipientAdress, msgTextSubject, 
                    msgText)
                    VALUES (%s, %s, %s, %s, %s)""",
                    (message_id, sending_datetime, message_to, message_subject,
                        message_body))
    conn.commit()

def store_preparation_emails(recipients, daylist, jokes):
    """
    Takes a message, a list of recipients and a list of datetimes to store
    emails including a timestamp as basis of a scheduled mail sender
    """
    number_of_jokes = len(jokes)
    if number_of_jokes < len(daylist):
        print('Not enough jokes for so many days. reducing daycount to ' +
            str(number_of_jokes))
    joke_schedule = zip(daylist,jokes)

    for sending_datetime, joke in joke_schedule:
        print(sending_datetime)
        for recipient in recipients:
            msg = generate_email(recipient, sending_datetime, joke)
            store(msg, sending_datetime)

#def get_and_print_emails:
    
        


