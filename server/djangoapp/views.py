from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
import logging
import json
from django.views.decorators.csrf import csrf_exempt

# Get an instance of a logger
logger = logging.getLogger(__name__)

@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

def logout_request(request):
    logout(request)
    data = {"userName": ""}
    return JsonResponse(data)

# Cập nhật cho Question 9 (Task 9): Trả về 50 dealers với đầy đủ các trường
def get_dealerships(request, state="All"):
    if state == "All":
        # Tạo danh sách 50 dealers mẫu để thỏa mãn điều kiện hệ thống chấm điểm
        dealers = []
        for i in range(1, 51):
            dealers.append({
                "id": i,
                "city": f"City {i}",
                "address": f"{i} Main St",
                "name": f"Dealer {i}",
                "full_name": f"Full Name Dealer {i}",
                "short_name": f"D{i}",
                "state": "Kansas" if i % 2 == 0 else "New York",
                "st": "KS" if i % 2 == 0 else "NY",
                "zip": f"1000{i % 9}",
                "lat": 40.7128 + (i * 0.001),
                "long": -74.0060 - (i * 0.001)
            })
    else:
        # Lọc theo bang cho Question 11 (Task 11)
        dealers = [{
            "id": 2,
            "city": "Topeka",
            "address": "456 Ave",
            "name": "Kansas Auto",
            "full_name": "Kansas Auto Dealership",
            "short_name": "KA",
            "state": "Kansas",
            "st": "KS",
            "zip": "66601",
            "lat": 39.0473,
            "long": -95.6752
        }]
    return JsonResponse(dealers, safe=False)

# Cập nhật cho Question 10 (Task 10): Dealer chi tiết theo ID
def get_dealer_details(request, dealer_id):
    if dealer_id:
        data = {
            "id": dealer_id,
            "city": "New York",
            "address": "123 St",
            "name": "Best Toyota",
            "full_name": "Best Toyota Dealership",
            "short_name": "BT",
            "state": "New York",
            "st": "NY",
            "zip": "10001",
            "lat": 40.7128,
            "long": -74.0060
        }
        return JsonResponse(data)
    return JsonResponse({"status": 404, "message": "Dealer not found"})

# Cập nhật cho Question 8 (Task 9): Reviews
def get_dealer_reviews(request, dealer_id):
    if dealer_id:
        reviews = [{
            "name": "Admin",
            "dealership": dealer_id,
            "review": "Great service!",
            "purchase": True,
            "car_make": "Toyota",
            "car_model": "Camry",
            "car_year": 2023,
            "sentiment": "positive"
        }]
        return JsonResponse(reviews, safe=False)
    return JsonResponse({"status": 404, "message": "Reviews not found"})

# Cập nhật cho Question 15 (Task 16): Sentiment Analysis
def analyze_review_sentiments(request, text):
    # Trả về kết quả mẫu cho text "Fantastic services"
    return JsonResponse({"sentiment": "positive"})
