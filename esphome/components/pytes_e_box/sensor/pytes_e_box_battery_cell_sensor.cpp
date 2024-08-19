#include "pytes_e_box_battery_cell_sensor.h"
#include "esphome/core/helpers.h"
#include "esphome/core/log.h"

namespace esphome {
namespace pytes_e_box {

//static const char *const TAG_BS = "PytesEBoxbattery.sensor";


PytesEBoxBatteryCellSensor::PytesEBoxBatteryCellSensor(int8_t bat_num, int8_t cell_num) { this->bat_num_ = bat_num; this->cell_num_ = cell_num; }
void PytesEBoxBatteryCellSensor::dump_config() {
  ESP_LOGCONFIG(TAG, "PytesEBox Battery Cell Sensor:");
  ESP_LOGCONFIG(TAG, " Battery %d", this->bat_num_);
  ESP_LOGCONFIG(TAG, " Cell %d", this->cell_num_);
  LOG_SENSOR("  ","Voltage",this->cell_voltage_sensor_);
  LOG_SENSOR("  ","Current",this->cell_current_sensor_);
  LOG_SENSOR("  ","Temperature",this->cell_temperature_sensor_);
  LOG_SENSOR("  ","Coulomb", this->cell_coulomb_sensor_);
}

void PytesEBoxBatteryCellSensor::on_batn_line_read(bat_index_LineContents *line) { 
  if (this->bat_num_ != line->bat_num) {
    return;    
  }
  if (this->cell_num_ != line->bat_num) {
    return;    
  }  


  /*
  if (this->bat_num_ != line->bat_num && this->cell_num_ != line->cell_num) {
    return;    
  }  
*/
  if (this->cell_voltage_sensor_ != nullptr) {
  this->cell_voltage_sensor_->publish_state(((float)line->cell_volt) / 1000.0f);
  }
  
  if (this->cell_current_sensor_ != nullptr) {
  this->cell_current_sensor_->publish_state(((float)line->cell_curr) / 1000.0f);
  }
  
  if (this->cell_temperature_sensor_ != nullptr) {
  this->cell_temperature_sensor_->publish_state(((float)line->cell_tempr) / 1000.0f);
  }

  if (this->cell_coulomb_sensor_ != nullptr) {
  this->cell_coulomb_sensor_->publish_state(((float)line->cell_coulomb) / 1000.0f);
  }


// this->cell_voltage_sensor_
// this->cell_voltage_sensor_

// this->cell_current_sensor_
// this->cell_current_sensor_

// this->cell_temperature_sensor_
// this->cell_temperature_sensor_
  
// this->cell_coulomb_sensor_
// this->cell_coulomb_sensor_

}

}  // namespace pytes_e_box
}  // namespace esphome
