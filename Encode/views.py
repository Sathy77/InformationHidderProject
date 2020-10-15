from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EncodedDataForm
from .models import EncodedData

# Create your views here.
@login_required
def encodePage(request):
    EncodedData_list = EncodedData.objects.filter(user=request.user)

    if len(EncodedData_list) != 0:
        Data = EncodedData.objects.get(user=request.user)
        form = EncodedDataForm(initial={'Starting_Index': Data.Starting_Index,
                                        'Ghap': Data.Ghap,
                                        'Add_a_Value': Data.Add_a_Value,
                                        'HiddenData': Data.HiddenData,
                                        })
    else:
        Data = None
        form = EncodedDataForm()

    if request.method == "POST":
        form = EncodedDataForm(request.POST, request.FILES)

        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user

            if Data == None:
                instance.save()
            else:
                Data.Starting_Index = instance.Starting_Index
                Data.Ghap = instance.Ghap
                Data.Add_a_Value = instance.Add_a_Value
                Data.HiddenData = instance.HiddenData
                Data.DataImage = instance.DataImage
                Data.save()
            return redirect('profile')
    context = {
        'form': form
    }
    return render(request, 'Encode/Encode.html', context)