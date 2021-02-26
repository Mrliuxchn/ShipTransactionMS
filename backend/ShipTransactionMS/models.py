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

#伙食费
class Board_wages(models.Model):
    Registration_date #TODO
    ID = models.CharField(max_length=10)
    Ship_name = models.CharField(max_length=32)
    Start_date #TODO
    expiration_date #TODO
    number_of_people = models.CharField(max_length=6) #人数
    standard = models.CharField(max_length=6) #标准
    number_of_day = models.CharField(max_length=6) #天数
    money = models.CharField(max_length=6) #金额
    reference_column = models.CharField(max_length=255) #备注

#采购入库单
class Warehouse_Purchase(models.Model):
    Inbound_date #TODO #入库日期
    warehouse_warrant = models.CharField(max_length=32) #入库单号
    Ship_name = models.CharField(max_length=32) #船名
    department = models.CharField(max_length=32) #部门
    stock_number = models.CharField(max_length=32) #物料编号
    Name_Specifications = models.CharField(max_length=32) #名称及规格
    category = models.CharField(max_length=32) #类别
    unit = models.CharField(max_length=5) #单位
    unit_pricen = models.CharField(max_length=32) #单价
    quantity = models.CharField(max_length=32) #数量
    money = models.CharField(max_length=32) #金额
    supplier = models.CharField(max_length=32) #供应商
    Storage_location = models.CharField(max_length=32) #存放位置

#合同登记
class Contract_registration(models.Model):
    ID = models.CharField(max_length=32) #序号
    ship_name = models.CharField(max_length=32) #船名
    Contract_no = models.CharField(max_length=32) #合同编号
    Party_a = models.CharField(max_length=32) #甲方
    Party_b = models.CharField(max_length=32) #乙方
    Signing_date #TODO #签订日期
    name = models.CharField(max_length=32) #名称
    category = models.CharField(max_length=10) #类别
    main_issues = models.CharField(max_length=255) #主要事宜
    reference_column = models.CharField(max_length=255) #备注
    Storage_location = models.CharField(max_length=32) #存放位置

#航修费用明细
class Details_of_maintenance_charges(models.Model):
    ID = models.CharField(max_length=32) #编号
    Name_Specifications = models.CharField(max_length=32) #名称及规格
    unit = models.CharField(max_length=5) #单位
    unit_pricen = models.CharField(max_length=32) #单价
    quantity = models.CharField(max_length=32) #数量
    money = models.CharField(max_length=32) #金额
    reference_column = models.CharField(max_length=255) #备注

#厂修费用明细
class A(models.Model):
    ID = models.CharField(max_length=32) #编号
    Name_Specifications = models.CharField(max_length=32) #名称及规格
    unit = models.CharField(max_length=5) #单位
    unit_pricen = models.CharField(max_length=32) #单价
    quantity = models.CharField(max_length=32) #数量
    money = models.CharField(max_length=32) #金额
    reference_column = models.CharField(max_length=255) #备注

#备件费用明细
class B(models.Model):
    ID = models.CharField(max_length=32) #编号
    Name_Specifications = models.CharField(max_length=32) #名称及规格
    unit = models.CharField(max_length=5) #单位
    unit_pricen = models.CharField(max_length=32) #单价
    quantity = models.CharField(max_length=32) #数量
    money = models.CharField(max_length=32) #金额
    reference_column = models.CharField(max_length=255) #备注

#物料费用明细
class C(models.Model):
    ID = models.CharField(max_length=32) #编号
    Name_Specifications = models.CharField(max_length=32) #名称及规格
    unit = models.CharField(max_length=5) #单位
    unit_pricen = models.CharField(max_length=32) #单价
    quantity = models.CharField(max_length=32) #数量
    money = models.CharField(max_length=32) #金额
    reference_column = models.CharField(max_length=255) #备注

#工具费用明细
class D(models.Model):
    ID = models.CharField(max_length=32) #编号
    Name_Specifications = models.CharField(max_length=32) #名称及规格
    unit = models.CharField(max_length=5) #单位
    unit_pricen = models.CharField(max_length=32) #单价
    quantity = models.CharField(max_length=32) #数量
    money = models.CharField(max_length=32) #金额
    reference_column = models.CharField(max_length=255) #备注

