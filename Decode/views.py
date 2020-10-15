from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DecodedData

# Create your views here.
@login_required
def decodePage(request):
    form = DecodedData()
    if request.method == 'POST':
        form = DecodedData(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = DecodedData()

    return render(request, 'Decode/Decode.html')
