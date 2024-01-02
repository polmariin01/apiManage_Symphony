from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Symphony_Counting_Model
from .serializers import Symphony_Serializer

import requests
# Create your views here.

class Symphony_ListView(generics.ListCreateAPIView):
    queryset = Symphony_Counting_Model.objects.all()
    serializer_class = Symphony_Serializer


@api_view(['POST'])
def count_interaction(request, pk):
    # curl -X POST http://localhost:8000/composer/12/count/
    try:
        # Si existeix a la taula, actualitza el valor de clicks
        model = Symphony_Counting_Model.objects.get(pk=pk)
    except Symphony_Counting_Model.DoesNotExist:
        # Si no existeix a la taula, crida a la API on hi ha les dades i extreu el nom del compositor amb aquella id
        # Crea una nova instancia a la base de dades, amb la id, el nom corresponent i 1 interacció

        # Calls the original api to know the name of the composer
        try:
            url = f'https://api.openopus.org/composer/list/ids/{pk}.json'
            response = requests.get(url)
            print(response)
            if response.status_code == 200:
                data = response.json()
                name = data['composers'][0]['complete_name'] 
        except:
            name = f'Object {pk}'

#        model = Symphony_Counting_Model(id = id, countedInteractions = 1, name=f"Object {id}", isTrending = False)
        model = Symphony_Counting_Model(id = pk, countedInteractions = 1, name = name, isTrending = False)

        model.save()

        serializer = Symphony_Serializer(model)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    except:
        return Response({'error': 'Object not found & not possible to create'}, status=status.HTTP_404_NOT_FOUND)

    model.countedInteractions += 1
    model.save()

    serializer = Symphony_Serializer(model)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_interactions(request, pk):
    try:
        model = Symphony_Counting_Model.objects.get(pk=pk)
    except:
        return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = Symphony_Serializer(model)
    return Response(serializer.data, status=status.HTTP_200_OK)


def index(request):
    return HttpResponse("Hello, world.")
