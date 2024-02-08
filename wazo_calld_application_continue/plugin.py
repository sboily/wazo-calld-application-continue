# Copyright 2023-2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_amid_client import Client as AmidClient

from .resources import CallContinueResource, SwitchCallResource
from .services import CallContinueService


class Plugin(object):

    def load(self, dependencies):
        api = dependencies['api']
        config = dependencies['config']
        ari = dependencies['ari']
        token_changed_subscribe = dependencies['token_changed_subscribe']

        amid_client = AmidClient(**config['amid'])
        token_changed_subscribe(amid_client.set_token)

        service = CallContinueService(ari.client, amid_client)

        api.add_resource(CallContinueResource, '/applications/<application_uuid>/calls/<call_id>/continue', resource_class_args=[service])
        api.add_resource(SwitchCallResource, '/calls/<call_id>/applications/<application_uuid>', resource_class_args=[service])
