# IoT Access Point Configuration

## Configuring the Access Point

### Files that are edited

- `/etc/network/interfaces`
- `/etc/hostapd/hostapd.conf`
- `/etc/default/hostapd`
- `/etc/dnsmasq.conf`

### Configuration
[`access_point_setup.py`] - 
This script edits the above files in order to configure the Raspberry Pi for a wireless access point.


In `/etc/network/interfaces` the script writes to the file to setup the necessary bridge between ports in order to
create the access point rather than attempting to connect to the internet through the wireless drivers or through the 
ethernet port. 

In `/etc/hostapd/hostapd.conf` the script writes to this file and creates the configuration for the wireless access 
point. This file defines the name of the access point, the password, the security for it, and other configuration 
options needed for the access point to be created. 

In `/etc/default/hostapd` the script changes the configuration for the hostapd Daemon to
read from the file that was previously changed (`/etc/hostapd/hostapd.conf`). 

In `/etc/dnsmasq.conf` the script adds the
interface used for the bridge that generates the access point. This also add the certain number of accessable IP addresses
that will be assigned when devices connect to the access point.



## Configuring the Internet Access

### Files that are edited

- `/etc/wpa_supplicant/wpa_supplicant.conf`
- `/etc/dnsmasq.conf`
- `/etc/hostapd/hostapd.conf`
- `/etc/default/hostapd`

### Configuration
[`configuration.py`] - 
This script edits the above files in order to configure the Raspberry Pi for a Wi-Fi access.

In `/etc/wpa_supplicant/wpa_supplicant.conf` the script adds the name of the network and the password required to join
the network. The type of authentication (i.e. WPA, WPA2, etc.) and the credentials are specified in this file.

In `/etc/dnsmasq.conf` the script *`removes/comments`* the lines added earlier in order to step towards turning off the access point.

In `/etc/hostapd/hostapd.conf` the script *`removes/comments`* all of the lines within this file in order to stop the
configuration from being created. All lines need to be editted in order for the initial configuration of the access
point to be stopped.

In `/etc/default/hostapd` the script *`removes/comments`* the specific line edited earlier in order to remove the
location of the configuration file so that the access point cannot start up again.

























