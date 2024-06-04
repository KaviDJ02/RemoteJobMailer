import requests
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

COMMASPACE = ', '

BASE_URL = "https://remoteok.com/api/"
USER_AGENT ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
REQUEST_HEADER = {
    'User-Agent' : USER_AGENT,
    'Accept-Language' : 'en-US, en;q=0.5'
}

def get_job_posting():
    res = requests.get(url=BASE_URL, headers=REQUEST_HEADER) 
    return res.json()

def output_jobs_to_xls(data):
    wb = Workbook()
    job_sheet = wb.add_sheet('jobs')
    headers = list(data[0].keys())
    for i in range(0, len(headers)):
        job_sheet.write(0, i, headers[i])
    for i in range(0, len(data)):
        job = data[i]
        values = list(job.values())
        for x in range(0, len(values)):
            if isinstance(values[x], str):
                value = values[x][:32767]  
            else:
                value = values[x]  
            job_sheet.write(i+1, x, value)
    wb.save('remote_jobs.xls')

def send_email(send_from, send_to, subject, text, files=None):
    assert isinstance(send_to, list)
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(fil.read(), Name=basename(f))
        part['Content-Disposition'] = f'attachment; filename="{basename(f)}"'
        msg.attach(part) 

    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(send_from, 'Password')  # Replace with a secure password storage mechanism
        smtp.sendmail(send_from, send_to, msg.as_string()) 
        smtp.close() 
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    json = get_job_posting()[1:]
    output_jobs_to_xls(json)
    send_email('[send-from email]',['[send-to email]'], 'Jobs Posting', 'Please, find attached a list of job posting to this email', files=['remote_jobs.xls'])