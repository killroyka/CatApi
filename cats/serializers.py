from rest_framework import serializers

from cats.models import Cat, Breed, Grade


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'user', 'grade']
        read_only_fields = ['id']


class CatSerializer(serializers.ModelSerializer):
    grades = GradeSerializer(many=True, read_only=True)

    class Meta:
        model = Cat
        fields = '__all__'
        read_only_fields = ['id']


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'
        read_only_fields = ['id']
