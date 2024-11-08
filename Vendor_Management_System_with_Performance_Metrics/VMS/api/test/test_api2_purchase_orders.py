import requests
import json
from django.utils import timezone
from enum import StrEnum
import os

class OrderStatus(StrEnum):
    PENDING = "pending"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    
    @classmethod
    def is_valid_status(cls, status: str):
        return status.lower() in [i.name.lower() for i in cls]

#end class

po_number_for_test = ['po1','po2','po3']
#vendor_code_for_test = ['1','2',]
vendor_id_created_for_test = []

print("****************Running ",os.path.basename(__file__),"**************************")
#Following code retrieves the token for a user.
#You can also use POSTMAN:Enter URL=http://127.0.0.1:8000/api-token-auth/ with method=POST,
# then select the 'Body' tab and under 'raw' enter {"username":"admin","password": "admin"} 
url = 'http://127.0.0.1:8000/api-token-auth/'
response = requests.post(url,data={'username': 'admin', 'password': 'admin'})
print('Response from server: ' + str(response.json()))
response_dict = json.loads(response.text)
token = response_dict['token']
print('token=',token) ## This token is valid infinitely long time.
HEADERS={"Authorization": "Token " + token }
print("#############################")

print("Creating 3 purchase orders for testing.....")
#Send a POST request to create a new vendor
print("..1st we create 2 vendors..")
print("....Sending POST /api/vendors/")
response = requests.post("http://127.0.0.1:8000/api/vendors/", 
    data={'name': 'vendor1', 'contact_details': 'vendor1 contact details here',
          'address': 'vendor1 address here',
          'on_time_delivery_rate': 1.0, 'quality_rating_avg': 1.0, 'fulfillment_rate': 1.0,
          'average_response_time': 1.0
          },
    headers=HEADERS,
)
print('....Response from server: ' + str(response.json()))
response_dict = json.loads(response.text)
vendor_id1 = response_dict["id"]
vendor_id_created_for_test.append(vendor_id1)
print("....successfully created vendor_id:",vendor_id1)

print("....Sending POST /api/vendors/")
response = requests.post("http://127.0.0.1:8000/api/vendors/", 
    data={'name': 'vendor2', 'contact_details': 'vendor2 contact details here',
          'address': 'vendor2 address here',
          'on_time_delivery_rate': 2.0, 'quality_rating_avg': 2.0, 'fulfillment_rate': 2.0,
          'average_response_time': 2.0
          },
    headers=HEADERS,
)
print('....Response from server: ' + str(response.json()))
response_dict = json.loads(response.text)
vendor_id2 = response_dict["id"] 
vendor_id_created_for_test.append(vendor_id2)
print("....successfully created vendor_id:",vendor_id2)
print("......successfully created vendor_id_created_for_test:",vendor_id_created_for_test)


print("Sending POST /api/purchase_orders/")
response = requests.post("http://127.0.0.1:8000/api/purchase_orders/", 
    data={'po_number': po_number_for_test[0], 
          'vendor': vendor_id1, # NOTE: This needs to valid vendor
          'order_date':          '2024-05-04T05:01:33.32',
          'issue_date':          '2024-05-05T05:01:33.32',
          'acknowledgment_date': '2024-05-06T05:01:33.32',
          'delivery_date':       '2024-05-12T05:01:33.32',
          'quantity': 1,
          'status': OrderStatus.PENDING,
          'quality_rating': 1.0,
          'items': json.dumps("Really Cool Item"),
          #'items':  json.dumps({"item_name": "Cool Item", "quantity":13, "unit_price": 1.0}) #This works too
          },
    headers=HEADERS,
)
print('Response from server: ' + str(response.json()))
response_dict = json.loads(response.text)
po_id1 = response_dict["id"] 
print("Successfully created purchase order id: ",po_id1)

