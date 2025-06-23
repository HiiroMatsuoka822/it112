from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer


@api_view(['GET'])
def get_all_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, content_type='application/json')

@api_view(['GET'])
def get_single_item(request):
    item_id = request.GET.get('id')
    if item_id is not None:
        try:
            item = Item.objects.get(id=item_id)
            serializer = ItemSerializer(item)
            return Response(serializer.data, content_type='application/json')
        except Item.DoesNotExist:
            return Response({'error': 'Item not found'}, content_type='application/json')
    else:
        return Response({'error': 'No id provided'}, content_type='application/json')

@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Item created successfully'}, status=200, content_type='application/json')
    else:
        return Response({'error': 'Failed to create item'}, status=200, content_type='application/json')


