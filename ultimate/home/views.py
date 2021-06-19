from django.shortcuts import render

class Home:
    def index (request):
      return render(request, 'homepage.html')
