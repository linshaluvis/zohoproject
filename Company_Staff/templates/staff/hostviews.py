def invoice_import(request):
    if request.method == 'POST' and 'file' in request.FILES:
        if 'login_id' in request.session:
            log_id = request.session['login_id']
            if 'login_id' not in request.session:
                return redirect('/')
            log_details = LoginDetails.objects.get(id=log_id)

            if log_details.user_type == 'Staff':
                staff = StaffDetails.objects.get(login_details=log_details)
                company = staff.company
                    
            elif log_details.user_type == 'Company':
                company = CompanyDetails.objects.get(login_details=log_details)

            excel_file = request.FILES['file']
            workbook = load_workbook(excel_file)
            
            sheet1 = workbook['Sheet1']
            sheet2 = workbook['Sheet2']
            
            invoices = []  # List to store created invoices

            for row in sheet1.iter_rows(min_row=2, values_only=True):
                try:
                    customer = Customer.objects.get(first_name=row[1],customer_email=row[2],company=company)
                    payment_terms1 = Company_Payment_Term.objects.get(term_name=row[9], company=company)
                    print(payment_terms1)
                except ObjectDoesNotExist:
                    print(f"Customer with name or email '{row[1]}' or Payment term with term name '{row[9]}' does not exist in the database.")
                    continue
                
                # Create and save the invoice object
                latest_inv = invoice.objects.filter(company_id = company).order_by('-id').first()

                new_number = int(latest_inv.reference_number) + 1 if latest_inv else 1

                if invoiceReference.objects.filter(company_id = company).exists():
                    deleted = invoiceReference.objects.get(company_id = company)
                    
                    if deleted:
                        while int(deleted.reference_number) >= new_number:
                            new_number+=1
                created_invoice = invoice(
                    company=company,
                    login_details=log_details,
                    customer=customer,
                    payment_terms=payment_terms1,
                    customer_email=row[2],
                    customer_billingaddress=row[3],
                    customer_GSTtype=row[4],
                    customer_GSTnumber=row[5],
                    customer_place_of_supply=row[6],
                    invoice_number=row[0],
                    date=row[8],
                    expiration_date=row[10],
                    payment_method=row[12],
                    cheque_number=row[13],
                    UPI_number=row[14],
                    bank_account_number=row[15],
                    sub_total=row[19],
                    CGST=row[20],
                    SGST=row[21],
                    IGST=row[29],

                    
                    tax_amount=row[22],
                    shipping_charge=row[23],
                    grand_total=row[25],
                    advanced_paid=row[26],
                    balance=row[27],
                    description=row[16],
                    status=row[28],
                    reference_number=new_number

                )
               
                created_invoice.save()
                invoices.append(created_invoice)
                
                # Save invoice history
                invoiceHistory.objects.create(
                    company=company,
                    login_details=log_details,
                    invoice=created_invoice,
                    date=datetime.now(),
                    action='Created'
                )
        
            for row in sheet2.iter_rows(min_row=2, values_only=True):
                try:
                    item = Items.objects.get(item_name=row[1],company=company)
                except ObjectDoesNotExist:
                    print(f"Item with name '{row[1]}' does not exist in the database.")
                    continue
                
                matching_invoices = [inv for inv in invoices if inv.invoice_number == row[0]]
                if not matching_invoices:
                    print(f"No invoice found for row with invoice number '{row[0]}'")
                    continue

                # Assuming there's only one matching invoice
                invoice1 = matching_invoices[0]

                # Create and save the invoice item object
                invoice_item = invoiceitems(
                    invoice=invoice1,
                    company=company,
                    Items=item,
                    logindetails=log_details,
                    hsn=row[2],
                    quantity=row[3],
                    price=row[4],
                    tax_rate=row[5],
                    discount=row[6],
                    total=row[7],
                )
                invoice_item.save()
                
                # Update current stock for the item
                item.current_stock -= int(row[3])
                item.save()

            return redirect('invoice_list_out')

    return HttpResponse("No file uploaded or invalid request method")
