from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class RoomBookingAPITest(APITestCase):
    def setUp(self):
        self.url = reverse('room_booking-list')
        self.booking_data = {
            "booked_by": "John Doe",
            "booking_start": "2025-02-11T10:00:00Z",
            "duration_minutes": 60
        }

    def test_create_room_booking(self):
        response = self.client.post(self.url, self.booking_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('booking_end', response.data)
        self.assertEqual(response.data['booked_by'], "John Doe")

    def test_retrieve_room_booking(self):
        create_response = self.client.post(self.url, self.booking_data, format='json')
        room_id = create_response.data.get('room_id')
        retrieve_url = reverse('room_booking-detail', kwargs={'pk': room_id})
        response = self.client.get(retrieve_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['room_id'], room_id)

    def test_update_room_booking(self):
        create_response = self.client.post(self.url, self.booking_data, format='json')
        room_id = create_response.data.get('room_id')
        update_url = reverse('room_booking-detail', kwargs={'pk': room_id})
        updated_data = {
            "booked_by": "Jane Doe",
            "booking_start": "2025-02-11T11:00:00Z",
            "duration_minutes": 90
        }
        response = self.client.put(update_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['booked_by'], "Jane Doe")

    def test_delete_room_booking(self):
        create_response = self.client.post(self.url, self.booking_data, format='json')
        room_id = create_response.data.get('room_id')
        delete_url = reverse('room_booking-detail', kwargs={'pk': room_id})
        response = self.client.delete(delete_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
