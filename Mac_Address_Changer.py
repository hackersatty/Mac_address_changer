from ast import parse
import subprocess
import optparse
import re
print("""
 _                _                       _   _         
| |              | |                     | | | |        
| |__   __ _  ___| | _____ _ __ ___  __ _| |_| |_ _   _ 
| '_ \ / _` |/ __| |/ / _ \ '__/ __|/ _` | __| __| | | |
| | | | (_| | (__|   <  __/ |  \__ \ (_| | |_| |_| |_| |
|_| |_|\__,_|\___|_|\_\___|_|  |___/\__,_|\__|\__|\__, |
                                                   __/ |
                                                  |___/ 

""")
def get_arguments():
        parse=optparse.OptionParser()
        parse.add_option("-i", "--interface", dest="interface", help="Interface to change its mac address")
        parse.add_option("-m", "--mac", dest="new_mac", help="New Mac_address For the Given Interface")
        (options, arguments)=parse.parse_args()
        if not options.interface:
                parse.error("[-] Please Specify the -i interface , or --help for more info")
        elif not options.new_mac:
            parse.error("[-] Please Specify the -m new_mac , or --help for more info")
        return options
def mac_address(interface,new_mac):
        print("[+] The mac address is changing for " + interface + " to " + new_mac)
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["ifconfig", interface, "up"])
        # subprocess.call(["ifconfig", interface])

def get_current_mac(interface):
    ifconfig_result=subprocess.check_output(["ifconfig", interface])
    # \w\w:\w\w:\w\w:\w\w:\w\w:\w\w for implementing regex for finding mac_address
    search_mac_address=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if search_mac_address:
        return search_mac_address.group(0)
    else:
        print("[-]Mac_adress has not get")

options = get_arguments()
current_mac=get_current_mac(options.interface)
print("[+] The Current mac adress  = " + str(current_mac))
mac_address(options.interface, options.new_mac)
current_mac=get_current_mac(options.interface)
if current_mac==options.new_mac:
    print("[+] The mac_address has successfully changed = " + str(current_mac))
else:
    print("[-] Mac-Address doesnt changed")