import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_admin(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            response = requests.post('http://localhost:3000/api/login/admin', json=data)
            response.raise_for_status()  # Esto lanzará una excepción si la respuesta no es 200 OK
            try:
                data = response.json()
            except ValueError:
                return JsonResponse({'error': 'Respuesta no es un JSON válido', 'content': response.text}, status=500)
            return JsonResponse(data)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def get_viajes_pasajero(request):
    try:
        response = requests.get('http://localhost:3000/api/viajes_pasajero')
        response.raise_for_status()
        try:
            data = response.json()
        except ValueError:
            return JsonResponse({'error': 'Respuesta no es un JSON válido', 'content': response.text}, status=500)
        return JsonResponse(data, safe=False)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_viaje_pasajero_by_id(request, id):
    try:
        response = requests.get(f'http://localhost:3000/api/viajes_pasajero/{id}')
        response.raise_for_status()
        try:
            data = response.json()
        except ValueError:
            return JsonResponse({'error': 'Respuesta no es un JSON válido', 'content': response.text}, status=500)
        return JsonResponse(data)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_vehiculos(request):
    try:
        response = requests.get('http://localhost:3000/api/vehiculos')
        response.raise_for_status()
        try:
            data = response.json()
        except ValueError:
            return JsonResponse({'error': 'Respuesta no es un JSON válido', 'content': response.text}, status=500)
        return JsonResponse(data, safe=False)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_vehiculo_by_id(request, id):
    try:
        response = requests.get(f'http://localhost:3000/api/vehiculos/{id}')
        response.raise_for_status()
        try:
            data = response.json()
        except ValueError:
            return JsonResponse({'error': 'Respuesta no es un JSON válido', 'content': response.text}, status=500)
        return JsonResponse(data)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def create_vehiculo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            response = requests.post('http://localhost:3000/api/vehiculos', json=data)
            response.raise_for_status()
            try:
                data = response.json()
            except ValueError:
                return JsonResponse({'error': 'Respuesta no es un JSON válido', 'content': response.text}, status=500)
            return JsonResponse(data, status=201)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def update_vehiculo(request, id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            response = requests.put(f'http://localhost:3000/api/vehiculos/{id}', json=data)
            response.raise_for_status()
            try:
                data = response.json()
            except ValueError:
                return JsonResponse({'error': 'Respuesta no es un JSON válido', 'content': response.text}, status=500)
            return JsonResponse(data)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def delete_vehiculo(request, id):
    if request.method == 'DELETE':
        try:
            response = requests.delete(f'http://localhost:3000/api/vehiculos/{id}')
            response.raise_for_status()
            return JsonResponse({'message': 'Vehículo eliminado'})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)