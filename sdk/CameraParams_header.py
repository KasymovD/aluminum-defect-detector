# -*- coding: utf-8 -*-
# flags '-c -d -v C:\test_h\CameraParams.xml -o CameraParams_header.py'
from ctypes import *
from .CameraParams_const import *
from .PixelType_header import *

STRING = c_char_p

MV_PointCloudFile_Undefined = 0                  # < \~chinese 未定义的点云格式                  \~english Undefined point cloud format
MV_ACQ_MODE_CONTINUOUS = 2                       # < \~chinese 持续采集模式                      \~english Continuous Mode
MV_ACQ_MODE_MUTLI = 1                            # < \~chinese 多帧模式                          \~english Multi Mode
MV_TRIGGER_MODE_ON = 1                           # < \~chinese 打开                              \~english On
AM_CycleDetect = 6                               # < \~chinese 内部用于AccessMode循环检测         \~english used internally for AccessMode cycle detection
AM_Undefined = 5                                 # < \~chinese 对象未被初始化                     \~english Object is not yet initialized
AM_RW = 4                                        # < \~chinese 读和写                            \~english Read and Write
AM_RO = 3                                        # < \~chinese 只读                              \~english Read Only
AM_WO = 2                                        # < \~chinese 只写                              \~english Write Only
AM_NA = 1                                        # < \~chinese 不可用                            \~english Not available
AM_NI = 0                                        # < \~chinese 没有实现                          \~english Not implemented
MV_Image_Tif = 4                                 # < \~chinese Tif格式                           \~english Tif image file
MV_Image_Png = 3                                 # < \~chinese Png格式                           \~english Png image file
MV_Image_Jpeg = 2                                # < \~chinese Jpeg格式                          \~english Jpeg image file
MV_Image_Bmp = 1                                 # < \~chinese Bmp格式                           \~english Bmp image file
MV_GAIN_MODE_CONTINUOUS = 2                      # < \~chinese 连续                              \~english Gain Mode Continuous 
MV_GAIN_MODE_ONCE = 1                            # < \~chinese 单次                              \~english Gain Mode Once
MV_GrabStrategy_UpcomingImage = 3                # < \~chinese 等待下一帧图像                     \~english Wait for the next image
MV_GrabStrategy_LatestImages = 2                 # < \~chinese 获取列表中最新的图像               \~english Gets the latest image in the list
MV_GrabStrategy_LatestImagesOnly = 1             # < \~chinese 获取列表中最新的一帧图像（同时清除列表中的其余图像）         \~english Gets the most recent image in the list (while clearing the rest of the images in the list)
MV_PointCloudFile_OBJ = 3                        # < \~chinese OBJ点云格式                       \~english The point cloud format named OBJ
MV_PointCloudFile_CSV = 2                        # < \~chinese CSV点云格式                       \~english The point cloud format named CSV
MV_PointCloudFile_PLY = 1                        # < \~chinese PLY点云格式                       \~english The point cloud format named PLY
MV_ACQ_MODE_SINGLE = 0                           # < \~chinese 单帧模式                          \~english Single Mode
MV_TRIGGER_MODE_OFF = 0                          # < \~chinese 关闭                             \~english Off
MV_TRIGGER_SOURCE_SOFTWARE = 7                   # < \~chinese 软触发                           \~english Trigger source software
MV_EXPOSURE_MODE_TIMED = 0                       # < \~chinese 曝光超时模式                      \~english exposure mode timed
MV_FormatType_Undefined = 0                      # < \~chinese 未定义的格式类型                  \~english Undefined format type
MV_GAIN_MODE_OFF = 0                             # < \~chinese 关闭增益模式                     \~english Gain mode off
MV_EXPOSURE_AUTO_MODE_CONTINUOUS = 2             # < \~chinese 自动连续曝光模式                 \~english Exposure auto mode continuous
MV_EXPOSURE_AUTO_MODE_ONCE = 1                   # < \~chinese 单次自动曝光模式                 \~english Exposure auto mode once
MV_EXPOSURE_AUTO_MODE_OFF = 0                    # < \~chinese 关闭自动曝光模式                 \~english Exposure auto mode off
IFT_IValue = 0                                   # < \~chinese IValue接口类型                  \~english IValue interface
MV_GrabStrategy_OneByOne = 0                     # < \~chinese 从旧到新一帧一帧的获取图像        \~english Frame by frame from old to new
MV_FormatType_AVI = 1                            # < \~chinese AVI视频格式                     \~english AVI format type
MV_GAMMA_SELECTOR_USER = 1                       # < \~chinese gamma选择项User                 \~english This enumeration selects the type of gamma to apply
IFT_IString = 6                                  # < \~chinese IString接口类型                 \~english IString interface
MV_BALANCEWHITE_AUTO_OFF = 0                     # < \~chinese 白平衡自动关闭                   \~english Balance white auto off
MV_GAMMA_SELECTOR_SRGB = 2                       # < \~chinese gamma选择项SRGB                 \~english This enumeration selects the type of gamma to apply
IFT_IPort = 11                                   # < \~chinese IPort接口类型                   \~english IPort interface
MV_BALANCEWHITE_AUTO_CONTINUOUS = 1              # < \~chinese 白平衡自动连续                   \~english Balance white auto continuous
IFT_IEnumEntry = 10                              # < \~chinese IEnumEntry接口类型              \~english IEnumEntry interface
IFT_ICategory = 8                                # < \~chinese ICategory接口类型               \~english ICategory interface
IFT_IRegister = 7                                # < \~chinese IRegister接口类型               \~english IRegister interface
MV_Image_Undefined = 0                           # < \~chinese 未定义的图像类型                 \~english Image undefined
IFT_IFloat = 5                                   # < \~chinese IFloat接口类型                  \~english IFloat interface
IFT_IEnumeration = 9                             # < \~chinese IEnumeration接口类型            \~english IEnumeration interface
IFT_ICommand = 4                                 # < \~chinese ICommand接口类型                \~english ICommand interface
IFT_IBoolean = 3                                 # < \~chinese IBoolean接口类型                \~english IBoolean interface
IFT_IInteger = 2                                 # < \~chinese IInteger接口类型                \~english IInteger interface
MV_GIGE_TRANSTYPE_MULTICAST_WITHOUT_RECV = 65537 # < \~chinese 表示组播模式，但本实例不接收图像数据         \~english Multicast without receive data
IFT_IBase = 1                                    # < \~chinese IBase接口类型                             \~english IBase interface
MV_GIGE_TRANSTYPE_UNICAST_WITHOUT_RECV = 65536   # < \~chinese 表示设置了单播，但本实例不接收图像数据       \~english Unicast without receive data
MV_BALANCEWHITE_AUTO_ONCE = 2                    # < \~chinese 单次自动白平衡                             \~english Balance white auto once
MV_GIGE_TRANSTYPE_LIMITEDBROADCAST = 2           # < \~chinese 表示局域网内广播，暂不支持                  \~english Limited broadcast mode,not support
MV_GIGE_TRANSTYPE_MULTICAST = 1                  # < \~chinese 表示组播                                  \~english Multicast mode
MV_GIGE_TRANSTYPE_UNICAST = 0                    # < \~chinese 表示单播(默认)                            \~english Unicast mode(default)
MV_GIGE_TRANSTYPE_CAMERADEFINED = 4              # < \~chinese 表示从相机获取，暂不支持                   \~english Transtype from camera,not support
MV_GIGE_TRANSTYPE_SUBNETBROADCAST = 3            # < \~chinese 表示子网内广播，暂不支持                   \~english Subnet broadcast mode,not support
MV_EXPOSURE_MODE_TRIGGER_WIDTH = 1               # < \~chinese 曝光模式触发宽                            \~english Trigger width
MV_GIGE_TRANSTYPE_UNICAST_DEFINED_PORT = 5       # < \~chinese 表示用户自定义应用端接收图像数据Port号      \~english User Defined Receive Data Port
MV_TRIGGER_SOURCE_FrequencyConverter = 8         # < \~chinese 触发源变频器                              \~english Trigger source frequency converter
MV_TRIGGER_SOURCE_COUNTER0 = 4                   # < \~chinese 触发源计数器                              \~english Trigger source conuter
MV_TRIGGER_SOURCE_LINE3 = 3                      # < \~chinese LINE3 触发源                             \~english Trigger source line3
MV_TRIGGER_SOURCE_LINE2 = 2                      # < \~chinese LINE2 触发源                             \~english Trigger source line2
MV_TRIGGER_SOURCE_LINE1 = 1                      # < \~chinese LINE1 触发源                             \~english Trigger source line1
MV_TRIGGER_SOURCE_LINE0 = 0                      # < \~chinese LINE0 触发源                             \~english Trigger source line0
SortMethod_SerialNumber = 0                      # < \~chinese 按序列号排序                     \~english Sorting by SerialNumber
SortMethod_UserID = 1                            # < \~chinese 按用户自定义名字排序             \~english Sorting by UserID
SortMethod_CurrentIP_ASC = 2                     # < \~chinese 按当前IP地址排序（升序）         \~english Sorting by current IP（Ascending）
SortMethod_CurrentIP_DESC = 3                    # < \~chinese 按当前IP地址排序（降序）         \~english Sorting by current IP（Descending）
MV_IMAGE_ROTATE_90 = 1                           # < \~chinese 旋转90度         \~english Rotate 90 degrees
MV_IMAGE_ROTATE_180 = 2                          # < \~chinese 旋转180度         \~english Rotate 180 degrees
MV_IMAGE_ROTATE_270 = 3                          # < \~chinese 旋转270度         \~english Rotate 270 degrees
MV_FLIP_VERTICAL = 1                             # < \~chinese 垂直翻转          \~english flip vertical
MV_FLIP_HORIZONTAL = 2                           # < \~chinese 水平翻转         \~english flip horizontal
MV_CC_GAMMA_TYPE_NONE = 0                        # < \~chinese 不启用                       \~english Disable
MV_CC_GAMMA_TYPE_VALUE = 1                       # < \~chinese Gamma值                      \~english Gamma value
MV_CC_GAMMA_TYPE_USER_CURVE = 2                  # < \~chinese Gamma曲线                    \~english Gamma curve
MV_CC_GAMMA_TYPE_LRGB2SRGB = 3                   # < \~chinese linear RGB to sRGB           \~english linear RGB to sRGB
MV_CC_GAMMA_TYPE_SRGB2LRGB = 4                   # < \~chinese sRGB to linear RGB(仅色彩插值时支持，色彩校正时无效) \~english sRGB to linear RGB
MV_CC_STREAM_EXCEPTION_ABNORMAL_IMAGE = 0x4001   # < \~chinese 异常的图像，该帧被丢弃            \~english abnormal image,the frame is discarded
MV_CC_STREAM_EXCEPTION_LIST_OVERFLOW = 0x4002    # < \~chinese 缓存列表溢出，清除最旧的一帧       \~english Cache list overflow, clear the oldest frame
MV_CC_STREAM_EXCEPTION_LIST_EMPTY = 0x4003       # < \~chinese 缓存列表为空，该帧被丢弃           \~english Cache list is empty,the frame is discarded
MV_CC_STREAM_EXCEPTION_RECONNECTION = 0x4004    # < \~chinese 断流恢复                         \~english reconnect
MV_CC_STREAM_EXCEPTION_DISCONNECTED = 0x4005    # < \~chinese 断流,恢复失败,取流被中止    \~english reconnect fail, stream is  terminated
MV_CC_STREAM_EXCEPTION_DEVICE = 0x4006          # < \~chinese 设备异常,取流被中止         \~english device exception
MV_SPLIT_BY_LINE = 1                            #< \~chinese 源图像按行拆分成多张图像         \~english Source image split into multiple images by line

int8_t = c_int8
int16_t = c_int16
int32_t = c_int32
int64_t = c_int64
uint8_t = c_uint8
uint16_t = c_uint16
uint32_t = c_uint32
uint64_t = c_uint64
int_least8_t = c_byte
int_least16_t = c_short
int_least32_t = c_int
int_least64_t = c_long
uint_least8_t = c_ubyte
uint_least16_t = c_ushort
uint_least32_t = c_uint
uint_least64_t = c_ulong
int_fast8_t = c_byte
int_fast16_t = c_long
int_fast32_t = c_long
int_fast64_t = c_long
uint_fast8_t = c_ubyte
uint_fast16_t = c_ulong
uint_fast32_t = c_ulong
uint_fast64_t = c_ulong
intptr_t = c_long
uintptr_t = c_ulong
intmax_t = c_long
uintmax_t = c_ulong

# GigE设备信息    \~english GigE device info
class _MV_GIGE_DEVICE_INFO_(Structure):
    pass
