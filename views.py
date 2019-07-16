#i have created this file views .py
from django.http import HttpResponse
from django .shortcuts import render
def index(request):
    #return render(render, 'index.html')
    return HttpResponse('''<h1>Hello Ampil you are very cazy man.</h1>" <a href="https://www.linkedin.com/in/ampil-verma-1814b9122/"> Go to my Linkedin  profile"''')

# 2nd function about crating
def about(request):
    return HttpResponse("<h2>about me i am very egostic person and  i am also fun loving person</h2>") 