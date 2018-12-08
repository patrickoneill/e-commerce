from django.shortcuts import render

def index(request):
    ''' a view that will create an index page '''
    return render(request, 'index.html')
    
