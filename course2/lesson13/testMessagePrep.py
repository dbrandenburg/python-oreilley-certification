#!/usr/bin/env python3
"""
Read in resipients a start datetime abd a daycount for messages to 
be prepared for automatic sending.

NOTE: This test creates the message table, dropping any
previous version and should leave it empty. DANGER: this
test will delete any existing message table.
"""
import unittest
import mysql.connector as msc
from database import login_info
import messagePrep
from datetime import datetime
import email
from email.mime.text import MIMEText
from email.utils import make_msgid
import settings


conn = msc.Connect(**login_info)
conn.autocommit = True
curs = conn.cursor()

TBLDEF = """\
CREATE TABLE message (
     msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
     msgMessageID VARCHAR(128),
     msgDate DATETIME,
     msgRecipientAdress VARCHAR(128),
     msgTextSubject VARCHAR(128),
     msgText LONGTEXT
)"""

class testMailPrepareation(unittest.TestCase):
    def setUp(self):
        """
        Reads an arbitrary number of mail messages and
        stores them in a brand new messages table.
        
        DANGER: Any existing message table WILL be lost.
        """
        curs.execute("DROP TABLE IF EXISTS message")
        conn.commit()
        curs.execute(TBLDEF)
        conn.commit()
    
    def test_generate_daylist(self):
        """
        Tests the generate_daylist function by passing a start time and a count
        to get a list of dates back, counting from one day after the starttime.
        
        Info: Considering STARTTIME is the vacation leaving day, I'm not
        calculating -1 day for mails to start getting sent.
        """
        starttime = datetime(2015,3,1)
        daycount = 3
        daylist = messagePrep.generate_daylist(starttime, daycount)
        self.assertEqual([datetime(2015, 3, 2, 0, 0), 
            datetime(2015, 3, 3, 0, 0), 
            datetime(2015, 3, 4, 0, 0)], 
            daylist, 'Schould contain a list of days in datetime format')
    
    def test_generate_email(self):
        """
        Testing the email generation.
        """
        recipient = 'rec01@test.com'
        subject = 'This is a test message.'
        bodytext = 'JOTD'
        msg =  messagePrep.generate_email(recipient, subject, bodytext)
        self.assertEqual('rec01@test.com', msg['to'], 'Should contain'+
            ' correct recipient')
        self.assertEqual('This is a test message.',  msg['subject'], 'Should'+
            ' contain correct subject')
        self.assertEqual('JOTD', msg.get_payload(), 'Should contain correct'+
            ' mail body')
        self.assertTrue(msg['message-id'], 'Should contain a message-id')
        msg.as_string()

    def test_write_email_to_db(self):
        """
        Test for a message to get stored in the database.
        """
        msg = MIMEText('test')
        msg['subject'] = 'subject'
        msg['from'] = 'from@test.com'
        msg['to'] = 'to@test.com'
        msg['message-id'] = make_msgid()
        test_date = datetime(2015, 3, 4, 0, 0)
        messagePrep.store(msg, test_date)
        curs.execute("SELECT * FROM message")
        result = curs.fetchall()
        self.assertEqual(
            [(1, msg['message-id'], test_date, msg['to'], msg['subject'], 
            msg.get_payload())], result, 'Schould return stored message')
    
    def test_write_to_db_per_recipient(self):
        """
        Testing the database preparation by passing in a daylist, recipients
        and a list of jokes to store_preparation_emails
        """
        recipients = settings.RECIPIENTS
        starttime = settings.STARTTIME
        daycount = settings.DAYCOUNT
        jokes = settings.JOKES
        daylist = messagePrep.generate_daylist(starttime, daycount)
        
        messagePrep.store_preparation_emails(recipients, daylist, jokes)
        curs.execute("SELECT COUNT(*) FROM message") 
        
        mailcount = min(daycount, len(jokes))
        number_of_recipients = len(recipients)
        result = curs.fetchall()
        
        expected_total_mailcount = mailcount * number_of_recipients
        mails_in_db = result[0][0]
        
        self.assertEqual(expected_total_mailcount, mails_in_db, 
            'Mails in db should equal to prepared joke-days times recipients')

    
if __name__ == "__main__":
    unittest.main()