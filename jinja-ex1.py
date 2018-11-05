#!usr/bin/env python
from __future__ import unicode_literals, print_function
import jinja2

#The process ID, network, wildcard mask, and area should all be variables in the Jinja2 template.
#Use a template directly embedded in your Python script.

ospf_cfg = """
router ospf {{ process_id }}
 network {{ network }} {{ wildcard_mask }} area {{ area }}

 """

ospf_vars = {
    'process_id' : 40,
    'network' : '10.220.88.0',
    'wildcard_mask' : '0.0.0.255',
    'area' : 0

 }

template = jinja2.Template(ospf_cfg)
output = template.render(**ospf_vars)
print(output)
