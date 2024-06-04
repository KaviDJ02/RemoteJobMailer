
# Remote Jobs Script

This repository contains a Python script to fetch remote job postings from the Remote OK API, save the data into an Excel file, and send the file via email.




## Features

- Fetch remote job postings from the Remote OK API
- Save job postings to an Excel file (remote_jobs.xls)
- Send the Excel file as an email attachment

## Requirements

- Python 3.x
- requests library
- xlwt library
- smtplib and email modules (standard libraries)





## Installation

1. Clone the repository:

```bash
git clone https://github.com/KaviDJ02/RemoteJobMailer.git
cd RemoteJobMailer

```
2. Install the required libraries:

```bash
pip install requests xlwt

```

    
## Usage

1. Open the script file and replace the placeholder values with your own:

- Replace [send-from email] with your email address.
- Replace [send-to email] with the recipient's email address.
- Replace 'Password' with your email account password.


```python
send_email('[send-from email]', ['[send-to email]'], 'Jobs Posting', 'Please, find attached a list of job posting to this email', files=['remote_jobs.xls'])
```

2. Run the script:

```bash
python remoteok_scraper.py
```


## Script Explanation

### Functions

- get_job_posting(): Fetches job postings from the Remote OK API and returns the data in JSON format.
- output_jobs_to_xls(data): Takes job posting data as input and writes it to an Excel file (remote_jobs.xls).
- send_email(send_from, send_to, subject, text, files=None): Sends an email with the specified subject and text, attaching any files provided.

### Main Execution

- Fetch job postings data from the API, skipping the first entry.
- Save the job postings to an Excel file.
- Send the Excel file via email.

## Important Notes

- Make sure to use a secure method to handle your email password. Consider using environment variables or a secrets manager for storing sensitive information.
- The script uses Gmail's SMTP server. If you are using a different email provider, update the SMTP server details accordingly.

