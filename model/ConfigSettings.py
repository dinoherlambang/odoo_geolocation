#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class ConfigSettings(models.Model):

    _name = "res.config.settings"
    _description = "res.config.settings"


    @api.model
    def get_geolocation(self, ):
        """
        {
          "@api.model":false
        }
        """
        token = self.ipinfo_token
        response = requests.get(f'https://ipinfo.io?token={token}')
        data = response.json()
        return data


    _inherit = "res.config.settings"
    ipinfo_token = fields.Char( string=_("Ipinfo Token"))


