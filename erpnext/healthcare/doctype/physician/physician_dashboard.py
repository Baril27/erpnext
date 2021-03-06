from frappe import _

def get_data():
	return {
		'heatmap': True,
		'heatmap_message': _('This is based on transactions against this Physician.'),
		'fieldname': 'physician',
		'transactions': [
			{
				'label': _('Appointments and Consultations'),
				'items': ['Patient Appointment', 'Consultation']
			},
			{
				'label': _('Lab Tests'),
 				'items': ['Lab Test']
			}
		]
	}