_MV_GIGE_DEVICE_INFO_._fields_ = [
    ('nIpCfgOption', c_uint),                     # < \~chinese IP配置选项         \~english Ip config option
    ('nIpCfgCurrent', c_uint),                    # < \~chinese 当前IP地址配置     \~english IP configuration:bit31-static bit30-dhcp bit29-lla
    ('nCurrentIp', c_uint),                       # < \~chinese 当前主机IP地址     \~english Current host Ip 
    ('nCurrentSubNetMask', c_uint),               # < \~chinese 当前子网掩码       \~english curtent subnet mask
    ('nDefultGateWay', c_uint),                   # < \~chinese 默认网关           \~english Default gate way
    ('chManufacturerName', c_ubyte * 32),         # < \~chinese 厂商名称           \~english Manufacturer Name
    ('chModelName', c_ubyte * 32),                # < \~chinese 型号名称           \~english Mode name
    ('chDeviceVersion', c_ubyte * 32),            # < \~chinese 设备固件版本       \~english Device Version
    ('chManufacturerSpecificInfo', c_ubyte * 48), # < \~chinese 厂商特殊信息       \~english Manufacturer Specific Infomation
    ('chSerialNumber', c_ubyte * 16),             # < \~chinese 序列号            \~english serial number
    ('chUserDefinedName', c_ubyte * 16),          # < \~chinese 用户定义名称       \~english User Defined Name
    ('nNetExport', c_uint),                       # < \~chinese 网口Ip地址         \~english NetWork Ip address
    ('nReserved', c_uint * 4),                    # < \~chinese 保留字节           \~english Reserved bytes
]
MV_GIGE_DEVICE_INFO = _MV_GIGE_DEVICE_INFO_

# USB设备信息    \~english USB device info
class _MV_USB3_DEVICE_INFO_(Structure):
    pass
_MV_USB3_DEVICE_INFO_._fields_ = [
    ('CrtlInEndPoint', c_ubyte),                            # < \~chinese 控制输入端点          \~english Control input endpoint
    ('CrtlOutEndPoint', c_ubyte),                           # < \~chinese 控制输出端点          \~english Control output endpoint
    ('StreamEndPoint', c_ubyte),                            # < \~chinese 流端点                \~english Flow endpoint
    ('EventEndPoint', c_ubyte),                             # < \~chinese 事件端点              \~english Event endpoint
    ('idVendor', c_ushort),                                 # < \~chinese 供应商ID号            \~english Vendor ID Number
    ('idProduct', c_ushort),                                # < \~chinese 产品ID号              \~english Device ID Number
    ('nDeviceNumber', c_uint),                              # < \~chinese 设备序列号            \~english Device Serial Number
    ('chDeviceGUID', c_ubyte * INFO_MAX_BUFFER_SIZE),       # < \~chinese 设备GUID号            \~english Device GUID Number
    ('chVendorName', c_ubyte * INFO_MAX_BUFFER_SIZE),       # < \~chinese 供应商名字            \~english Vendor Name
    ('chModelName', c_ubyte * INFO_MAX_BUFFER_SIZE),        # < \~chinese 型号名字              \~english Model Name
    ('chFamilyName', c_ubyte * INFO_MAX_BUFFER_SIZE),       # < \~chinese 家族名字              \~english Family Name
    ('chDeviceVersion', c_ubyte * INFO_MAX_BUFFER_SIZE),    # < \~chinese 设备版本号            \~english Device Version
    ('chManufacturerName', c_ubyte * INFO_MAX_BUFFER_SIZE), # < \~chinese 制造商名字            \~english Manufacturer Name
    ('chSerialNumber', c_ubyte * INFO_MAX_BUFFER_SIZE),     # < \~chinese 序列号                \~english Serial Number
    ('chUserDefinedName', c_ubyte * INFO_MAX_BUFFER_SIZE),  # < \~chinese 用户自定义名字         \~english User Defined Name
    ('nbcdUSB', c_uint),                                    # < \~chinese 支持的USB协议         \~english Support USB Protocol
    ('nDeviceAddress', c_uint),                             # < \~chinese 设备地址              \~english Device Address
    ('nReserved', c_uint * 2),                              # < \~chinese 保留字节              \~english Reserved bytes
]
MV_USB3_DEVICE_INFO = _MV_USB3_DEVICE_INFO_

# CameraLink设备信息    \~english CameraLink device info
class _MV_CamL_DEV_INFO_(Structure):
    pass
_MV_CamL_DEV_INFO_._fields_ = [
    ('chPortID', c_ubyte * INFO_MAX_BUFFER_SIZE),           # < \~chinese 端口号            \~english Port ID         
    ('chModelName', c_ubyte * INFO_MAX_BUFFER_SIZE),        # < \~chinese 设备型号          \~english Model name
    ('chFamilyName', c_ubyte * INFO_MAX_BUFFER_SIZE),       # < \~chinese 家族名字          \~english Family Name
    ('chDeviceVersion', c_ubyte * INFO_MAX_BUFFER_SIZE),    # < \~chinese 设备版本号        \~english Device Version
    ('chManufacturerName', c_ubyte * INFO_MAX_BUFFER_SIZE), # < \~chinese 制造商名字        \~english Manufacturer Name
    ('chSerialNumber', c_ubyte * INFO_MAX_BUFFER_SIZE),     # < \~chinese 序列号            \~english Serial Number
    ('nReserved', c_uint * 38),                             # < \~chinese 保留字节          \~english Reserved bytes
]
MV_CamL_DEV_INFO = _MV_CamL_DEV_INFO_

# 采集卡Camera Link相机信息          \~english Camera Link device information on frame grabber
class _MV_CML_DEVICE_INFO_(Structure):
    pass
_MV_CML_DEVICE_INFO_._fields_ = [
    ('chInterfaceID', c_ubyte * INFO_MAX_BUFFER_SIZE),   # < \~chinese 采集卡ID   \~english Interface ID of Frame Grabber
    ('chVendorName', c_ubyte * INFO_MAX_BUFFER_SIZE),    # < \~chinese 供应商名字       \~english Vendor name
    ('chModelName', c_ubyte * INFO_MAX_BUFFER_SIZE),     # < \~chinese 型号名字         \~english Model name
    ('chManufacturerInfo', c_ubyte * INFO_MAX_BUFFER_SIZE),   # < \~chinese 厂商信息   \~english Manufacturer information
    ('chDeviceVersion', c_ubyte * INFO_MAX_BUFFER_SIZE),    # < \~chinese 相机版本          \~english Device version
    ('chSerialNumber', c_ubyte * INFO_MAX_BUFFER_SIZE),     # < \~chinese 序列号            \~english Serial Number
    ('chUserDefinedName', c_ubyte * INFO_MAX_BUFFER_SIZE),  # < \~chinese 用户自定义名字      \~english User defined name
    ('chDeviceID', c_ubyte * INFO_MAX_BUFFER_SIZE),         # < \~chinese 相机ID            \~english Device ID
    ('nReserved', c_uint * 7),                              # < \~chinese 保留字节           \~english Reserved bytes
]
MV_CML_DEVICE_INFO = _MV_CML_DEVICE_INFO_

# CoaXPress相机信息      \~english CoaXPress device information
class _MV_CXP_DEVICE_INFO_(Structure):
    pass
_MV_CXP_DEVICE_INFO_._fields_ = [
    ('chInterfaceID', c_ubyte * INFO_MAX_BUFFER_SIZE),   # < \~chinese 采集卡ID   \~english Interface ID of Frame Grabber
    ('chVendorName', c_ubyte * INFO_MAX_BUFFER_SIZE),    # < \~chinese 供应商名字       \~english Vendor name
    ('chModelName', c_ubyte * INFO_MAX_BUFFER_SIZE),     # < \~chinese 型号名字         \~english Model name
    ('chManufacturerInfo', c_ubyte * INFO_MAX_BUFFER_SIZE),   # < \~chinese 厂商信息   \~english Manufacturer information
    ('chDeviceVersion', c_ubyte * INFO_MAX_BUFFER_SIZE),    # < \~chinese 相机版本          \~english Device version
    ('chSerialNumber', c_ubyte * INFO_MAX_BUFFER_SIZE),     # < \~chinese 序列号            \~english Serial Number
    ('chUserDefinedName', c_ubyte * INFO_MAX_BUFFER_SIZE),  # < \~chinese 用户自定义名字      \~english User defined name
    ('chDeviceID', c_ubyte * INFO_MAX_BUFFER_SIZE),         # < \~chinese 相机ID            \~english Device ID
    ('nReserved', c_uint * 7),                              # < \~chinese 保留字节           \~english Reserved bytes
]
MV_CXP_DEVICE_INFO = _MV_CXP_DEVICE_INFO_

# XoFLink相机信息      \~english XoFLink device information
class _MV_XOF_DEVICE_INFO_(Structure):
    pass
_MV_XOF_DEVICE_INFO_._fields_ = [
    ('chInterfaceID', c_ubyte * INFO_MAX_BUFFER_SIZE),   # < \~chinese 采集卡ID   \~english Interface ID of Frame Grabber
    ('chVendorName', c_ubyte * INFO_MAX_BUFFER_SIZE),    # < \~chinese 供应商名字       \~english Vendor name
    ('chModelName', c_ubyte * INFO_MAX_BUFFER_SIZE),     # < \~chinese 型号名字         \~english Model name
    ('chManufacturerInfo', c_ubyte * INFO_MAX_BUFFER_SIZE),   # < \~chinese 厂商信息   \~english Manufacturer information
    ('chDeviceVersion', c_ubyte * INFO_MAX_BUFFER_SIZE),    # < \~chinese 相机版本          \~english Device version
    ('chSerialNumber', c_ubyte * INFO_MAX_BUFFER_SIZE),     # < \~chinese 序列号            \~english Serial Number
    ('chUserDefinedName', c_ubyte * INFO_MAX_BUFFER_SIZE),  # < \~chinese 用户自定义名字      \~english User defined name
    ('chDeviceID', c_ubyte * INFO_MAX_BUFFER_SIZE),         # < \~chinese 相机ID            \~english Device ID
    ('nReserved', c_uint * 7),                              # < \~chinese 保留字节           \~english Reserved bytes
]
MV_XOF_DEVICE_INFO = _MV_XOF_DEVICE_INFO_

# CameraParams.h 80
class _MV_CC_DEVICE_INFO_(Structure):
    pass
# 设备信息    \~english Device info
class N19_MV_CC_DEVICE_INFO_3DOT_0E(Union):
    pass
N19_MV_CC_DEVICE_INFO_3DOT_0E._fields_ = [
    ('stGigEInfo', MV_GIGE_DEVICE_INFO),                   # < \~chinese Gige设备信息        \~english Gige device infomation
    ('stUsb3VInfo', MV_USB3_DEVICE_INFO),                  # < \~chinese U3V设备信息         \~english u3V device information
    ('stCamLInfo', MV_CamL_DEV_INFO),                      # < \~chinese CamLink设备信息     \~english CamLink device information
    ('stCMLInfo', MV_CML_DEVICE_INFO),  # < \~chinese 采集卡CameraLink设备信息     \~english CameraLink Device Info On Frame Grabber
    ('stCXPInfo', MV_CXP_DEVICE_INFO),  # < \~chinese 采集卡CoaXPress设备信息     \~english CoaXPress Device Info On Frame Grabber
    ('stXoFInfo', MV_XOF_DEVICE_INFO),  # < \~chinese 采集卡XoF设备信息          \~english XoF Device Info On Frame Grabber
]

_MV_CC_DEVICE_INFO_._fields_ = [
    ('nMajorVer', c_ushort),                              # < \~chinese 规范的主要版本         \~english Major version of the specification.
    ('nMinorVer', c_ushort),                              # < \~chinese 规范的次要版本         \~english Minor version of the specification
    ('nMacAddrHigh', c_uint),                             # < \~chinese MAC地址高位           \~english Mac address high
    ('nMacAddrLow', c_uint),                              # < \~chinese MAC地址低位           \~english Mac address low
    ('nTLayerType', c_uint),                              # < \~chinese 设备传输层协议类型     \~english Device Transport Layer Protocol Type, e.g. MV_GIGE_DEVICE
    ('nDevTypeInfo', c_uint),                             # < \~chinese 设备类型信息         \~english Device Type Info
    ('nReserved', c_uint * 3),                            # < \~chinese 保留字节              \~english Reserved bytes
    ('SpecialInfo', N19_MV_CC_DEVICE_INFO_3DOT_0E),       # < \~chinese 不同设备特有信息       \~english Special information
]
MV_CC_DEVICE_INFO = _MV_CC_DEVICE_INFO_

# 设备信息列表    \~english Device Information List
class _MV_CC_DEVICE_INFO_LIST_(Structure):
    pass
_MV_CC_DEVICE_INFO_LIST_._fields_ = [
    ('nDeviceNum', c_uint),                                          # < \~chinese 在线设备数量         \~english Online Device Number
    ('pDeviceInfo', POINTER(MV_CC_DEVICE_INFO) * MV_MAX_DEVICE_NUM), # < \~chinese 支持最多256个设备    \~english Support up to 256 devices
]
MV_CC_DEVICE_INFO_LIST = _MV_CC_DEVICE_INFO_LIST_

# 通过GenTL枚举到的Interface信息    \~english Interface Information with GenTL
class _MV_GENTL_IF_INFO_(Structure):
    pass
_MV_GENTL_IF_INFO_._fields_ = [
    ('chInterfaceID', c_ubyte * INFO_MAX_BUFFER_SIZE), # < \~chinese GenTL接口ID        \~english Interface ID of GenTL
    ('chTLType', c_ubyte * INFO_MAX_BUFFER_SIZE),      # < \~chinese 传输层类型          \~english Transport Layer type
    ('chDisplayName', c_ubyte * INFO_MAX_BUFFER_SIZE), # < \~chinese 设备显示名称         \~english Display name
    ('nCtiIndex', c_uint),                             # < \~chinese GenTL的cti文件索引   \~english Cti file index of GenTL 
    ('nReserved', c_uint * 8),                         # < \~chinese 保留字节             \~english Reserved bytes
]
MV_GENTL_IF_INFO = _MV_GENTL_IF_INFO_

