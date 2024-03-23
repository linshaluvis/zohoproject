def invoice_createpage(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        if 'login_id' not in request.session:
            return redirect('/')
        log_details= LoginDetails.objects.get(id=log_id)
        data = LoginDetails.objects.get(id = log_id)
        log_details= LoginDetails.objects.get(id=log_id)
        
        if log_details.user_type == 'Staff':
                staff = StaffDetails.objects.get(login_details=log_details)
                company = staff.company
                allmodules=ZohoModules.objects.get(company=staff.company)
                dash_details = StaffDetails.objects.get(login_details=log_details,company_approval=1)
                    
        elif log_details.user_type == 'Company':
                company = CompanyDetails.objects.get(login_details=log_details)
                dash_details = CompanyDetails.objects.get(login_details=log_details,superadmin_approval=1,Distributor_approval=1)

                allmodules= ZohoModules.objects.get(company=company,status='New')
        invoices = invoice.objects.filter(company = company)

        customers=Customer.objects.filter(company_id = company, customer_status = 'Active')
        item=Items.objects.filter(company_id = company)
        payments=Company_Payment_Term.objects.filter(company_id = company)
        banks = Banking.objects.filter(company_id = company)
        unit = Unit.objects.filter(company_id = company)
        acc = Chart_of_Accounts.objects.filter(Q(account_type='Expense') | Q(account_type='Other Expense') | Q(account_type='Cost Of Goods Sold'), company=company).order_by('account_name')

        latest_inv = invoice.objects.filter(company_id = company).order_by('-id').first()

        new_number = int(latest_inv.reference_number) + 1 if latest_inv else 1

        if invoiceReference.objects.filter(company_id = company).exists():
            deleted = invoiceReference.objects.get(company_id = company)
            
            if deleted:
                while int(deleted.reference_number) >= new_number:
                    new_number+=1

        # Finding next invoice number w r t last invoic number if exists.
        nxtInv = ""
        lastInv = invoice.objects.filter(company_id = company).last()
        if lastInv:
            inv_no = str(lastInv.invoice_number)
            numbers = []
            stri = []
            for word in inv_no:
                if word.isdigit():
                    numbers.append(word)
                else:
                    stri.append(word)
            
            num=''
            for i in numbers:
                num +=i
            
            st = ''
            for j in stri:
                st = st+j

            inv_num = int(num)+1

            if num[0] == '0':
                if inv_num <10:
                    nxtInv = st+'0'+ str(inv_num)
                else:
                    nxtInv = st+ str(inv_num)
            else:
                nxtInv = st+ str(inv_num)


       

        context={
            'details':dash_details,
            'allmodules': allmodules,
             'c':customers,
            'p':item,
            'payments':payments,
            'banks':banks,
            'units': unit,
            'ref_no':new_number,
            'invNo':nxtInv,
            'accounts':acc,
            'company':company,



            
        }
        return render(request,'staff/createinvoice.html',context)