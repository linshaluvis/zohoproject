# Generated by Django 5.0 on 2024-03-26 05:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0015_remove_invoice_tax_amount_or_igst_invoice_igst_and_more'),
        ('Register_Login', '0015_remove_paymenttermsupdates_interested_to_continue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('status', models.CharField(max_length=255, null=True)),
                ('reason', models.CharField(max_length=255, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.payroll_employee')),
                ('login_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('month', models.IntegerField(null=True)),
                ('year', models.IntegerField(null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.payroll_employee')),
                ('login_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('action', models.CharField(max_length=100, null=True)),
                ('attendance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.attendance')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Loandate', models.DateField(null=True)),
                ('LoanAmount', models.IntegerField(blank=True, null=True)),
                ('duration', models.CharField(blank=True, max_length=255)),
                ('Expiry_date', models.DateField(null=True)),
                ('payment_method', models.CharField(blank=True, max_length=220, null=True)),
                ('cheque_number', models.CharField(blank=True, max_length=220, null=True)),
                ('upi_id', models.CharField(blank=True, max_length=220, null=True)),
                ('bank_acc_number', models.CharField(blank=True, max_length=220, null=True)),
                ('Monthly_payment_type', models.CharField(blank=True, max_length=220, null=True)),
                ('MonthlyCut_percentage', models.IntegerField(blank=True, null=True)),
                ('MonthlyCut_Amount', models.IntegerField(blank=True, null=True)),
                ('note', models.CharField(blank=True, max_length=220, null=True)),
                ('file', models.FileField(null=True, upload_to='images/')),
                ('status', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('emp_name', models.CharField(blank=True, max_length=220, null=True)),
                ('emp_no', models.IntegerField(blank=True, null=True)),
                ('join_date', models.DateField(null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('Employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.payroll_employee')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='employeeloan_comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.employeeloan')),
                ('logindetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='Employeeloan_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now=True, null=True)),
                ('action', models.CharField(blank=True, max_length=220, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('employeeloan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.employeeloan')),
                ('login_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeLoanRepayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal_amount', models.IntegerField(null=True)),
                ('interest_amonut', models.IntegerField(null=True)),
                ('payment_date', models.DateField(null=True)),
                ('payment_method', models.CharField(max_length=255, null=True)),
                ('cheque_id', models.CharField(blank=True, max_length=255, null=True)),
                ('upi_id', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_id', models.CharField(blank=True, max_length=255, null=True)),
                ('total_payment', models.IntegerField(null=True)),
                ('balance', models.IntegerField(null=True)),
                ('particular', models.CharField(max_length=255, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('emp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.employeeloan')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.payroll_employee')),
                ('logindetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('holiday_name', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='holiday',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.holiday'),
        ),
        migrations.CreateModel(
            name='LoanDuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(blank=True, null=True)),
                ('duration', models.CharField(choices=[('Months', 'Months'), ('Month', 'Month'), ('Years', 'Years'), ('Year', 'Year')], max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('logindetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('type', models.CharField(choices=[('Sales', 'Sales'), ('Purchase', 'Purchase')], max_length=10, null=True)),
                ('item_rate_type', models.CharField(choices=[('Percentage', 'Percentage'), ('Each Item', 'Each Item')], max_length=15, null=True)),
                ('description', models.TextField(null=True)),
                ('percentage_type', models.CharField(blank=True, choices=[('Markup', 'Markup'), ('Markdown', 'Markdown')], max_length=10, null=True)),
                ('percentage_value', models.IntegerField(blank=True, null=True)),
                ('round_off', models.CharField(choices=[('Never Mind', 'Never Mind'), ('Nearest Whole Number', 'Nearest Whole Number'), ('0.99', '0.99'), ('0.50', '0.50'), ('0.49', '0.49')], max_length=20, null=True)),
                ('currency', models.CharField(choices=[('Indian Rupee', 'Indian Rupee')], max_length=20, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=10)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='price_list_attachment/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='PriceListComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('price_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.pricelist')),
            ],
        ),
        migrations.CreateModel(
            name='PriceListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('custom_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.items')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('price_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.pricelist')),
            ],
        ),
        migrations.CreateModel(
            name='PriceListTransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('action', models.CharField(choices=[('Created', 'Created'), ('Edited', 'Edited')], max_length=10, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('price_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.pricelist')),
            ],
        ),
        migrations.CreateModel(
            name='SalaryDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday', models.IntegerField(blank=True, default=0, null=True)),
                ('salary_date', models.DateField(null=True)),
                ('casual_leave', models.IntegerField(blank=True, default=0, null=True)),
                ('month', models.CharField(max_length=100, null=True)),
                ('year', models.IntegerField(blank=True, default=0, null=True)),
                ('basic_salary', models.IntegerField(blank=True, default=0, null=True)),
                ('conveyance_allowance', models.IntegerField(blank=True, default=0, null=True)),
                ('hra', models.IntegerField(blank=True, default=0, null=True)),
                ('other_allowance', models.IntegerField(blank=True, default=0, null=True)),
                ('total_working_days', models.IntegerField(blank=True, default=0, null=True)),
                ('other_cuttings', models.IntegerField(blank=True, default=0, null=True)),
                ('add_bonus', models.IntegerField(blank=True, default=0, null=True)),
                ('salary', models.FloatField(blank=True, default=0, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(default='Active', max_length=100, null=True)),
                ('DraftorSave', models.CharField(max_length=100, null=True)),
                ('total_amount', models.FloatField(blank=True, default=0, null=True)),
                ('attendance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.attendance')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.payroll_employee')),
            ],
        ),
        migrations.CreateModel(
            name='HistorySalaryDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('action', models.CharField(choices=[('add', 'Add'), ('edit', 'Edit')], default='add', max_length=7)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('salary_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.salarydetails')),
            ],
        ),
        migrations.CreateModel(
            name='CommentSalaryDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.payroll_employee')),
                ('salary_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.salarydetails')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('vendor_display_name', models.CharField(blank=True, max_length=255, null=True)),
                ('vendor_email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(default='', max_length=15)),
                ('phone', models.CharField(default='', max_length=15)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('skype_name_number', models.CharField(blank=True, max_length=255, null=True)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.URLField(blank=True, default='', null=True)),
                ('gst_treatment', models.CharField(blank=True, max_length=255, null=True)),
                ('gst_number', models.CharField(blank=True, max_length=20, null=True)),
                ('pan_number', models.CharField(blank=True, max_length=20, null=True)),
                ('currency', models.CharField(blank=True, max_length=255, null=True)),
                ('opening_balance_type', models.CharField(blank=True, max_length=255, null=True)),
                ('opening_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('current_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('credit_limit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('source_of_supply', models.CharField(blank=True, max_length=255, null=True)),
                ('billing_attention', models.CharField(blank=True, max_length=255, null=True)),
                ('billing_address', models.TextField(blank=True, null=True)),
                ('billing_city', models.CharField(blank=True, max_length=255, null=True)),
                ('billing_state', models.CharField(blank=True, max_length=255, null=True)),
                ('billing_country', models.CharField(blank=True, max_length=255, null=True)),
                ('billing_pin_code', models.CharField(blank=True, max_length=10, null=True)),
                ('billing_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('billing_fax', models.CharField(blank=True, max_length=15, null=True)),
                ('shipping_attention', models.CharField(blank=True, max_length=255, null=True)),
                ('shipping_address', models.TextField(blank=True, null=True)),
                ('shipping_city', models.CharField(blank=True, max_length=255, null=True)),
                ('shipping_state', models.CharField(blank=True, max_length=255, null=True)),
                ('shipping_country', models.CharField(blank=True, max_length=255, null=True)),
                ('shipping_pin_code', models.CharField(blank=True, max_length=10, null=True)),
                ('shipping_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('shipping_fax', models.CharField(blank=True, max_length=15, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('vendor_status', models.CharField(blank=True, max_length=10, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('payment_term', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Company_Staff.company_payment_term')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor_comments_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor_doc_upload_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('document', models.FileField(upload_to='doc/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor_mail_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_from', models.TextField(max_length=300)),
                ('mail_to', models.TextField(max_length=300)),
                ('subject', models.TextField(max_length=250)),
                ('content', models.TextField(max_length=900)),
                ('mail_date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor_remarks_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.CharField(max_length=500)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='VendorContactPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('work_phone', models.CharField(max_length=15)),
                ('mobile', models.CharField(max_length=15)),
                ('skype_name_number', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='VendorHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('action', models.CharField(blank=True, max_length=200, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.vendor')),
            ],
        ),
    ]
