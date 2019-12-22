from celery import shared_task
from time import sleep
from datetime import datetime
import smtplib

@shared_task
def send_email(subject, body, to, sleep_time):
    sleep(sleep_time)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('bhargav999reddy@gmail.com','dddessvocdaykvvi')

    msg = "Subject: {} \n\n{}".format(subject, body)

    status = server.sendmail(
        'bhargav999reddy@gmail.com',
        to,
        msg
    )
    server.close()
    return 200


def mail_task(mail_data):
    mail_check_out_time = mail_data['check_out_time']
    now = datetime.now()
    present_time = now.strftime("%H:%M")
    hours_now = int(present_time[:2])
    minutes_now = int(present_time[3:5])
    present_time = hours_now * 60 + minutes_now
    time_left = mail_check_out_time
    hours_left = time_left.hour
    minutes_left = time_left.minute
    time_left = hours_left * 60 + minutes_left - present_time
    host_body = "name: {}\nemail : {}\nphone : {}\nCheckin time : {}\nCheckout time : {}".format(mail_data["visitor_name"],mail_data["visitor_mail_id"],mail_data["visitor_phone"],mail_data["check_in_time"],mail_data["check_out_time"])
    visitor_body = "name: {}\nemail : {}\nphone : {}\nCheckin time : {}\nCheckout time : {}\nHost : {}\nAddress visited : {}".format(mail_data["visitor_name"],mail_data["visitor_mail_id"],mail_data["visitor_phone"],mail_data["check_in_time"],mail_data["check_out_time"], mail_data["host_name"],mail_data["host_addr"])
    send_email.delay('New Visitor',host_body,'bhargav999reddy@gmail.com',0)
    send_email.delay('Thank you for visiting',visitor_body,mail_data["visitor_mail_id"],abs(time_left))
