#!usr/bin/env python
from __future__ import unicode_literals, print_function
import jinja2

#The process ID, network, wildcard mask, and area should all be variables in the Jinja2 template.
#Use a template directly embedded in your Python script.
#The following items should all be variables in the template: process_id, network, wildcard, area, loopback0_addr, loopback0_mask.
#Additionally, the 'interface Loopback0' and its ip address configuration should only be generated if the loopback0_addr variable is defined (i.e. use an if-condition here).

with open('ospf_config.j2') as f:
    ospf_cfg = f.read()


my_vars = {
    'process_id' : 40,
    'network' : '10.220.88.0',
    'wildcard_mask' : '0.0.0.255',
    'area' : 0,
    'Loopback0_addr' : '172.31.255.1',
    'Loopback0_mask' : '255.255.255.255'

 }

template = jinja2.Template(ospf_cfg)
output = template.render(my_vars)
print(output)
