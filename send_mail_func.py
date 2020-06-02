def send_mail(smtp,port,sent_from, email_from_password, email_to, subject, body):
    import smtplib

    sent_from=sent_from
    email_from_password=email_from_password
    email_to=[email_to]
    subject=subject
    body=body
    smtp = smtp
    port=port


    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(email_to), subject, body)

    try:
        server = smtplib.SMTP_SSL(smtp, port)
        server.ehlo()
        server.login(sent_from, email_from_password)
        server.sendmail(sent_from, email_to, email_text)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')
