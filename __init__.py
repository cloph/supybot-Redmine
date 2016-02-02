###
# coding: utf-8
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
###

"""
a simple plugin that queries redmine for project, title and assignee when a
redmine URL is pasted to one of the channels the bot lurks in
"""
import supybot
import supybot.world as world
import config
import plugin
if world.testing:
    # noinspection PyUnresolvedReferences
    import test

__version__ = "1"

__author__ = supybot.Author('Christian Lohmaier', 'cloph',
                            'lohmaier+github@googlemail.com')

__contributors__ = {}

__url__ = 'https://github.com/cloph/supybot-Redmine'

reload(plugin)  # In case we're being reloaded.

Class = plugin.Class
configure = config.configure
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
