from odoo import api, fields, models, _

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient"
    
    reference = fields.Char(string='Reference', required=True,
                            copy=False,
                            readonly=True,
                            default=lambda self: _('New')
    )
    name = fields.Char(string='Name', required=True,)
    age = fields.Integer(string='Age',)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),],
        required=True, default='male',
    )
    
    @api.model
    def create(self, vals):
        if vals.get('reference', _('New')) == _('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
        rtn = super(HospitalPatient, self).create(vals)
        return rtn

