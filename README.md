# Odoo Geolocation Module

This module adds a simple geolocation functionality to the Odoo HR module. It uses the IPinfo API to retrieve geolocation data.

## Description

This Odoo module extends the `hr.employee` and `res.config.settings` models to add geolocation functionality. The module uses the IPinfo API to retrieve geolocation data based on the IP address of the employee. The geolocation data includes the city, region, country, and location coordinates.

## Installation

1. Copy the module directory into your Odoo addons directory.
2. Update the addons list in Odoo.
3. Install the module through the Odoo apps menu.

## Configuration

1. Go to the settings menu in Odoo.
2. Enter your IPinfo API token, remember to make a token in ipinfo website!

## Usage

The module adds a new action button to the employee form. Clicking this button will update the employee's geolocation data.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the GNU GPL License.
