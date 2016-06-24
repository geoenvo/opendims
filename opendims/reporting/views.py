from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from screamshot.utils import render_template

from reports.models import Event


def test_screamshot(request):
    event = get_object_or_404(Event, pk=4)
    context = {
        'event': event
    }
    # render_template(
    #     'reporting/test_screamshot.html',
    #     context,
    #     output='/home/vagrant/test_screamshot.pdf',
    #     render='pdf',
    #     wait=5000
    # )
    # return HttpResponse('done!')
    return render(request, 'reporting/test_screamshot.html', context)