# 通过GenTL枚举到的设备信息列表    \~english Device Information List with GenTL
class _MV_GENTL_IF_INFO_LIST_(Structure):
    pass
_MV_GENTL_IF_INFO_LIST_._fields_ = [
    ('nInterfaceNum', c_uint),                                    # < \~chinese 在线设备数量         \~english Online Device Number
    ('pIFInfo', POINTER(MV_GENTL_IF_INFO) * MV_MAX_GENTL_IF_NUM), # < \~chinese 支持最多256个设备     \~english Support up to 256 devices
]
MV_GENTL_IF_INFO_LIST = _MV_GENTL_IF_INFO_LIST_

# 通过GenTL枚举到的设备信息    \~english Device Information with GenTL
class _MV_GENTL_DEV_INFO_(Structure):
    pass
_MV_GENTL_DEV_INFO_._fields_ = [
    ('chInterfaceID', c_ubyte * INFO_MAX_BUFFER_SIZE),          # < \~chinese GenTL接口ID         \~english Interface ID of GenTL
    ('chDeviceID', c_ubyte * INFO_MAX_BUFFER_SIZE),             # < \~chinese 设备ID              \~english Device ID
    ('chVendorName', c_ubyte * INFO_MAX_BUFFER_SIZE),           # < \~chinese 供应商名字          \~english Vendor Name
    ('chModelName', c_ubyte * INFO_MAX_BUFFER_SIZE),            # < \~chinese 型号名字            \~english Model name
    ('chTLType', c_ubyte * INFO_MAX_BUFFER_SIZE),               # < \~chinese 传输层类型          \~english Transport Layer type
    ('chDisplayName', c_ubyte * INFO_MAX_BUFFER_SIZE),          # < \~chinese 显示名称           \~english Display name
    ('chUserDefinedName', c_ubyte * INFO_MAX_BUFFER_SIZE),      # < \~chinese 用户自定义名字      \~english User defined name
    ('chSerialNumber', c_ubyte * INFO_MAX_BUFFER_SIZE),         # < \~chinese 序列号             \~english Serial number
    ('chDeviceVersion', c_ubyte * INFO_MAX_BUFFER_SIZE),        # < \~chinese 设备版本号         \~english Device version
    ('nCtiIndex', c_uint),                                      # < \~chinese cti索引            \~english Cti Index
    ('nReserved', c_uint * 8),                                  # < \~chinese 保留字节           \~english Reserved bytes
]
MV_GENTL_DEV_INFO = _MV_GENTL_DEV_INFO_

# 通过GenTL枚举到的设备信息列表    \~english Device Information List with GenTL
class _MV_GENTL_DEV_INFO_LIST_(Structure):
    pass
_MV_GENTL_DEV_INFO_LIST_._fields_ = [
    ('nDeviceNum', c_uint),                                             # < \~chinese 在线设备数量         \~english Online Device Number
    ('pDeviceInfo', POINTER(MV_GENTL_DEV_INFO) * MV_MAX_GENTL_DEV_NUM), # < \~chinese GenTL设备信息       \~english device infomation of GenTL device
]
MV_GENTL_DEV_INFO_LIST = _MV_GENTL_DEV_INFO_LIST_

# Chunk内容    \~english The content of ChunkData
class _MV_CHUNK_DATA_CONTENT_(Structure):
    pass
_MV_CHUNK_DATA_CONTENT_._fields_ = [
    ('pChunkData', POINTER(c_ubyte)),  # < \~chinese 块数据             \~english Chunk data
    ('nChunkID', c_uint),              # < \~chinese 块数据ID           \~english Chunk id
    ('nChunkLen', c_uint),             # < \~chinese 块数据长度         \~english Chunk len
    ('nReserved', c_uint * 8),         # < \~chinese 保留字节           \~english Reserved bytes
]
MV_CHUNK_DATA_CONTENT = _MV_CHUNK_DATA_CONTENT_

# 输出帧的信息    \~english Output Frame Information
class _MV_FRAME_OUT_INFO_EX_(Structure):
    pass
# values for enumeration 'MvGvspPixelType'
MvGvspPixelType = c_int # enum

class N22_MV_FRAME_OUT_INFO_EX_3DOT_1E(Union):
    pass
N22_MV_FRAME_OUT_INFO_EX_3DOT_1E._fields_ = [
    ('pUnparsedChunkContent', POINTER(MV_CHUNK_DATA_CONTENT)), # < \~chinese Chunk内容         \~english Chunk Content
    ('nAligning', int64_t),                                    # < \~chinese 校准字段          \~english Aligning
]
_MV_FRAME_OUT_INFO_EX_._fields_ = [
    ('nWidth', c_ushort),
    # < \~chinese 图像宽(最大65535，超出请用nExtendWidth)    \~english Image Width (over 65535, use nExtendWidth)
    ('nHeight', c_ushort),
    # < \~chinese 图像高(最大65535，超出请用nExtendHeight)   \~english Image Height(over 65535, use nExtendHeight)
    ('enPixelType', MvGvspPixelType),                        # < \~chinese 像素格式           \~english Pixel Type
    ('nFrameNum', c_uint),                                   # < \~chinese 帧号               \~english Frame Number
    ('nDevTimeStampHigh', c_uint),                           # < \~chinese 时间戳高32位       \~english Timestamp high 32 bits
    ('nDevTimeStampLow', c_uint),                            # < \~chinese 时间戳低32位       \~english Timestamp low 32 bits
    ('nReserved0', c_uint),                                  # < \~chinese 保留，8字节对齐     \~english Reserved, 8-byte aligned
    ('nHostTimeStamp', int64_t),                             # < \~chinese 主机生成的时间戳    \~english Host-generated timestamp
    ('nFrameLen', c_uint),                                   # < \~chinese 帧的长度           \~english Frame length
    # < \~chinese 以下为chunk新增水印信息 \~english The followings are chunk add frame-specific information
    # < \~chinese 设备水印时标 \~english Device frame-specific time scale
    ('nSecondCount', c_uint),                                # < \~chinese 秒数               \~english The Seconds                         
    ('nCycleCount', c_uint),                                 # < \~chinese 周期数             \~english The Count of Cycle                
    ('nCycleOffset', c_uint),                                # < \~chinese 周期偏移量         \~english The Offset of Cycle                  
    ('fGain', c_float),                                      # < \~chinese 增益               \~english Gain
    ('fExposureTime', c_float),                              # < \~chinese 曝光时间           \~english Exposure Time
    ('nAverageBrightness', c_uint),                          # < \~chinese 平均亮度           \~english Average brightness
    # < \~chinese:白平衡相关 \~english White balance
    ('nRed', c_uint),                                        # < \~chinese 红色               \~english Red     
    ('nGreen', c_uint),                                      # < \~chinese 绿色               \~english Green
    ('nBlue', c_uint),                                       # < \~chinese 蓝色               \~english Blue
    ('nFrameCounter', c_uint),                               # < \~chinese 帧计数             \~english Frame counter
    ('nTriggerIndex', c_uint),                               # < \~chinese 触发计数           \~english Trigger index
    # < \~chinese  输入/输出 \~english Line Input/Output
    ('nInput', c_uint),                                      # < \~chinese 输入               \~english input
    ('nOutput', c_uint),                                     # < \~chinese 输出               \~english output
    # < \~chinese ROI区域 \~english ROI Region                       
    ('nOffsetX', c_ushort),                                  # < \~chinese 水平偏移量             \~english OffsetX   
    ('nOffsetY', c_ushort),                                  # < \~chinese 垂直偏移量             \~english OffsetY
    ('nChunkWidth', c_ushort),                               # < \~chinese chunk 宽              \~english The Width of Chunk
    ('nChunkHeight', c_ushort),                              # < \~chinese chunk 高               \~english The Height of Chunk
    ('nLostPacket', c_uint),                                 # < \~chinese 本帧丢包数            \~english Lost Pacekt Number In This Frame
    ('nUnparsedChunkNum', c_uint),                           # < \~chinese 未解析的Chunkdata个数 \~english Unparsed chunk number
    ('UnparsedChunkList', N22_MV_FRAME_OUT_INFO_EX_3DOT_1E), # < \~chinese 数据库链表            \~english Unparsed chunk list
    ('nExtendWidth', c_uint),                                # < \~chinese 图像宽(扩展变量)       \~english Image Width
    ('nExtendHeight', c_uint),                               # < \~chinese 图像高(扩展变量)       \~english Image Height
    ('nReserved', c_uint * 34),                              # < \~chinese 保留字节            \~english Reserved bytes
]
MV_FRAME_OUT_INFO_EX = _MV_FRAME_OUT_INFO_EX_

# \~chinese 显示帧信息   \~english Display frame information
class _MV_DISPLAY_FRAME_INFO_EX_(Structure):
    pass
_MV_DISPLAY_FRAME_INFO_EX_._fields_ = [
    ('nWidth', c_uint),                # < \~chinese 图像宽    \~english Image Width
    ('nHeight', c_uint),               # < \~chinese 图像高    \~english Image Height
    ('enPixelType', MvGvspPixelType),  # < \~chinese 像素格式            \~english Pixel Type
    ('pImageBuf', POINTER(c_ubyte)),   # < \~chinese 输入图像缓存         \~english Input image buffer
    ('nImageBufLen', c_uint),          # < \~chinese 输入图像长度         \~english Input image length
    ('enRenderMode', c_uint),          # < \~chinese 图像渲染方式 0-GDI(默认), 1-D3D, 2-OPENGL \~english Render mode 0-GDI(default), 1-D3D, 2-OPENGL
    ('nRes', c_uint * 3),              # < \~chinese 保留字节            \~english Reserved bytes
]
MV_DISPLAY_FRAME_INFO_EX = _MV_DISPLAY_FRAME_INFO_EX_

# 图像结构体，输出图像指针地址及图像信息    \~english Image Struct, output the pointer of Image and the information of the specific image
class _MV_FRAME_OUT_(Structure):
    pass
_MV_FRAME_OUT_._fields_ = [
    ('pBufAddr', POINTER(c_ubyte)),         # < \~chinese 图像指针地址         \~english pointer of image
    ('stFrameInfo', MV_FRAME_OUT_INFO_EX),  # < \~chinese 图像信息            \~english information of the specific image
    ('nRes', c_uint * 16),                  # < \~chinese 保留字节            \~english Reserved bytes
]
MV_FRAME_OUT = _MV_FRAME_OUT_

# values for enumeration '_MV_GRAB_STRATEGY_'
_MV_GRAB_STRATEGY_ = c_int # enum       
MV_GRAB_STRATEGY = _MV_GRAB_STRATEGY_   

# 网络传输的相关信息    \~english Network transmission information
class _MV_NETTRANS_INFO_(Structure):
    pass
_MV_NETTRANS_INFO_._fields_ = [
    ('nReceiveDataSize', int64_t),          # < \~chinese 已接收数据大小  [统计StartGrabbing和StopGrabbing之间的数据量]         \~english Received Data Size  [Calculate the Data Size between StartGrabbing and StopGrabbing]  
    ('nThrowFrameCount', c_int),            # < \~chinese 丢帧数量             \~english Throw frame number
    ('nNetRecvFrameCount', c_uint),         # < \~chinese 收到帧计数           \~english Receive Frame count
    ('nRequestResendPacketCount', int64_t), # < \~chinese 请求重发包数         \~english Request Resend Packet Count
    ('nResendPacketCount', int64_t),        # < \~chinese 重发包数            \~english Resend Packet Count
]
MV_NETTRANS_INFO = _MV_NETTRANS_INFO_

# 全匹配的一种信息结构体    \~english A fully matched information structure
class _MV_ALL_MATCH_INFO_(Structure):
    pass
_MV_ALL_MATCH_INFO_._fields_ = [
    ('nType', c_uint),              # < \~chinese 需要输出的信息类型                  \~english Information type need to output
    ('pInfo', c_void_p),            # < \~chinese 输出的信息缓存，由调用者分配         \~englishOutput information cache, which is allocated by the caller
    ('nInfoSize', c_uint),          # < \~chinese 信息缓存的大小                      \~english Information cache size
]
MV_ALL_MATCH_INFO = _MV_ALL_MATCH_INFO_

# 网络流量和丢包信息反馈结构体，对应类型为 MV_MATCH_TYPE_NET_DETECT    \~english Network traffic and packet loss feedback structure, the corresponding type is MV_MATCH_TYPE_NET_DETECT
class _MV_MATCH_INFO_NET_DETECT_(Structure):
    pass
_MV_MATCH_INFO_NET_DETECT_._fields_ = [
    ('nReceiveDataSize', int64_t),          # < \~chinese 已接收数据大小      \~english Received data size
    ('nLostPacketCount', int64_t),          # < \~chinese 丢失的包数量        \~english Number of packets lost
    ('nLostFrameCount', c_uint),            # < \~chinese 丢帧数量           \~english Number of frames lost
    ('nNetRecvFrameCount', c_uint),         # < \~chinese 收到帧计数           \~english Receive Frame count
    ('nRequestResendPacketCount', int64_t), # < \~chinese 请求重发包数         \~english Request Resend Packet Count
    ('nResendPacketCount', int64_t),        # < \~chinese 重发包数            \~english Resend Packet Count
]
MV_MATCH_INFO_NET_DETECT = _MV_MATCH_INFO_NET_DETECT_

