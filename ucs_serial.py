#!/usr/local/bin/python
#coding: utf-8
"""Get the Serial Numbers for Blades, Rack Servers, Fabric Interconnnects,
    and IOMs"""

import csv
import argparse
import getpass
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.ucsconstants import NamingId
from ucsmsdk.ucsexception import UcsException


CONST_HEADER_ROW = (('EQUIPMENT_TYPE', 'EQUIPMENT_ID', 'SERIAL_NUMBER'))


def get_equipment(handle, equipment_type):
    """function to wrap the handle query"""
    equipment_out = []
    try:
        equipment_out = handle.query_classid(equipment_type)
    except UcsException as err:
        print err

    return equipment_out

def main(args):
    """Main Function, open a csv file and write to it"""

    #get the username if not set
    if not args.id:
        args.id = raw_input("Please Enter UCS Username: ")

    #set secure=False to disable cert chain validation
    handle = UcsHandle(args.ucs, args.id, getpass.getpass(), secure=True)
    handle.login()

    #list of tuples specifying equipment alias and their sdk Constants
    # Note: Using the NamingId Classs Constants rather than their values
    equipment_to_get = [('BLADE', NamingId.COMPUTE_BLADE),
                        ('SERVER', NamingId.COMPUTE_RACK_UNIT),
                        ('CHASSIS', NamingId.EQUIPMENT_CHASSIS),
                        ('IOM', NamingId.EQUIPMENT_IOCARD),
                        ('FABRIC_INTERCONNECT', NamingId.NETWORK_ELEMENT),
                        ('FABRIC_EXPANSION', NamingId.EQUIPMENT_SWITCH_CARD)]

    #build a dictionary of aliases and the list of equipment
    equipment_output = {}
    for equipment in equipment_to_get:
        print "Getting Serials for {0}".format(equipment[0])
        equipment_output[equipment[0]] = get_equipment(handle, equipment[1])

    with open(args.out, 'w') as file_out:
        writer = csv.writer(file_out)
        writer.writerow(CONST_HEADER_ROW)

        for key in equipment_output:
            for equipment in equipment_output[key]:
                writer.writerow((key, equipment.dn, equipment.serial))

    print "Wrote output to {0}".format(args.out)
    handle.logout()

if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(description="Dump Serial Numbers to CSV")
    PARSER.add_argument('-u', '--ucs', help="UCS Manager IP", required=True)
    PARSER.add_argument('-i', '--id', help="UCS User ID", required=False)
    PARSER.add_argument('-o', '--out', help="Out CSV File Path", required=True)

    ARGS = PARSER.parse_args()
    main(ARGS)

