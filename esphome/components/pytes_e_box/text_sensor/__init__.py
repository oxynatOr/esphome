#import logging
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_VOLTAGE,
    CONF_CURRENT,
    CONF_TEMPERATURE,
    CONF_ID,
    CONF_NAME,    
    UNIT_VOLT,
    UNIT_AMPERE,
    UNIT_CELSIUS,
    UNIT_PERCENT,
    STATE_CLASS_MEASUREMENT,
    DEVICE_CLASS_EMPTY,
    DEVICE_CLASS_VOLTAGE,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_BATTERY
    )

from .. import (pytes_e_box_ns ,CONF_PYTES_E_BOX_ID, PYTES_E_BOX_COMPONENT_SCHEMA, CONF_CELL, CONF_BAT_ARRAY_ID,
                CONF_BATTERIES_COMPONENT, CONF_PYTES_E_BOX_ID, CONF_BATTERY, CONF_CELL_ARRAYS, CONF_CELL_ARRAY_ID, 
                CV_NUM_CELLS, CV_NUM_BATTERIES
                
                )


PytesEBoxBatteryTextSensor = pytes_e_box_ns.class_("PytesEBoxBatteryTextSensor", cg.Component)
PytesEBoxBatteryCellTextSensor = pytes_e_box_ns.class_("PytesEBoxBatteryCellTextSensor", cg.Component)

CONF_BASE_STATE = "base_state"
CONF_VOLTAGE_STATE = "voltage_state"
CONF_CURRENT_STATE = "current_state"
CONF_TEMPERATURE_STATE = "temperature_state"
CONF_BARCODE = "barcode"
CONF_DEV_TYPE = "dev_type"
CONF_FIRM_VERSION = "firm_version"
CONF_COULOMB_STATUS = "coulomb_status"
CONF_BAT_STATUS = "bat_status"
CONF_CMOS_STATUS = "cmos_status"
CONF_DMOS_STATUS = "dmos_status"
CONF_BAT_PROTECT_ENA = "bat_protect_ena"
CONF_PWR_PROTECT_ENA = "pwr_protect_ena"
CONF_BAT_EVENTS = "bat_events"
CONF_POWER_EVENTS = "power_events"
CONF_SYSTEM_FAULT = "system_fault"

BAT_TYPES: list[str] = [
    CONF_BASE_STATE,
    CONF_VOLTAGE_STATE,
    CONF_CURRENT_STATE,
    CONF_TEMPERATURE_STATE,
    CONF_BARCODE,
    CONF_DEV_TYPE,
    CONF_FIRM_VERSION,
    CONF_COULOMB_STATUS,
    CONF_BAT_STATUS,
    CONF_CMOS_STATUS,
    CONF_DMOS_STATUS,
    CONF_BAT_PROTECT_ENA,
    CONF_PWR_PROTECT_ENA,
    CONF_BAT_EVENTS,
    CONF_POWER_EVENTS,
    CONF_SYSTEM_FAULT,
]

CELL_TYPES: list[str] = [
    CONF_BASE_STATE,
    CONF_VOLTAGE_STATE,
    CONF_CURRENT_STATE,
    CONF_TEMPERATURE_STATE,
]



CELLS_ARRAYS_SCHEMA = cv.ensure_list(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(PytesEBoxBatteryCellTextSensor),
            cv.Required(CONF_CELL): CV_NUM_CELLS,
            cv.Optional(CONF_NAME): cv.string_strict,
        }
    ).extend({cv.Optional(marker): text_sensor.text_sensor_schema() for marker in CELL_TYPES})
)



CONFIG_SCHEMA = PYTES_E_BOX_COMPONENT_SCHEMA.extend(
        {
            cv.GenerateID(): cv.declare_id(PytesEBoxBatteryTextSensor),
            cv.Required(CONF_BATTERY): CV_NUM_BATTERIES,
            cv.Optional(CONF_NAME): cv.string_strict,
            cv.Optional(CONF_CELL_ARRAYS): CELLS_ARRAYS_SCHEMA,
        }
    ).extend({cv.Optional(marker): text_sensor.text_sensor_schema() for marker in BAT_TYPES})
           

async def to_code(config):
    paren = await cg.get_variable(config[CONF_PYTES_E_BOX_ID])

    if CONF_BATTERY in config:
        bat = cg.new_Pvariable(config[CONF_ID], config[CONF_BATTERY])
        for marker in BAT_TYPES:
            if marker_config := config.get(marker):
                sens = await text_sensor.new_sensor(marker_config)
                cg.add(getattr(bat, f"set_{marker}_text_sensor")(sens))
        cg.add(paren.register_listener(bat))    

    if CONF_CELL_ARRAYS in config:
        for cells_config in config[CONF_CELL_ARRAYS]:
            cell_var = cg.new_Pvariable(cells_config[CONF_ID], config[CONF_BATTERY], cells_config[CONF_CELL])
            for marker in CELL_TYPES:
                if marker in cells_config:
                    sens = await text_sensor.new_sensor(cells_config[marker])
                    cg.add(getattr(cell_var, f"set_{marker}_text_sensor")(sens))
            cg.add(paren.register_listener(cell_var))