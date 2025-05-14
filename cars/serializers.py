from rest_framework import serializers
from .models import Car, CarImage, Review
from dropbox_utils import upload_to_dropbox


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['id', 'image']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user_name', 'user_position', 'comment', 'rating', 'date']


class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = [
            'id', 'name', 'description', 'type', 'capacity',
            'transmission', 'fuel_type', 'fuel_capacity',
            'price_per_day', 'original_price', 'is_favorite',
            'images', 'reviews'
        ]


class CarCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )

    class Meta:
        model = Car
        fields = [
            'name', 'description', 'type', 'capacity',
            'transmission', 'fuel_type', 'fuel_capacity',
            'price_per_day', 'original_price', 'is_favorite',
            'images'
        ]

    def create(self, validated_data):
        images = validated_data.pop('images', [])
        car = Car.objects.create(**validated_data)

        for image_file in images:
            image_url = upload_to_dropbox(image_file, image_file.name)
            CarImage.objects.create(car=car, image=image_url)

        return car
