import smtplib
from email.mime.text import MIMEText

title = '테스트'
text = '테스트'

send_email = 'withq.network@gmail.com'
pwd = 'rtlgoixgbvrkojyu' # APP 비밀번호 발급 필수
receive_email = 'withq_network@naver.com'

smtp = smtplib.SMTP('smtp.gmail.com', 587) # 계정 IMAP 활성화 필수
smtp.ehlo()
smtp.starttls()
smtp.login(send_email, pwd)

mail = MIMEText(text)

mail['Subject'] = title
mail['From'] = send_email
mail['To']= receive_email

smtp.sendmail(send_email, receive_email, mail.as_string())

smtp.quit()
