import subprocess


def subprocess_run(cmd):
    p = subprocess.Popen(cmd, shell=True)
    p.wait()
    return p.returncode

print(subprocess_run("apt-get update -y"))
print(subprocess_run("apt-get upgrade -y"))
print(subprocess_run("apt-get install rfkill hostapd hostap-utils iw dnsmasq bridge-utils -y"))

with open("files/wifi_wap/etc_network_interfaces.txt", "r") as r:
    with open("/etc/network/interfaces", "w") as w:
        for line in r:
            w.write(line)

with open("files/wifi_wap/etc_hostapd_hostapd_conf.txt", "r") as r:
    with open("/etc/hostapd/hostapd.conf", "w") as w:
        for line in r:
            w.write(line)

with open("files/wifi_wap/hostapd_wap.txt", "r") as r:
    with open("/etc/default/hostapd", "w") as w:
        for line in r:
            w.write(line)

with open("files/wifi_wap/dnsmasq_conf_wap.txt", "r") as r:
    with open("/etc/dnsmasq.conf", "w") as w:
        for line in r:
            w.write(line)

print(subprocess_run("service networking restart"))
print(subprocess_run("service hostapd restart"))
print(subprocess_run("service dnsmasq restart"))
print(subprocess_run("sleep 5"))
print(subprocess_run("reboot"))


