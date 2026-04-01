from django.test import TestCase
from restaurant.models import Menu, Booking
from datetime import datetime
from django.utils.timezone import make_aware


class MenuModelTest(TestCase):
    def setUp(self):
        self.item = Menu.objects.create(
            title='Pasta',
            price=12.99,
            inventory=10,
        )

    def test_create_menu_item(self):
        self.assertEqual(self.item.title, 'Pasta')

    def test_menu_item_str(self):
        self.assertEqual(str(self.item), 'Pasta : 12.99')

    def test_menu_item_price(self):
        self.assertEqual(self.item.price, 12.99)


class BookingModelTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(
            name='John',
            no_of_guests=4,
            booking_date=make_aware(datetime(2024, 6, 15, 19, 0)),
        )

    def test_create_booking(self):
        self.assertEqual(self.booking.name, 'John')

    def test_booking_str(self):
        self.assertEqual(str(self.booking), 'John')

    def test_booking_guests(self):
        self.assertEqual(self.booking.no_of_guests, 4)


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='Bruschetta', price=8.50, inventory=15)
        Menu.objects.create(title='Lemon Cake', price=6.00, inventory=20)

    def test_menu_api_get(self):
        response = self.client.get('/restaurant/api/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
