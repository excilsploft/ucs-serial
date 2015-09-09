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
        - Python 2.7.7*
        - Cisco UCS Manager Python SDK v0.8.3 [UcsSdk](https://communities.cisco.com/servlet/JiveServlet/downl oad/36899-13-76835/UcsSdk-0.8.3.tar.gz)
        - csv module

        * It is extremely important you use only Python 2.7.7, the SDK provided by Cisco is incompatible with Python 2.7.9 due to how the urllib2 library has changed in regard to SSL cert validation.

    Arguments to the Script are required, they are:
        * -u --ucs      The IP or HostName of the UCS Manager VIP
        * -o --out      The Out File path for the generated CSV


    Caveats:
        This Script does no error handling, it is "select" only and should have no deleterious effect on your UCS Domain.  However, running it repeatedly with failures can leave API sesssions lingering in UCSM of which there are a finite amount of.

