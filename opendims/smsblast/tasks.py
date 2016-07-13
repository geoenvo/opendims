from django_rq import job

from smsblast.models import Template, Contact, Group, Message


@job
