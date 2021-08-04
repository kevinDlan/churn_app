from django.db import models

# Create your models here.
class Clients(models.Model):
    total_ct_chng_q4_q1 = models.FloatField(db_column='Total_Ct_Chng_Q4_Q1', blank=True, null=True)  # Field name made lowercase.
    total_trans_amt = models.IntegerField(db_column='Total_Trans_Amt', blank=True, null=True)  # Field name made lowercase.
    total_revolving_bal = models.IntegerField(db_column='Total_Revolving_Bal', blank=True, null=True)  # Field name made lowercase.
    total_relationship_count = models.IntegerField(db_column='Total_Relationship_Count', blank=True, null=True)  # Field name made lowercase.
    total_amt_chng_q4_q1 = models.FloatField(db_column='Total_Amt_Chng_Q4_Q1', blank=True, null=True)  # Field name made lowercase.
    total_trans_ct = models.IntegerField(db_column='Total_Trans_Ct', blank=True, null=True)  # Field name made lowercase.
    contacts_count_12_mon = models.IntegerField(db_column='Contacts_Count_12_mon', blank=True, null=True)  # Field name made lowercase.
    attrition_flag = models.TextField(db_column='Attrition_Flag', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(unique=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'clients'