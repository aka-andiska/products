from django.test import TestCase
from .models import Product

from django.core.urlresolvers import reverse

class PeroductMethodTest(TestCase):
    def test_index(self):
        """
        Index should display all peoples
        """
        table = Product.objects.create(name="table", description="long table") #this how to arrange
        chair = Product.objects.create(name="chair", description="office chair")

        response = self.client.get(reverse('index')) #this is how to act

        self.assertEqual(response.status_code, 200) #this is how to assert
        self.assertEqual(len(response.context['products']),2)
        self.assertEqual(response.context['products'][0], table)
        self.assertEqual(response.context['products'][1], chair)

    def test_create(self):
        """
        crete should can creating new data and post in index
        """
        glass = Product.objects.create(name="glass", description="roar")
        spoon = Product.objects.create(name="spoon", description="meow")
        response = self.client.post(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['products']),2)

    def test_edit(self):
        """
        edit should can editing data and get by id
        """
        products = Product.objects.all()
        to_edit = Product.objects.filter(id=2)

        response = self.client.post(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(to_edit, products)

    def test_update(self):
        """
        update can be post data to index after editing by id
        """
        products = Product.objects.all()
        to_update = Product.objects.filter(id=1)

        response = self.client.post(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertNotIn(to_update, products)

    def test_delete(self):
        """
        delete can deleting data by id
        """
        to_delete = Product.objects.filter(id=2)
        products = Product.objects.all()
        self.assertNotIn(to_delete, products)