from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Labor
from .serializers import LaborSerializer
import random
# Create your views here.

@api_view(['GET'])
def helloAPI(request):
    return Response('hello world')


@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Labor.objects.all()
    randomQuizs = random.sample(list(totalQuizs), id)
    serializer = LaborSerializer(randomQuizs, many=True)
    return Response(serializer.data)

