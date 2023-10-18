# -*- coding: utf-8 -*-
# Copyright 2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from marshmallow import (
    fields,
    Schema,
)
from marshmallow.validate import Length


class CallContinueSchema(Schema):
    context = fields.Str(validate=Length(min=1))
    extension = fields.Str(validate=Length(min=1))
    priority = fields.Integer()
    label = fields.Str(validate=Length(min=1))

    class Meta:
        strict = True

call_continue_schema = CallContinueSchema()
