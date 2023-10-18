# -*- coding: utf-8 -*-
# Copyright 2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging


class CallContinueService:

    def __init__(self, ari):
        self._ari = ari

    def call_continue(self, call_id, request):
        channel = self._ari.channels.get(channelId=call_id)
        return channel.continueInDialplan(**request)
