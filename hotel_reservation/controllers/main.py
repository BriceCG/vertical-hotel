from odoo import http
from odoo.http import request
from datetime import datetime


class HotelReservation(http.Controller):

    def get_datetime_format(self):
        """ This function allows to get lang from backoffice """
        lang = request.env['res.lang'].search([('code', '=', request.env.user.lang)], limit=1)
        return "%s %s" % (lang.date_format, lang.time_format)

    @http.route("/get-reservations", auth="user", type="json")
    def get_reservation(self, date_from, date_to):
        """ This function allows to  get the date of reservations """
        datetime_format = self.get_datetime_format()
        values = {
            "date_from": datetime.strptime(date_from, datetime_format),
            "date_to": datetime.strptime(date_to, datetime_format)
        }
        fake_reservation_summary = request.env['room.reservation.summary'].new(values=values)
        fake_reservation_summary.get_room_summary()
        return {
            "summary_header": fake_reservation_summary.summary_header,
            "room_summary": fake_reservation_summary.room_summary
        }
