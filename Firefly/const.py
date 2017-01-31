
AUTHOR = 'Zachary Priddy (me@zpriddy.com)'

# #### SETTINGS ####
FIREFLY_CONFIG_SECTION = 'FIREFLY'
CONFIG_PORT = 'port'
CONFIG_DEFAULT_PORT = 6002
CONFIG_HOST = 'host'
CONFIG_DEFAULT_HOST = 'localhost'
CONFIG_FILE = 'dev_config/firefly.config'

SERVICE_CONFIG_FILE = 'dev_config/services.config'

ALIAS_FILE = 'dev_config/device_alias.json'
DEVICE_FILE = 'dev_config/devices.json'
AUTOMATION_FILE = 'dev_config/automation.json'


SERVICE_NOTIFICATION = 'FIREFLY_NOTIFICATION_SERVICE'
NOTIFY_DEFAULT = 'DEFAULT'
PRIORITY_NORMAL = 0
PRIORITY_LOW = -1
PRIORITY_HIGH = 1
PRIORITY_EMERGENCY = 2



# #### EVENT TYPES ####
EVENT_TYPE_ANY = 'ANY'
EVENT_TYPE_COMMAND = 'COMMAND'
EVENT_TYPE_UPDATE = 'UPDATE'
EVENT_TYPE_BROADCAST = 'BROADCAST'
EVENT_TYPE_REQUEST = 'REQUEST'

# #### EVENT ACTIONS ####
EVENT_ACTION_ANY = 'ANY'
EVENT_ACTION_ON = 'ON'
EVENT_ACTION_OFF = 'OFF'
EVENT_ACTION_ACTIVE = 'ACTIVE'
EVENT_ACTION_INACTIVE = 'INACTIVE'
EVENT_ACTION_OPEN = 'OPEN'
EVENT_ACTION_CLOSE = 'CLOSE'
EVENT_ACTION_LEVEL = 'LEVEL'

TYPE_AUTOMATION = 'TYPE_AUTOMATION'
TYPE_DEVICE = 'TYPE_DEVICE'
TYPE_SERVICE = 'TYPE_SERVICE'

API_INFO_REQUEST = 'API_INFO_REQUEST'



EVENT_DAWN = 'dawn'
EVENT_SUNRISE = 'sunrise'
EVENT_NOON = 'noon'
EVENT_SUNSET = 'sunset'
EVENT_DUSK = 'dusk'
DAY_EVENTS = [EVENT_DAWN, EVENT_SUNRISE, EVENT_NOON, EVENT_SUNSET, EVENT_DUSK]

# #### COMMAND ACTIONS ####
COMMAND_NOTIFY = 'NOTIFY'
COMMAND_SPEECH = 'SPEECH'
COMMAND_ROUTINE = 'ROUTINE'

ACTION_OFF = 'OFF'
ACTION_ON = 'ON'
ACTION_TOGGLE = 'TOGGLE'
ACTION_LEVEL = 'LEVEL'

# #### REQUESTS ####
STATE = 'STATE'
LEVEL = 'LEVEL'
PRESENCE = 'PRESENCE'

STATE_OFF = False
STATE_ON = True
STATE_CLOSED = 'CLOSED'


# #### DEVICE TYPES ####
DEVICE_TYPE_SWITCH = 'SWITCH'
DEVICE_TYPE_DIMMER = 'DIMMER'
DEVICE_TYPE_COLOR_LIGHT = 'COLOR_LIGHT'
DEVICE_TYPE_THERMOSTAT = 'THERMOSTAT'
DEVICE_TYPE_NOTIFICATION = 'NOTIFICATION'
DEVICE_TYPE_MOTION = 'MOTION'


SOURCE_LOCATION = 'LOCATION'
SOURCE_TRIGGER = 'SOURCE_TRIGGER'


# #### CONDITIONS ####
IS_DARK = 'IS_DARK'
IS_LIGHT = 'IS_LIGHT'
IS_MODE = 'IS_MODE'
IS_NOT_MODE = 'IS_NOT_MODE'
IS_TIME_RANGE = 'TIME_RANGE'
IS_NOT_TIME_RANGE = 'NOT_TIME_RANGE'

COMPONENT_MAP = [
  {
    'type': TYPE_AUTOMATION,
    'file': AUTOMATION_FILE
  },
  {
    'type': TYPE_DEVICE,
    'file': DEVICE_FILE
  }
]

# TODO: This may not be needed
SENSORS = {
  'Energy': 'ENERGY',
  'Previous Reading': 'PREVIOUS READING',
  'Interval': 'INTERVAL',
  'Power': 'POWER',
  'Voltage': 'VOLTAGE',
  'Current': 'CURRENT',
  'Exporting': 'EXPORTING',
  'Sensor': 'SENSOR',
  'Temperature': 'TEMPERATURE',
  'Luminance': 'LUMINANCE',
  'Relative Humidity': 'RELATIVE HUMIDITY',
  'Ultraviolet': 'ULTRAVIOLET'
}