#zoho Final
from django.urls import path,re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    # -------------------------------Company section--------------------------------
    path('Company/Dashboard',views.company_dashboard,name='company_dashboard'),
    path('Company/Staff-Request',views.company_staff_request,name='company_staff_request'),
    path('Company/Staff-Request/Accept/<int:pk>',views.staff_request_accept,name='staff_request_accept'),
    path('Company/Staff-Request/Reject/<int:pk>',views.staff_request_reject,name='staff_request_reject'),
    path('Company/All-Staffs',views.company_all_staff,name='company_all_staff'),
    path('Company/Staff-Approval/Cancel/<int:pk>',views.staff_approval_cancel,name='staff_approval_cancel'),
    path('Company/Profile',views.company_profile,name='company_profile'),
    path('Company/Profile-Editpage',views.company_profile_editpage,name='company_profile_editpage'),
    path('Company/Profile/Edit/Basicdetails',views.company_profile_basicdetails_edit,name='company_profile_basicdetails_edit'),
    path('Company/Password_Change',views.company_password_change,name='company_password_change'),
    path('Company/Profile/Edit/Companydetails',views.company_profile_companydetails_edit,name='company_profile_companydetails_edit'),
    path('Company/Module-Editpage',views.company_module_editpage,name='company_module_editpage'),
    path('Company/Module-Edit',views.company_module_edit,name='company_module_edit'),
    path('Company/Renew/Payment_terms',views.company_renew_terms,name='company_renew_terms'),
    path('Company/Notifications',views.company_notifications,name='company_notifications'),
    path('company/messages/read/<int:pk>',views.company_message_read,name='company_message_read'),
    path('Company/Payment_History',views.company_payment_history,name='company_payment_history'),
    path('Company/Trial/Review',views.company_trial_feedback,name='company_trial_feedback'),
    path('Company/Profile/Edit/gsttype',views.company_gsttype_change,name='company_gsttype_change'),


    # -------------------------------Staff section--------------------------------
    path('Staff/Dashboard',views.staff_dashboard,name='staff_dashboard'),
    path('Staff/Profile',views.staff_profile,name='staff_profile'),
    path('Staff/Profile-Editpage',views.staff_profile_editpage,name='staff_profile_editpage'),
    path('Staff/Profile/Edit/details',views.staff_profile_details_edit,name='staff_profile_details_edit'),
    path('Staff/Password_Change',views.staff_password_change,name='staff_password_change'),
        # -------------------------------Staff section invoice--------------------------------
    path('Staff/invoice_listout',views.invoice_list_out,name='invoice_list_out'),
    path('Staff/invoice/create',views.invoice_create,name='invoice_create'),
    path('Staff/invoice/invoice_createpage',views.invoice_createpage,name='invoice_createpage'),
    path('Staff/invoice/itemdata',views.itemdata,name='itemdata'),
    path('Staff/invoice/viewInvoice',views.viewInvoice,name='viewInvoice'),
    path('Staff/invoice/customerdata',views.customerdata,name='customerdata'),
    path('Staff/invoice/getInvoiceCustomerData',views.getInvoiceCustomerData,name='getInvoiceCustomerData'),
    path('Staff/invoice/getInvItemDetails',views.getInvItemDetails,name='getInvItemDetails'),
    path('Staff/invoice/getBankAccount',views.getBankAccount,name='getBankAccount'),
    path('Staff/invoice/createInvoice',views.createInvoice,name='createInvoice'),
    path('Staff/invoice/checkInvoiceNumber',views.checkInvoiceNumber,name='checkInvoiceNumber'),
    path('Staff/invoice/invoice_import',views.invoice_import,name='invoice_import'),
    path('Staff/invoice/view/<int:pk>',views.view,name='view'),

    path('Staff/invoice/filter_invoice_draft/<int:pk>',views.filter_invoice_draft,name='filter_invoice_draft'),
    path('Staff/invoice/filter_invoice_sent/<int:pk>',views.filter_invoice_sent,name='filter_invoice_sent'),
    path('Staff/invoice/filter_invoice_name/<int:pk>',views.filter_invoice_name,name='filter_invoice_name'),
    path('Staff/invoice/filter_invoice_number/<int:pk>',views.filter_invoice_number,name='filter_invoice_number'),
     path('Staff/invoice/edit_invoice/<int:id>',views.editInvoice, name='editInvoice'),
    path('Staff/invoice/update_invoice/<int:id>',views.updateInvoice, name='updateInvoice'),
    path('Staff/invoice/convert_invoice/<int:id>',views.convertInvoice, name='convertInvoice'),
    path('Staff/invoice/invoicePdf/<int:id>',views.invoicePdf, name='invoicePdf'),
    path('Staff/invoice/delete_invoice/<int:id>',views.deleteInvoice, name= 'deleteInvoice'),
    path('Staff/invoice/Invoice_history/<int:id>',views.InvoiceHistory, name='InvoiceHistory'),
    path('Staff/invoice/add_attach/<int:id>',views.add_attach, name='add_attach'),
    path('Staff/invoice/share_invoice_to_email/<int:id>',views.shareInvoiceToEmail, name='shareInvoiceToEmail'),
    path('Staff/invoice/addInvoiceComment/<int:id>',views.addInvoiceComment, name='addInvoiceComment'),
    path('Staff/invoice/deleteInvoiceComment/<int:id>',views.deleteInvoiceComment, name='deleteInvoiceComment'),
    path('Staff/invoice/newCustomerPaymentTerm',views.newCustomerPaymentTerm, name='newCustomerPaymentTerm'),
    path('Staff/invoice/checkCustomerName',views.checkCustomerName, name='checkCustomerName'),
    path('Staff/invoice/checkCustomerGSTIN',views.checkCustomerGSTIN, name='checkCustomerGSTIN'),
    path('Staff/invoice/checkCustomerPAN',views.checkCustomerPAN, name='checkCustomerPAN'),
    path('Staff/invoice/checkCustomerPhone',views.checkCustomerPhone, name='checkCustomerPhone'),
    path('Staff/invoice/checkCustomerEmail',views.checkCustomerEmail, name='checkCustomerEmail'),
    path('Staff/invoice/createInvoiceCustomer',views.createInvoiceCustomer, name='createInvoiceCustomer'),
    path('Staff/invoice/invoice_item',views.invoice_item, name='invoice_item'),

    path('Staff/invoice/getCustomers',views.getCustomers, name='getCustomers'),
    path('Staff/invoice/createInvoiceItem',views.createInvoiceItem, name='createInvoiceItem'),
    path('Staff/invoice/getItems',views.getItems, name='getItems'),
    path('Staff/invoice/saveItemUnit',views.saveItemUnit, name='saveItemUnit'),
    path('Staff/invoice/show_unit_dropdown',views.show_unit_dropdown, name='show_unit_dropdown'),
    path('Staff/invoice/createNewAccountFromItems',views.createNewAccountFromItems, name='createNewAccountFromItems'),
    path('Staff/invoice/checkAccounts',views.checkAccounts, name='checkAccounts'),
    path('Staff/invoice/add_customer_invoice',views.add_customer_invoice, name='add_customer_invoice'),
        path('Staff/invoice/create_item_invoice',views.create_item_invoice, name='create_item_invoice'),
    path('Staff/invoice/getAllAccounts',views.getAllAccounts, name='getAllAccounts'),


