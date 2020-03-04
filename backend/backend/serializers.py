from rest_framework import serializers
from backend.models import *


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Person
        fields = '__all__'


class CoupleSerializer(serializers.ModelSerializer):
    person_1 = PersonSerializer()
    person_2 = PersonSerializer()

    class Meta:
        model = Couple
        fields = 'person_1', 'person_2'


class SessionSerializer(serializers.ModelSerializer):
    couples = CoupleSerializer(many=True)

    class Meta:
        model = Session
        fields = 'creation_date', 'valid', 'couples'
