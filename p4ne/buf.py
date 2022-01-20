from pysnmp.hlapi import *

snmp_object1 = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_object2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')
snmp_object3 = ObjectIdentity('SNMPv2-MIB', 'sysObjectID', 0)

snmp_objects = ( snmp_object1 , snmp_object2, snmp_object3)

for snmp_object in snmp_objects:
    for r in getCmd(SnmpEngine(), CommunityData('public', mpModel=0), UdpTransportTarget(('10.31.70.107', 161)), ContextData(), ObjectType(snmp_object)):
        for r2 in r[3]:
            print(r2)