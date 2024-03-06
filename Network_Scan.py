#!usr/bin/env python

import scapy.all as scapy
import argparse 


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast  = broadcast/arp_request
    lista_respuesta = scapy.srp(arp_broadcast, timeout=1, verbose=False)[0]

    lista_clientes = []
    for element in lista_respuesta:
        diccionario_cliente = {"IP": element[1].psrc, "MAC": element[1].hwsrc}
        lista_clientes.append(diccionario_cliente)
    return lista_clientes

def print_result(lista_resultados):
    print("IP\t\t\t MAC Address\n------------------------------------------")
    for element in lista_resultados:
        print (element["IP"] + "\t\t" + element["MAC"])


options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)