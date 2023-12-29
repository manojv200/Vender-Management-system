import json
from django.shortcuts import render
from.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(('GET','POST',))
def create_vendor(request):
    print(request.method)
    try:
        
        if request.method == 'POST':
            data = request.POST
            name = data['vendor_name']
            mob = data['mob']
            email = data['email']
            address = data['address']
            pin_code = data['pin_code']
            contacts = mob+',\n'+email
            address+=',\n'+pin_code
            Vendor(vendor_name=name,contact_details=contacts,address=address).save()
            res = {'msg':'success'}
        else:
            vendors = Vendor.objects.all()
            vendor_list=[]
            for vendor in vendors:
                vendor_list.append(vendor.vendor_name)
            res = {'msg':'success',
               'vendor_list':vendor_list}

        return Response(res)
    except Exception as e:
        res = {'msg':str(e)}
        return Response(res)
@api_view(('GET','PUT','DELETE',))
def list_vendor(request,vendor_id):
    try:
        if request.method =="GET":
            vendor = Vendor.objects.get(id=vendor_id)
            vendor_dict = {}

            vendor_dict['vendor_id'] = vendor.id
            vendor_dict['vendor_name'] = vendor.vendor_name
            vendor_dict['contacts'] = vendor.contact_details
            vendor_dict['address']=vendor.address
            vendor_dict['vendor_code'] = vendor.vendor_code
            vendor_dict['vendor_on_time_delivery_rate'] = vendor.on_time_delivery_rate
            vendor_dict['vendor_quality_rating_avg'] = vendor.quality_rating_avg
            vendor_dict['vendor_average_response_time'] = vendor.average_response_time
            vendor_dict['vendor_fulfillment_rate'] = vendor.fulfillment_rate
            res = {'msg':'success',
               'vendor_details':vendor_dict}
        elif request.method == "PUT":
             data = json.loads(request.body.decode('utf-8'))
             print(data)
             instance = Vendor.objects.get(id=vendor_id)

             # Update the fields based on the data received
             for key, value in data.items():
                 setattr(instance, key, value)

             # Save the updated instance
             instance.save()
             res = {'msg':'success'}
        elif request.method == 'DELETE':
             instance = Vendor.objects.get(id=vendor_id)
             instance.delete()
             res = {'msg':'Deleted successfully'
               }

        return Response(res)
    except Exception as e:
        res = {'msg':str(e)}
        return Response(res)
@api_view(('GET','POST',))
def create_purchase_order(request):
    print(request.method)
    try:
        
        if request.method == 'POST':
            data = request.POST
            del_date = data['del_date']
            items = data['items']
            quantity = data['quantity']
            status = data['status']
            issue_date = data['issue_date']
            Purchase_order(delivery_date=del_date,items=items,quantity=quantity,status=status,issue_date=issue_date).save()
            res = {'msg':'success'}
        else:
            orders = Purchase_order.objects.all()
            order_list={}
            orders_l = []
            for order in orders:
                print(order)
                # orders_l.append()
                # order_list['vendor'] =  
            res = {'msg':'success',
               'vendor_list':order_list}

        return Response(res)
    except Exception as e:
        res = {'msg':str(e)}
        return Response(res)
@api_view(('GET','PUT','DELETE',))
def list_purchase_orders(request,vendor_id):
    try:
        if request.method =="GET":
            vendor = Vendor.objects.get(id=vendor_id)
            vendor_dict = {}

            vendor_dict['vendor_id'] = vendor.id
            vendor_dict['vendor_name'] = vendor.vendor_name
            vendor_dict['contacts'] = vendor.contact_details
            vendor_dict['address']=vendor.address
            vendor_dict['vendor_code'] = vendor.vendor_code
            vendor_dict['vendor_on_time_delivery_rate'] = vendor.on_time_delivery_rate
            vendor_dict['vendor_quality_rating_avg'] = vendor.quality_rating_avg
            vendor_dict['vendor_average_response_time'] = vendor.average_response_time
            vendor_dict['vendor_fulfillment_rate'] = vendor.fulfillment_rate
            res = {'msg':'success',
               'vendor_details':vendor_dict}
        elif request.method == "PUT":
             data = json.loads(request.body.decode('utf-8'))
             print(data)
             instance = Vendor.objects.get(id=vendor_id)

             # Update the fields based on the data received
             for key, value in data.items():
                 setattr(instance, key, value)

             # Save the updated instance
             instance.save()
             res = {'msg':'success'}
        elif request.method == 'DELETE':
             instance = Vendor.objects.get(id=vendor_id)
             instance.delete()
             res = {'msg':'Deleted successfully'
               }

        return Response(res)
    except Exception as e:
        res = {'msg':str(e)}
        return Response(res)


