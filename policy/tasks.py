from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from lxml import html


def notify_new_term_version(term: dict, member: dict):

    to = ['{} <{}>'.format(member.get('first_name'), member.get('email'))]
    subject = 'Estamos atualizando nossos Termos de Uso'
    reply_to = [settings.EMAIL_HOST_REPLY_TO]

    template_name = 'policy/mail_new_term_version.html'
    body = render_to_string(template_name, {
        'member': member,
        'term': term,
    })
    body_txt = html.document_fromstring(body).text_content()

    mail = EmailMultiAlternatives(
        subject=subject.strip(),
        body=body_txt,
        from_email=settings.EMAIL_HOST_FROM,
        to=to,
        reply_to=reply_to,
    )

    mail.attach_alternative(body, 'text/html')

    return mail.send()
