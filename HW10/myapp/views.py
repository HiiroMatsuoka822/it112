import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MyItem

# Decorator to allow POST requests without CSRF token for API endpoints.
# In a production environment, ensure proper authentication and security measures
# are in place to protect your API.
@csrf_exempt
def get_all_items(request):
    """
    Handles GET requests to return all items in the database.
    Returns:
        JsonResponse: A JSON list of all MyItem objects.
    """
    if request.method == 'GET':
        # Retrieve all MyItem objects from the database
        items = MyItem.objects.all()
        # Convert each item to a dictionary for JSON serialization
        items_data = [{"id": item.id, "title": item.title, "description": item.description, "created_at": item.created_at.isoformat()} for item in items]
        # Return a JsonResponse with the list of items
        return JsonResponse(items_data, safe=False, content_type="application/json")
    else:
        # If not a GET request, return a method not allowed error
        return JsonResponse({"error": "Method Not Allowed"}, status=405, content_type="application/json")

@csrf_exempt
def get_single_item(request):
    """
    Handles GET requests to return a single item based on a query parameter (id).
    Expected query parameter: 'id'
    Returns:
        JsonResponse: A JSON object of the requested MyItem or an error.
    """
    if request.method == 'GET':
        item_id = request.GET.get('id')
        if not item_id:
            # If 'id' query parameter is missing
            return JsonResponse({"error": "Missing 'id' query parameter"}, status=400, content_type="application/json")
        try:
            # Attempt to retrieve the item by its ID
            item = MyItem.objects.get(id=item_id)
            # Convert the item to a dictionary
            item_data = {"id": item.id, "title": item.title, "description": item.description, "created_at": item.created_at.isoformat()}
            # Return a JsonResponse with the single item
            return JsonResponse(item_data, content_type="application/json")
        except MyItem.DoesNotExist:
            # If no item with the given ID is found
            return JsonResponse({"error": "Item not found"}, status=404, content_type="application/json")
    else:
        # If not a GET request, return a method not allowed error
        return JsonResponse({"error": "Method Not Allowed"}, status=405, content_type="application/json")

@csrf_exempt
def add_item(request):
    """
    Handles POST requests to receive and insert data for a new database record.
    Expected POST data (JSON): {"title": "...", "description": "..."}
    Returns:
        JsonResponse: A success or error message with HTTP status code 200.
    """
    if request.method == 'POST':
        try:
            # Load JSON data from the request body
            data = json.loads(request.body)
            title = data.get('title')
            description = data.get('description')

            # Basic validation for required fields
            if not title or not description:
                return JsonResponse({"status": "failure", "message": "Title and description are required."}, status=200, content_type="application/json")

            # Create and save the new MyItem object
            item = MyItem.objects.create(title=title, description=description)
            item.save()

            # Return a success response
            return JsonResponse({"status": "success", "message": "Item added successfully", "id": item.id}, status=200, content_type="application/json")

        except json.JSONDecodeError:
            # Handle invalid JSON in the request body
            return JsonResponse({"status": "failure", "message": "Invalid JSON format"}, status=200, content_type="application/json")
        except Exception as e:
            # Catch any other unexpected errors
            return JsonResponse({"status": "failure", "message": str(e)}, status=200, content_type="application/json")
    else:
        # If not a POST request, return a method not allowed error
        return JsonResponse({"error": "Method Not Allowed"}, status=405, content_type="application/json")