# \~chinese host收到从u3v设备端的总字节数，对应类型为 MV_MATCH_TYPE_USB_DETECT    \~english The total number of bytes host received from the u3v device side, the corresponding type is MV_MATCH_TYPE_USB_DETECT
class _MV_MATCH_INFO_USB_DETECT_(Structure):
    pass
_MV_MATCH_INFO_USB_DETECT_._fields_ = [
    ('nReceiveDataSize', int64_t),   # < \~chinese 已接收数据大小      \~english Received data size
    ('nReceivedFrameCount', c_uint), # < \~chinese 已收到的帧数        \~english Number of frames received
    ('nErrorFrameCount', c_uint),    # < \~chinese 错误帧数            \~english Number of error frames
    ('nReserved', c_uint * 2),       # < \~chinese 保留字节            \~english Reserved bytes
]
MV_MATCH_INFO_USB_DETECT = _MV_MATCH_INFO_USB_DETECT_

# \~chinese 显示帧信息   \~english Display frame information
class _MV_DISPLAY_FRAME_INFO_(Structure):
    pass
_MV_DISPLAY_FRAME_INFO_._fields_ = [
    ('hWnd', c_void_p),               # < \~chinese 窗口句柄           \~english Windows handle
    ('pData', POINTER(c_ubyte)),      # < \~chinese 显示的数据         \~english Data Buffer
    ('nDataLen', c_uint),             # < \~chinese 数据长度           \~english Data Size
    ('nWidth', c_ushort),             # < \~chinese 图像宽             \~english Width
    ('nHeight', c_ushort),            # < \~chinese 图像高             \~english Height
    ('enPixelType', MvGvspPixelType), # < \~chinese 像素格式           \~english Pixel format
    ('enRenderMode', c_uint),         # < \~chinese 图像渲染方式 0-GDI(默认), 1-D3D, 2-OPENGL \~english Render mode 0-GDI(default), 1-D3D, 2-OPENGL
    ('nRes', c_uint * 3),             # < \~chinese 保留字节           \~english Reserved bytes
]
MV_DISPLAY_FRAME_INFO = _MV_DISPLAY_FRAME_INFO_

# values for enumeration 'MV_SAVE_POINT_CLOUD_FILE_TYPE'
MV_SAVE_POINT_CLOUD_FILE_TYPE = c_int # enum

# \~chinese 保存3D数据到缓存    \~english Save 3D data to buffer
class _MV_SAVE_POINT_CLOUD_PARAM_(Structure):
    pass
_MV_SAVE_POINT_CLOUD_PARAM_._fields_ = [
    ('nLinePntNum', c_uint),                                 # < \~chinese 每一行点的数量，即图像宽                                             \~english The number of points in each row,which is the width of the image
    ('nLineNum', c_uint),                                    # < \~chinese 行数，即图像高                                                       \~english The number of rows,which is the height of the image
    ('enSrcPixelType', MvGvspPixelType),                     # < \~chinese 输入数据的像素格式                                                    \~english The pixel format of the input data
    ('pSrcData', POINTER(c_ubyte)),                          # < \~chinese 输入数据缓存                                                          \~english Input data buffer
    ('nSrcDataLen', c_uint),                                 # < \~chinese 输入数据大小                                                           \~english Input data size
    ('pDstBuf', POINTER(c_ubyte)),                           # < \~chinese 输出像素数据缓存                                                        \~english Output pixel data buffer
    ('nDstBufSize', c_uint),                                 # < \~chinese 提供的输出缓冲区大小(nLinePntNum * nLineNum * (16*3 + 4) + 2048)         \~english Output buffer size provided (nLinePntNum * nLineNum * (16*3 + 4) + 2048) 
    ('nDstBufLen', c_uint),                                  # < \~chinese 输出像素数据缓存长度                                                     \~english Output pixel data buffer size
    ('enPointCloudFileType', MV_SAVE_POINT_CLOUD_FILE_TYPE), # < \~chinese 提供输出的点云文件类型                                                    \~english Output point data file type provided
    ('nReserved', c_uint * 8),                               # < \~chinese 保留字节                                                                 \~english Reserved bytes
]
MV_SAVE_POINT_CLOUD_PARAM = _MV_SAVE_POINT_CLOUD_PARAM_

# values for enumeration 'MV_SAVE_IAMGE_TYPE'
MV_SAVE_IAMGE_TYPE = c_int # enum

# \~chinese 图片保存参数    \~english Save Image Parameters
class _MV_SAVE_IMAGE_PARAM_T_EX_(Structure):
    pass
_MV_SAVE_IMAGE_PARAM_T_EX_._fields_ = [
    ('pData', POINTER(c_ubyte)),                            # < \~chinese 输入数据缓存         \~english Input Data Buffer
    ('nDataLen', c_uint),                                   # < \~chinese 输入数据大小         \~english Input Data Size
    ('enPixelType', MvGvspPixelType),                       # < \~chinese 输入数据的像素格式         \~english Input Data Pixel Format
    ('nWidth', c_ushort),                                   # < \~chinese 图像宽         \~english Image Width
    ('nHeight', c_ushort),                                  # < \~chinese 图像高         \~english Image Height
    ('pImageBuffer', POINTER(c_ubyte)),                     # < \~chinese 输出图片缓存         \~english Output Image Buffer
    ('nImageLen', c_uint),                                  # < \~chinese 输出图片大小         \~english Output Image Size
    ('nBufferSize', c_uint),                                # < \~chinese 提供的输出缓冲区大小         \~english Output buffer size provided
    ('enImageType', MV_SAVE_IAMGE_TYPE),                    # < \~chinese 输出图片格式         \~english Output Image Format
    ('nJpgQuality', c_uint),                                # < \~chinese 编码质量, (50-99]         \~english Encoding quality, (50-99]
    # < \~chinese     ch:Bayer格式转为RGB24的插值方法 0-快速 1-均衡 2-最优 3-最优+
    # < \~english   en:Interpolation method of convert Bayer to RGB24  0-Fast 1-Equilibrium 2-Optimal 3-Optimal plus
    ('iMethodValue', c_uint),
    ('nReserved', c_uint * 3),                              # < \~chinese 保留字节           \~english Reserved bytes
]
MV_SAVE_IMAGE_PARAM_EX = _MV_SAVE_IMAGE_PARAM_T_EX_

class _MV_SAVE_IMAGE_PARAM_EX3_(Structure):
    pass
_MV_SAVE_IMAGE_PARAM_EX3_._fields_ = [
    ('pData', POINTER(c_ubyte)),                            # < \~chinese 输入数据缓存         \~english Input Data Buffer
    ('nDataLen', c_uint),                                   # < \~chinese 输入数据大小         \~english Input Data Size
    ('enPixelType', MvGvspPixelType),                       # < \~chinese 输入数据的像素格式         \~english Input Data Pixel Format
    ('nWidth', c_uint),                                   # < \~chinese 图像宽         \~english Image Width
    ('nHeight', c_uint),                                  # < \~chinese 图像高         \~english Image Height
    ('pImageBuffer', POINTER(c_ubyte)),                     # < \~chinese 输出图片缓存         \~english Output Image Buffer
    ('nImageLen', c_uint),                                  # < \~chinese 输出图片大小         \~english Output Image Size
    ('nBufferSize', c_uint),                                # < \~chinese 提供的输出缓冲区大小         \~english Output buffer size provided
    ('enImageType', MV_SAVE_IAMGE_TYPE),                    # < \~chinese 输出图片格式         \~english Output Image Format
    ('nJpgQuality', c_uint),                                # < \~chinese 编码质量, (50-99]         \~english Encoding quality, (50-99]
    # < \~chinese     ch:Bayer格式转为RGB24的插值方法 0-快速 1-均衡 2-最优 3-最优+
    # < \~english   en:Interpolation method of convert Bayer to RGB24  0-Fast 1-Equilibrium 2-Optimal 3-Optimal plus
    ('iMethodValue', c_uint),
    ('nReserved', c_uint * 3),                              # < \~chinese 保留字节           \~english Reserved bytes
]
MV_SAVE_IMAGE_PARAM_EX3 = _MV_SAVE_IMAGE_PARAM_EX3_

# \~chinese 保存BMP、JPEG、PNG、TIFF图片文件的参数    \~english Save BMP、JPEG、PNG、TIFF image file parameters
class _MV_SAVE_IMG_TO_FILE_PARAM_(Structure):
    pass
_MV_SAVE_IMG_TO_FILE_PARAM_._fields_ = [
    ('enPixelType', MvGvspPixelType),    # < \~chinese 输入数据的像素格式                    \~english The pixel format of the input data
    ('pData', POINTER(c_ubyte)),         # < \~chinese 输入数据缓存                          \~english Input Data Buffer
    ('nDataLen', c_uint),                # < \~chinese 输入数据大小                           \~english Input Data Size
    ('nWidth', c_ushort),                # < \~chinese 图像宽                                  \~english Image Width
    ('nHeight', c_ushort),               # < \~chinese 图像高                                   \~english Image Height
    ('enImageType', MV_SAVE_IAMGE_TYPE), # < \~chinese 输入图片格式                               \~english Input Image Format
    ('nQuality', c_uint),                # < \~chinese JPG编码质量(50-99]         \~english JPG Encoding quality(50-99]
    ('pImagePath', c_char * 256),        # < \~chinese 输入文件路径         \~english Input file path
    # < \~chinese     ch:Bayer格式转为RGB24的插值方法 0-快速 1-均衡 2-最优 3-最优+
    # < \~english   en:Interpolation method of convert Bayer to RGB24  0-Fast 1-Equilibrium 2-Optimal 3-Optimal plus
    ('iMethodValue', c_int),             
    ('nReserved', c_uint * 8),           # < \~chinese 保留字节           \~english Reserved bytes
]
MV_SAVE_IMG_TO_FILE_PARAM = _MV_SAVE_IMG_TO_FILE_PARAM_

class _MV_SAVE_IMAGE_TO_FILE_PARAM_EX_(Structure):
    pass
_MV_SAVE_IMAGE_TO_FILE_PARAM_EX_._fields_ = [
    ('nWidth', c_uint),  # < \~chinese 图像宽                                  \~english Image Width
    ('nHeight', c_uint),  # < \~chinese 图像高                                 \~english Image Height
    # < \~chinese 输入数据的像素格式                    \~english The pixel format of the input data
    ('enPixelType', MvGvspPixelType),
    ('pData', POINTER(c_ubyte)),  # < \~chinese 输入数据缓存                          \~english Input Data Buffer
    ('nDataLen', c_uint),  # < \~chinese 输入数据大小                           \~english Input Data Size
    # < \~chinese 输入图片格式                               \~english Input Image Format
    ('enImageType', MV_SAVE_IAMGE_TYPE),
    ('pcImagePath', POINTER(c_char)),  # < \~chinese 输入文件路径         \~english Input file path
    ('nQuality', c_uint),      # < \~chinese JPG编码质量(50-99]，其他格式无效    \~english JPG Encoding quality(50-99]
    # < \~chinese     ch:Bayer格式转为RGB24的插值方法 0-快速 1-均衡 2-最优 3-最优+
    # < \~english   en:Interpolation method of convert Bayer to RGB24  0-Fast 1-Equilibrium 2-Optimal 3-Optimal plus
    ('iMethodValue', c_int),
    ('nReserved', c_uint * 8),  # < \~chinese 保留字节           \~english Reserved bytes
]
MV_SAVE_IMAGE_TO_FILE_PARAM_EX = _MV_SAVE_IMAGE_TO_FILE_PARAM_EX_

# \~chinese 图像转换结构体    \~english Pixel convert structure
class _MV_CC_PIXEL_CONVERT_PARAM_T_(Structure):
    pass
_MV_CC_PIXEL_CONVERT_PARAM_T_._fields_ = [
    ('nWidth', c_ushort),                # < \~chinese 图像宽             \~english Image Width
    ('nHeight', c_ushort),               # < \~chinese 图像高              \~english Image Height
    ('enSrcPixelType', MvGvspPixelType), # < \~chinese 源像素格式            \~english Source pixel format
    ('pSrcData', POINTER(c_ubyte)),      # < \~chinese 输入数据缓存           \~english Input data buffer
    ('nSrcDataLen', c_uint),             # < \~chinese 输入数据大小            \~english Input data size
    ('enDstPixelType', MvGvspPixelType), # < \~chinese 目标像素格式             \~english Destination pixel format
    ('pDstBuffer', POINTER(c_ubyte)),    # < \~chinese 输出数据缓存              \~english Output data buffer
    ('nDstLen', c_uint),                 # < \~chinese 输出数据大小               \~english Output data size
    ('nDstBufferSize', c_uint),          # < \~chinese 提供的输出缓冲区大小         \~english Provided outbut buffer size
    ('nRes', c_uint * 4),                # < \~chinese 保留字节                     \~english Reserved bytes
]
MV_CC_PIXEL_CONVERT_PARAM = _MV_CC_PIXEL_CONVERT_PARAM_T_

class _MV_PIXEL_CONVERT_PARAM_EX_T_(Structure):
    pass
