from django.db import models
from languages_plus.models import Language as MasterLanguage
from countries_plus.models import Country as MasterCountry


class Language(models.Model):
    """ The languages available in the UI. They aren't enforced by the API.
    """
    language = models.OneToOneField(MasterLanguage)

    class Meta:
        ordering = ['language__name_en']

    def __unicode__(self):
        return unicode(self.language)


class Subtype(models.Model):
    name = models.CharField(max_length=1024, help_text="Name of the document subtype")
    abbreviation = models.CharField(max_length=20, help_text="Short abbreviation to use in FRBR URI. No punctuation.", unique=True)

    def clean(self):
        if self.abbreviation:
            self.abbreviation = self.abbreviation.lower()

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.abbreviation)


class Country(models.Model):
    """ The countries available in the UI. They aren't enforced by the API.
    """
    country = models.OneToOneField(MasterCountry)

    class Meta:
        ordering = ['country__name']

    def __unicode__(self):
        return unicode(self.country.name)
