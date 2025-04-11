# Copyright (C) 2025 Jesus Remiro <bilbonet@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Hr Attendance Geolocation Map",
    "summary": 
        """
        With this module, you can see in Google Maps the place from the 
        geolocation information in each attendance record.
        """,
    "version": "15.0.1.0.0",
    "development_status": "Alpha",
    "category": "Human Resources",
    "website": "https://github.com/bilbonet/mnere-custom",
    "author": "Jesus Ramiro, Bilbonet",
    "maintainers": ["Bilbonet"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "hr_attendance_geolocation",
    ],
    "data": [
        "views/hr_attendance_views.xml",
    ],
}
