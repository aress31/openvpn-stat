# openvpn-stat
[![Language](https://img.shields.io/badge/Lang-Python-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-red.svg)](https://opensource.org/licenses/Apache-2.0)

This script parses `OpenVPN` status log files to display connected clients and their respective routing information in a user-friendly table. This enables VPN administrators to easily monitor and troubleshoot `OpenVPN` servers. The log file location is set using the `OpenVPN` `status` directive.

## Installation
```
$ git clone https://github.com/AresS31/openvpn-stat
# python -m pip install -r openvpn-stat/requirements.txt
```

## Usage
### Generic usage
```
usage: openvpn-stat.py [-h] -iL INPUT_LOG {client,routing} ...

Display OpenVPN connected clients and routing information

positional arguments:
  {client,routing}

optional arguments:
  -h, --help            show this help message and exit
  -iL INPUT_LOG, -input--log INPUT_LOG
                        OpenVPN status log file
```

### Client usage
```
usage: openvpn-stat.py client [-h]
                              [-s {Real Address,Common Name,Bytes Received,Bytes Sent,Connected Since}]

optional arguments:
  -h, --help            show this help message and exit
  -s {Real Address,Common Name,Bytes Received,Bytes Sent,Connected Since}, --sort {Real Address,Common Name,Bytes Received,Bytes Sent,Connected Since}
                        sort table by selected field
```

### Routing usage
```
usage: openvpn-stat.py routing [-h]
                               [-s {Virtual Address,Common Name,Real Address,Last Ref}]

optional arguments:
  -h, --help            show this help message and exit
  -s {Virtual Address,Common Name,Real Address,Last Ref}, --sort {Virtual Address,Common Name,Real Address,Last Ref}
                        sort table by selected field
```

## Possible Improvements
- [ ] Improve the sorting feature.
- [ ] Improve the table design/look.
- [ ] Source code optimisation.

## Licenses
### openvpn-stat
Copyright (C) 2018 Alexandre Teyar

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  <http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. 
