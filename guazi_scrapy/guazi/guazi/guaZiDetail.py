from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class GuaZiDetail(Base):
    __tablename__ = 'guazi_detail'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    # 车主
    carOwner = Column(String(128))
    # 上牌时间
    lastTime = Column(String(128))
    # 行驶路程
    drivingDistance = Column(String(128))
    # 上牌地
    filingAddress = Column(String(128))
    # 变速箱
    transmissionCase = Column(String(128))
    # 排量
    displacement = Column(String(128))
    # 过户次数
    numberOfTransfer = Column(String(128))
    # 看车地址
    carAddress = Column(String(128))
    # 年检日期
    yearlyInspection = Column(String(128))
    # 交强险
    trongInsurances = Column(String(128))
    # 商业险
    commercialInsurance = Column(String(128))

    ############基本配置 ############3
    title = Column(String(128))
    # 证件品牌型号
    standard_type = Column(String(128))
    # 生产商
    standard_producer = Column(String(128))
    # 级别
    standard_grade = Column(String(128))
    # 发动机
    standard_motor = Column(String(128))
    # 变速箱
    standard_gearbox = Column(String(128))
    # 车生结构
    standard_structure = Column(String(128))
    # 长宽高
    standard_volume = Column(String(128))
    # 轴距
    standard_wheelbase = Column(String(128))
    # 行李箱容积
    standard_cargoVolume = Column(String(128))
    # 装备质量
    standard_quality = Column(String(128))

    ########## 发动机参数  ##########

    # 排量
    motor_displacement = Column(String(128))
    # 进气方式
    motor_intakeForm = Column(String(128))
    # 气缸
    motor_cylinder = Column(String(128))
    # 最大马力
    motor_maxPs = Column(String(128))
    # 最大扭矩
    motor_maxNm = Column(String(128))
    # 燃料类型
    motor_fuelType = Column(String(128))
    # 燃油标号
    motor_fuelLabeling = Column(String(128))
    # 供油方式
    motor_oilSupplyMode = Column(String(128))
    # 排放标准
    motor_emissionStandard = Column(String(128))

    ####### 底盘及制动 #########
    # 驱动方式
    chassis_drivingMode = Column(String(128))
    # 助力类型
    chassis_typeOfSupport = Column(String(128))
    # 前悬挂类型
    chassis_frontSuspension = Column(String(128))
    # 后悬挂类型
    chassis_rearSuspension = Column(String(128))
    # 前制动类型
    chassis_frontBrake = Column(String(128))
    # 后制动类型
    chassis_rearBrake = Column(String(128))
    # 驻车制动类型
    chassis_parkingBrakeType = Column(String(128))
    # 前轮胎规格
    chassis_frontTireSpecification = Column(String(128))
    # 后轮胎规格
    chassis_rearTireSpecification = Column(String(128))

    ####################  安全配置   ###################
    # 主副驾驶安全气囊
    security_principalAndAssistant = Column(String(128))
    # 前后排侧气囊
    security_roundSide = Column(String(128))
    # 前后排头部气囊
    security_roundHead = Column(String(128))
    # 胎压检测
    security_tirePressureDetection = Column(String(128))
    # 车内中控锁
    security_internalControlLock = Column(String(128))
    # 儿童座椅接口
    security_childSeat = Column(String(128))
    # 无钥匙启动
    security_keylessStartUp = Column(String(128))
    # 防抱死系统(ABS)
    security_antiLockBrakingSystem = Column(String(128))
    # 车身稳定控制(ESP)
    security_vehicleStabilityControlSystem = Column(String(128))

    ####### 外部配置 ##########

    # 电动天窗
    outer_electricSkylight = Column(String(128))
    # 全景天窗
    outer_panoramicSunroof = Column(String(128))
    # 电动吸合门
    outer_electricallyOperatedSuctionDoor = Column(String(128))
    # 感应后备箱
    outer_speechTrunk = Column(String(128))
    # 感应雨刷
    outer_inductionWiper = Column(String(128))
    # 后雨刷
    outer_rearWiper = Column(String(128))
    # 前后电动车窗
    outer_frontAndRearPowerWindows = Column(String(128))
    # 后视镜电动调节
    outer_electricAdjustmentOfRearviewMirror = Column(String(128))
    # 后视镜加热
    outer_rearviewMirrorHeating = Column(String(128))

    ########## 内部配置   #######
    # 多功能方向盘
    internal_multifunctionalSteeringWheel = Column(String(128))
    # 定速巡航
    internal_cruiseControl = Column(String(128))
    # 空调
    internal_airConditioner = Column(String(128))
    # 自动空调
    internal_automaticAirConditioning = Column(String(128))
    # GPS导航
    internal_gps = Column(String(128))
    # 倒车雷达
    internal_PDCParkingDistanceControl = Column(String(128))
    # 倒车影像系统
    internal_rearCameraParkingAid = Column(String(128))
    # 真皮座椅
    internal_leatherSeat = Column(String(128))
    # 前后排座椅加热
    internal_frontAndRearSeatHeating = Column(String(128))
