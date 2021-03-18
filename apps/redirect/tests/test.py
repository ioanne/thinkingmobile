from django.test import TestCase

from apps.redirect.factories import Redirect


class RedirectTestCase(TestCase):

    def setUp(self):
        self.redirect = Redirect.objects.create(
            key='123456',
            url='https://www.google.com.ar/images/123456/'
        )
        Redirect.objects.create(
            key='56789',
            url='https://www.google.com.ar/images/56789/'
        )
        Redirect.objects.create(
            key='445566',
            url='https://www.google.com.ar/images/445566/',
            active=False
        )

    def test_set_active_to_cache(self):
        self.assertEqual(
            len(self.redirect.set_active_to_cache()), 2
        )

    def test_get_active_from_cache(self):
        redirect_active_data = {'123456': 'https://www.google.com.ar/images/123456/', '56789': 'https://www.google.com.ar/images/56789/'}
        self.assertDictEqual(self.redirect.get_active_from_cache(), redirect_active_data)

    def test_get_redirect(self):
        self.assertEqual(Redirect.get_redirect(11111111), None)
        self.assertEqual(
            Redirect.get_redirect('123456'),
            {'key': '123456', 'url': 'https://www.google.com.ar/images/123456/'}
        )
        self.assertEqual(Redirect.get_redirect('445566'), None)
