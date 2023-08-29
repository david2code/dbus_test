import dbus
from pprint import pprint
from dbus import SystemBus
from dbus import Interface
from xml.etree import ElementTree

def print_network_ifaces(bus, service, object_path):
    try:
        if object_path == "/org/freedesktop/NetworkManager/Devices":
            return

        obj = bus.get_object(service, object_path)
        interface = Interface(obj, 'org.freedesktop.DBus.Properties')

        m = interface.get_dbus_method('Get', dbus_interface=None)

        ifacename = m('org.freedesktop.NetworkManager.Device', 'Interface')
        print(ifacename)

    except Exception, err:
        print err

def rec_intro(bus, service, object_path, callback):
    callback(bus, service, object_path)
    obj = bus.get_object(service, object_path)
    interface = Interface(obj, 'org.freedesktop.DBus.Introspectable')
    xmlstring = interface.Introspect()
    for child in ElementTree.fromstring(xmlstring):
        if child.tag == 'node':
            if object_path == '/':
                object_path = ''
            new_path = '/' . join((object_path, child.attrib['name']))
            rec_intro(bus, service, new_path, callback)

bus = SystemBus()
rec_intro(bus, 'org.freedesktop.NetworkManager', '/org/freedesktop/NetworkManager/Devices', print_network_ifaces)