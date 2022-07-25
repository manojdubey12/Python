import asyncio
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import aiosmtplib

MAIL_PARAMS = {'TLS': True, 'host': 'stmp.gmail.com', 'password': 'manoj@321', 'user': 'thoughtwin.manoj@gmail.com', 'port': 587}

if sys.platform == 'win32':
    loop = asyncio.get_event_loop()
    if not loop.is_running() and not isinstance(loop, asyncio.ProactorEventLoop):
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)


async def send_mail_async(sender, to, subject, text, textType='plain', **params):
    """Send an outgoing email with the given parameters.

    :param sender: From whom the email is being sent
    :type sender: str

    :param to: A list of recipient email addresses.
    :type to: list

    :param subject: The subject of the email.
    :type subject: str

    :param text: The text of the email.
    :type text: str

    :param textType: Mime subtype of text, defaults to 'plain' (can be 'html').
    :type text: str

    :param params: An optional set of parameters. (See below)
    :type params; dict

    Optional Parameters:
    :cc: A list of Cc email addresses.
    :bcc: A list of Bcc email addresses.
    """

    # Default Parameters
    cc = params.get("cc", [])
    bcc = params.get("bcc", [])
    mail_params = params.get("mail_params", MAIL_PARAMS)

    # Prepare Message
    msg = MIMEMultipart()
    msg.preamble = subject
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(to)
    if len(cc): msg['Cc'] = ', '.join(cc)
    if len(bcc): msg['Bcc'] = ', '.join(bcc)

    msg.attach(MIMEText(text, textType, 'utf-8'))

    # Contact SMTP server and send Message
    host = mail_params.get('host', 'smtp.gmail.com')
    isSSL = mail_params.get('SSL', False);
    isTLS = mail_params.get('TLS', False);
    port = mail_params.get('port', 465 if isSSL else 25)
    smtp = aiosmtplib.SMTP(hostname=host, port=587, use_tls=isSSL)
    await smtp.connect()
    print("connected")
    if isTLS:
        await smtp.starttls()
    if 'user' in mail_params:
        await smtp.login(mail_params['user'], mail_params['password'])
    await smtp.send_message(msg)
    print()
    await smtp.quit()

    if __name__ == "__main__":
        email = "rajatm@thoughtwin.com"
        print("rasdsd")
        co1 = send_mail_async(email,
                          [email],
                          "Test 1",
                          'Test 1 Message',
                          textType="plain")
        co2 = send_mail_async(email,
                          [email],
                          "Test 2",
                          'Test 2 Message',
                          textType="plain")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(co1, co2))
        print(co2)
        loop.close()
