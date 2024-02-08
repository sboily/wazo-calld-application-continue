# Copyright 2023-2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


from flask import request
from flask_restful import Resource

from wazo_calld.auth import required_acl
from wazo_calld.http import AuthResource

from .schema import call_continue_schema


class CallContinueResource(AuthResource):

    def __init__(self, service):
        self._service = service

    @required_acl('calld.applications.{application_uuid}.calls.{call_id}.update')
    def put(self, application_uuid, call_id):
        request_body = call_continue_schema.load(request.get_json(force=True))
        result = self._service.call_continue(call_id, request_body)

        return result, 204

class SwitchCallResource(AuthResource):

    def __init__(self, service):
        self._service = service

    @required_acl('calld.calls.{call_id}.applications.{application_uuid}.update')
    def put(self, call_id, application_uuid, call_id):
        result = self._service.switch_call_to_application(call_id, application_uuid)

        return result, 204
