# -*- coding: utf-8 -*-
# Copyright 2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_auth_client import Client as AuthClient

from .resources import CallContinueResource
from .services import CallContinueService


class Plugin(object):

    def load(self, dependencies):
        api = dependencies['api']
        config = dependencies['config']
        ari = dependencies['ari']

        service = CallContinueService(ari.client)

        api.add_resource(CallContinueResource, '/applications/<application_uuid>/calls/<call_id>/continue', resource_class_args=[service])
