from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Inventory
# Create your views here.



def dashboard(request):

    Invs = Inventory.objects.all()

    user = get_user_model()
    guys = user.objects.all()

    return render(request,'dashboard.html', { 'guys': guys, 'Invs': Invs })