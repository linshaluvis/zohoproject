path('getinvCustomerDetails',views.getinvCustomerDetails,name='getinvCustomerDetails'),
    path('getinvBankAccountNumber',views.getinvBankAccountNumber,name='getinvBankAccountNumber'),
    path('newinvPaymentTerm',views.newinvPaymentTerm,name='newinvPaymentTerm'),
    path('getinvItemDetails',views.getinvItemDetails,name='getinvItemDetails'),
    path('checkInvoiceNumber',views.checkInvoiceNumber,name='checkInvoiceNumber'),
    path('addinv_unit',views.addinv_unit,name='addinv_unit'),
    path('showinvunit_dropdown',views.showinvunit_dropdown,name='showinvunit_dropdown'),

    path('createNewIteminv',views.createNewIteminv,name='createNewIteminv'),
    path('getAllItemsinv',views.getAllItemsinv,name='getAllItemsinv'),
    
    
    
    # models
    class invoice(models.Model):
    company = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE,null=True,blank=True)
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    payment_terms = models.ForeignKey(Company_Payment_Term,on_delete=models.CASCADE,null=True,blank=True)

    customer_email=models.EmailField(max_length=220,null=True,blank=True)
    customer_billingaddress=models.CharField(max_length=220,null=True,blank=True)
    customer_GSTtype=models.CharField(max_length=220,null=True,blank=True)
    customer_GSTnumber=models.CharField(max_length=220,null=True,blank=True)
    customer_place_of_supply=models.CharField(max_length=220,null=True,blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True) 
    expiration_date = models.DateField(auto_now_add=True, null=True, blank=True) 
    reference_number=models.IntegerField(blank=True,null=True,)
    invoice_number=models.CharField(max_length=220,null=True,blank=True) 
    payment_method=models.CharField(max_length=220,null=True,blank=True) 
    cheque_number=models.CharField(max_length=220,null=True,blank=True) 
    UPI_number=models.CharField(max_length=220,null=True,blank=True) 
    bank_account_number=models.CharField(max_length=220,null=True,blank=True) 
    description=models.CharField(max_length=220,null=True,blank=True) 
    terms_and_condition=models.CharField(max_length=220,null=True,blank=True) 
    document=models.FileField(upload_to="images/",null=True)
    sub_total=models.FloatField(default=0.0, null=True, blank=True)
    CGST=models.FloatField(default=0.0, null=True, blank=True)
    SGST=models.FloatField(default=0.0, null=True, blank=True)
    IGST = models.FloatField(default=0.0, null=True, blank=True)
    price_list_applied = models.BooleanField(null=True, default=False)
    price_list = models.ForeignKey(PriceList, on_delete = models.SET_NULL,null=True)


    tax_amount=models.FloatField(default=0.0, null=True, blank=True)
    shipping_charge=models.FloatField(default=0.0, null=True, blank=True)
    adjustment=models.FloatField(default=0.0, null=True, blank=True)
    grand_total=models.FloatField(default=0.0, null=True, blank=True)
    advanced_paid=models.FloatField(default=0.0, null=True, blank=True)
    balance=models.FloatField(default=0.0, null=True, blank=True)
    status=models.CharField(max_length=220,null=True,blank=True) 