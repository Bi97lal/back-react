from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Booking,Course
import json

@csrf_exempt
def post_student(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        booking=Course(
            coursesName= data['firstName'],
            is_puplish=1,
            cateoryID_id=1
             # lastnNme=data['lastName'],
            # email=data['email'],
            # phone=data['phone'],
            # age=data['age'],
            # coursesID=['coursesID']
        )
        booking.save()

        response_data = {
            'firstName': data.get('firstName', ''),
            'lastName': data.get('lastName', ''),
        }
        return JsonResponse({'data': response_data}, status=200)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)
    

def get_courses(request):
    courses=Course.objects.all()
    data = [{'id': course.id, 'name': course.coursesName,'Description': course.Description,'img':course.image,'is_puplish':course.is_puplish,'cateoryID':course.cateoryID.categoryName } for course in courses]
    return JsonResponse(data,safe=False)

