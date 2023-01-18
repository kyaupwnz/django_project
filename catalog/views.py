from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'catalog/index.html')

def contacts(request):
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('phone'))
        print(request.POST.get('message'))
    return render(request, 'catalog/contacts.html')