import os

import os


def run(net, cred):
    print(net, cred)

    with open("/etc/wpa_supplicant/wpa_supplicant.conf", "a") as f:
        f.write('network={ \n\t ssid = "' + net + '"\n\t scan_ssid=1 \n\t psk="' + cred + '"\n\t key_mgmt=WPA-PSK \n}')
    print("Made it past wpa_supplicant")

    with open("dnsmasq_conf.txt", "r") as r:
        with open("/etc/dnsmasq.conf", "w") as w:
            for line in r:
                w.write(line)

    with open("hostapd_wifi.txt", "r") as r:
        with open("/etc/default/hostapd", "w") as w:
            for line in r:
                w.write(line)

    with open("hostapd_conf_wifi.txt", "r") as r:
        with open("/etc/hostapd/hostapd.conf", "w") as w:
            for line in r:
                w.write(line)

    ''' 
    aksjdfh
    
        with open("/etc/dnsmasq.conf", "r+") as f:
        print("Before loop")
        for line in f:
            print(line)
            print("Looping my way downtown..")
            if "interface=wlan0" in line:
                print("Before replace line 1")
                line.replace(line, '#' + line)
                print("replaced line 1")
            if "dhcp-range=192.168.2.1, 192.168.2.254, 12h" in line:
                print('Before replace line 2')
                line.replace(line, '#' + line)
                print("replaced line 2")
    print("Made it past dnsmasq")

    with open("/etc/default/hostapd", "r+") as f:
        for line in f:
            if 'DAEMON_CONF="/etc/hostapd/hostapd.conf"' in line:
                line.replace(line, '#' + line)
    print("Made it past hostapd")

    with open("/etc/hostapd/hostapd.conf", "r+") as f:
        for line in f:
            line.replace(line, '#' + line)
    print("Made it past hostapd conf")
    
    '''










