import logging
import esphome.codegen as cg
from esphome.components import uart
import esphome.config_validation as cv
from esphome.const import (
    CONF_ID,
    CONF_NAME,
)

_LOGGER = logging.getLogger(__name__)

CODEOWNERS = ["@oxynatOr"]
DEPENDENCIES = ["uart"]
#AUTO_LOAD = ["sensor"]
MULTI_CONF = True

## Helper
CV_NUM_BATTERIES = cv.int_range(1, 16)
CV_NUM_CELLS = cv.int_range(0, 16)

##Icons
ICON_CURRENT_DC = "mdi:current-dc"
ICON_MIN_VOLTAGE_CELL = "mdi:battery-minus-outline"
ICON_MAX_VOLTAGE_CELL = "mdi:battery-plus-outline"
ICON_BATTERY_STRINGS = "mdi:car-battery"
ICON_CAPACITY_REMAINING_DERIVED = "mdi:battery-50"
ICON_ACTUAL_BATTERY_CAPACITY = "mdi:battery-50"
ICON_TOTAL_BATTERY_CAPACITY_SETTING = "mdi:battery-sync"
ICON_DEVICE_ADDRESS = "mdi:identifier"
ICON_ERRORS_BITMASK = "mdi:alert-circle-outline"
ICON_OPERATION_MODE_BITMASK = "mdi:heart-pulse"
ICON_CHARGING_CYCLES = "mdi:battery-sync"
ICON_ALARM_LOW_VOLUME = "mdi:volume-high"

##Custom 
UNIT_AMPERE_HOURS = "Ah"

pytes_e_box_ns = cg.esphome_ns.namespace("pytes_e_box")
PytesEBoxComponent = pytes_e_box_ns.class_("PytesEBoxComponent", cg.PollingComponent, uart.UARTDevice)
CONF_BATTERIES_COMPONENT = "batteries"
#CONF_BATTERIES = "batteries_in_rack"
CONF_POLL_TIMEOUT = "poll_timeout"
#CONF_CMD_IDLE_TIME = "command_idle_time" 


CONF_PYTES_E_BOX_ID = "pytes_e_box_id"
CONF_CELL = "cell"



CONF_BATTERY = "battery"

PytesEBoxBatteryCellSensor = pytes_e_box_ns.class_("PytesEBoxBatteryCellSensor", cg.Component)
CONF_CELL_ARRAYS = "cells"
CONF_CELL_ARRAY_ID = "cell_id"


BATTERY_SCHEMA = cv.Schema(
        {
            cv.GenerateID(CONF_PYTES_E_BOX_ID): cv.use_id(PytesEBoxComponent),
            #cv.GenerateID(): cv.declare_id(PytesEBoxBatterySensor),
            cv.Required(CONF_BATTERY): CV_NUM_BATTERIES,
            cv.Optional(CONF_NAME): cv.string_strict,
        }
    )



CELLS_ARRAYS_SCHEMA = BATTERY_SCHEMA.ensure_list(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(PytesEBoxBatteryCellSensor),
            cv.Required(CONF_CELL_ARRAY_ID): CV_NUM_CELLS,
            cv.Optional(CONF_NAME): cv.string_strict,
        }
    )
)


PYTES_E_BOX_COMPONENT_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_PYTES_E_BOX_ID): cv.use_id(PytesEBoxComponent),
        #cv.Required(CONF_BATTERY): cv.int_range(1, 16),
        #cv.Optional(CONF_CELL): cv.int_range(0, 16),
    }
)


CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(PytesEBoxComponent),
            cv.Required(CONF_BATTERIES_COMPONENT): CV_NUM_BATTERIES,
            cv.Required(CONF_POLL_TIMEOUT): cv.positive_time_period_milliseconds,
        }
    )
    .extend(cv.polling_component_schema("15s"))
    .extend(uart.UART_DEVICE_SCHEMA)
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    cg.add(var.set_system_battery_count(config[CONF_BATTERIES_COMPONENT]))
    cg.add(var.set_polling_timeout(config[CONF_POLL_TIMEOUT]))
    #cg.add(var.set_cmd_idle_time(config[CONF_CMD_IDLE_TIME]))
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)
