import schedule
print(schedule.__version__)
import time
from send_email import send_email
from generate_report import generate_report

def job():
    report = generate_report()
    send_email(
        subject="Daily Report",
        body=report,
        to_email="recipient_email@example.com"
    )

schedule.every().day.at("09:00").do(job)  # Adjust the time as needed

while True:
    schedule.run_pending()
    time.sleep(1)
