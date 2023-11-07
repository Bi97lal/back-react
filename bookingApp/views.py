from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Booking,Course
from django.core import serializers

import json

@csrf_exempt
def post_student(request):
    if request.method == 'POST':
        if request.body:
            try:
                data = json.loads(request.body)
                # Now, you can access and use the JSON data as needed
                firstName = data.get('firstName', '')
                lastnNme = data.get('lastnNme', '')
                email = data.get('email', '')
                phone = data.get('phone', '')
                age = data.get('age', '')
                
                # Create and save the Course instance here

                response_data = {
                     'firstName': data.get('firstName', ''),
                     'lastName': data.get('lastName', ''),
                    ' email': data.get('email', ''),
                    'email': email,
                    'phone': phone,
                     'age': age,

                }

                return JsonResponse({'data': response_data}, status=200)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        else:
            return JsonResponse({'error': 'Empty request body'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)
    
def get_courses(request):
    courses=Course.objects.all()
    data = [{'id': course.id, 'name': course.coursesName,'Description': course.Description,'img':course.image,'is_puplish':course.is_puplish,'cateoryID':course.cateoryID.categoryName } for course in courses]
    return JsonResponse(data,safe=False)

    
def get_details(request,id):
    try:
        course = Course.objects.get(pk=id)
        course_data = serializers.serialize('json', [course])
        return JsonResponse({'course':course_data}, safe=False)
    except Course.DoesNotExist:
        return JsonResponse({'error': 'Course not found'})
    
        
def deleteItem(request,id):
    try:
        course = Course.objects.get(pk=id)
        course.delete()  # This will delete the course
        return JsonResponse({'message': 'Deleted item successfully'})
    except Course.DoesNotExist:
        return JsonResponse({'error': 'Course not found'})