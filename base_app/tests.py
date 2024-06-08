from django.test import TestCase
from .models import Booking, Table 



# Create your tests here.


class Table_Model_Test(TestCase):
    table_no = "1"
    def setUp(self):
        """_summary_
        Create a table instance without setting the isbooked property so I can assert that by default, its value is set to false
        """
        self.table = Table.objects.create(
            no = self.table_no,
            seating_capacity = "6",
            price="$400",
            description="Single table by the water side"
        )

    def test_table_default_isbooked_value(self):
        self.assertFalse(self.table.is_booked)

    def test_string_representation(self):
        self.assertEqual(str(self.table),f"Table {self.table_no}") 