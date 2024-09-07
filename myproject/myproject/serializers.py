from rest_framework import serializers
from college.models import College
              

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['id', 'collage_name','address','phone_no']

    def  validate_collage_name(self, value):     # Custom validation for unique college_name
        if College.objects.filter(collage_name=value).exists():
            raise serializers.ValidationError("This college name already exists.")
        return value