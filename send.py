import sys
# import requests
# from datetime import datetime

from formatting import format_msg
from send_mail import send_mail

def send(name, website=None, to_email=None, verbose=False):
    assert to_email != None

    # check input content
    if website != None:
        msg = format_msg(my_name=name, my_website=website)
    else:
        msg = format_msg(my_name=name)

    # If the user enters unnecessary things, the warning will be given
    if verbose:
        msg_warning = f"Is your name {name}, Your website is {website} and you want to send to {to_email}! Your Right!!!"
        print(msg_warning)
    
    # send the message
    try:
        send_mail(text=msg, to_emails=[to_email], html=None)
        sent = True
    except:
        sent = False
    return sent

# ?
if __name__ == "__main__":
    # Print all element content user input
    print(sys.argv)

    # default name = Unknown, email = None
    name = "Unknown"
    email = None

    # If number elements is 1 then name = 1th of argv
    if len(sys.argv) > 1:
        name = sys.argv[1]
    
    # If number elements is 2 then mail = 2th of argv
    if len(sys.argv) > 2:
        email = sys.argv[2]

    # Call function send email
    response = send(name, to_email=email, verbose=True)
    print(response)