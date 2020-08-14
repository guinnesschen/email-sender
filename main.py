import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def read_email_login(filename):
    with open(filename, mode='r', encoding='utf-8') as email_login:
        lines = email_login.readlines()
        return lines[0].strip('\n'), lines[1].strip('\n')


def read_message(filename):
    with open(filename, 'r', encoding='utf-8') as message_file:
        return message_file.read()


def main(login_file, message_file, recipient, subject):
    my_address, my_password = read_email_login(login_file)
    message = read_message(message_file)
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(my_address, my_password)

    msg = MIMEMultipart()  # create a message

    # setup the parameters of the message
    msg['From'] = my_address
    msg['To'] = recipient
    msg['Subject'] = subject

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg

    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == '__main__':
    main(login_file=sys.argv[1], message_file=sys.argv[2], recipient=sys.argv[3], subject=sys.argv[4])
