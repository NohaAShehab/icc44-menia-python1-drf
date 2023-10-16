


from rest_framework import serializers
from students.models import Student
from rest_framework import validators


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(validators=[validators.UniqueValidator(queryset=Student.get_all_students())])
    grade = serializers.IntegerField(default=0)
    image= serializers.ImageField(allow_empty_file=True, allow_null=True, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


    def create(self, validated_data):
        return  Student.objects.create(**validated_data)



    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.email = validated_data['email']
        instance.grade = validated_data['grade']
        instance.image = validated_data['image']
        instance.save()
        return  instance