_MV_PIXEL_CONVERT_PARAM_EX_T_._fields_ = [
    ('nWidth', c_uint),                # < \~chinese 图像宽             \~english Image Width
    ('nHeight', c_uint),               # < \~chinese 图像高              \~english Image Height
    ('enSrcPixelType', MvGvspPixelType), # < \~chinese 源像素格式            \~english Source pixel format
    ('pSrcData', POINTER(c_ubyte)),      # < \~chinese 输入数据缓存           \~english Input data buffer
    ('nSrcDataLen', c_uint),             # < \~chinese 输入数据大小            \~english Input data size
    ('enDstPixelType', MvGvspPixelType), # < \~chinese 目标像素格式             \~english Destination pixel format
    ('pDstBuffer', POINTER(c_ubyte)),    # < \~chinese 输出数据缓存              \~english Output data buffer
    ('nDstLen', c_uint),                 # < \~chinese 输出数据大小               \~english Output data size
    ('nDstBufferSize', c_uint),          # < \~chinese 提供的输出缓冲区大小         \~english Provided outbut buffer size
    ('nRes', c_uint * 4),                # < \~chinese 保留字节                     \~english Reserved bytes
]
MV_CC_PIXEL_CONVERT_PARAM_EX = _MV_PIXEL_CONVERT_PARAM_EX_T_

# values for enumeration '_MV_RECORD_FORMAT_TYPE_'
_MV_RECORD_FORMAT_TYPE_ = c_int # enum
MV_RECORD_FORMAT_TYPE = _MV_RECORD_FORMAT_TYPE_

# \~chinese 录像参数    \~english Record Parameters
class _MV_CC_RECORD_PARAM_T_(Structure):
    pass
_MV_CC_RECORD_PARAM_T_._fields_ = [
    ('enPixelType', MvGvspPixelType),           # < \~chinese 输入数据的像素格式                                \~english Ip config option
    ('nWidth', c_ushort),                       # < \~chinese 图像宽(指定目标参数时需为2的倍数)                   \~english Ip config option
    ('nHeight', c_ushort),                      # < \~chinese 图像高(指定目标参数时需为2的倍数)                    \~english Ip config option
    ('fFrameRate', c_float),                    # < \~chinese 帧率fps(1/16-120)                                  \~english Ip config option
    ('nBitRate', c_uint),                       # < \~chinese 码率kbps(128kbps-16Mbps)                            \~english Ip config option
    ('enRecordFmtType', MV_RECORD_FORMAT_TYPE), # < \~chinese 录像格式                                              \~english Ip config option
    ('strFilePath', STRING),                    # < \~chinese 录像文件存放路径(如果路径中存在中文，需转成utf-8)         \~english Video file storage path (if there is Chinese in the path, it needs to be converted to utf-8)
    ('nRes', c_uint * 8),                       # < \~chinese 保留字节                                                \~english Reserved bytes
]
MV_CC_RECORD_PARAM = _MV_CC_RECORD_PARAM_T_

# \~chinese 录像数据    \~english Record Data
class _MV_CC_INPUT_FRAME_INFO_T_(Structure):
    pass
_MV_CC_INPUT_FRAME_INFO_T_._fields_ = [
    ('pData', POINTER(c_ubyte)),  # < \~chinese 图像数据指针         \~english Input Data Buffer
    ('nDataLen', c_uint),         # < \~chinese  输入数据大小         \~english Input Data Size
    ('nRes', c_uint * 8),         # < \~chinese 保留字节               \~english Reserved bytes
]
MV_CC_INPUT_FRAME_INFO = _MV_CC_INPUT_FRAME_INFO_T_

# values for enumeration '_MV_CAM_ACQUISITION_MODE_'
_MV_CAM_ACQUISITION_MODE_ = c_int # enum
MV_CAM_ACQUISITION_MODE = _MV_CAM_ACQUISITION_MODE_

# values for enumeration '_MV_CAM_GAIN_MODE_'
_MV_CAM_GAIN_MODE_ = c_int # enum
MV_CAM_GAIN_MODE = _MV_CAM_GAIN_MODE_

# values for enumeration '_MV_CAM_EXPOSURE_MODE_'
_MV_CAM_EXPOSURE_MODE_ = c_int # enum
MV_CAM_EXPOSURE_MODE = _MV_CAM_EXPOSURE_MODE_

# values for enumeration '_MV_CAM_EXPOSURE_AUTO_MODE_'
_MV_CAM_EXPOSURE_AUTO_MODE_ = c_int # enum
MV_CAM_EXPOSURE_AUTO_MODE = _MV_CAM_EXPOSURE_AUTO_MODE_

# values for enumeration '_MV_CAM_TRIGGER_MODE_'
_MV_CAM_TRIGGER_MODE_ = c_int # enum
MV_CAM_TRIGGER_MODE = _MV_CAM_TRIGGER_MODE_

# values for enumeration '_MV_CAM_GAMMA_SELECTOR_'
_MV_CAM_GAMMA_SELECTOR_ = c_int # enum
MV_CAM_GAMMA_SELECTOR = _MV_CAM_GAMMA_SELECTOR_

# values for enumeration '_MV_CAM_BALANCEWHITE_AUTO_'
_MV_CAM_BALANCEWHITE_AUTO_ = c_int # enum
MV_CAM_BALANCEWHITE_AUTO = _MV_CAM_BALANCEWHITE_AUTO_

# values for enumeration '_MV_CAM_TRIGGER_SOURCE_'
_MV_CAM_TRIGGER_SOURCE_ = c_int # enum
MV_CAM_TRIGGER_SOURCE = _MV_CAM_TRIGGER_SOURCE_

# \~chinese Event事件回调信息\    \~english Event callback infomation
class _MV_EVENT_OUT_INFO_(Structure):
    pass
_MV_EVENT_OUT_INFO_._fields_ = [
    ('EventName', c_char * MAX_EVENT_NAME_SIZE), # < \~chinese Event名称       \~english Event name
    ('nEventID', c_ushort),                      # < \~chinese Event号          \~english Event ID
    ('nStreamChannel', c_ushort),                # < \~chinese 流通道序号         \~english Circulation number
    ('nBlockIdHigh', c_uint),                    # < \~chinese 帧号高位  (暂无固件支持)          \~english BlockId high, not support
    ('nBlockIdLow', c_uint),                     # < \~chinese 帧号低位  (暂无固件支持)           \~english BlockId low, not support
    ('nTimestampHigh', c_uint),                  # < \~chinese 时间戳高位            \~english Timestramp high
    ('nTimestampLow', c_uint),                   # < \~chinese 时间戳低位             \~english Timestramp low
    ('pEventData', c_void_p),                    # < \~chinese Event数据     (暂无固件支持)         \~english Event data, not support
    ('nEventDataSize', c_uint),                  # < \~chinese Event数据长度 (暂无固件支持)         \~english Event data len, not support
    ('nReserved', c_uint * 16),                  # < \~chinese 保留字节                 \~english Reserved bytes
]
MV_EVENT_OUT_INFO = _MV_EVENT_OUT_INFO_

# \~chinese 文件存取    \~english File Access
class _MV_CC_FILE_ACCESS_T(Structure):
    pass
_MV_CC_FILE_ACCESS_T._fields_ = [
    ('pUserFileName', STRING),  # < \~chinese 用户文件名         \~english User file name
    ('pDevFileName', STRING),   # < \~chinese 设备文件名          \~english Device file name
    ('nReserved', c_uint * 32), # < \~chinese 保留字节             \~english Reserved bytes
]
MV_CC_FILE_ACCESS = _MV_CC_FILE_ACCESS_T

# \~chinese 文件存取进度    \~english File Access Progress
class _MV_CC_FILE_ACCESS_PROGRESS_T(Structure):
    pass
_MV_CC_FILE_ACCESS_PROGRESS_T._fields_ = [
    ('nCompleted', int64_t),     # < \~chinese 已完成的长度         \~english Completed Length
    ('nTotal', int64_t),         # < \~chinese 总长度               \~english Total Length
    ('nReserved', c_uint * 8),   # < \~chinese 保留字节              \~english Reserved bytes
]
MV_CC_FILE_ACCESS_PROGRESS = _MV_CC_FILE_ACCESS_PROGRESS_T

# values for enumeration '_MV_GIGE_TRANSMISSION_TYPE_'
_MV_GIGE_TRANSMISSION_TYPE_ = c_int # enum
MV_GIGE_TRANSMISSION_TYPE = _MV_GIGE_TRANSMISSION_TYPE_

# 传输模式，可以为单播模式、组播模式等    \~english Transmission type
class _MV_TRANSMISSION_TYPE_T(Structure):
    pass
_MV_TRANSMISSION_TYPE_T._fields_ = [
    ('enTransmissionType', MV_GIGE_TRANSMISSION_TYPE),  # < \~chinese 传输模式                      \~english Transmission type
    ('nDestIp', c_uint),                                # < \~chinese 目标IP，组播模式下有意义        \~english Destination IP
    ('nDestPort', c_ushort),                            # < \~chinese 目标Port，组播模式下有意义        \~english Destination port
    ('nReserved', c_uint * 32),                         # < \~chinese 保留字节                          \~english Reserved bytes
]
MV_TRANSMISSION_TYPE = _MV_TRANSMISSION_TYPE_T

# \~chinese 动作命令信息    \~english Action Command
class _MV_ACTION_CMD_INFO_T(Structure):
    pass
_MV_ACTION_CMD_INFO_T._fields_ = [
    ('nDeviceKey', c_uint),        # < \~chinese 设备密钥                                     \~english Device key
    ('nGroupKey', c_uint),         # < \~chinese 组键                                          \~english Group key
    ('nGroupMask', c_uint),        # < \~chinese 组掩码                                         \~english Group mask
    ('bActionTimeEnable', c_uint), # < \~chinese 只有设置成1时Action Time才有效，非1时无效         \~english Action time enable
    ('nActionTime', int64_t),      # < \~chinese 预定的时间，和主频有关                             \~english Action time
    ('pBroadcastAddress', STRING), # < \~chinese 广播包地址                                         \~english Broadcast address
    ('nTimeOut', c_uint),          # < \~chinese 等待ACK的超时时间，如果为0表示不需要ACK               \~english Timeout
    ('nReserved', c_uint * 16),    # < \~chinese 预留                                                 \~english Reserved bytes
]
MV_ACTION_CMD_INFO = _MV_ACTION_CMD_INFO_T

# \~chinese 动作命令返回信息    \~english Action Command Result
class _MV_ACTION_CMD_RESULT_T(Structure):
    pass
_MV_ACTION_CMD_RESULT_T._fields_ = [
    ('strDeviceAddress', c_ubyte * 16), # < \~chinese IP配置选项         \~english IP address of the device
    #1.0x0000:success.
    #2.0x8001:Command is not supported by the device.
    #3.0x8013:The device is not synchronized to a master clock to be used as time reference.
    #4.0x8015:A device queue or packet data has overflowed.
    #5.0x8016:The requested scheduled action command was requested at a time that is already past.
    ('nStatus', c_int),                 # < \~chinese 状态码            \~english status
    ('nReserved', c_uint * 4),          # < \~chinese 预留              \~english Reserved bytes
]
MV_ACTION_CMD_RESULT = _MV_ACTION_CMD_RESULT_T

# \~chinese 动作命令返回信息列表    \~english Action Command Result List
class _MV_ACTION_CMD_RESULT_LIST_T(Structure):
    pass
_MV_ACTION_CMD_RESULT_LIST_T._fields_ = [
    ('nNumResults', c_uint),                     # < \~chinese 返回值个数         \~english Num Results
    ('pResults', POINTER(MV_ACTION_CMD_RESULT)), # < \~chinese 动作命令返回信息        \~english action command result list
]
MV_ACTION_CMD_RESULT_LIST = _MV_ACTION_CMD_RESULT_LIST_T

# values for enumeration 'MV_XML_InterfaceType'
MV_XML_InterfaceType = c_int # enum

# values for enumeration 'MV_XML_AccessMode'
MV_XML_AccessMode = c_int # enum

# \~chinese 枚举类型值    \~english Enumeration Value
class _MVCC_ENUMVALUE_T(Structure):
    pass
_MVCC_ENUMVALUE_T._fields_ = [
    ('nCurValue', c_uint),                               # < \~chinese 当前值                \~english Current Value
    ('nSupportedNum', c_uint),                           # < \~chinese 数据的有效数据个数      \~english Number of valid data
    ('nSupportValue', c_uint * MV_MAX_XML_SYMBOLIC_NUM), # < \~chinese 支持值列表              \~english Support value list
    ('nReserved', c_uint * 4),                           # < \~chinese 预留                    \~english Reserved bytes
]
MVCC_ENUMVALUE = _MVCC_ENUMVALUE_T

# \~chinese Int类型值    \~english Int Value
class _MVCC_INTVALUE_T(Structure):
    pass
_MVCC_INTVALUE_T._fields_ = [
    ('nCurValue', c_uint),     # < \~chinese 当前值        \~english Current Value
    ('nMax', c_uint),          # < \~chinese 最大值         \~english Max Value
    ('nMin', c_uint),          # < \~chinese 最小值          \~english Min Value
    ('nInc', c_uint),          # < \~chinese 步径             \~english Step size
    ('nReserved', c_uint * 4), # < \~chinese 预留              \~english Reserved bytes
]
MVCC_INTVALUE = _MVCC_INTVALUE_T

# \~chinese Int类型值Ex    \~english Int Value Ex
class _MVCC_INTVALUE_EX_T(Structure):
    pass
