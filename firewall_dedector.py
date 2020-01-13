#!/usr/bin python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Firewall Dedector")
os.system("figlet Simus")

print("""
Welcome to Firewall Dedector.....

    1. This tool can only detect limited numbers of firewalls, listed below.
    2. Profense
    3. NetContinuum
    4. Barracuda
    5. HyperGuard
    6. BinarySec
    7. Teros
    8. F5 Trafficshield
    9. F5 ASM
    10. Airlock
    11. Citrix NetScaler
    12. ModSecurity
    13. DenyALL
    14. dotDefender
    15. webApp.secure
    16. BIG-IP
    17. URLScan
    18. WebKnight
    19. SecureIIS
    20. Imperva



""")

site = raw_input("Enter a Website: ")
os.system("wafw00f " + site)