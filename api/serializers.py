from rest_framework import serializers
from .models import RoomBooking

class RoomBookingSerializer(serializers.ModelSerializer):
    booking_end = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = RoomBooking
        fields = ['room_id', 'booked_by', 'booking_start', 'duration_minutes', 'booking_end']
        read_only_fields = ['room_id', 'booking_end']
    
    def get_booking_end(self, obj):
        return obj.booking_end

    def validate_duration_minutes(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be a positive number.")
        return value