_MVCC_INTVALUE_EX_T._fields_ = [
    ('nCurValue', int64_t),     # < \~chinese 当前值         \~english Current Value
    ('nMax', int64_t),          # < \~chinese 最大值          \~english Max Value
    ('nMin', int64_t),          # < \~chinese 最小值           \~english Min Value
    ('nInc', int64_t),          # < \~chinese 步径              \~english Step size
    ('nReserved', c_uint * 16), # < \~chinese 预留               \~english Reserved bytes
]
MVCC_INTVALUE_EX = _MVCC_INTVALUE_EX_T

# \~chinese Float类型值    \~english Float Value
class _MVCC_FLOATVALUE_T(Structure):
    pass
_MVCC_FLOATVALUE_T._fields_ = [
    ('fCurValue', c_float),    # < \~chinese 当前值         \~english Current Value
    ('fMax', c_float),         # < \~chinese 最大值          \~english Max Value
    ('fMin', c_float),         # < \~chinese 最小值           \~english Min Value
    ('nReserved', c_uint * 4), # < \~chinese 预留              \~english Reserved bytes
]
MVCC_FLOATVALUE = _MVCC_FLOATVALUE_T

# \~chinese String类型值    \~english String Value
class _MVCC_STRINGVALUE_T(Structure):
    pass
_MVCC_STRINGVALUE_T._fields_ = [
    ('chCurValue', c_char * 256), # < \~chinese 当前值         \~english Current Value
    ('nMaxLength', int64_t),      # < \~chinese 最大长度        \~english Max length
    ('nReserved', c_uint * 2),    # < \~chinese 预留            \~english Reserved bytes
]
MVCC_STRINGVALUE = _MVCC_STRINGVALUE_T

# \~chinese 水印信息     \~english  Frame-specific information
class _MV_CC_FRAME_SPEC_INFO_(Structure):
    pass
_MV_CC_FRAME_SPEC_INFO_._fields_ = [
    # < \~chinese 设备水印时标      \~english Device frame-specific time scale
    ('nSecondCount', c_uint),        # < \~chinese 秒数                  \~english The Seconds
    ('nCycleCount', c_uint),         # < \~chinese 周期数                 \~english The Count of Cycle
    ('nCycleOffset', c_uint),        # < \~chinese 周期偏移量              \~english The Offset of Cycle
    ('fGain', c_float),              # < \~chinese 增益                   \~english Gain
    ('fExposureTime', c_float),      # < \~chinese 曝光时间                \~english Exposure Time
    ('nAverageBrightness', c_uint),  # < \~chinese 平均亮度                \~english Average brightness
    # < \~chinese 白平衡相关        \~english White balance
    ('nRed', c_uint),    # < \~chinese 红色                   \~english Red
    ('nGreen', c_uint),  # < \~chinese 绿色                    \~english Green
    ('nBlue', c_uint),   # < \~chinese 蓝色                    \~english Blue
    ('nFrameCounter', c_uint),  # < \~chinese 总帧数           \~english Frame Counter
    ('nTriggerIndex', c_uint),  # < \~chinese 触发计数          \~english Trigger Counting
    ('nInput', c_uint),  # < \~chinese 输入                   \~english Input
    ('nOutput', c_uint), # < \~chinese 输出                   \~english Output
    # < \~chinese ROI区域           \~english ROI Region
    ('nOffsetX', c_ushort),      # < \~chinese 水平偏移量        \~english OffsetX
    ('nOffsetY', c_ushort),      # < \~chinese 垂直偏移量         \~english OffsetY
    ('nFrameWidth', c_ushort),   # < \~chinese 水印宽            \~english The Width of Chunk
    ('nFrameHeight', c_ushort),  # < \~chinese 水印高            \~english The Height of Chunk
    ('nReserved', c_uint * 16),   # < \~chinese 预留              \~english Reserved bytes
]
MV_CC_FRAME_SPEC_INFO = _MV_CC_FRAME_SPEC_INFO_

# \~chinese 无损解码参数              \~english High Bandwidth decode structure
class _MV_CC_HB_DECODE_PARAM_T_(Structure):
    pass
_MV_CC_HB_DECODE_PARAM_T_._fields_ = [
    ('pSrcBuf', POINTER(c_ubyte)),      # < \~chinese 输入数据缓存           \~english Input data buffer
    ('nSrcLen', c_uint),                # < \~chinese 输入数据大小           \~english Input data size
    ('nWidth', c_uint),                 # < \~chinese 图像宽                \~english Image Width
    ('nHeight', c_uint),                # < \~chinese 图像高                \~english Image Height
    ('pDstBuf', POINTER(c_ubyte)),      # < \~chinese 输出数据缓存           \~english Output data buffer
    ('nDstBufSize', c_uint),            # < \~chinese 提供的输出缓冲区大小     \~english Provided output buffer size
    ('nDstBufLen', c_uint),             # < \~chinese 输出数据大小            \~english Output data size
    ('enDstPixelType', MvGvspPixelType),  # < \~chinese 输出的像素格式        \~english Output pixel format
    ('stFrameInfo', MV_CC_FRAME_SPEC_INFO),  # < \~chinese 水印信息          \~english Frame Spec Info
    ('nRes', c_uint * 8),                 # < \~chinese 保留字节             \~english Reserved bytes
]
MV_CC_HB_DECODE_PARAM = _MV_CC_HB_DECODE_PARAM_T_

# values for enumeration '_MV_SORT_METHOD_'
_MV_SORT_METHOD_ = c_int  # enum
MV_SORT_METHOD = _MV_SORT_METHOD_

# values for enumeration '_MV_IMG_ROTATION_ANGLE_'
_MV_IMG_ROTATION_ANGLE_ = c_int  # enum
MV_IMG_ROTATION_ANGLE = _MV_IMG_ROTATION_ANGLE_

# values for enumeration '_MV_IMG_FLIP_TYPE_'
_MV_IMG_FLIP_TYPE_ = c_int  # enum
MV_IMG_FLIP_TYPE = _MV_IMG_FLIP_TYPE_

# values for enumeration '_MV_CC_GAMMA_TYPE_'
_MV_CC_GAMMA_TYPE_ = c_int  # enum
MV_CC_GAMMA_TYPE = _MV_CC_GAMMA_TYPE_

# values for enumeration '_MV_CC_STREAM_EXCEPTION_TYPE_'
_MV_CC_STREAM_EXCEPTION_TYPE_ = c_int  # enum
MV_CC_STREAM_EXCEPTION_TYPE = _MV_CC_STREAM_EXCEPTION_TYPE_

# values for enumeration '_MV_IMAGE_RECONSTRUCTION_METHOD_'
_MV_IMAGE_RECONSTRUCTION_METHOD_ = c_int  # enum
MV_IMAGE_RECONSTRUCTION_METHOD = _MV_IMAGE_RECONSTRUCTION_METHOD_

# \~chinese 图像旋转结构体            \~english Rotate image structure
class _MV_CC_ROTATE_IMAGE_PARAM_T_(Structure):
    pass
_MV_CC_ROTATE_IMAGE_PARAM_T_._fields_ = [
    ('enPixelType', MvGvspPixelType),   # < \~chinese 像素格式              \~english pixel format
    ('nWidth', c_uint),                 # < \~chinese 图像宽                \~english Image Width
    ('nHeight', c_uint),                # < \~chinese 图像高                \~english Image Height
    ('pSrcData', POINTER(c_ubyte)),     # < \~chinese 输入数据缓存           \~english Input data buffer
    ('nSrcDataLen', c_uint),            # < \~chinese 输入数据大小           \~english Input data length
    ('pDstBuf', POINTER(c_ubyte)),      # < \~chinese 输出数据缓存           \~english Output data buffer
    ('nDstBufLen', c_uint),             # < \~chinese输出数据长度            \~english Output data length
    ('nDstBufSize', c_uint),            # < \~chinese  提供的输出缓冲区大小    \~english Provided output buffer size
    ('enRotationAngle', MV_IMG_ROTATION_ANGLE),   # < \~chinese  旋转角度               \~english Rotation angle
    ('nRes', c_uint * 8),               # < \~chinese 保留字节               \~english Reserved bytes
]
MV_CC_ROTATE_IMAGE_PARAM = _MV_CC_ROTATE_IMAGE_PARAM_T_

# \~chinese 图像翻转结构体            \~english Flip image structure
class _MV_CC_FLIP_IMAGE_PARAM_T_(Structure):
    pass
_MV_CC_FLIP_IMAGE_PARAM_T_._fields_ = [
    ('enPixelType', MvGvspPixelType),   # < \~chinese 像素格式              \~english pixel format
    ('nWidth', c_uint),                 # < \~chinese 图像宽                \~english Image Width
    ('nHeight', c_uint),                # < \~chinese 图像高                \~english Image Height
    ('pSrcData', POINTER(c_ubyte)),     # < \~chinese 输入数据缓存           \~english Input data buffer
    ('nSrcDataLen', c_uint),            # < \~chinese 输入数据大小           \~english Input data length
    ('pDstBuf', POINTER(c_ubyte)),      # < \~chinese 输出数据缓存           \~english Output data buffer
    ('nDstBufLen', c_uint),             # < \~chinese输出数据长度            \~english Output data length
    ('nDstBufSize', c_uint),            # < \~chinese  提供的输出缓冲区大小    \~english Provided output buffer size
    ('enFlipType', MV_IMG_FLIP_TYPE),   # < \~chinese  翻转类型              \~english Flip type
    ('nRes', c_uint * 8),               # < \~chinese 保留字节               \~english Reserved bytes
]
MV_CC_FLIP_IMAGE_PARAM = _MV_CC_FLIP_IMAGE_PARAM_T_

# \~chinese Gamma信息结构体           \~english Gamma info structure
class _MV_CC_GAMMA_PARAM_T_(Structure):
    pass
_MV_CC_GAMMA_PARAM_T_._fields_ = [
    ('enGammaType', MV_CC_GAMMA_TYPE),       # < \~chinese Gamma类型              \~english Gamma type
    ('fGammaValue', c_float),                # < \~chinese Gamma值[0.1,4.0]       \~english Gamma value[0.1,4.0]
    ('pGammaCurveBuf', POINTER(c_ubyte)),    # < \~chinese Gamma曲线缓存          \~english Gamma curve buffer
    ('nGammaCurveBufLen', c_uint),           # < \~chinese Gamma曲线长度          \~english Gamma curve buffer size
    ('nRes', c_uint * 8),                    # < \~chinese 保留字节             \~english Reserved bytes
]
MV_CC_GAMMA_PARAM = _MV_CC_GAMMA_PARAM_T_

# \~chinese CCM参数                   \~english CCM param
class _MV_CC_CCM_PARAM_T_(Structure):
    pass
_MV_CC_CCM_PARAM_T_._fields_ = [
    ('bCCMEnable', c_bool),         # < \~chinese 是否启用CCM            \~english CCM enable
    ('nCCMat', c_int * 9),          # < \~chinese CCM矩阵[-8192~8192]   \~english Color correction matrix[-8192~8192]
    ('nRes', c_uint * 8),           # < \~chinese 保留字节             \~english Reserved bytes
]
MV_CC_CCM_PARAM = _MV_CC_CCM_PARAM_T_

# \~chinese CCM参数                   \~english CCM param
class _MV_CC_CCM_PARAM_EX_T_(Structure):
    pass
_MV_CC_CCM_PARAM_EX_T_._fields_ = [
    ('bCCMEnable', c_bool),         # < \~chinese 是否启用CCM            \~english CCM enable
    ('nCCMat', c_int * 9),          # < \~chinese CCM矩阵[-65536~65536]  \~english Color correction matrix[-65536~65536]
    ('nCCMScale', c_uint),          # < \~chinese 量化系数（2的整数幂,最大65536）    \~english Quantitative scale(Integer power of 2, <= 65536)
    ('nRes', c_uint * 8),           # < \~chinese 保留字节             \~english Reserved bytes
]
MV_CC_CCM_PARAM_EX = _MV_CC_CCM_PARAM_EX_T_

# \~chinese 对比度调节结构体          \~english Contrast structure
class _MV_CC_CONTRAST_PARAM_T_(Structure):
    pass
_MV_CC_CONTRAST_PARAM_T_._fields_ = [
    ('nWidth', c_uint),                 # < \~chinese 图像宽(最小8)         \~english Image Width
    ('nHeight', c_uint),                # < \~chinese 图像高(最小8)         \~english Image Height
    ('pSrcBuf', POINTER(c_ubyte)),      # < \~chinese 输入数据缓存           \~english Input data buffer
    ('nSrcBufLen', c_uint),             # < \~chinese 输入数据大小           \~english Input data length
    ('enPixelType', MvGvspPixelType),   # < \~chinese 像素格式               \~english pixel format
    ('pDstBuf', POINTER(c_ubyte)),      # < \~chinese 输出数据缓存          \~english Output data buffer
    ('nDstBufSize', c_uint),            # < \~chinese提供的输出缓冲区大小     \~english Provided output buffer size
    ('nDstBufLen', c_uint),            # < \~chinese  输出数据长度           \~english Output data length
    ('nContrastFactor', c_uint),       # < \~chinese  对比度值，[1,10000]    \~english Contrast factor,[1,10000]
    ('nRes', c_uint * 8),                 # < \~chinese 保留字节             \~english Reserved bytes
]
MV_CC_CONTRAST_PARAM_T = _MV_CC_CONTRAST_PARAM_T_

