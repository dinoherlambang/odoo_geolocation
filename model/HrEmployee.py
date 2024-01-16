#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class HrEmployee(models.Model):

    _name = "hr.employee"
    _description = "hr.employee"


    @api.depends("city","region","country","loc")
    def action_geolocation(self, ):
        """
        {
          "@api.depends":["city","region","country","loc"],
           "position" : "smart_button", 
           "icon"     : "fa-iconname"
        }
        """
        # Retrieve the IPinfo API URL from the settings
        Config = self.env['res.config.settings']
        ipinfo_url = Config.get_values().get('ipinfo_url')

        # Make the request to the IPinfo API
        response = requests.get(ipinfo_url)
        data = response.json()

        # Update the employee record with the geolocation data
        for record in self:
            record.city = data['city']
            record.region = data['region']
            record.country = data['country']
            record.loc = data['loc']


    _inherit = "hr.employee"
    city = fields.Char( string=_("City"))
    region = fields.Char( string=_("Region"))
    country = fields.Char( string=_("Country"))
    loc = fields.Char( string=_("Loc"))


