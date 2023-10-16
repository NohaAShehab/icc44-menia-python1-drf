

from rest_framework import serializers

from students.models import Student
from tracks.api.serializers import TrackModelSerializer
class StudentModelSerializer(serializers.ModelSerializer):
    # track  =serializers.StringRelatedField(read_only=True)
    track = TrackModelSerializer(read_only=True)
    # track_name = serializers.CharField(source=track.data.name, read_only=True)
    track_id = serializers.IntegerField(write_only=True, required=False)
    class Meta:
        model = Student
        fields = '__all__'