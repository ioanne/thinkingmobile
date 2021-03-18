import factory
from factory.django import DjangoModelFactory
from faker import Factory

from apps.redirect.models import Redirect

faker = Factory.create()


class RedirectFactory(DjangoModelFactory):
    class Meta:
        model = Redirect

    id = factory.Sequence(lambda n: n+1)
