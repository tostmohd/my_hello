# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 ZestyBeanz Technologies Pvt Ltd(<http://www.zbeanztech.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http:/'spire_package' module/www.gnu.org/licenses/>.
#'spire_package' module
###############################################################################
from openerp import models, fields, api, _
import openerp.addons.decimal_precision as dp

class travel_package(models.Model):
    _name = "travel.package"
    _description = "Package"
    _inherit = ["mail.thread", "ir.needaction_mixin"]
    
    name =  fields.Char('Destination', size=64,required=True)
    fare = fields.Float(string='Fare',digits=dp.get_precision('Product_Price_Spire_Travel'))
    airline =  fields.Char(string='A/L')
    package_class = fields.Char(string='Class')
    package_hotel = fields.Char(string='Hotel')
    days = fields.Integer(string='Days')
    from_date = fields.Date('From Date')
    to_date = fields.Date('To Date',)
    active = fields.Boolean('Active',default=True,track_visibility='onchange')
    open_till = fields.Date('Booking Open Till')
    
    @api.multi
    def pack_deactivate(self):
        self.write({'active': False})
        return True
    
    # vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: