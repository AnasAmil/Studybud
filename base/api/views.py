from django.http import JsonReponse

def getRoutes(request):
    routes = [
        'GET /api/rooms',
        'GET /api/rooms/:id',

    ]
    return JsonReponse(routes, safe=False)