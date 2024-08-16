import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_VOLTAGE,
    CONF_CURRENT,
    CONF_TEMPERATURE,
    CONF_ID,
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

from .. import (pytes_e_box_ns ,CONF_PYTES_E_BOX_ID, PYTES_E_BOX_COMPONENT_SCHEMA, CONF_CELL, PytesEBoxBatterySensor, PytesEBoxBatteryCellSensor, 
                CONF_BATTERIES_COMPONENT, CONF_PYTES_E_BOX_ID, CONF_BATTERY, CONF_CELL_ARRAYS, CONF_CELL_ARRAY_ID, BATTERIES_ARRAYS_SCHEMA, 
                CELLS_ARRAYS_SCHEMA
                )



##Custom 
UNIT_AMPERE_HOURS       = "Ah"

CONF_COULOMB            = "coulomb"
CONF_TEMPERATURE_LOW    = "temperature_low"
CONF_TEMPERATURE_HIGH   = "temperature_high"
CONF_VOLTAGE_LOW        = "voltage_low"
CONF_VOLTAGE_HIGH       = "voltage_high"

CONF_SOC_VOLTAGE        = "soc_voltage"
CONF_TOTAL_COULOMB      = "total_coulomb"
CONF_REAL_COULOMB       = "real_coulomb"
CONF_TOTAL_POWER_IN     = "total_power_in"
CONF_TOTAL_POWER_OUT    = "total_power_out"
CONF_WORK_STATUS        = "work_status"
CONF_CELLS              = "cells"

CONF_CELL_VOLTAGE       = "voltage"
CONF_CELL_TEMPERATURE   = "temperature"
CONF_CELL_COULOMB       = "coulomb"
CONF_CELL_CURRENT       = "current"


CONF_BATTERY_ID         = "battery_sensor"
CONF_CELL_ID            = "cell_sensor"


