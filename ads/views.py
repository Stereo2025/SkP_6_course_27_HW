import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import DetailView

from ads.models import Ads, Categories


# Create your views here.
class StatusView(View):
    def get(self, request):
        if request.method == "GET":
            return JsonResponse({'Status': "OK"}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdsView(View):
    def get(self, request):
        ads_result = Ads.objects.all()

        response = []
        for row in ads_result:
            response.append({
                'id': row.id,
                'name': row.name,
                'author': row.author,
                'price': row.price,
                'description': row.description,
                'address': row.address,
                'is_published': row.is_published,
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        ads_data = json.loads(request.body)

        ads_result = Ads(**ads_data)
        ads_result.save()
        response = {
            'id': ads_result.id,
            'name': ads_result.name,
            'author': ads_result.author,
            'price': ads_result.price,
            'description': ads_result.description,
            'address': ads_result.address,
            'is_published': ads_result.is_published,
        }
        return JsonResponse(response,
                            json_dumps_params={"ensure_ascii": False})


# class AdsEntityView(View):
#     def get(self, request, pk):
#         try:
#             ads_result = Ads.objects.get(id=pk)
#         except Ads.DoesNotExist:
#             return JsonResponse({'Error': "NotFound"}, status=404)
#
#         return JsonResponse({
#             'id': ads_result.id,
#             'name': ads_result.name,
#             'author': ads_result.author,
#             'price': ads_result.price,
#             'description': ads_result.description,
#             'address': ads_result.address,
#             'is_published': ads_result.is_published,
#         })
class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ads_result = self.get_object()
        return JsonResponse({
            'id': ads_result.id,
            'name': ads_result.name,
            'author': ads_result.author,
            'price': ads_result.price,
            'description': ads_result.description,
            'address': ads_result.address,
            'is_published': ads_result.is_published,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    def get(self, request):
        categories = Categories.objects.all()

        response = []
        for row in categories:
            response.append({
                'id': row.id,
                'name': row.name,
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        category_data = json.loads(request.body)

        category = Categories(**category_data)
        category.save()
        response = {
            'id': category.id,
            'name': category.name
        }
        return JsonResponse(response,
                            json_dumps_params={"ensure_ascii": False})


# class CategoriesEntityView(View):
#     def get(self, request, pk):
#         try:
#             category = Categories.objects.get(id=pk)
#         except Categories.DoesNotExist:
#             return JsonResponse({'Error': "NotFound"}, status=404)
#
#         return JsonResponse({
#             'id': category.id,
#             'name': category.name,
#         })
class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({
            'id': category.id,
            'name': category.name
        })
