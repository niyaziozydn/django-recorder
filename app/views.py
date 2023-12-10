from django.shortcuts import render

def camrecorder(request):
    context = {}
    return render(request,"recorder.html",context)