BAT_TYPES = {
    CONF_VOLTAGE: sensor.sensor_schema(
        PytesEBoxBatterySensor,
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=3,
        device_class=DEVICE_CLASS_VOLTAGE,
    ),
    CONF_CURRENT: sensor.sensor_schema(
        PytesEBoxBatterySensor,
        unit_of_measurement=UNIT_AMPERE,
        accuracy_decimals=3,
        device_class=DEVICE_CLASS_CURRENT,
    ),
    CONF_TEMPERATURE: sensor.sensor_schema(
        PytesEBoxBatterySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
    ),
    CONF_TEMPERATURE_LOW: sensor.sensor_schema(
        PytesEBoxBatterySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
    ),
    CONF_TEMPERATURE_HIGH: sensor.sensor_schema(
        PytesEBoxBatterySensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
    ),
    CONF_VOLTAGE_LOW: sensor.sensor_schema(
        PytesEBoxBatterySensor,
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=3,
        device_class=DEVICE_CLASS_VOLTAGE,
    ),
    CONF_VOLTAGE_HIGH: sensor.sensor_schema(
        PytesEBoxBatterySensor,
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=3,
        device_class=DEVICE_CLASS_VOLTAGE,
    ),
    CONF_COULOMB: sensor.sensor_schema(
        PytesEBoxBatterySensor,
        unit_of_measurement=UNIT_PERCENT,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_BATTERY,
    ),
    CONF_SOC_VOLTAGE: sensor.sensor_schema(
        PytesEBoxBatterySensor,
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=3,
        device_class=DEVICE_CLASS_VOLTAGE,
    ),    
    CONF_WORK_STATUS: sensor.sensor_schema(
        PytesEBoxBatterySensor,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_EMPTY,
    ),
    CONF_CELLS: sensor.sensor_schema(
        PytesEBoxBatterySensor,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_EMPTY,
    ),
    CONF_TOTAL_COULOMB: sensor.sensor_schema(
        PytesEBoxBatterySensor,
        unit_of_measurement=UNIT_AMPERE_HOURS,
        accuracy_decimals=3,
        device_class=DEVICE_CLASS_EMPTY,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_REAL_COULOMB: sensor.sensor_schema(
        PytesEBoxBatterySensor,
        unit_of_measurement=UNIT_AMPERE_HOURS,
        accuracy_decimals=3,
        device_class=DEVICE_CLASS_EMPTY,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_TOTAL_POWER_IN: sensor.sensor_schema(
        PytesEBoxBatterySensor,
        unit_of_measurement=UNIT_AMPERE_HOURS,
        accuracy_decimals=3,
        device_class=DEVICE_CLASS_EMPTY,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    CONF_TOTAL_POWER_OUT: sensor.sensor_schema(
        PytesEBoxBatterySensor,
        unit_of_measurement=UNIT_AMPERE_HOURS,
        device_class=DEVICE_CLASS_EMPTY,
        state_class=STATE_CLASS_MEASUREMENT,
        accuracy_decimals=3,
    ),
}

CELL_TYPES = {
    CONF_CELL_VOLTAGE: sensor.sensor_schema(
        PytesEBoxBatteryCellSensor,
        unit_of_measurement=UNIT_VOLT,
        accuracy_decimals=3,
        device_class=DEVICE_CLASS_VOLTAGE,
    ),
    CONF_CELL_CURRENT: sensor.sensor_schema(
        PytesEBoxBatteryCellSensor,
        unit_of_measurement=UNIT_AMPERE,
        accuracy_decimals=3,
        device_class=DEVICE_CLASS_CURRENT,
    ),
    CONF_CELL_TEMPERATURE: sensor.sensor_schema(
        PytesEBoxBatteryCellSensor,
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
    ),  
    CONF_CELL_COULOMB: sensor.sensor_schema(
        PytesEBoxBatteryCellSensor,
        unit_of_measurement=UNIT_PERCENT,
        accuracy_decimals=0,
        device_class=DEVICE_CLASS_BATTERY,
    ),
    #unit_of_measurement=UNIT_AMPERE_HOURS,
    #device_class=DEVICE_CLASS_EMPTY,
    #state_class=STATE_CLASS_MEASUREMENT,    
}

BAT_SCHEMA = cv.Schema(
    {cv.Optional(marker): schema for marker, schema in BAT_TYPES.items()}
)
CELL_SCHEMA = cv.Schema(
    {cv.Optional(marker): schema for marker, schema in CELL_TYPES.items()}    
)







# CELL_ARRAYS_SCHEMA = CELLS_ARRAYS_SCHEMA.extend(
#     {cv.GenerateID(): cv.declare_id(PytesEBoxBatteryCell)}
# ).extend({cv.Optional(marker): schema for marker, schema in CELL_TYPES.items()})



CONFIG_SCHEMA = PYTES_E_BOX_COMPONENT_SCHEMA.extend(
    {cv.GenerateID(): cv.declare_id(PytesEBoxBatterySensor)}
).extend({cv.Optional(marker): schema for marker, schema in BAT_TYPES.items()})






            
# CONFIG_SCHEMA = cv.Schema(
#     {
#         cv.GenerateID(): cv.declare_id(PytesEBoxComponent),
#         cv.Optional(CONF_BATTERIES): cv.All(cv.ensure_list(cv.Schema({
#             cv.GenerateID(CONF_BATTERY_ID): cv.declare_id(PytesEBoxBatterySensor),
#             cv.Required(CONF_BATTERY_ID): CV_NUM_BATTERIES,
#             cv.Optional(CONF_BATTERY_ID): BAT_SCHEMA,
#             #cv.Optional(CONF_CELL): CV_NUM_CELLS,

#         }))),
#         cv.Optional(CONF_CELLS): cv.All(cv.ensure_list(cv.Schema({
#             cv.Required(CONF_BATTERY_ID): cv.use_id(PytesEBoxBatterySensor),
#             cv.Required(cv.GenerateID(CONF_CELL_ID)): cv.declare_id(PytesEBoxBatteryCellSensor),
#             cv.Optional(CONF_BATTERY_ID): CELL_SCHEMA,

#         }))),            
#         #cv.Required(CONF_CMD_IDLE_TIME): cv.positive_time_period_milliseconds,
#     }
# )

async def to_code(config):
    var = await cg.get_variable(config[CONF_PYTES_E_BOX_ID])

    bat = cg.new_Pvariable(config[CONF_ID], config[CONF_BATTERY])

    for marker in TYPES:
        if marker_config := config.get(marker):
            sens = await sensor.new_sensor(marker_config)
            cg.add(getattr(bat, f"set_{marker}_sensor")(sens))

    cg.add(paren.register_listener(bat))

    # if CONF_BATTERIES in config:
    #     for battery_config in config[CONF_BATTERIES]:
    #         battery_sensor = await cg.get_variable(battery_config[CONF_BATTERY_ID])
    #         battery = cg.new_Pvariable(battery_sensor)
    #         for marker, sensor_schema in BAT_TYPES.items():
    #             if marker in battery_config:
    #                 sensor_var = await sensor.new_sensor(battery_config[marker])
    #                 cg.add(getattr(battery, f"set_{marker}_sensor")(sensor_var))
    #                 cg.add(var.add_battery_sensor(battery_sensor))

    # if CONF_CELLS in config:
    #     for cell_config in config[CONF_CELLS]:
    #         battery_sensor = await cg.get_variable(cell_config[CONF_BATTERY_ID])
    #         for cell in cell_config[CONF_CELLS]:
    #             cell_sensor = await cg.get_variable(cell[CONF_CELL_ID])
    #             cell_var = cg.new_Pvariable(cell_sensor)
    #             for marker, sensor_schema in CELL_TYPES.items():
    #                 if marker in cell:
    #                     sensor_var = await sensor.new_sensor(cell[marker])
    #                     cg.add(getattr(cell_var, f"set_{marker}_sensor")(sensor_var))
    #                     cg.add(var.add_cell_sensor(cell_var))
