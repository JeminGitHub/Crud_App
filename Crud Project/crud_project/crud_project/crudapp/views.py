from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Crud
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="signup.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")

            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="signin.html", context={"login_form": form})


class CrudDeleteView(DeleteView):
    model = Crud
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'crud'


def add(request):
    if request.method == 'POST':
        sl_no = request.POST.get('sl_no', '')
        item_name = request.POST.get('item_name', '').title()
        desc = request.POST.get('desc', '')
        date = request.POST.get('date', '')
        if sl_no and item_name and desc and date:  # Validate the fields
            crud = Crud(sl_no=sl_no, item_name=item_name, desc=desc, date=date)
            crud.save()
        else:
            return redirect('home')  # Redirect to the home page if any field is missing or empty

    return render(request, 'home.html')


# def edit(request):
#     crud1 = Crud.objects.all
#     return render(request,'for_edit.html',{'crud1':crud1})


class Crudlistview(ListView):
    model = Crud
    template_name = 'listview.html'
    context_object_name = 'crud1'


class CrudDetailview(DetailView):
    model = Crud
    template_name = 'detail.html'
    context_object_name = 'crud'


class CrudUpdate(UpdateView):
    model = Crud
    template_name = 'update.html'
    context_object_name = 'crud'
    fields = ('sl_no', 'item_name', 'desc', 'date')

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.id})


class CrudDeleteView(DeleteView):
    model = Crud
    template_name = 'delete.html'
    success_url = reverse_lazy('edit')
    context_object_name = 'crud'