# \~chinese 枚举类型条目          \~english Enumeration Entry
class _MVCC_ENUMENTRY_T(Structure):
    pass
_MVCC_ENUMENTRY_T._fields_ = [
    ('nValue', c_uint),                             # < \~chinese 指定值               \~english Value
    ('chSymbolic', c_char * MV_MAX_SYMBOLIC_LEN),  # < \~chinese 指定值对应的符号       \~english Symbolic

    ('nReserved', c_uint * 4),                      # < \~chinese 预留                 \~english Reserved bytes
]
MVCC_ENUMENTRY = _MVCC_ENUMENTRY_T

# \~chinese 辅助线颜色                \~english Color of Auxiliary Line
class _MVCC_COLORF(Structure):
    pass
_MVCC_COLORF._fields_ = [
    ('fR', c_float),
    # < \~chinese 红色，根据像素颜色的相对深度，范围为[0.0 , 1.0]，代表着[0, 255]的颜色深度   \~english Red，Range[0.0, 1.0]
    ('fG', c_float),
    # < \~chinese 绿色，根据像素颜色的相对深度，范围为[0.0 , 1.0]，代表着[0, 255]的颜色深度   \~english Green，Range[0.0, 1.0]
    ('fB', c_float),
    # < \~chinese 蓝色，根据像素颜色的相对深度，范围为[0.0 , 1.0]，代表着[0, 255]的颜色深度   \~english Blue，Range[0.0, 1.0]
    ('fAlpha', c_float),
    # < \~chinese 透明度，根据像素颜色的相对透明度，范围为[0.0 , 1.0] (此参数功能暂不支持)    \~english Alpha，Range[0.0, 1.0](Not Support)
    ('nReserved', c_uint * 4),     # < \~chinese 保留字节                            \~english Reserved bytes
]
MVCC_COLORF = _MVCC_COLORF

# \~chinese 自定义点                    \~english Point defined
class _MVCC_POINTF(Structure):
    pass
_MVCC_POINTF._fields_ = [
    ('fX', c_float),
    # < \~chinese 该点距离图像左边缘距离，根据图像的相对位置，范围为[0.0 , 1.0]   \~english Distance From Left，Range[0.0, 1.0]
    ('fY', c_float),
    # < \~chinese 该点距离图像上边缘距离，根据图像的相对位置，范围为[0.0 , 1.0]   \~english Distance From Top，Range[0.0, 1.0]
    ('nReserved', c_uint * 4),     # < \~chinese 保留字节                 \~english Reserved bytes
]
MVCC_POINTF = _MVCC_POINTF

# \~chinese 矩形框区域信息            \~english Rect Area Info
class _MVCC_RECT_INFO(Structure):
    pass
_MVCC_RECT_INFO._fields_ = [
    ('fTop', c_float),
    # < \~chinese 矩形上边缘距离图像上边缘的距离，根据图像的相对位置，范围为[0.0 , 1.0]   \~english Distance From Top，Range[0, 1.0]
    ('fBottom', c_float),
    # < \~chinese 矩形下边缘距离图像下边缘的距离，根据图像的相对位置，范围为[0.0 , 1.0]   \~english Distance From Bottom，Range[0, 1.0]
    ('fLeft', c_float),
    # < \~chinese 矩形左边缘距离图像左边缘的距离，根据图像的相对位置，范围为[0.0 , 1.0]   \~english Distance From Left，Range[0, 1.0]
    ('fRight', c_float),
    # < \~chinese 矩形右边缘距离图像右边缘的距离，根据图像的相对位置，范围为[0.0 , 1.0]   \~english Distance From Right，Range[0, 1.0]
    ('stColor', MVCC_COLORF),      # < \~chinese 辅助线颜色信息                \~english Color of Auxiliary Line
    ('nLineWidth', c_uint),        # < \~chinese 辅助线宽度，宽度只能是1或2      \~english Width of Auxiliary Line, width is 1 or 2
    ('nReserved', c_uint * 4),     # < \~chinese 保留字节                     \~english Reserved bytes
]
MVCC_RECT_INFO = _MVCC_RECT_INFO

# \~chinese 圆形框区域信息            \~english Circle Area Info
class _MVCC_CIRCLE_INFO(Structure):
    pass
_MVCC_CIRCLE_INFO._fields_ = [
    ('stCenterPoint', MVCC_POINTF),  # < \~chinese 圆心信息                   \~english Circle Point Info
    ('fR1', c_float),
    # < \~chinese 宽向半径，根据图像的相对位置[0, 1.0]，半径与圆心的位置有关，需保证画出的圆在显示框范围之内，否则报错  \~english Width Radius, Range[0, 1.0]
    ('fR2', c_float),
    # < \~chinese高向半径，根据图像的相对位置[0, 1.0]，半径与圆心的位置有关，需保证画出的圆在显示框范围之内，否则报错  \~english Height Radius, Range[0, 1.0]
    ('stColor', MVCC_COLORF),      # < \~chinese 辅助线颜色信息                \~english Color of Auxiliary Line
    ('nLineWidth', c_uint),        # < \~chinese 辅助线宽度，宽度只能是1或2      \~english Width of Auxiliary Line, width is 1 or 2
    ('nReserved', c_uint * 4),     # < \~chinese 保留字节                     \~english Reserved bytes
]
MVCC_CIRCLE_INFO = _MVCC_CIRCLE_INFO

# \~chinese 线条辅助线信息    \~english Linear Auxiliary Line Info
class _MVCC_LINES_INFO(Structure):
    pass
_MVCC_LINES_INFO._fields_ = [
    ('stStartPoint', MVCC_POINTF), # < \~chinese 线条辅助线的起始点坐标         \~english The Start Point of Auxiliary Line
    ('stEndPoint', MVCC_POINTF),   # < \~chinese线条辅助线的终点坐标            \~english The End Point of Auxiliary Line
    ('stColor', MVCC_COLORF),      # < \~chinese 辅助线颜色信息                \~english Color of Auxiliary Line
    ('nLineWidth', c_uint),        # < \~chinese 辅助线宽度，宽度只能是1或2      \~english Width of Auxiliary Line, width is 1 or 2
    ('nReserved', c_uint * 4),     # < \~chinese 保留字节             \~english Reserved bytes
]
MVCC_LINES_INFO = _MVCC_LINES_INFO

# \~chinese 图像重构后的图像列表      \~english List of images after image reconstruction
class _MV_OUTPUT_IMAGE_INFO_(Structure):
    pass
_MV_OUTPUT_IMAGE_INFO_._fields_ = [
    ('nWidth', c_uint),                 # < \~chinese 图像宽                \~english Image Width
    ('nHeight', c_uint),                # < \~chinese 图像高                \~english Image Height
    ('enPixelType', MvGvspPixelType),   # < \~chinese 像素格式               \~english pixel format
    ('pBuf', POINTER(c_ubyte)),      # < \~chinese 输出数据缓存          \~english Output data buffer
    ('nBufLen', c_uint),             # < \~chinese 输出数据长度          \~english Output data length
    ('nBufSize', c_uint),            # < \~chinese  提供的输出缓冲区大小  \~english Provided output buffer size
    ('nRes', c_uint * 8),                 # < \~chinese 保留字节             \~english Reserved bytes
]
MV_OUTPUT_IMAGE_INFO = _MV_OUTPUT_IMAGE_INFO_

# \~chinese 重构图像参数信息      \~english Restructure image parameters
class _MV_RECONSTRUCT_IMAGE_PARAM_(Structure):
    pass
_MV_RECONSTRUCT_IMAGE_PARAM_._fields_ = [
    ('nWidth', c_uint),                 # < \~chinese 图像宽                \~english Image Width
    ('nHeight', c_uint),                # < \~chinese 图像高                \~english Image Height
    ('enPixelType', MvGvspPixelType),   # < \~chinese 像素格式               \~english pixel format
    ('pSrcData', POINTER(c_ubyte)),      # < \~chinese 输入数据缓存           \~english input data buffer
    ('nSrcDataLen', c_uint),             # < \~chinese 输入数据大小            \~english input data size
    ('nExposureNum', c_uint),            # < \~chinese  曝光个数(1-8]     \~english Exposure number
    ('enReconstructMethod', MV_IMAGE_RECONSTRUCTION_METHOD),   # < \~chinese 图像重构方式      \~english Image restructuring method
    ('stDstBufList', MV_OUTPUT_IMAGE_INFO * MV_MAX_SPLIT_NUM),  # < \~chinese 输出数据缓存信息  \~english Output data info
    ('nRes', c_uint * 4),                 # < \~chinese 保留字节             \~english Reserved bytes
]
MV_RECONSTRUCT_IMAGE_PARAM = _MV_RECONSTRUCT_IMAGE_PARAM_

# \~chinese 文件存取                  \~english File Access
class _MV_CC_FILE_ACCESS_E(Structure):
    pass
_MV_CC_FILE_ACCESS_E._fields_ = [
    ('pUserFileBuf', POINTER(c_char)),  # < \~chinese 用户文件数据        \~english User file data
    ('pFileBufSize', c_uint),  # < \~chinese 用户数据缓存大小       \~english data buffer size
    ('pFileBufLen', c_uint),   # < \~chinese 用户数据缓存长度       \~english data buffer len
    ('pDevFileName', STRING),           # < \~chinese 设备文件名          \~english Device file name
    ('nReserved', c_uint * 32),         # < \~chinese 保留字节            \~english Reserved bytes
]
MV_CC_FILE_ACCESS_EX = _MV_CC_FILE_ACCESS_E

# 采集卡信息            \~english Interface information
class _MV_INTERFACE_INFO_(Structure):
    pass
_MV_INTERFACE_INFO_._fields_ = [
    ('nTLayerType', c_uint),               # < \~chinese 采集卡类型    \~english Interface type
    ('nPCIEInfo', c_uint),                 # < \~chinese 采集卡的PCIE插槽信息  \~english PCIe slot information of interface
    ('chInterfaceID', c_ubyte * INFO_MAX_BUFFER_SIZE),  # < \~chinese 采集卡ID    \~english Interface ID
    ('chDisplayName', c_ubyte * INFO_MAX_BUFFER_SIZE),  # < \~chinese 显示名称    \~english Display name
    ('chSerialNumber', c_ubyte * INFO_MAX_BUFFER_SIZE),  # < \~chinese 序列号      \~english Serial number
    ('chModelName', c_ubyte * INFO_MAX_BUFFER_SIZE),     # < \~chinese 型号        \~english model name
    ('chManufacturer', c_ubyte * INFO_MAX_BUFFER_SIZE),  # < \~chinese 厂商        \~english manufacturer name
    ('chDeviceVersion', c_ubyte * INFO_MAX_BUFFER_SIZE),  # < \~chinese 版本号      \~english device version
    ('chUserDefinedName', c_ubyte * INFO_MAX_BUFFER_SIZE),  # < \~chinese 自定义名称 \~english user defined name
    ('nReserved', c_uint * 64),                             # < \~chinese 保留字节   \~english Reserved bytes
]
MV_INTERFACE_INFO = _MV_INTERFACE_INFO_

# 采集卡信息列表           \~english Interface Information List
class _MV_INTERFACE_INFO_LIST_(Structure):
    pass
_MV_INTERFACE_INFO_LIST_._fields_ = [
    ('nInterfaceNum', c_uint),                                          # < \~chinese 在线设备数量         \~english Online Device Number
    ('pInterfaceInfos', POINTER(MV_INTERFACE_INFO) * MV_MAX_INTERFACE_NUM), # < \~chinese 支持最多256个设备    \~english Support up to 256 devices
]
MV_INTERFACE_INFO_LIST = _MV_INTERFACE_INFO_LIST_

# 串口信息      \~english Serial Port Info
class _MV_CAML_SERIAL_PORT_(Structure):
    pass
_MV_CAML_SERIAL_PORT_._fields_ = [
    ('chSerialPort', c_char * INFO_MAX_BUFFER_SIZE),   # < \~chinese 串口号          \~english Serial Port
    ('nRes', c_uint * 4),                              # < \~chinese 保留字节        \~english Reserved bytes
]
MV_CAML_SERIAL_PORT = _MV_CAML_SERIAL_PORT_

# 本机串口列表            \~english serial port list
class _MV_CAML_SERIAL_PORT_LIST_(Structure):
    pass
_MV_CAML_SERIAL_PORT_LIST_._fields_ = [
    ('nSerialPortNum', c_uint),                                      # < \~chinese 串口数量   \~english Serial Port Num
    ('stSerialPort', MV_CAML_SERIAL_PORT * MV_MAX_SERIAL_PORT_NUM),  # < \~chinese 串口信息   \~english Serial Port Information
    ('nRes', c_uint * 4),  # < \~chinese 保留字节   \~english Reserved bytes
]
MV_CAML_SERIAL_PORT_LIST = _MV_CAML_SERIAL_PORT_LIST_

