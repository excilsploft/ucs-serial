UCS SERIAL NUMBER DUMP
======================

ucs_serial.py
-------------

    This Script retrieves the DN (Distinguished Name in the Managed Object Tree) and Serial Number for the following equipment:
        - Fabric Interconnects
        - Fabric Interconnect Expansion Cards
        - Chassis
        - Chassis IO Modules
        - Blade Servers
        - Rack Servers


    Dependencies for this script include:
        - Python 2.7.X
        - https://github.com/CiscoUcs/ucsmsdk
        - csv module
        - argparse module
        - getpass module


    Arguments to the Script are required, they are:
        * -u --ucs      The IP or HostName of the UCS Manager VIP
        * -o --out      The Out File path for the generated CSV


    Caveats:
        This Script does little error handling, it is "select" only and should have no deleterious effect on your UCS Domain.  However, running it repeatedly with failures can leave API sesssions lingering in UCSM of which there are a finite amount of.

