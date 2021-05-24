import json
from django.views import View
from django.http import JsonResponse
from .models import Menu

class ProductListView(View):
    def get(self, request):
        menus = Menu.objects.all()
        result = []
        for menu in menus:
            result.append(menu.name)
        return JsonResponse({'result': result}, status=200)

    def post(self, request):
        try:
            data = json.loads(request.body) #json->python
            Menu.objects.create(name = data['name'])
            return JsonResponse({'result': "SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({'message': 'INVAILID_KEY'}, status=400)