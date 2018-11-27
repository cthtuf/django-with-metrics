from random import randint

from django.http import JsonResponse


def view_with_always_200(request):
    return JsonResponse({'some_param': 'some_value'})


def view_with_random_code(request):
    possible_responses = [
        {'code': 500, 'data': {'error': 'Something goes wrong on the server.'}},
        {'code': 400, 'data': {'error': 'You request looks bad. Retry with better data.'}},
        {'code': 404, 'data': {'error': 'Cant find the page.'}},
        {'code': 401, 'data': {'error': 'You have to pass credentials.'}},
        {'code': 403, 'data': {'error': 'Permission denied'}}
    ]
    current_response = possible_responses[randint(0, 4)]
    return JsonResponse(data=current_response['data'], status=current_response['code'])


def view_with_always_500(request):
    raise Exception("I'll break this request")
