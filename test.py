###
# coding: utf-8
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
###

from supybot.test import *


class RedmineTestCase(ChannelPluginTestCase):
    plugins = ('Redmine',)

    sampleTicketDomain = 'redmine.documentfoundation.org'
    sampleTicketID = 40
    sampleTicketTitle = 'Vorbereitung der LibOx 4.2 DE'
    sampleTicketProject = 'DE'
    sampleTicketType = 'Feature'
    sampleTicketAssignee = 'unassigned'
    sampleTicketResolution = 'Rejected'

    expectedResponse = \
        'redmine: »{}« in {} ({} for {}) [{}]'.format(
            sampleTicketTitle, sampleTicketProject, sampleTicketType,
            sampleTicketAssignee, sampleTicketResolution)
    expectedResponseWithURL = '{} https://{}/issues/{}'.format(
        expectedResponse, sampleTicketDomain, sampleTicketID)

    config = {'supybot.plugins.Redmine.globalRedmineDomain':
              sampleTicketDomain}
    if network:
        def testFullURL(self):
            self.assertSnarfResponse(
                'bla https://{}/issues/{} bla'.format(
                    self.sampleTicketDomain, self.sampleTicketID),
                self.expectedResponse)

        def testShort(self):
            self.assertSnarfResponse(
                'bla bla redmine#{} bla bla'.format(
                    self.sampleTicketID), self.expectedResponseWithURL)

        def testCommand(self):
            self.assertResponse('redmine {}'.format(self.sampleTicketID,),
                                self.expectedResponseWithURL)

    def testInvalidCommands(self):
        self.assertSnarfNoResponse('bla on rdm redmine#')
        self.assertSnarfNoResponse('bla on redmine 123a something')
        self.assertHelp('redmine')
        self.assertError('redmine bla')
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
