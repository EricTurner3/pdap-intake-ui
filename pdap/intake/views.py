from django.shortcuts import render
#from intake.models import get_doltdata, get_agencies_in_state, get_datasets_for_agency
from master.models import State, Data_Type, Format_Type, Source_Type, Update_Frequency, Agency_Type, Agency, Dataset
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def index(request):
    states = State.objects.all()
    data_types = Data_Type.objects.all()
    format_types = Format_Type.objects.all()
    source_types = Source_Type.objects.all()
    update = Update_Frequency.objects.all()
    context = {'states': states, 'data_types': data_types, 'format_types': format_types, 'source_types': source_types, 'update': update}
    return render(request, 'index.html', context=context)

# similar to above but built specifically for scrapers to auto-build the schema.json
def schema(request):
    states = State.objects.all()
    data_types = Data_Type.objects.all()
    format_types = Format_Type.objects.all()
    source_types = Source_Type.objects.all()
    update = Update_Frequency.objects.all()
    agency_types = Agency_Type.objects.all()
    context = {'states': states, 'data_types': data_types, 'format_types': format_types, 'source_types': source_types, 'update': update, 'agency_types': agency_types}
    return render(request, 'schema.html', context=context)

def get_agencies(request, state_iso):
    data = serializers.serialize('json', Agency.objects.all().filter(state_iso=State.objects.get(name_iso=state_iso)).order_by('name'))
    return HttpResponse(data, content_type="application/json")

def get_datasets(request, id):
    return JsonResponse(Dataset(agency=id).objects.all(), safe=False)