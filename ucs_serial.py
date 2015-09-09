#coding: utf-8
"""Get the Serial Numbers for Blades, Rack Servers, Fabric Interconnnects,
    and IOMs"""

from UcsSdk.UcsHandle import UcsHandle
from UcsSdk.MoMeta.ComputeBlade import ComputeBlade
from UcsSdk.MoMeta.EquipmentChassis import EquipmentChassis
from UcsSdk.MoMeta.ComputeRackUnit import ComputeRackUnit
from UcsSdk.MoMeta.NetworkElement import NetworkElement
#from UcsSdk.MoMeta.EquipmentFex import  EquipmentFex
from UcsSdk.MoMeta.EquipmentIOCard import  EquipmentIOCard
from UcsSdk.MoMeta.EquipmentSwitchCard import  EquipmentSwitchCard

import csv
import argparse

CONST_DEBUG = False
CONST_HEADER_ROW = (('EQUIPMENTTYPE', 'EQUIPMENTID', 'SERIALNUMBER'))


def main(args):
    """Main Function, open a file, write to it"""

    handle = UcsHandle()
    handle.Login(args.ucs)

    # Get All the Blades in the Domain
    blades = handle.GetManagedObject(None, ComputeBlade.ClassId(), None,
                                     dumpXml=CONST_DEBUG)

    # Get All the Rack Servers in the Domain
    rack_servers = handle.GetManagedObject(None, ComputeRackUnit.ClassId(),
                                           None, dumpXml=CONST_DEBUG)

    # Get All the Chassis' in the Domain
    chassis_list = handle.GetManagedObject(None, EquipmentChassis.ClassId(),
                                           None, dumpXml=CONST_DEBUG)
    #Get All the IOM's in the domain
    iom_list = handle.GetManagedObject(None, EquipmentIOCard.ClassId(),
                                       None, dumpXml=CONST_DEBUG)

    # Get the Fabric Interconnects
    fabric_list = handle.GetManagedObject(None, NetworkElement.ClassId(), None,
                                          dumpXml=CONST_DEBUG)

    # Get the Fabric Interconnect Expansion Cards
    fex_list = handle.GetManagedObject(None, EquipmentSwitchCard.ClassId(),
                                       None, dumpXml=CONST_DEBUG)


    with open(args.out, 'w') as file_out:
        writer = csv.writer(file_out)
        writer.writerow(CONST_HEADER_ROW)

        for blade  in blades:
            writer.writerow(('BLADE', blade.Dn, blade.Serial))

        for server in rack_servers:
            writer.writerow(('RACK_SERVER', server.Dn, server.Serial))

        for chassis in chassis_list:
            writer.writerow(('CHASSIS', chassis.Dn, chassis.Serial))

        for iom in iom_list:
            writer.writerow(('IOM', iom.Dn, iom.Serial))

        for fabric in fabric_list:
            writer.writerow(('FABRIC', fabric.Dn, fabric.Serial))

        for fex in fex_list:
            writer.writerow(('FABRIC_EXPANSION', fex.Dn, fex.Serial))

    handle.Logout()

if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(description="Dump Serial Numbers to CSV")
    PARSER.add_argument('-u', '--ucs', help="UCS Manager IP", required=True)
    PARSER.add_argument('-o', '--out', help="out CSV File Path", required=True)

    ARGS = PARSER.parse_args()
    main(ARGS)

