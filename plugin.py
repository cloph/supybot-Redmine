###
# coding: utf-8
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
###
import re
from supybot.commands import *
import supybot.callbacks as callbacks
import supybot.conf as conf
import supybot.utils as utils
import simplejson as json


def GetRedmineInfo(ticket, domain, printurl=0):
    _REDMINE_URL = 'https://{}'.format(domain)
    try:
        text = utils.web.getUrl(
            '{}/issues/{}.json'.format(_REDMINE_URL, ticket))
        redmineInfo = json.loads(text)
        redmineInfo = redmineInfo['issue']

        # assemble the response string
        response = u'redmine: »{}« in {} ({} for {}) [{}]'.format(
            redmineInfo['subject'], redmineInfo['project']['name'],
            redmineInfo['tracker']['name'],
            redmineInfo['assigned_to']['name'] if 'assigned_to' in redmineInfo
            else 'unassigned',
            redmineInfo['status']['name'])

        if printurl == 1:
            response = u'{} {}/issues/{}'.format(
                response, _REDMINE_URL, redmineInfo['id'])

        return response.encode('utf-8')
    except utils.web.Error, e:
        if printurl == 1:
            e = '{} - please visit the URL yourself: {}/issues/{}'.format(
                str(e), _REDMINE_URL, ticket)
        return e
    except Exception, e:
        print 'unknown error {}'.format(str(e))
        return 'unknown error - please visit the URL yourself: {}/issues/{}'\
            .format(_REDMINE_URL, ticket)


class Redmine(callbacks.PluginRegexp):
    """the Redmine plugin snarfs the messages for either an URL to a redmine
    ticket, or for special short form like e.g. rdm#1234"""
    # what subs implement a snarfer
    regexps = ['parseURL', 'parseID']

    # noinspection PyIncorrectDocstring,PyUnusedLocal
    @urlSnarfer
    def parseID(self, irc, msg, match):
        r"""(?:^|\s)(?:redmine|rd?m)(?: |#|:)(\d+)"""
        ticket = match.group(1)
        redmineInfo = GetRedmineInfo(
            ticket, self.registryValue('globalRedmineDomain'), printurl=1)
        irc.reply('{}'.format(redmineInfo))

    # noinspection PyIncorrectDocstring,PyUnusedLocal
    @urlSnarfer
    def parseURL(self, irc, msg, match):
        ticket = match.group(1)
        redmineInfo = GetRedmineInfo(
            ticket, self.registryValue('globalRedmineDomain'), printurl=0)
        irc.reply('{}'.format(redmineInfo))
    parseURL.__doc__ = '{}{}{}'.format(
           r'(?:http[s]?://)?',
           re.escape(conf.supybot.plugins.Redmine.globalRedmineDomain()),
           r'/issues/(\d+)')

    # noinspection PyIncorrectDocstring,PyUnusedLocal,PyMethodMayBeStatic
    def redmine(self, irc, msg, args, ticket):
        """<number>
        
        Ask the bot to get redmine info based on a numeric-ID"""
        redmineInfo = GetRedmineInfo(
            ticket, self.registryValue('globalRedmineDomain'), printurl=1)
        irc.reply('{}'.format(redmineInfo))
    redmine = wrap(redmine, ['positiveInt'])

Class = Redmine
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
