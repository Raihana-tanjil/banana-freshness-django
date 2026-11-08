from django.shortcuts import render, redirect
from .models import BananaRecord
from .forms import BananaRecordForm

def index_view(request):
    if request.method == 'POST':
        form = BananaRecordForm(request.POST)
        if form.is_valid():
            form.save() # Saves record to the SQLite database
            return redirect('index')
    else:
        form = BananaRecordForm()
    
    # Fetch all records from database, newest first
    records = BananaRecord.objects.all().order_by('-created_at')
    
    context = {
        'form': form,
        'records': records
    }
    return render(request, 'inspector/index.html', context)