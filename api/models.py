import uuid
from datetime import timedelta
from django.db import models

class RoomBooking(models.Model):
    room_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    booked_by = models.CharField(max_length=255)
    booking_start = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()

    @property
    def booking_end(self):
        return self.booking_start + timedelta(minutes=self.duration_minutes)

    def __str__(self):
        return f"{self.room_id} booked by {self.booked_by}"
