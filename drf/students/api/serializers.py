


from rest_framework import serializers
from students.models import Student
from rest_framework import validators
from tracks.models import Track
from tracks.api.serializers import  TrackSerializer

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(validators=[validators.UniqueValidator(queryset=Student.get_all_students())])
    grade = serializers.IntegerField(default=0)
    image= serializers.ImageField(allow_empty_file=True, allow_null=True, required=False)
    track = TrackSerializer(read_only=True)
    track_id = serializers.IntegerField(write_only=True)
    track_name = serializers.StringRelatedField(read_only=True)
    # track_name= serializers.StringRelatedField(read_only=True, source=track)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def get_track_name(self, obj):
        if obj:
            return  obj.track.name
        return  None

    def create(self, validated_data):
        return  Student.objects.create(**validated_data)



    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.email = validated_data['email']
        instance.grade = validated_data['grade']
        instance.image = validated_data['image']
        instance.save()
        return  instance