#润油费用明细
class E(models.Model):
    ID = models.CharField(max_length=32) #编号
    Name_Specifications = models.CharField(max_length=32) #名称及规格
    unit = models.CharField(max_length=5) #单位
    unit_pricen = models.CharField(max_length=32) #单价
    quantity = models.CharField(max_length=32) #数量
    money = models.CharField(max_length=32) #金额
    reference_column = models.CharField(max_length=255) #备注

#氧乙炔（记录氧乙炔的费情况）
class F(models.Model):
    ID = models.CharField(max_length=32) #编号
    registration_day #TODO #登记日期
    ship_name = models.CharField(max_length=32) #船名
    flights = models.CharField(max_length=32) #航次
    money = models.CharField(max_length=32) #金额
    location = models.CharField(max_length=32) #地点
    responsible_person = models.CharField(max_length=10) #经办人
    reimbursement_datem #TODO #报销日期
    reference_column = models.CharField(max_length=255) #备注
    Storage_location = models.CharField(max_length=32) #存放位置

#氧乙炔统计（统计期间段内氧乙炔费用）
class G(models.Model):
    ID = models.CharField(max_length=32) #编号
    registration_day #TODO #登记日期
    ship_name = models.CharField(max_length=32) #船名
    flights = models.CharField(max_length=32) #航次
    money = models.CharField(max_length=32) #金额
    location = models.CharField(max_length=32) #地点
    responsible_person = models.CharField(max_length=10) #经办人
    reimbursement_datem #TODO #报销日期
    reference_column = models.CharField(max_length=255) #备注
    Storage_location = models.CharField(max_length=32) #存放位置
    Start_date #TODO #起始日期
    expiration_date #TODO #截止日期

#劳务费
class Service_fee(models.Model):
    ID = models.CharField(max_length=32) #编号
    ship_name = models.CharField(max_length=32) #船名
    money = models.CharField(max_length=32) #金额
    record_date #TODO #记录日期
    issuing_month = models.CharField(max_length=3) #发放月
    Work_on = models.CharField(max_length=3) #工作月
    category = models.CharField(max_length=10) #类别
    department = models.CharField(max_length=32) #部门
    after_tax = models.CharField(max_length=32) #税后
    reference_column = models.CharField(max_length=255) #备注
    Storage_location = models.CharField(max_length=32) #存放位置

#劳务费统计
class Statistics_of_labor_costs(models.Model):
    ID = models.CharField(max_length=32) #编号
    ship_name = models.CharField(max_length=32) #船名
    money = models.CharField(max_length=32) #金额
    record_date #TODO #记录日期
    issuing_month = models.CharField(max_length=3) #发放月
    Work_on = models.CharField(max_length=3) #工作月
    category = models.CharField(max_length=10) #类别
    department = models.CharField(max_length=32) #部门
    after_tax = models.CharField(max_length=32) #税后
    reference_column = models.CharField(max_length=255) #备注
    Storage_location = models.CharField(max_length=32) #存放位置
    Start_date #TODO #起始日期
    expiration_date #TODO #截止日期

#其他费用
class Other_fees(models.Model):
    ID = models.CharField(max_length=32) #编号
    ship_name = models.CharField(max_length=32) #船名
    name = models.CharField(max_length=32) #名称
    occurrence_time #TODO #发生时间
    money = models.CharField(max_length=32) #金额
    responsible_person = models.CharField(max_length=10) #经办人
    record_date #TODO #记录日期
    reference_column = models.CharField(max_length=255) #备注
    Storage_location = models.CharField(max_length=32) #存放位置

#其他费用统计
class Other_expenses_statistics(models.Model):
    ID = models.CharField(max_length=32) #编号
    ship_name = models.CharField(max_length=32) #船名
    name = models.CharField(max_length=32) #名称
    occurrence_time #TODO #发生时间
    money = models.CharField(max_length=32) #金额
    responsible_person = models.CharField(max_length=10) #经办人
    record_date #TODO #记录日期
    reference_column = models.CharField(max_length=255) #备注
    Storage_location = models.CharField(max_length=32) #存放位置
    Start_date #TODO #起始日期
    expiration_date #TODO #截止日期

