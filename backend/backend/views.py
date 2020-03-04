import random

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from backend.error_responses import ErrorResponses
from backend.models import Person, Session, Couple
from backend.serializers import PersonSerializer, SessionSerializer


def persons(request):
    try:
        if request.method == 'GET':
            return JsonResponse(PersonSerializer(Person.objects.all(), many=True).data, safe=False)
        else:
            return ErrorResponses.method_not_allowed(request)
    except Exception as e:
        return ErrorResponses.error_500(str(e))


def sessions(request):
    try:
        if request.method == 'GET':
            return JsonResponse(SessionSerializer(Session.objects.filter(valid=True), many=True).data, safe=False)
        else:
            return ErrorResponses.method_not_allowed(request)
    except Exception as e:
        return ErrorResponses.error_500(str(e))


@csrf_exempt
def random_session(request):
    # try:
    if request.method == 'POST':
        session = Session()
        session.save()

        def pop_random(lst):
            idx = random.randrange(0, len(lst))
            return lst.pop(idx)

        persons = list(Person.objects.all())
        while len(persons) > 1:
            person_1 = pop_random(persons)
            person_2 = pop_random(persons)
            Couple(
                session=session,
                person_1=person_1,
                person_2=person_2,
            ).save()
        return JsonResponse(SessionSerializer(session).data, safe=False)
    else:
        return ErrorResponses.method_not_allowed(request)
    # except Exception as e:
    #     return ErrorResponses.error_500(str(e))


def validate_session(request, session_id):
    try:
        if request.method == 'PUT':
            session = Session.objects.get(pk=session_id)
            session.valid = True
            session.save()
            return JsonResponse(SessionSerializer(session).data, safe=False)
        else:
            return ErrorResponses.method_not_allowed(request)
    except Exception as e:
        return ErrorResponses.error_500(str(e))