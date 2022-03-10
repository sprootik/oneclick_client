## oneclick-client

![](https://img.shields.io/badge/python-3.9-green) ![](https://img.shields.io/badge/python-3.10-green)

This is a simple library for working with the Spectrum OneClick API.
The basic working methods are implemented, the response can be returned in json, like a python dict, or in xml, like a bs4 object. You can also use xml or json in requests, passing them as text.   

------------
## Installation
````
pip install oneclick-client
````
------------

## Launch examples 
See example.py for more working examples.

```python
# import
from oneclick_client import spectrum as sp

# initialization
api = sp.SpectrumClient(server='https://192.168.0.1:8888',
                        user='spectrum',
                        password='spectrum',
                        verify=False,
                        timeout=5)

# get devices, output in json (python dict)
devices = api.get(out_format='json',
                    app='devices',
                    params={
                        'throttlesize': 10000,
                        'landscape': '0x1000000',
                        'attr': ['0x129e7', '0x129fa', '0x1006e']
                    })

# create service
model = api.post(out_format='json',
                    app='model',
                    params={
                        'landscapeid': '0x1000000',
                        'mtypeid': '0x1046f',
                        'attr': ['0x12a51', '0x1006e'],
                        'val': ['7', 'test_srv'],
                    })
mh = model['create-model-response']['model']['@mh']

# update service name, output in xml (bs4 obj)
update = api.put(app=f"model/{mh}",
                    params={
                        'attr': '0x1006e',
                        'val': 'test_srv_update',
                    })

# request with data in xml and output in json (python dict)
xml_request = """<!-- xml body request GET ALL ASA MODELS -->
<rs:model-request throttlesize="10000"
xmlns:rs="http://www.ca.com/spectrum/restful/schema/request"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.ca.com/spectrum/restful/schema/request ../../../xsd/Request.xsd ">
<rs:target-models>
    <rs:models-search>
        <rs:search-criteria
            xmlns="http://www.ca.com/spectrum/restful/schema/filter">
        <filtered-models>
        <is-derived-from>
            <attribute id="AttributeID.MTYPE_HANDLE">
            <value>0x2101ea</value> <!-- CiscoASA -->
            </attribute>
        </is-derived-from>
        </filtered-models>
    </rs:search-criteria>
    </rs:models-search>
</rs:target-models>
    <rs:requested-attribute id="0x1006e" /> <!-- Device Name -->
    <rs:requested-attribute id="0x10000" /> <!-- Model Type Name -->
    <rs:requested-attribute id="0x10032" /> <!-- Manufacturer -->
    <rs:requested-attribute id="0x129fa" /> <!-- Model Handle -->
    <rs:requested-attribute id="0x1027f" /> <!-- IP Address -->
    <rs:requested-attribute id="0x10004" /> <!-- Contact status -->
    <rs:requested-attribute id="0x110df" /> <!-- MAC Address -->
    <rs:requested-attribute id="0x82002d" /> <!-- Last verified unix timestamp  -->
</rs:model-request>"""

asa_models = api.post(out_format='json', app='models', data=xml_request)
```