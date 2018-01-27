from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


@require_http_methods(['GET'])
def index(request):
	return render(request, 'index.html')


@csrf_exempt
@require_http_methods(['POST'])
def controlador1(request):
	usuario = request.POST['user_name']
	contrasenia = request.POST['user_password']
	return render(request, 'secundaria.html', 
                  {'usuario': usuario, 'contrasenia': contrasenia})


@csrf_exempt
@require_http_methods(['POST'])
def controlador2(request):
	usuario = request.POST['user_name']
	contrasenia = request.POST['user_password']
	valor1 = request.POST['user_valor1']
	valor2 = request.POST['user_valor2']
	resultado = int(valor1) + int(valor2)
	return render(request, 'final.html', 
                  {'resultado': resultado, 'usuario': usuario, 
                   'contrasenia': contrasenia, 'valor1': valor1, 
                   'valor2': valor2})
