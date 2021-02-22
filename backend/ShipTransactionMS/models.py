from django.db import models

#员工信息
class Employee_information(models.Model):
    Employee_ID = models.CharField(max_length=6)
    Employee_name = models.CharField(max_length=32)
    Employee_department = models.CharField(max_length=32)
    Employee_phoneNumber = models.CharField(max_length=11)
    Employee_landlineNumber = models.CharField(max_length=11)
    Employee_homeADD = models.CharField(max_length=255)
    Employee_location = models.CharField(max_length=32)

#船盘信息
class Ship_information(models.Model):
    Ship_name = models.CharField(max_length=32)
    Ship_manufacturingDate = models.CharField(max_length=32)
    Ship_manufacturingSite = models.CharField(max_length=255)
    Ship_flag = models.CharField(max_length=32)
    Ship_tier = models.CharField(max_length=32)
    Ship_port = models.CharField(max_length=32)
    Ship_tonnageGross = models.CharField(max_length=8)
    Ship_tonnageNet = models.CharField(max_length=8)
    Ship_size = models.CharField(max_length=32)
    Ship_mainEngineAndPower = models.CharField(max_length=255)
    Ship_location = models.CharField(max_length=255)