__all__ = ['_MV_ALL_MATCH_INFO_', 'MV_CC_FILE_ACCESS_PROGRESS',
           'N19_MV_CC_DEVICE_INFO_3DOT_0E', 'MV_FRAME_OUT',
           'MV_CAM_GAIN_MODE',
           'MV_ALL_MATCH_INFO',
           'MV_GIGE_TRANSTYPE_UNICAST_WITHOUT_RECV',
           'MV_TRIGGER_SOURCE_LINE0', 'MV_PointCloudFile_Undefined',
           'MV_TRIGGER_SOURCE_LINE2', 'MV_TRIGGER_SOURCE_LINE3',
           'AM_CycleDetect',
           'MV_GrabStrategy_UpcomingImage', 'IFT_IFloat',
           'MV_EVENT_OUT_INFO', 'MV_TRANSMISSION_TYPE',
           'uint_fast16_t', 'MV_CHUNK_DATA_CONTENT','MV_ACTION_CMD_RESULT',
           'MV_CC_INPUT_FRAME_INFO',
           '_MV_ACTION_CMD_RESULT_T',
           'AM_RO', 'IFT_IPort', 'uint_least16_t',
           '_MV_FRAME_OUT_INFO_EX_', '_MV_TRANSMISSION_TYPE_T',
           'MV_SAVE_IMAGE_PARAM_EX', 'MV_SAVE_IMAGE_PARAM_EX3', 'AM_RW', 'MV_XML_InterfaceType',
           'int32_t', '_MV_ACTION_CMD_INFO_T', 'intptr_t',
           'uint_least64_t', '_MV_NETTRANS_INFO_',
           '_MV_CAM_TRIGGER_MODE_', 'int_least32_t',
           'MV_GIGE_TRANSTYPE_SUBNETBROADCAST',
           'MV_SAVE_POINT_CLOUD_FILE_TYPE',
           'MV_ACTION_CMD_RESULT_LIST',
           'MV_BALANCEWHITE_AUTO_CONTINUOUS',
           '_MV_CHUNK_DATA_CONTENT_', 'MV_FormatType_AVI',
           '_MV_CC_PIXEL_CONVERT_PARAM_T_','_MV_PIXEL_CONVERT_PARAM_EX_T_',
           'MV_GENTL_IF_INFO',
           'MV_ACQ_MODE_SINGLE',
           'MV_TRIGGER_MODE_ON',
           'int_least16_t', 'N22_MV_FRAME_OUT_INFO_EX_3DOT_1E',
           'MV_GIGE_TRANSTYPE_LIMITEDBROADCAST', 'int_fast32_t',
           '_MV_CAM_GAIN_MODE_',
           'MV_RECORD_FORMAT_TYPE', 'MV_CC_DEVICE_INFO',
           'IFT_ICommand', '_MV_RECORD_FORMAT_TYPE_',
           '_MV_CAM_ACQUISITION_MODE_',
           '_MVCC_STRINGVALUE_T',
           'MV_GIGE_TRANSTYPE_MULTICAST_WITHOUT_RECV',
           '_MV_MATCH_INFO_NET_DETECT_', 'MVCC_INTVALUE',
           'MV_PointCloudFile_OBJ', '_MV_GIGE_TRANSMISSION_TYPE_',
           '_MV_CC_RECORD_PARAM_T_',
           '_MV_GENTL_IF_INFO_', 'MV_EXPOSURE_MODE_TIMED', 'intmax_t',
           'int16_t',
           'MV_DISPLAY_FRAME_INFO', '_MV_CC_FILE_ACCESS_PROGRESS_T',
           '_MV_GRAB_STRATEGY_', '_MV_SAVE_IMG_TO_FILE_PARAM_', '_MV_SAVE_IMAGE_TO_FILE_PARAM_EX_',
           'int_fast64_t',
           'MV_XML_AccessMode',
           'MV_GAIN_MODE_ONCE', 'IFT_IInteger',
           'MV_CAM_BALANCEWHITE_AUTO', 'int_least8_t',
           'MV_PointCloudFile_CSV', 'IFT_IBase',
           'MV_TRIGGER_MODE_OFF', 'MV_Image_Bmp',
           '_MV_GENTL_DEV_INFO_', 'MV_CC_FILE_ACCESS',
           '_MV_CAM_EXPOSURE_AUTO_MODE_',
           'uint_least8_t',
           'MV_ACTION_CMD_INFO',
           '_MV_CC_INPUT_FRAME_INFO_T_',
           'MV_GENTL_DEV_INFO_LIST', '_MV_CAM_TRIGGER_SOURCE_',
           'MV_GRAB_STRATEGY',
           'IFT_IEnumeration', 'uint64_t', 'uint8_t',
           '_MV_GENTL_DEV_INFO_LIST_',
           'MV_CAM_GAMMA_SELECTOR',
           'MV_CamL_DEV_INFO', 'MV_GENTL_IF_INFO_LIST',
           'MV_CAM_TRIGGER_MODE', 'MV_GIGE_TRANSTYPE_MULTICAST',
           'uint16_t', 'uint_fast8_t',
           '_MV_ACTION_CMD_RESULT_LIST_T',
           '_MV_MATCH_INFO_USB_DETECT_',
           '_MVCC_ENUMVALUE_T',
           'MV_SAVE_POINT_CLOUD_PARAM', '_MV_CC_DEVICE_INFO_',
           'IFT_IBoolean',
           'MV_MATCH_INFO_USB_DETECT', 'MV_PointCloudFile_PLY',
           'MVCC_ENUMVALUE',
           'IFT_IString',
           'MV_ACQ_MODE_CONTINUOUS',
           'MV_TRIGGER_SOURCE_FrequencyConverter',
           'MV_TRIGGER_SOURCE_COUNTER0',
           'MV_GAIN_MODE_OFF', '_MV_CC_DEVICE_INFO_LIST_',
           'MV_GIGE_DEVICE_INFO', '_MV_SAVE_IMAGE_PARAM_T_EX_', '_MV_SAVE_IMAGE_PARAM_EX3_',
           'AM_NA', 'uint_least32_t',
           'MV_CC_PIXEL_CONVERT_PARAM', 'MV_CC_PIXEL_CONVERT_PARAM_EX','AM_NI',
           '_MVCC_INTVALUE_EX_T', 'uintptr_t', 'MV_Image_Tif',
           'MVCC_FLOATVALUE', 'MV_GIGE_TRANSTYPE_CAMERADEFINED',
           '_MV_GENTL_IF_INFO_LIST_', 'MV_NETTRANS_INFO',
           'IFT_IRegister', 'MV_GIGE_TRANSMISSION_TYPE',
           'MV_EXPOSURE_AUTO_MODE_ONCE', 'MV_GIGE_TRANSTYPE_UNICAST',
           'int8_t', '_MV_GIGE_DEVICE_INFO_', 'IFT_IValue', 'AM_WO',
           'int_fast8_t',
           'MV_GAMMA_SELECTOR_SRGB','int_least64_t',
           'MV_GrabStrategy_LatestImagesOnly',
           'MV_EXPOSURE_AUTO_MODE_OFF', 'MV_CAM_EXPOSURE_AUTO_MODE',
           'MV_EXPOSURE_AUTO_MODE_CONTINUOUS',
           'MV_CAM_ACQUISITION_MODE', 'AM_Undefined',
           'MV_MATCH_INFO_NET_DETECT',
           '_MV_CC_FILE_ACCESS_T',
           '_MV_DISPLAY_FRAME_INFO_','MV_GrabStrategy_OneByOne',
           'MV_TRIGGER_SOURCE_SOFTWARE', 'MV_FormatType_Undefined',
           'MV_BALANCEWHITE_AUTO_ONCE',
           'uintmax_t', 'int_fast16_t',
           '_MV_CAM_EXPOSURE_MODE_','MV_BALANCEWHITE_AUTO_OFF',
           'int64_t', 'MV_Image_Undefined', 'MV_GAIN_MODE_CONTINUOUS',
           'uint_fast32_t',
           'MV_CAM_TRIGGER_SOURCE', 'MV_GrabStrategy_LatestImages',
           'MV_Image_Png',
           'MV_Image_Jpeg', '_MV_CamL_DEV_INFO_',
           '_MVCC_FLOATVALUE_T',
           'MV_FRAME_OUT_INFO_EX', '_MV_SAVE_POINT_CLOUD_PARAM_',
           '_MV_CAM_BALANCEWHITE_AUTO_', 'MV_CC_RECORD_PARAM',
           '_MV_USB3_DEVICE_INFO_',
           'MVCC_INTVALUE_EX', 'MV_EXPOSURE_MODE_TRIGGER_WIDTH',
           'MV_GIGE_TRANSTYPE_UNICAST_DEFINED_PORT',
           'MV_SAVE_IAMGE_TYPE','MV_GENTL_DEV_INFO',
           'MV_CAM_EXPOSURE_MODE',
           'MVCC_STRINGVALUE',
           'MvGvspPixelType',
           'MV_CC_DEVICE_INFO_LIST',
           'MV_TRIGGER_SOURCE_LINE1',
           'uint_fast64_t','_MVCC_INTVALUE_T',
           'IFT_ICategory',
           'MV_SAVE_IMG_TO_FILE_PARAM', 'MV_SAVE_IMAGE_TO_FILE_PARAM_EX', '_MV_FRAME_OUT_',
           'MV_GAMMA_SELECTOR_USER',
           'uint32_t', '_MV_CAM_GAMMA_SELECTOR_', 'MV_ACQ_MODE_MUTLI',
           'MV_USB3_DEVICE_INFO', '_MV_EVENT_OUT_INFO_', 'MV_CC_FRAME_SPEC_INFO', 'MV_CC_HB_DECODE_PARAM',
           'MV_SORT_METHOD', '_MV_SORT_METHOD_',
           'SortMethod_SerialNumber', 'SortMethod_UserID', 'SortMethod_CurrentIP_ASC', 'SortMethod_CurrentIP_DESC',
           '_MV_IMG_ROTATION_ANGLE_', 'MV_IMG_ROTATION_ANGLE',
           'MV_IMAGE_ROTATE_90', 'MV_IMAGE_ROTATE_180', 'MV_IMAGE_ROTATE_270',
           '_MV_IMG_FLIP_TYPE_', 'MV_IMG_FLIP_TYPE', 'MV_FLIP_VERTICAL', 'MV_FLIP_HORIZONTAL',
           '_MV_CC_GAMMA_TYPE_', 'MV_CC_GAMMA_TYPE', 'MV_CC_GAMMA_TYPE_NONE', 'MV_CC_GAMMA_TYPE_VALUE',
           'MV_CC_GAMMA_TYPE_USER_CURVE', 'MV_CC_GAMMA_TYPE_LRGB2SRGB', 'MV_CC_GAMMA_TYPE_SRGB2LRGB',
           'MV_CC_STREAM_EXCEPTION_TYPE', '_MV_CC_STREAM_EXCEPTION_TYPE_',
           'MV_CC_STREAM_EXCEPTION_ABNORMAL_IMAGE', 'MV_CC_STREAM_EXCEPTION_LIST_OVERFLOW',
           'MV_CC_STREAM_EXCEPTION_LIST_EMPTY', 'MV_CC_STREAM_EXCEPTION_RECONNECTION',
           'MV_CC_STREAM_EXCEPTION_DISCONNECTED', 'MV_CC_STREAM_EXCEPTION_DEVICE', 
           '_MV_IMAGE_RECONSTRUCTION_METHOD_', 'MV_IMAGE_RECONSTRUCTION_METHOD', 'MV_SPLIT_BY_LINE',
           'MVCC_COLORF', '_MVCC_COLORF', '_MVCC_POINTF', 'MVCC_POINTF', '_MVCC_RECT_INFO', 'MVCC_RECT_INFO',
           '_MVCC_CIRCLE_INFO', 'MVCC_CIRCLE_INFO', '_MVCC_LINES_INFO', 'MVCC_LINES_INFO', '_MV_OUTPUT_IMAGE_INFO_',
           'MV_OUTPUT_IMAGE_INFO', 'MV_RECONSTRUCT_IMAGE_PARAM', '_MV_RECONSTRUCT_IMAGE_PARAM_',
           '_MVCC_ENUMENTRY_T', 'MVCC_ENUMENTRY','_MV_CC_CONTRAST_PARAM_T_', 'MV_CC_CONTRAST_PARAM_T',
           '_MV_CC_CCM_PARAM_EX_T_', 'MV_CC_CCM_PARAM_EX', 'MV_CC_CCM_PARAM', '_MV_CC_CCM_PARAM_T_',
           'MV_CC_GAMMA_PARAM', '_MV_CC_GAMMA_PARAM_T_', 'MV_CC_FLIP_IMAGE_PARAM', '_MV_CC_FLIP_IMAGE_PARAM_T_',
           '_MV_CC_ROTATE_IMAGE_PARAM_T_', 'MV_CC_ROTATE_IMAGE_PARAM', 'MV_CC_FILE_ACCESS_EX', '_MV_CC_FILE_ACCESS_E',
           '_MV_DISPLAY_FRAME_INFO_EX_', 'MV_DISPLAY_FRAME_INFO_EX', 'MV_CML_DEVICE_INFO', '_MV_CML_DEVICE_INFO_',
           'MV_CXP_DEVICE_INFO', '_MV_CXP_DEVICE_INFO_', '_MV_XOF_DEVICE_INFO_', 'MV_XOF_DEVICE_INFO',
           '_MV_INTERFACE_INFO_LIST_', 'MV_INTERFACE_INFO_LIST', '_MV_INTERFACE_INFO_', 'MV_INTERFACE_INFO',
           '_MV_CAML_SERIAL_PORT_LIST_', 'MV_CAML_SERIAL_PORT_LIST', '_MV_CAML_SERIAL_PORT_', 'MV_CAML_SERIAL_PORT']
