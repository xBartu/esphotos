from django.core.mail import EmailMessage


def esphoto_email(num):
    if num <= 500 and num % 100 == 0:
        to = ['demirkiran.bartud@gmail.com']
        subject = '#carnival has {} photos'.format(num)
        body = 'I\'m awesome'
        email_from = 'Hashtag@EversnapApp.com'
        bcc = 'davide@geteversnap.com'
        email = EmailMessage(subject, body, email_from, to, bcc)
        email.send()
