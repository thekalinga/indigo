from django.utils.translation import ugettext as _

from indigo.plugins import LocaleBasedMatcher, plugins
from indigo_api.models import Subtype


@plugins.register('work-detail')
class BaseWorkDetail(LocaleBasedMatcher):
    """ Provides some locale-specific work details.

    Subclasses should implement `work_numbered_title`.
    """

    def work_numbered_title(self, work):
        """ Return a formatted title using the number for this work, such as "Act 5 of 2009".
        This usually differs from the short title. May return None.
        """
        number = work.number
        if number == 'constitution':
            return None
        uri = work.work_uri
        work_type = self.work_friendly_type(work)
        return _('%(type)s %(number)s of %(year)s') % {'type': _(work_type), 'number': number, 'year': work.year}

    def work_friendly_type(self, work):
        """ Return a friendly document type for this work, such as "Act" or "By-law".
        """
        uri = work.work_uri

        if uri.subtype:
            # use the subtype full name, if we have it
            subtype = Subtype.for_abbreviation(uri.subtype)
            if subtype:
                return _(subtype.name)
            return _(uri.subtype.upper())

        return _('Act')
