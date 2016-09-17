from django.core.mail import EmailMessage


def esphoto_email(num):
    """ The function for sending mail as required.
    Params
    to: mail addresses to email
    subject: email subject
    boddy: email boddy
    email_from: the sender email
    bcc: bcc email
    email = EmailMessage instance
    """
    if num <= 500 and num % 100 == 0:
        to = ['demirkiran.bartud@gmail.com']
        subject = '#carnival has {} photos'.format(num)
        body = 'I\'m awesome'
        email_from = 'Hashtag@EversnapApp.com'
        bcc = 'davide@geteversnap.com'
        email = EmailMessage(subject, body, email_from, to, bcc)
        email.send()
