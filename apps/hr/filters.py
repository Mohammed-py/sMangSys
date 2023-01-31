from logging import PlaceHolder
from random import choices
from re import search
import django_filters
from django_filters import DateFilter, CharFilter
from django import forms
from django.db.models import Q
from .models import *


##########
# Mixin to solve problme CHarFiled form model to Dropdown menu !!!!


class DynamicChoiceMixin(object):

    @property
    def field(self):
        queryset = self.parent.queryset
        field = super(DynamicChoiceMixin, self).field

        choices = list()
        have = list()
        # iterate through the queryset and pull out the values for the field name
        for item in queryset:
            name = getattr(item, self.field_name)
            if name in have:
                continue
            have.append(name)
            choices.append((name, name))
        field.choices.choices = choices
        return field


class DynamicChoiceFilter(DynamicChoiceMixin, django_filters.ChoiceFilter):
    pass


###################


class EmpProfileFilter(django_filters.FilterSet):

   # Name = django_filters.CharFilter(widget=forms.TextInput(      attrs={"class": " text-red text-center ", 'placeholder': 'Subscriber Search... '}), label='', method='search_by_name')

    class Meta:
        model = EmpProfile
        # fields = '__all__'
        fields = ['name']
        # exclude = ['customer', 'date_created']
