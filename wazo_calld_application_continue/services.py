# Copyright 2023-2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging


class CallContinueService:

    def __init__(self, ari, ami):
        self._ari = ari
        self._ami = ami

    def call_continue(self, call_id, request):
        channel = self._ari.channels.get(channelId=call_id)
        return channel.continueInDialplan(**request)

    def switch_call_to_application(self, call_id, application_uuid):
        channel = self._ari.channels.get(channelId=call_id)
        action = {
            'Channel': channel.json['name'],
            'Exten': 's',
            'Context': f'stasis-wazo-app-{application_uuid}'
        }

        return self.amid.action('redirect', action)
