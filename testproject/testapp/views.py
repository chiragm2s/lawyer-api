
from rest_framework.viewsets import ModelViewSet
from . models import *
from . serializers import *



class lawclass(ModelViewSet):
    serializer_class=lawSerializers
    queryset=testtable.objects.all()




# @csrf_exempt
# def post(request):
#     if request.method=='POST':
#         # serializer=lawSerializers(data=request.data)
#         # if serializer.is_valid(raise_exception=True):
#         #     serializer.save()
#         #     return Response(serializer.data)
#         data = json.loads(request.body.encode("utf-8"))
#         p_name = data.get('caseId')
#         p_price = data.get('userName')
#         p_quantity = data.get('caseSection')
#         p_Detail = data.get('caseDetails')
#         p_type = data.get('caseType')

#         product_data = {
#             'caseId': p_name,
#             'userName': p_price,
#             'caseSection': p_quantity,
#             'caseDetails':p_Detail,
#             'caseType':p_type,
#         }

#         cart_item = testtable.objects.create(**product_data)

#         data = {
#             "message": f"New item added to Cart with id: "
#         }
#         return HttpResponse(data, status=201)



# def testtem(request):
#     if request.method=='GET':
#         return render(request,'test11\caseDetails.html') 