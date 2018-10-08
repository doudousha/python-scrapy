# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models.guaZiDetail import GuaZiDetail


class GuaziPipeline(object):

    def __init__(self):
        print('__init__---------------------------------------------------')
        pass

    # 可选实现，做参数初始化等
    # doing something

    # item (Item 对象) – 被爬取的item
    # spider (Spider 对象) – 爬取该item的spider
    # 这个方法必须实现，每个item pipeline组件都需要调用该方法，
    # 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。
    def process_item(self, item, spider):
        print('process_item---------------------------------------------------')
        guazi = self.convert(item)

        self.session.add(guazi)
        self.session.commit()
        print('process_item success---------------------------------------------------')
        return item

    def open_spider(self, spider):
        engine = create_engine('mysql+pymysql://guazi:Cp54w6wPhmyxF27s@45.78.9.17:3306/guazi')
        Session = sessionmaker(bind=engine)
        self.session = Session()
        pass

    # spider (Spider 对象) – 被开启的spider
    # 可选实现，当spider被开启时，这个方法被调用。

    def close_spider(self, spider):
        self.session.close()
        pass


    def convert(self,item):
        guazi = GuaZiDetail()
        guazi.title = item['title']
        guazi.carOwner = item['carOwner']
        # 上牌时间
        guazi.lastTime = item['lastTime']
        # 行驶路程
        guazi.drivingDistance = item['drivingDistance']
        # 上牌地
        guazi.filingAddress = item['filingAddress']
        # 变速箱
        guazi.transmissionCase = item['transmissionCase']
        # 排量
        guazi.displacement = item['displacement']
        # 过户次数
        guazi.numberOfTransfer = item['numberOfTransfer']
        # 看车地址
        guazi.carAddress = item['carAddress']
        # 年检日期
        guazi.yearlyInspection = item['yearlyInspection']
        # 交强险
        guazi.trongInsurances = item['trongInsurances']
        # 商业险
        guazi.commercialInsurance = item['commercialInsurance']


        # 证件品牌型号
        guazi.standard_type = item['standard_type']
        # 生产商
        guazi.standard_producer = item['standard_producer']
        # 级别
        guazi.standard_grade = item['standard_grade']
        # 发动机
        guazi.standard_motor = item['standard_motor']
        # 变速箱
        guazi.standard_gearbox = item['standard_gearbox']
        # 车身结构
        guazi.standard_structure = item['standard_structure']
        # 长宽高
        guazi.standard_volume = item['standard_volume']
        # 轴距
        guazi.standard_wheelbase = item['standard_wheelbase']
        # 行李箱容积
        guazi.standard_cargoVolume = item['standard_cargoVolume']
        # 装备质量
        guazi.standard_quality = item['standard_quality']

        ######### 发动机参数  ##########

        # 排量
        guazi.motor_displacement = item['motor_displacement']
        # 进气方式
        guazi.motor_intakeForm = item['motor_intakeForm']
        # 气缸
        guazi.motor_cylinder = item['motor_cylinder']
        # 最大马力
        guazi.motor_maxPs = item['motor_maxPs']
        # 最大扭矩
        guazi.motor_maxNm = item['motor_maxNm']
        # 燃料类型
        guazi.motor_fuelType = item['motor_fuelType']
        # 燃油标号
        guazi.motor_fuelLabeling = item['motor_fuelLabeling']
        # 供油方式
        guazi.motor_oilSupplyMode = item['motor_oilSupplyMode']
        # 排放标准
        guazi.motor_emissionStandard = item['motor_emissionStandard']

        ####### 底盘及制动 #########
        # 驱动方式
        guazi.chassis_drivingMode = item['chassis_drivingMode']
        # 助力类型
        guazi.chassis_typeOfSupport = item['chassis_typeOfSupport']
        # 前悬挂类型
        guazi.chassis_frontSuspension = item['chassis_frontSuspension']
        # 后悬挂类型
        guazi.chassis_rearSuspension = item['chassis_rearSuspension']
        # 前制动类型
        guazi.chassis_frontBrake = item['chassis_frontBrake']
        # 后制动类型
        guazi.chassis_rearBrake = item['chassis_rearBrake']
        # 驻车制动类型
        guazi.chassis_parkingBrakeType = item['chassis_parkingBrakeType']
        # 前轮胎规格
        guazi.chassis_frontTireSpecification = item['chassis_frontTireSpecification']
        # 后轮胎规格
        guazi.chassis_rearTireSpecification = item['chassis_rearTireSpecification']

        ####################  安全配置   ###################
        # 主副驾驶安全气囊
        guazi.security_principalAndAssistant = item['security_principalAndAssistant']
        # 前后排侧气囊
        guazi.security_roundSide = item['security_roundSide']
        # 前后排头部气囊
        guazi.security_roundHead = item['security_roundHead']
        # 胎压检测
        guazi.security_tirePressureDetection = item['security_tirePressureDetection']
        # 车内中控锁
        guazi.security_internalControlLock = item['security_internalControlLock']
        # 儿童座椅接口
        guazi.security_childSeat = item['security_childSeat']
        # 无钥匙启动
        guazi.security_keylessStartUp = item['security_keylessStartUp']
        # 防抱死系统(ABS)
        guazi.security_antiLockBrakingSystem = item['security_antiLockBrakingSystem']
        # 车身稳定控制(ESP)
        guazi.security_vehicleStabilityControlSystem = item['security_vehicleStabilityControlSystem']

        ####### 外部配置 ##########

        # 电动天窗
        guazi.outer_electricSkylight = item['outer_electricSkylight']
        # 全景天窗
        guazi.outer_panoramicSunroof = item['outer_panoramicSunroof']
        # 电动吸合门
        guazi.outer_electricallyOperatedSuctionDoor = item['outer_electricallyOperatedSuctionDoor']
        # 感应后备箱
        guazi.outer_speechTrunk = item['outer_speechTrunk']
        # 感应雨刷
        guazi.outer_inductionWiper = item['outer_inductionWiper']
        # 后雨刷
        guazi.outer_rearWiper = item['outer_rearWiper']
        # 前后电动车窗
        guazi.outer_frontAndRearPowerWindows = item['outer_frontAndRearPowerWindows']
        # 后视镜电动调节
        guazi.outer_electricAdjustmentOfRearviewMirror = item['outer_electricAdjustmentOfRearviewMirror']
        # 后视镜加热
        guazi.outer_rearviewMirrorHeating = item['outer_rearviewMirrorHeating']

        ########## 内部配置   #######
        # 多功能方向盘
        guazi.internal_multifunctionalSteeringWheel = item['internal_multifunctionalSteeringWheel']
        # 定速巡航
        guazi.internal_cruiseControl = item['internal_cruiseControl']
        # 空调
        guazi.internal_airConditioner = item['internal_airConditioner']
        # 自动空调
        guazi.internal_automaticAirConditioning = item['internal_automaticAirConditioning']
        # GPS导航
        guazi.internal_gps = item['internal_gps']
        # 倒车雷达
        guazi.internal_PDCParkingDistanceControl = item['internal_PDCParkingDistanceControl']
        # 倒车影像系统
        guazi.internal_rearCameraParkingAid = item['internal_rearCameraParkingAid']
        # 真皮座椅
        guazi.internal_leatherSeat = item['internal_leatherSeat']
        # 前后排座椅加热
        guazi.internal_frontAndRearSeatHeating = item['internal_frontAndRearSeatHeating']
        return guazi