path('check_customer_phonenumber_exist',views.check_customer_phonenumber_exist,name='check_customer_phonenumber_exist'),
    path('check_customer_work_phone_exist',views.check_customer_work_phone_exist,name='check_customer_work_phone_exist'),
    path('check_customer_email_exist',views.check_customer_email_exist,name='check_customer_email_exist'),
    path('check_customer_term_exist',views.check_customer_term_exist,name='check_customer_term_exist'),
    path('customer_payment_terms_add',views.customer_payment_terms_add,name='customer_payment_terms_add'),
    path('customer_check_pan',views.customer_check_pan,name='customer_check_pan'),
        path('customer_check_gst',views.customer_check_gst,name='customer_check_gst'),
        
        # edit
    path('getinvCustomerDetails',views.getinvCustomerDetails,name='getinvCustomerDetails'),
    path('getinvBankAccountNumber',views.getinvBankAccountNumber,name='getinvBankAccountNumber'),
    path('newinvPaymentTerm',views.newinvPaymentTerm,name='newinvPaymentTerm'),
    path('getinvItemDetails',views.getinvItemDetails,name='getinvItemDetails'),
    path('checkInvoiceNumber',views.checkInvoiceNumber,name='checkInvoiceNumber'),
    path('addinv_unit',views.addinv_unit,name='addinv_unit'),
    path('showinvunit_dropdown',views.showinvunit_dropdown,name='showinvunit_dropdown'),

    path('createNewIteminv',views.createNewIteminv,name='createNewIteminv'),
    path('getAllItemsinv',views.getAllItemsinv,name='getAllItemsinv'),







        



































    
    
    # -------------------------------Zoho Modules section--------------------------------
    
    
  
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)