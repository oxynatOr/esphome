#include "waveshare_epaper.h"
#include "waveshare_lut.h"
#include "esphome/core/log.h"
#include "esphome/core/application.h"
#include "esphome/core/helpers.h"
#include <cinttypes>

namespace esphome {
namespace waveshare_epaper {

static const char *const TAG = "waveshare_7.5v2_partialrefresh";

/* 7.50inV2 with partial and fast refresh */
bool WaveshareEPaper7P5InV2P::wait_until_idle_() {
  if (this->busy_pin_ == nullptr) {
    return true;
  }

  const uint32_t start = millis();
  while (this->busy_pin_->digital_read()) {
    this->command(0x71);
    if (millis() - start > this->idle_timeout_()) {
      ESP_LOGE(TAG, "Timeout while displaying image!");
      return false;
    }
    App.feed_wdt();
    delay(10);  // NOLINT
  }
  return true;
}

void WaveshareEPaper7P5InV2P::reset_() {
  if (this->reset_pin_ != nullptr) {
    this->reset_pin_->digital_write(true);
    delay(20);  // NOLINT
    this->reset_pin_->digital_write(false);
    delay(2);  // NOLINT
    this->reset_pin_->digital_write(true);
    delay(20);  // NOLINT
  }
}

void WaveshareEPaper7P5InV2P::turn_on_display_() {
  this->command(0x12);
  delay(100);  // NOLINT
  this->wait_until_idle_();
}

void WaveshareEPaper7P5InV2P::initialize() {
  this->reset_();

  // COMMAND POWER SETTING
  this->command(0x01);
  this->data(0x07);
  this->data(0x07);
  this->data(0x3f);
  this->data(0x3f);

  // COMMAND BOOSTER SOFT START
  this->command(0x06);
  this->data(0x17);
  this->data(0x17);
  this->data(0x28);
  this->data(0x17);

  // COMMAND POWER DRIVER HAT UP
  this->command(0x04);
  delay(100);  // NOLINT
  this->wait_until_idle_();

  // COMMAND PANEL SETTING
  this->command(0x00);
  this->data(0x1F);

  // COMMAND RESOLUTION SETTING
  this->command(0x61);
  this->data(0x03);
  this->data(0x20);
  this->data(0x01);
  this->data(0xE0);

  // COMMAND DUAL SPI MM_EN, DUSPI_EN
  this->command(0x15);
  this->data(0x00);

  // COMMAND VCOM AND DATA INTERVAL SETTING
  this->command(0x50);
  this->data(0x10);
  this->data(0x07);

  // COMMAND TCON SETTING
  this->command(0x60);
  this->data(0x22);

/*
  // COMMAND ENABLE FAST UPDATE
  this->command(0xE0);
  this->data(0x02);
  this->command(0xE5);
  this->data(0x5A);
*/
  // COMMAND POWER DRIVER HAT DOWN
  this->command(0x02);
}

void WaveshareEPaper7P5InV2P::initialize_fast() {
  this->reset_();

  // COMMAND PANEL SETTING
  this->command(0x00);
  this->data(0x1F);

  // COMMAND VCOM AND DATA INTERVAL SETTING
  this->command(0x50);
  this->data(0x10);
  this->data(0x07);  

  // COMMAND POWER DRIVER HAT UP
  this->command(0x04);
  delay(100);  // NOLINT
  this->wait_until_idle_();

  // COMMAND BOOSTER SOFT START
  this->command(0x06);
  this->data(0x27);
  this->data(0x27);
  this->data(0x18);
  this->data(0x17);

  // COMMAND ENABLE FAST UPDATE
  this->command(0xE0);
  this->data(0x02);
  this->command(0xE5);
  this->data(0x5A);

}

void WaveshareEPaper7P5InV2P::initialize_part() {
  this->reset_();

  // COMMAND PANEL SETTING
  this->command(0x00);
  this->data(0x1F);

  // COMMAND POWER DRIVER HAT UP
  this->command(0x04);
  delay(100);  // NOLINT
  this->wait_until_idle_();


  // COMMAND ENABLE FAST UPDATE
  this->command(0xE0);
  this->data(0x02);
  this->command(0xE5);
  this->data(0x6E);
  
}

void HOT WaveshareEPaper7P5InV2P::display() {
  uint32_t buf_len = this->get_buffer_length_();

  // COMMAND POWER ON
  ESP_LOGI(TAG, "Power on the display and hat");

  this->command(0x04);
  delay(200);  // NOLINT
  this->wait_until_idle_();

  if (this->full_update_every_ == 1) {
    this->command(0x13);
    for (uint32_t i = 0; i < buf_len; i++) {
      this->data(~(this->buffer_[i]));
    }

    this->turn_on_display_();

    this->command(0x02);
    this->wait_until_idle_();
    return;
  }

  this->command(0x50);
  this->data(0xA9);
  this->data(0x07);

  if (this->at_update_ == 0) {
    // Enable fast refresh
    this->command(0xE5);
    this->data(0x5A);

    this->command(0x92);

    this->command(0x10);
    delay(2);  // NOLINT
    for (uint32_t i = 0; i < buf_len; i++) {
      this->data(~(this->buffer_[i]));
    }

    delay(100);  // NOLINT
    this->wait_until_idle_();

    this->command(0x13);
    delay(2);  // NOLINT
    for (uint32_t i = 0; i < buf_len; i++) {
      this->data(this->buffer_[i]);
    }

    delay(100);  // NOLINT
    this->wait_until_idle_();

    this->turn_on_display_();

  } else {
    // Enable partial refresh
    this->command(0xE5);
    this->data(0x6E);

    // Activate partial refresh and set window bounds
    this->command(0x91);
    this->command(0x90);

    this->data(0x00);
    this->data(0x00);
    this->data((get_width_internal() - 1) >> 8 & 0xFF);
    this->data((get_width_internal() - 1) & 0xFF);

    this->data(0x00);
    this->data(0x00);
    this->data((get_height_internal() - 1) >> 8 & 0xFF);
    this->data((get_height_internal() - 1) & 0xFF);

    this->data(0x01);

    this->command(0x13);
    delay(2);  // NOLINT
    for (uint32_t i = 0; i < buf_len; i++) {
      this->data(this->buffer_[i]);
    }

    delay(100);  // NOLINT
    this->wait_until_idle_();

    this->turn_on_display_();
  }

  ESP_LOGV(TAG, "Before command(0x02) (>> power off)");
  this->command(0x02);
  this->wait_until_idle_();
  ESP_LOGV(TAG, "After command(0x02) (>> power off)");

  this->at_update_ = (this->at_update_ + 1) % this->full_update_every_;
}

int WaveshareEPaper7P5InV2P::get_width_internal() { return 800; }
int WaveshareEPaper7P5InV2P::get_height_internal() { return 480; }
uint32_t WaveshareEPaper7P5InV2P::idle_timeout_() { return 10000; }
void WaveshareEPaper7P5InV2P::dump_config() {
  LOG_DISPLAY("", "Waveshare E-Paper", this);
  ESP_LOGCONFIG(TAG, "  Model: 7.5inV2rev2");
  ESP_LOGCONFIG(TAG, "  Full Update Every: %" PRIu32, this->full_update_every_);
  LOG_PIN("  Reset Pin: ", this->reset_pin_);
  LOG_PIN("  DC Pin: ", this->dc_pin_);
  LOG_PIN("  Busy Pin: ", this->busy_pin_);
  LOG_UPDATE_INTERVAL(this);
}
void WaveshareEPaper7P5InV2P::set_full_update_every(uint32_t full_update_every) {
  this->full_update_every_ = full_update_every;
}


}
}