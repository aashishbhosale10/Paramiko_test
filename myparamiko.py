from netmiko import ConnectHandler

router = {
    'device_type':'cisco_ios',
    'ip': '192.168.101.135',
    'username':'cisco',
    'password':'cisco',
    'port': 22,
    'verbose': True }

net_connect=ConnectHandler(**router)
print (net_connect.find_prompt())
print (net_connect.find_prompt())
