from django.shortcuts import render
from .models import get_doltdata, get_agencies_in_state, get_datasets_for_agency
from django.http import JsonResponse

# Create your views here.
def index(request):
    states = get_doltdata('states')
    data_types = get_doltdata('data_types')
    format_types = get_doltdata('format_types')
    source_types = get_doltdata('source_types')
    update = get_doltdata('update_frequency')
    context = {'states': states, 'data_types': data_types, 'format_types': format_types, 'source_types': source_types, 'update': update}
    return render(request, 'index.html', context=context)

def get_agencies(request, state_iso):
    return JsonResponse(get_agencies_in_state(state_iso), safe=False)

def get_datasets(request, id):
    return JsonResponse(get_datasets_for_agency(id), safe=False)