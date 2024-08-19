#include "pytes_e_box_battery_cell_sensor.h"
#include "esphome/core/helpers.h"
#include "esphome/core/log.h"

namespace esphome {
namespace pytes_e_box {

//static const char *const TAG_BS = "PytesEBoxbattery.sensor";


PytesEBoxBatteryCellSensor::PytesEBoxBatteryCellSensor(int8_t cell_num) { this->cell_num_ = cell_num; }
void PytesEBoxBatteryCellSensor::dump_config() {
  ESP_LOGCONFIG(TAG, "PytesEBox Battery Cell Sensor:");
  //ESP_LOGCONFIG(TAG, " Battery %d", this->bat_num_);
  ESP_LOGCONFIG(TAG, " Cell %d", this->cell_num_);
  LOG_SENSOR("  ","Voltage",this->cell_voltage_sensor_);
  LOG_SENSOR("  ","Current",this->cell_current_sensor_);
  LOG_SENSOR("  ","Temperature",this->cell_temperature_sensor_);
  LOG_SENSOR("  ","Coulomb", this->cell_coulomb_sensor_);
}

void PytesEBoxBatteryCellSensor::on_batn_line_read(bat_index_LineContents *line) { return; 
  // if (this->bat_num_ != line->bat_num) {
  //   return;    
  // }
  if (this->cell_num_ != line->bat_num) {
    return;    
  }  

}

}  // namespace pytes_e_box
}  // namespace esphome