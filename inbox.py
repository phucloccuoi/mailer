import imaplib
import email

host = 'imap.gmail.com'
userName = 'codingloc@gmail.com'
password = 'cuoibumlebE1@'

def get_inbox():
    mailer = imaplib.IMAP4_SSL(host)    # connect to server imap
    mailer.login(userName, password)    # Login server imap
    mailer.select(mailbox='INBOX')      # selectbox mailbox

    # Add data mail unseen to search_data
    _, search_data = mailer.search(None, 'UNSEEN')

    # Create a list of unread mails
    my_message = []

    # Browser all mail unread
    for numMail in search_data[0].split():
        # Create a dictionary for each mail
        email_data = {}

        # processing email data in RFC822 . format
        _, rfc_data = mailer.fetch(numMail, '(RFC822)')

        # Add data mail format to readable_data
        _, readable_data = rfc_data[0]

        # 
        email_messages = email.message_from_bytes(readable_data)

        # Add email header to dictionary
        for header in ['subject', 'to', 'from', 'date']:
            email_data[header] = email_messages[header]

        # Add email body to dictionary
        for part_body_mail in email_messages.walk():
            # If you encounter any body in plaintext format
            if part_body_mail.get_content_type() == "plain/text":
                body_mail = part_body_mail.get_payload(decode=True)
                email_data['boby'] = body_mail.decode()

            # If you encounter any body in html format
            elif part_body_mail.get_content_type() == "plain/html":
                html_mail = part_body_mail.get_payload(decode=True)
                email_data['html_body'] = html_mail.decode()

        # Add full mail to list
        my_message.append(email_data)

    # Return all mail
    return my_message

if __name__ == "__main__":
    my_inbox = get_inbox()
    print(my_inbox)