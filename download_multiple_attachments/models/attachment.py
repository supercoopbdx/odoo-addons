# -*- coding: utf-8 -*-
######################################################################################################
#
# Copyright (C) B.H.C. sprl - All Rights Reserved, http://www.bhc.be
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied,
# including but not limited to the implied warranties
# of merchantability and/or fitness for a particular purpose
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
######################################################################################################
from openerp import api, exceptions, fields, models, _


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    @api.multi
    def action_download_attachment(self):
        tab_id = []
        for attachment in self:
            tab_id.append(attachment.id)
        url = '/web/binary/download_document?tab_id=%s' % tab_id
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new',
        }
