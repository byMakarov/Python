#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interfaz", dest="interfaz", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interfaz:
        parser.error("Escoge una interfaz")
    elif not options.new_mac:
        parser.error("Porfavor escribe una nueva MAC")
    return options



def change_mac(interfaz, new_mac):
    print("Cambiando direccion MAC de " + interfaz + " por " + new_mac)

    subprocess.call(["ifconfig", interfaz, "down"])
    subprocess.call(["ifconfig", interfaz, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interfaz, "up"])

def get_current_mac(interfaz):
    ifconfig_result = subprocess.check_output(["ifconfig", interfaz])

    output_ifconfig_result = ifconfig_result.decode("utf-8")

    mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', output_ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("No hay MAC")

    if mac_address_search_result == options.new_mac:
        print("Hola")

options = get_arguments()
current_mac = get_current_mac(options.interfaz)
print("MAC Actual = " + str(current_mac))

change_mac(options.interfaz, options.new_mac)

current_mac = get_current_mac(options.interfaz)
if current_mac == options.new_mac:
    print("La direccion MAC ha sido cambiada con exito")
else:
    print("La direccion MAC no ha cambiado")