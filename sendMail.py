import smtplib
from email.mime.text import MIMEText

# accountData | Dictionary => {'email': 'yourEmail@example.com', 'protocol': 'TLS', 'smtp': 'smtp.example.com', 'port': '1234', 'pwd': 'example'}
# receiveEmail | str => receiveEmail@example.com
# title | str => mail title
# text | str => html
# sendMail() | return bool
def sendMail(accountData, receiveEmail, title, text):

    if isinstance(accountData, dict) == False:
        return False

    if ('email' not in accountData == False
    or 'protocol' not in accountData == False
    or 'smtp' not in accountData == False
    or 'port' not in accountData == False
    or 'pwd' not in accountData == False):
        return False
    
    send_email = accountData['email']
    protocol = accountData['protocol']
    smtp = accountData['smtp']
    port = accountData['port']
    pwd = accountData['pwd']

    if protocol == 'TLS':

        try:

            smtp = smtplib.SMTP(smtp, port)
            smtp.starttls()
            smtp.login(send_email, pwd)

        except smtplib.SMTPException as e:

            print(e)

            return False
        
        else:

            mail = MIMEText(text)
            mail['Subject'] = title
            mail['From'] = send_email
            mail['To']= receiveEmail
            smtp.sendmail(send_email, receiveEmail, mail.as_string())
            smtp.quit()

            return True

    elif protocol == 'SSL':

        try:

            smtp = smtplib.SMTP_SSL(smtp, port)
            smtp.login(send_email, pwd)

        except smtplib.SMTPException as e:

            print(e)

            return False

        else:

            mail = MIMEText(text)
            mail['Subject'] = title
            mail['From'] = send_email
            mail['To']= receiveEmail
            smtp.sendmail(send_email, receiveEmail, mail.as_string())
            smtp.quit()

            return True
    
    else:

        return False

dict_ = {
    'email': 'withq.network@gmail.com',
    'protocol': 'TLS',
    'smtp': 'smtp.gmail.com',
    'port': '587',
    'pwd': 'rtlgoixgbvrkojyu'
    }

bool_ = sendMail(dict_, 'withq_network@naver.com', '테스트', '안녕하세요~')

print(bool_)