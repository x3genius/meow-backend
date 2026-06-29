from .models import Pet, PetPhoto
from rest_framework import serializers

class PetPhotoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = PetPhoto
        fields = '__all__'

    def get_image(self, obj):
        return obj.image.url if obj.image else None

class PetSerializer(serializers.ModelSerializer):
    age = serializers.ReadOnlyField()
    age_category = serializers.ReadOnlyField()
    photos = PetPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Pet
        fields = '__all__'

