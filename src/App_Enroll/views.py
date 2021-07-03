from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse 
from . forms import Student_Rgistration
from . models import User

#..............ADD PART.............

def add_display(request):
    if request.method == 'POST':
        form = Student_Rgistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            registration = User(name=name, email=email, password=password) #creating a object 
            form.save()
            form = Student_Rgistration()
    else:
        form = Student_Rgistration()
    objects = User.objects.all
    return render(request, 'App_Enroll/add-show.html', context={'form':form, 'objects':objects})

#..............DELETE PART.............

def delete_student(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id).delete()
        # pi.delete()   
        
    return HttpResponseRedirect(reverse('display')) 

#.............. UPDATE PART.............

def edit_student(request, id):
    if request.method == 'POST': 
        pi = User.objects.get(pk=id)
        form = Student_Rgistration(request.POST, instance=pi)
        if form.is_valid:
            form.save()
    else: # for GET request
        pi = User.objects.get(pk=id)
        form = Student_Rgistration(instance=pi)
    return render(request, 'App_Enroll/update-student.html', context={'form':form})            