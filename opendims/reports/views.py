from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.conf import settings

from .serializers import EventSerializer, ReportSerializer
from rest_framework import generics, filters, response, status

from .models import Event, Report
from .filters import EventFilter


class EventListView(generic.ListView):
    queryset = Event.objects.order_by('-created')
    paginate_by = settings.ITEMS_PER_PAGE


class EventDetailView(generic.DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['reports'] = Report.objects.filter(event=self.get_object())
        return context


def report_list(request):
    reports = Report.objects.order_by('-created')
    context = {'reports': reports}
    return render(request, 'reports/report_list.html', context)


def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    context = {'report': report}
    return render(request, 'reports/report_detail.html', context)


class CustomListCreateAPIView(generics.ListCreateAPIView):
    """
    Subclass API View to deal with django-filter strict not working. Overrides
    get method to check for invalid query params. If found return error 400.
    http://stackoverflow.com/questions/27182527
    """
    def is_valid_query_params(self, query_params):
        if query_params:
            valid_params = self.filter_class.Meta.fields
            # Accept default "format" parameter
            valid_params.append('format')
            print valid_params
            query_params = [query_param.lower()
                            for query_param in query_params.keys()]
            invalid_params = set(query_params) - set(valid_params)
            if invalid_params:
                return False
        return True

    def get(self, request, *args, **kwargs):
        if not self.is_valid_query_params(request.query_params):
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        return super(CustomListCreateAPIView, self).get(
                                                    request, *args, **kwargs)


class APIEventList(CustomListCreateAPIView):
    queryset = Event.objects.filter(status='ACTIVE')
    serializer_class = EventSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    filter_class = EventFilter
    ordering_fields = ('created',)
    ordering = ('-created',)


class APIReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class APIReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
