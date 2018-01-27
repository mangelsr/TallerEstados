from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


@require_http_methods(['GET'])
def index(request):
	return render(request, 'index.html')


@csrf_exempt
@require_http_methods(['POST'])
def controlador1(request):
	response =  render(request, 'secundaria.html')
	response.set_cookie('usuario', request.POST['user_name'])
	response.set_cookie('contrasenia', request.POST['user_password'])
	return response

	
@csrf_exempt
@require_http_methods(['POST'])
def controlador2(request):
	usuario = request.COOKIES.get('usuario')
	contrasenia = request.COOKIES.get('contrasenia')
	valor1 = request.POST['user_valor1']
	valor2 = request.POST['user_valor2']
	resultado = int(valor1) + int(valor2)
	return render(request, 'final.html', 
                  {'resultado': resultado, 'usuario': usuario, 
                   'contrasenia': contrasenia, 'valor1': valor1, 
                   'valor2': valor2})
