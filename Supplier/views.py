from django.shortcuts import render
from .models import SupplierModel, ExcelFile
import pandas as pd
from django.http import JsonResponse 
from django.conf import settings
from datetime import datetime
import os

# Create your views here.

def export_supplier_to_excel(request):
    objs = SupplierModel.objects.all()
    data = []
    for obj in objs:
        data.append(obj.parse_to_json())
    pd.DataFrame(data).to_excel('output.xlsx')
    return JsonResponse({
        'status': 200
    })


def import_supplier(request):
    if (request.method == 'POST'):
        file = request.FILES['files']
        obj = ExcelFile.objects.create(file = file)
        path = str(obj.file)
        full_path = os.path.join(settings.MEDIA_ROOT, path)
        df = pd.read_excel(full_path, keep_default_na=False)
        for d in df.values:
            id = d[0]
            try:
                supplier = SupplierModel.objects.get(id=id)
                update_supplier(supplier, d)
            except:
                supplier = SupplierModel()
                update_supplier(supplier, d)
            
        return JsonResponse({'status': 200, 'msg':'Upload done'})
    else:
        return render(request, "excel.html")

def update_supplier(supplier, d):
    print('1 is {0}'.format(d[1]))
    print('2 is {0}'.format(d[2]))
    print('3 is {0}'.format(d[3]))
    print('4 is {0}'.format(d[4]))
    print('5 is {0}'.format(d[5]))
    print('6 is {0}'.format(d[6]))
    print('7 is {0}'.format(d[7]))
    print('8 is {0}'.format(d[8]))
    print('9 is {0}'.format(d[9]))
    print('10 is {0}'.format(d[10]))
    print('11 is {0}'.format(d[11]))
    print('12 is {0}'.format(d[12]))
    print('13 is {0}'.format(d[13]))
    print('14 is {0}'.format(d[14]))
    print('15 is {0}'.format(d[15]))
    print('16 is {0}'.format(d[16]))
    print('17 is {0}'.format(d[17]))
    print('18 is {0}'.format(d[18]))
    print('19 is {0}'.format(d[19]))
    print('20 is {0}'.format(d[20]))

    supplier.name = d[1]
    supplier.link = d[2]
    supplier.channel = d[3]
    supplier.follower = d[4]
    supplier.engagement_rate_percent = d[5]
    supplier.location = d[6]
    supplier.year_category = d[7]
    supplier.gender = d[8]
    supplier.industries = d[9]
    supplier.original_cost_picture = d[10]
    supplier.original_cost_video = d[11]
    supplier.original_cost_event = d[12]
    supplier.kpi = d[13]
    supplier.note = d[14]
    supplier.supplier_name = d[15]
    supplier.booking_contact_name = d[16]
    supplier.booking_contact_phone = d[17]
    supplier.booking_contact_email = d[18]
    supplier.latest_update = datetime.strptime(d[19], '%Y-%m-%d %H:%M')  #self.latest_update.strftime('%Y-%m-%d %H:%M')
    supplier.handle_by = d[20]
    supplier.group_chat_name = d[21]
    supplier.kenh = d[22]
    supplier.lana_leader = d[23]
    should_update_id = False
    id = d[0]
    if id == 0:
        should_update_id = True
    if id:
        should_update_id = True
    if should_update_id:
        supplier.id = d[0]
    supplier.save() 
