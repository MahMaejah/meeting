# Copyright (c) 2020, Bantoo Dev Zambia
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator


class Meeting(WebsiteGenerator):
    website = frappe._dict(
        template="templates/generators/meeting.html",
    )

    def validate(self):
        self.page_name = self.name.lower()
        #self.validate_attendees()
        """Set missing names and warn if duplicate"""
        found = []
        for attendee in self.attendees:
            if not attendee.full_name:
                attendee.full_name = get_full_name(attendee.attendee)
            if attendee.attendee in found:
                frappe.throw(
                    ("Attendee{0 entered twice}").format(attendee.attendee))
            found.append(attendee.attendee)

        def get_full_name(attendee):
            self = frappe.get_doc("User")
            return " ".join(filter(None, [self.first_name, self.middle_name, self.last_name]))
