from rest_framework import serializers
from college.models import College
              

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['id', 'collage_name','address','phone_no']

    def validate_name(self, value):
        if College.objects.filter(name=value).exists():
            raise serializers.ValidationError("This college name already exists.")
        return value