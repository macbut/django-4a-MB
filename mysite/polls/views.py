from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse('''
    
    <button style="background-color:blue" onclick="increases()">przycisk</button>
    <br><br>
    <input></input>
    <br><br>
    <selct></select>
    
    
    
    
    
    
    
    
    
    
    
    ''')