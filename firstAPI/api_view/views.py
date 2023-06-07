import json
from django.http import JsonResponse

def api_home(request, *arg, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    data['nombre'] = request.GET['nombre']
    print(data['nombre'])
    return JsonResponse({
        'message': data['nombre']
    })
