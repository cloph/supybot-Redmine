###
# coding: utf-8
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
###

import supybot.conf as conf
import supybot.registry as registry


# noinspection PyUnusedLocal
def configure(advanced):
    from supybot.questions import something
    conf.registerPlugin('Redmine', True)
    url = something(
        """please specify the domain to the Redmine instance to query""")
    Redmine.globalRedmineDomain.setValue(url)

Redmine = conf.registerPlugin('Redmine')
conf.registerChannelValue(Redmine, 'nonSnarfingRegexp', registry.Regexp(
        None,
        """Determines what URLs are to be snarfed and stored in the database in
        the channel; URLs matching the regexp given will not be snarfed. Give
        the empty string if you have no URLs that you'd like to exclude from
        being snarfed."""))

conf.registerGlobalValue(Redmine, 'globalRedmineDomain', registry.String(
    '',
    """the domain of the redmine instance the plugin should use"""))
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
