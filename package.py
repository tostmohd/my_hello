# -*- coding: utf-8 -*-
##############################################################################
#
# 
#
#    T
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
