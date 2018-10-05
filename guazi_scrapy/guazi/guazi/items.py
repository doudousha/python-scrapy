# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziItem(scrapy.Item):
    # 车主
    carOwner = scrapy.Field()
    # 上牌时间
    lastTime = scrapy.Field()
    # 行驶路程
    drivingDistance = scrapy.Field()
    # 上牌地
    filingAddress = scrapy.Field()
    # 变速箱
    transmissionCase = scrapy.Field()
    # 排量
    displacement = scrapy.Field()
    # 过户次数
    numberOfTransfer = scrapy.Field()
    # 看车地址
    carAddress = scrapy.Field()
    # 年检日期
    yearlyInspection = scrapy.Field()
    # 交强险
    trongInsurances = scrapy.Field()
    # 商业险
    commercialInsurance= scrapy.Field()

    ############基本配置 ############3
    title = scrapy.Field()
    # 证件品牌型号
    standard_type = scrapy.Field()
    # 生产商
    standard_producer = scrapy.Field()
    # 级别
    standard_grade = scrapy.Field()
    # 发动机
    standard_motor = scrapy.Field()
    # 变速箱
    standard_gearbox = scrapy.Field()
    # 车生结构
    standard_structure = scrapy.Field()
    # 长宽高
    standard_volume = scrapy.Field()
    # 轴距
    standard_wheelbase = scrapy.Field()
    # 行李箱容积
    standard_cargoVolume = scrapy.Field()
    # 装备质量
    standard_quality = scrapy.Field()

    ########## 发动机参数  ##########

    # 排量
    motor_displacement = scrapy.Field()
    # 进气方式
    motor_intakeForm = scrapy.Field()
    # 气缸
    motor_cylinder = scrapy.Field()
    # 最大马力
    motor_maxPs = scrapy.Field()
    # 最大扭矩
    motor_maxNm = scrapy.Field()
    # 燃料类型
    motor_fuelType = scrapy.Field()
    # 燃油标号
    motor_fuelLabeling = scrapy.Field()
    # 供油方式
    motor_oilSupplyMode = scrapy.Field()
    # 排放标准
    motor_emissionStandard = scrapy.Field()

    ####### 底盘及制动 #########
    # 驱动方式
    chassis_drivingMode = scrapy.Field()
    # 助力类型
    chassis_typeOfSupport = scrapy.Field()
    # 前悬挂类型
    chassis_frontSuspension = scrapy.Field()
    # 后悬挂类型
    chassis_rearSuspension = scrapy.Field()
    # 前制动类型
    chassis_frontBrake = scrapy.Field()
    # 后制动类型
    chassis_rearBrake = scrapy.Field()
    # 驻车制动类型
    chassis_parkingBrakeType = scrapy.Field()
    # 前轮胎规格
    chassis_frontTireSpecification = scrapy.Field()
    # 后轮胎规格
    chassis_rearTireSpecification = scrapy.Field()

    ####################  安全配置   ###################
    # 主副驾驶安全气囊
    security_principalAndAssistant = scrapy.Field()
    # 前后排侧气囊
    security_roundSide = scrapy.Field()
    # 前后排头部气囊
    security_roundHead = scrapy.Field()
    # 胎压检测
    security_tirePressureDetection = scrapy.Field()
    # 车内中控锁
    security_internalControlLock = scrapy.Field()
    # 儿童座椅接口
    security_childSeat = scrapy.Field()
    # 无钥匙启动
    security_keylessStartUp = scrapy.Field()
    # 防抱死系统(ABS)
    security_antiLockBrakingSystem = scrapy.Field()
    # 车身稳定控制(ESP)
    security_vehicleStabilityControlSystem = scrapy.Field()

    ####### 外部配置 ##########

    # 电动天窗
    outer_electricSkylight = scrapy.Field()
    # 全景天窗
    outer_panoramicSunroof = scrapy.Field()
    # 电动吸合门
    outer_electricallyOperatedSuctionDoor = scrapy.Field()
    # 感应后备箱
    outer_speechTrunk = scrapy.Field()
    # 感应雨刷
    outer_inductionWiper = scrapy.Field()
    # 后雨刷
    outer_rearWiper = scrapy.Field()
    # 前后电动车窗
    outer_frontAndRearPowerWindows = scrapy.Field()
    # 后视镜电动调节
    outer_electricAdjustmentOfRearviewMirror = scrapy.Field()
    # 后视镜加热
    outer_rearviewMirrorHeating = scrapy.Field()

    ########## 内部配置   #######
    # 多功能方向盘
    internal_multifunctionalSteeringWheel = scrapy.Field()
    # 定速巡航
    internal_cruiseControl = scrapy.Field()
    # 空调
    internal_airConditioner = scrapy.Field()
    # 自动空调
    internal_automaticAirConditioning = scrapy.Field()
    # GPS导航
    internal_gps = scrapy.Field()
    # 倒车雷达
    internal_PDCParkingDistanceControl = scrapy.Field()
    # 倒车影像系统
    internal_rearCameraParkingAid = scrapy.Field()
    # 真皮座椅
    internal_leatherSeat = scrapy.Field()
    # 前后排座椅加热
    internal_frontAndRearSeatHeating = scrapy.Field()