#造船费用明细
class Details_of_shipbuilding_costs(models.Model):
    ID = models.CharField(max_length=32) #编号
    Name_Specifications = models.CharField(max_length=32) #名称及规格
    unit = models.CharField(max_length=5) #单位
    unit_pricen = models.CharField(max_length=32) #单价
    quantity = models.CharField(max_length=32) #数量
    money = models.CharField(max_length=32) #金额
    reference_column = models.CharField(max_length=255) #备注

#差旅费
class Travel_expense(models.Model):
    registration_day #TODO #登记日期
    ID = models.CharField(max_length=32) #编号
    business_traveller = models.CharField(max_length=10) #出差人
    department = models.CharField(max_length=32) #部门
    Why_things = models.CharField(max_length=255) #事由
    time = models.CharField(max_length=32) #时间
    total_cost = models.CharField(max_length=32) #总费用
    reference_column = models.CharField(max_length=255) #备注

#事务事件
class The_transaction(models.Model):
    name = models.CharField(max_length=32) #名称
    main_content = models.CharField(max_length=255) #主要内容
    money = models.CharField(max_length=32) #金额
    deadline_date #TODO #限期日期

#事务提醒
class Remind_Transaction(models.Model):
    name = models.CharField(max_length=32) #名称
    main_content = models.CharField(max_length=255) #主要内容
    money = models.CharField(max_length=32) #金额
    deadline_date #TODO #限期日期

#证书有效状态
class H(models.Model):
    ship_name = models.CharField(max_length=32) #船名
    certificate_type = models.CharField(max_length=32) #证书种类
    certificate_validity = models.CharField(max_length=32) #证书有效期
    Next_inspection_content = models.CharField(max_length=255) #下次检验内容
    Date_of_next_survey #TODO #下次检验日期

#证书检验期状态
class I(models.Model):
    ship_name = models.CharField(max_length=32) #船名
    certificate_type = models.CharField(max_length=32) #证书种类
    certificate_validity = models.CharField(max_length=32) #证书有效期
    Next_inspection_content = models.CharField(max_length=255) #下次检验内容
    Date_of_next_survey #TODO #下次检验日期

#证书过期状态
class J(models.Model):
    ship_name = models.CharField(max_length=32) #船名
    certificate_type = models.CharField(max_length=32) #证书种类
    certificate_validity = models.CharField(max_length=32) #证书有效期
    Next_inspection_content = models.CharField(max_length=255) #下次检验内容
    Date_of_next_survey #TODO #下次检验日期

#有效期提前三月提醒
class K(models.Model):
    ship_name = models.CharField(max_length=32) #船名
    certificate_type = models.CharField(max_length=32) #证书种类
    certificate_validity = models.CharField(max_length=32) #证书有效期
    Next_inspection_content = models.CharField(max_length=255) #下次检验内容
    Date_of_next_survey #TODO #下次检验日期

#图纸资料
class L(models.Model):
    registration_day #TODO #登记日期
    ship_name = models.CharField(max_length=32) #船名
    drawing_number = models.CharField(max_length=32) #图纸编号
    Location_number = models.CharField(max_length=32) #位置及编号
    chinese_name = models.chinese_name(max_length=32) #中文名称
    copies_number = models.chinese_name(max_length=32) #复印件数量
    Copy_location_and_number = models.CharField(max_length=32) #复印位置及编号
    english_names = models.CharField(max_length=32) #英文名称
    reference_column = models.CharField(max_length=255) #备注

#图书清单
class book_list(models.Model):
    registration_day #TODO #登记日期
    book_number = models.CharField(max_length=32) #图书编号
    data_name = models.CharField(max_length=32) #资料名称
    category = models.CharField(max_length=32) #类别
    Storage_location = models.CharField(max_length=32) #存放位置
    publisher = models.CharField(max_length=32) #出版单位
    quantity = models.CharField(max_length=32) #数量
    the_price = models.CharField(max_length=32) #价格
    reference_column = models.CharField(max_length=255) #备注

#新船资料清单
class M(models.Model):
    serial_number = models.CharField(max_length=32)
    ship_name = models.CharField(max_length=32) #船名
    number_location = models.CharField(max_length=32) #编号及位置
    name = models.CharField(max_length=32) #名称
    category = models.CharField(max_length=32) #类别
    provenance = models.CharField(max_length=32) #出处
    Signing_date #TODO #签订日期
    #甲乙方
    main_content = models.CharField(max_length=255) #主要内容
    reference_column = models.CharField(max_length=255) #备注



