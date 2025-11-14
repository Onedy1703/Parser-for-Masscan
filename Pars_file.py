import re
import ipaddress

pattern = r'\s(\w+)="([^"]*)"'

#Change the path
filename_input = 'input.path.and.name'
#Change the path
filename_output = 'output.path.and.name'

#You can enter subnets that should be excluded from the list.
subnets = [
    '255.255.255.254/31',
    '0.0.0.0/31'
]
subnet_objects = [ipaddress.ip_network(subnet) for subnet in subnets]


def sort_key(ip):
    return tuple(int(part) for part in ip.split('.'))


if __name__ == "__main__":
    with open(filename_input, 'r') as file:
        ip_addresses = [{key: value for key, value in re.findall(pattern, line)}['addr'] for line in file]
        filtered_ip_addresses = [ip for ip in ip_addresses if
                                 not any(ipaddress.ip_address(ip) in subnet for subnet in subnet_objects)]

    sorted_filtered_ip_addresses = sorted(filtered_ip_addresses, key=sort_key)

    file = open(filename_output, 'w')
    for ip in sorted_filtered_ip_addresses:
        file.write(ip + '\n')
    file.close()


