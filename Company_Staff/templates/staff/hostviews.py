def createNewIteminv(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        log_details= LoginDetails.objects.get(id=log_id)
        if log_details.user_type == 'Company':
            com = CompanyDetails.objects.get(login_details = log_details)
        else:
            com = StaffDetails.objects.get(login_details = log_details).company

        name = request.POST['name']
        type = request.POST['type']
        unit = request.POST.get('unit')
        hsn = request.POST['hsn']
        tax = request.POST['taxref']
        gstTax = 0 if tax == 'None-Taxable' else request.POST['intra_st']
        igstTax = 0 if tax == 'None-Taxable' else request.POST['inter_st']
        purPrice = request.POST['pcost']
        purAccount = None if not 'pur_account' in request.POST or request.POST['pur_account'] == "" else request.POST['pur_account']
        purDesc = request.POST['pur_desc']
        salePrice = request.POST['salesprice']
        saleAccount = None if not 'sale_account' in request.POST or request.POST['sale_account'] == "" else request.POST['sale_account']
        saleDesc = request.POST['sale_desc']
        inventory = request.POST.get('invacc')
        stock = 0 if request.POST.get('stock') == "" else request.POST.get('stock')
        stockUnitRate = 0 if request.POST.get('stock_rate') == "" else request.POST.get('stock_rate')
        minStock = request.POST['min_stock']
        createdDate = date.today()
        
        #save item and transaction if item or hsn doesn't exists already
        if Items.objects.filter(company=com, item_name__iexact=name).exists():
            res = f"{name} already exists, try another!"
            return JsonResponse({'status': False, 'message':res})
        elif Items.objects.filter(company = com, hsn_code__iexact = hsn).exists():
            res = f"HSN - {hsn} already exists, try another.!"
            return JsonResponse({'status': False, 'message':res})
        else:
            item = Items(
                company = com,
                login_details = com.login_details,
                item_name = name,
                item_type = type,
                unit = None if unit == "" else Unit.objects.get(id = int(unit)),
                hsn_code = hsn,
                tax_reference = tax,
                intrastate_tax = gstTax,
                interstate_tax = igstTax,
                sales_account = saleAccount,
                selling_price = salePrice,
                sales_description = saleDesc,
                purchase_account = purAccount,
                purchase_price = purPrice,
                purchase_description = purDesc,
                date = createdDate,
                minimum_stock_to_maintain = minStock,
                inventory_account = inventory,
                opening_stock = stock,
                current_stock = stock,
                opening_stock_per_unit = stockUnitRate,
                track_inventory = int(request.POST['trackInv']),
                activation_tag = 'active',
                type = 'Opening Stock'
            )
            item.save()

            #save transaction

            Item_Transaction_History.objects.create(
                company = com,
                logindetails = com.login_details,
                items = item,
                Date = createdDate,
                action = 'Created'

            )
            
            return JsonResponse({'status': True})
    else:
       return redirect('/')

def getAllItemsinv(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        log_details= LoginDetails.objects.get(id=log_id)
        if log_details.user_type == 'Company':
            com = CompanyDetails.objects.get(login_details = log_details)
        else:
            com = StaffDetails.objects.get(login_details = log_details).company

        items = {}
        option_objects = Items.objects.filter(company = com, activation_tag='active')
        for option in option_objects:
            items[option.id] = [option.id,option.item_name]

        return JsonResponse(items)
    else:
        return redirect('/')