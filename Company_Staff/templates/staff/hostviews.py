def checkInvoiceNumber(request):
    if 'login_id' in request.session:
        log_id = request.session['login_id']
        log_details= LoginDetails.objects.get(id=log_id)
        if log_details.user_type == 'Company':
            com = CompanyDetails.objects.get(login_details = log_details)
        else:
            com = StaffDetails.objects.get(login_details = log_details).company
        
        RecInvNo = request.GET['RecInvNum']

        # Finding next rec_invoice number w r t last rec_invoice number if exists.
        nxtInv = ""
        lastInv = invoice.objects.filter(company = com).last()

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
           

            
            padding_length = len(num) - 1

                    
            nxtInv = f"{st}{num[0]}{inv_num:0{padding_length}d}"
            print(nxtInv)
            

        PatternStr = []
        for word in RecInvNo:
            if word.isdigit():
                pass
            else:
                PatternStr.append(word)
        
        pattern = ''
        for j in PatternStr:
            pattern += j
            print("patern")
            print(pattern)


        # pattern_exists = checkRecInvNumberPattern(pattern)

        # if pattern !="" and pattern_exists:
        #     return JsonResponse({'status':False, 'message':'Rec. Invoice No. Pattern already Exists.!'})
        if invoice.objects.filter(company = com, invoice_number__iexact = RecInvNo).exists():
            return JsonResponse({'status':False, 'message':'Invoice No. already Exists.!'})
        elif nxtInv != "" and RecInvNo != nxtInv:
            return JsonResponse({'status':False, 'message':'Invoice No. is not continuous.!'})
        else:
            return JsonResponse({'status':True, 'message':'Number is okay.!'})
    else:
       return redirect('/')
def invoice_createpage(request):
       if 'login_id' in request.session:
           log_id = request.session['login_id']
           log_details= LoginDetails.objects.get(id=log_id)
           if log_details.user_type == 'Company':
               cmp = CompanyDetails.objects.get(login_details = log_details)
               dash_details = CompanyDetails.objects.get(login_details=log_details)
           else:
               cmp = StaffDetails.objects.get(login_details = log_details).company
               dash_details = StaffDetails.objects.get(login_details=log_details)
   
           allmodules= ZohoModules.objects.get(company = cmp)
           cust = Customer.objects.filter(company = cmp, customer_status = 'Active')
           trm = Company_Payment_Term.objects.filter(company = cmp)
           repeat = CompanyRepeatEvery.objects.filter(company = cmp)
           bnk = Banking.objects.filter(company = cmp)
           priceList = PriceList.objects.filter(company = cmp, status = 'Active')
           itms = Items.objects.filter(company = cmp, activation_tag = 'active')
           units = Unit.objects.filter(company=cmp)
           accounts=Chart_of_Accounts.objects.filter(company=cmp)
   
           # Fetching last rec_invoice and assigning upcoming ref no as current + 1
           # Also check for if any bill is deleted and ref no is continuos w r t the deleted rec_invoice
           latest_inv = invoice.objects.filter(company = cmp).order_by('-id').first()
   
           new_number = int(latest_inv.reference_number) + 1 if latest_inv else 1
   
           if invoiceReference.objects.filter(company = cmp).exists():
               deleted = invoiceReference.objects.get(company = cmp)
               
               if deleted:
                   while int(deleted.reference_number) >= new_number:
                       new_number+=1
   
           # Finding next rec_invoice number w r t last rec_invoice number if exists.
           nxtInv = ""
           lastInv = invoice.objects.filter(company = cmp).last()
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
   
               padding_length = len(num) - 1
   
                       
               nxtInv = f"{st}{num[0]}{inv_num:0{padding_length}d}"
           else:
               nxtInv = 'in-01'
           context = {
               'cmp':cmp,'allmodules':allmodules, 'details':dash_details, 'customers': cust,'pTerms':trm, 'repeat':repeat, 'banks':bnk, 'priceListItems':priceList, 'items':itms,
               'invNo':nxtInv, 'ref_no':new_number,'units': units,'accounts':accounts,
           }
       
           return render(request,'staff/createinvoice.html',context)