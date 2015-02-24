import pyzmail

sender=(u'Me', 'andrew@andrewhennessy.net')
recipients=[(u'Him', 'andrewhennessy3455@gmail.com')]
subject=u'the subject'
text_content=u'Bonjour aux Fran\xe7ais'
prefered_encoding='iso-8859-1'
text_encoding='iso-8859-1'

payload, mail_from, rcpt_to, msg_id=pyzmail.compose_mail(\
        sender, \
        recipients, \
        subject, \
        prefered_encoding, \
        (text_content, text_encoding), \
        html=None, \
        attachments=[('attached content', 'text', 'plain', 'text.txt', \
                      'us-ascii')])

print payload






smtp_host='smtp.zoho.com'
smtp_port=465
smtp_mode='ssl'
smtp_login='andrew@andrewhennessy.net'
smtp_password='Srci41998'

ret=pyzmail.send_mail(payload, mail_from, rcpt_to, smtp_host, \
        smtp_port=smtp_port, smtp_mode=smtp_mode, \
        smtp_login=smtp_login, smtp_password=smtp_password)

if isinstance(ret, dict):
    if ret:
        print 'failed recipients:', ', '.join(ret.keys())
    else:
        print 'success'
else:
    print 'error:', ret