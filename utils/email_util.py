# -*- coding: utf-8 -*-


import tempfile

import smtplib
from contextlib import contextmanager
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from _local_settings import SMTP_SETTING


def send_email(receivers, ccs, subject, attachments=None, html_text=None):
    msg = MIMEMultipart()
    msg['from'] = SMTP_SETTING['sender']
    msg['subject'] = subject
    msg['to'] = ','.join(receivers)
    msg['cc'] = ','.join(ccs)

    attachments = [] if not attachments else attachments
    for attachment in attachments:
        att = MIMEBase('application', 'octet-stream')
        att.set_payload(attachment['fd'].read())
        encoders.encode_base64(att)
        att.add_header('Content-Disposition', 'attachment; filename="{}"'.
                       format(attachment['fn']))
        msg.attach(att)
    if html_text:
        html = MIMEText(html_text, 'html', 'utf-8')
        msg.attach(html)
    try:
        server = smtplib.SMTP()
        server.connect(SMTP_SETTING['server'])
        server.login(SMTP_SETTING['sender'].split('@')[0], SMTP_SETTING['passwd'])
        server.sendmail(msg['from'], receivers + ccs, msg.as_string())
        server.quit()
    except Exception as e:
        print(repr(e))


def write_tmp_file(data=None):
    fd = tempfile.TemporaryFile()
    try:
        if data:
            fd.write(data)
        fd.seek(0)
        return fd
    except Exception as e:
        fd.close()
        print(repr(e))
        raise e


@contextmanager
def get_tmp_file_fd():
    fd = tempfile.TemporaryFile()
    try:
        yield fd
    finally:
        fd.close()


