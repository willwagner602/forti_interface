from forti_api import fortigate_api

def forti_interface(configuration, api=None):
	required = ['name']
	for key in required:
		assert(key in configuration)

	api.print_data(api.edit(['cmdb', 'system', 'interface', configuration['name']], data=configuration))


# interface name - this is a top level variable
	# alias
	# link status
	# type
	# role

	## address
	# addressing mode (manual/dhcp/dedicated to fortiswitch)
	# ip/network mask (two items separated by /)

	## restrict access (checkboxes/bools)
	# HTTPS
	# PING
	# HTTP
	# FMG-Access
	# CAPWAP
	# SSH
	# SNMP
	# Radius Accounting
	# FortiTelemetry

	# DHCP Server (check/bool)

	## networked devices
	# device detection (bool)

	## admission control
	# Security Mode (list)

	## Miscellaneous
	# Scan outgoing connections to botnet sites (disable/block/monitor)

	## Status
	# comments
	# Interface state (enabled/disabled)


def main():
	fortigate_vm = "gesha.no-ip.com:10443"
	user = "admin"
	pw = "test"

	interface_test = {"name": "port2", "vdom": "root", "allowaccess": "http https ping", "type": "physical",
					  "ip": "192.0.1.4/255.255.255.0", "miscerror": ""}

	api = fortigate_api(fortigate_vm, user, pw)

	forti_interface(interface_test, api)


if __name__ == "__main__":
	main()