print("Sending POST /api/purchase_orders/")
response = requests.post("http://127.0.0.1:8000/api/purchase_orders/", 
    data={'po_number': po_number_for_test[1], 
          'vendor': vendor_id2, # NOTE: This needs to valid vendor
          'order_date':          '2024-05-04T05:01:33.32',
          'issue_date':          '2024-05-05T05:01:33.32',
          'acknowledgment_date': '2024-05-06T05:01:33.32',
          'delivery_date':       '2024-05-12T05:01:33.32',
          'quantity': 1,
          'status': OrderStatus.PENDING,
          'quality_rating': 1.0,
          'items': json.dumps("Another awesome Item"),
          #'items':  json.dumps({"item_name": "Cool Item", "quantity":13, "unit_price": 1.0}) #This works too
          },
    headers=HEADERS,
)
print('Response from server: ' + str(response.json()))
response_dict = json.loads(response.text)
po_id2 = response_dict["id"] 
print("Successfully created purchase order id: ",po_id2)

print("Sending POST /api/purchase_orders/")
response = requests.post("http://127.0.0.1:8000/api/purchase_orders/", 
    data={'po_number': po_number_for_test[2], 
          'vendor': vendor_id2, # NOTE: This needs to valid vendor
          'order_date':          '2024-05-04T05:01:33.32',
          'issue_date':          '2024-05-05T05:01:33.32',
          'acknowledgment_date': '2024-05-06T05:01:33.32',
          'delivery_date':       '2024-05-12T05:01:33.32',
          'quantity': 1,
          'status': OrderStatus.PENDING,
          'quality_rating': 1.0,
          'items': json.dumps("Weird Item"),
          #'items':  json.dumps({"item_name": "Cool Item", "quantity":13, "unit_price": 1.0}) #This works too
          },
    headers=HEADERS,
)
print('Response from server: ' + str(response.json()))
response_dict = json.loads(response.text)
po_id3 = response_dict["id"] 
print("Successfully created purchase order id: ",po_id3)

print("########################################")
#Send a GET request to retrieve all purchase_orders
print("Sending GET /api/purchase_orders/")
response = requests.get('http://127.0.0.1:8000/api/purchase_orders/',headers=HEADERS,)
print('Response from server: ' + str(response.json()))
print("#################################################")

#Send a PUT request to update purchase order 
print("Sending PUT /api/purchase_orders/{}/".format(po_id2))
response = requests.put("http://127.0.0.1:8000/api/purchase_orders/{}/".format(po_id2), 
    data={'po_number': po_number_for_test[1], 
          'vendor': vendor_id2, # NOTE: This needs to valid vendor
          'order_date':          '2024-05-04T05:01:33.32',
          'issue_date':          '2024-05-05T05:01:33.32',
          'acknowledgment_date': '2024-05-06T05:01:33.32',
          'delivery_date':       '2024-05-12T05:01:33.32',
          'quantity': 1,
          'status': OrderStatus.COMPLETED,
          'quality_rating': 1.0,
          'items': json.dumps("Updated Awesome Item"),
          },
    headers=HEADERS,
)
print('Response from server: ' + str(response.json()))
print("#################################################")

#Send a GET request to retrieve purchase order 
print("Sending GET /api/purchase_orders/{}/".format(po_id2))
response = requests.get("http://127.0.0.1:8000/api/purchase_orders/{}/".format(po_id2),headers=HEADERS,)
print('Response from server: ' + str(response.json()))

print("#################################################")

#Send a DELETE request to delete purchase order 
print("Sending DELETE /api/purchase_orders/{}/".format(po_id2))
response = requests.delete("http://127.0.0.1:8000/api/purchase_orders/{}/".format(po_id2),headers=HEADERS,)
print("Successfully deleted po_id = {}".format(po_id2))


print("#################################################")
print("Now we delete all vendors that we created in this test script:")

#we delete all these vendors
for i in range(len(vendor_id_created_for_test)):
    vendor_id = vendor_id_created_for_test[i]
    print("Sending DELETE /api/vendors/{}/".format(vendor_id))
    response = requests.delete( "http://127.0.0.1:8000/api/vendors/{}/".format(vendor_id),headers=HEADERS,)
    print("..Successfully deleted vendor_id = {}".format(vendor_id))

print("All purchase orders that were created for above vendors for testing are deleted too.")
print();print();print();print();print();






