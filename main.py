import sys
import urllib3
from vmware.vapi.vsphere.client import create_vsphere_client

# Connect My VM Server

session = requests.session

session.verify = False

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

vsphere_client = create_vsphere_client(server_ip = '<ip-address>', username = '<username>', password = '<user_password>', session = session)

vsphere_client.vcenter.VM.list()