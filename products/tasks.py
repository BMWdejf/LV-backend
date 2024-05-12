from celery import shared_task
from django.core.mail import send_mail


@shared_task
def task_done(send_to):
    subject = (
        "David Šablatura sablatura.david@gmail.com"
    )
    message = "This email is from Django. Hello Medium. How are you?"

    email_sent = send_mail(
        subject=subject,
        message=message,
        from_email=None,
        recipient_list=[send_to]
    )

    return email_sent