/*******************************************************************
 * basic_move
 
  Control the direction and speed of motors rotation by pwm,
  to make the car go forward, backward, left turn, right turn and stop.

******************************************************************/
#include "Arduino.h"
#include <SoftPWM.h>

/*
 *  [0]--|||--[1]
 *   |         |
 *   |         |
 *   |         |
 *   |         |
 *  [3]-------[2]
 */
/** Set the pins for the motors */
#define MOTOR_PINS       (uint8_t[8]){3, 4, 5, 6, A3, A2, A1, A0} 
/** Set the positive and negative directions for the motors */
#define MOTOR_DIRECTIONS (uint8_t[4]){1, 0, 0, 1}

#define MOTOR_POWER_MIN 28  // 28/255

int8_t power = 0;

void setup() {
  Serial.begin(115200);
  Serial.println("Zeus Car basic move");
  SoftPWMBegin(); //init pwm
  carBegin(); // init motor pins

}

void loop() {
  
  for (power = 0; power < 100; power += 10) {
    Serial.print("forward ");Serial.println(power);
    carForward(power);
    delay(100);
  }
  for (power = 100; power > 0; power -= 10) {
    Serial.print("forward ");Serial.println(power);
    carForward(power);
    delay(100);
  }

  for (power = 0; power < 100; power += 10) {
    Serial.print("backward ");Serial.println(power);
    carBackward(power);
    delay(100);
  }
  for (power = 100; power > 0; power -= 10) {
    Serial.print("backward ");Serial.println(power);
    carBackward(power);
    delay(100);
  }

  for (power = 0; power < 100; power += 10) {
    Serial.print("turn left ");Serial.println(power);
    carTurnLeft(power);
    delay(100);
  }
  for (power = 100; power > 0; power -= 10) {
    Serial.print("turn left ");Serial.println(power);
    carTurnLeft(power);
    delay(100);
  }

  for (power = 0; power < 100; power += 10) {
    Serial.print("turn right ");Serial.println(power);

    carTurnRight(power);
    delay(100);
  }
  for (power = 100; power > 0; power -= 10) {
    Serial.print("turn right ");Serial.println(power);
    carTurnRight(power);
    delay(100);
  }

  Serial.println("stop");
  carStop();
  delay(1000);
}


void carBegin() {
  for (uint8_t i = 0; i < 8; i++) {
    SoftPWMSet(MOTOR_PINS[i], 0);
    SoftPWMSetFadeTime(MOTOR_PINS[i], 100, 100);
  }
}

void carSetMotors(int8_t power0, int8_t power1, int8_t power2, int8_t power3) {
  bool dir[4];
  int8_t power[4] = {power0, power1, power2, power3};
  int8_t newPower[4];

  for (uint8_t i = 0; i < 4; i++) {
    dir[i] = power[i] > 0;

    if (MOTOR_DIRECTIONS[i]) dir[i] = !dir[i];

    if (power[i] == 0) {
      newPower[i] = 0;
    } else {
      newPower[i] = map(abs(power[i]), 0, 100, MOTOR_POWER_MIN, 255);
    }
    SoftPWMSet(MOTOR_PINS[i*2], dir[i] * newPower[i]);
    SoftPWMSet(MOTOR_PINS[i*2+1], !dir[i] * newPower[i]);
  }
}

void carForward(int8_t power) {
    carSetMotors(power, power, power, power);
}

void carBackward(int8_t power) {
    carSetMotors(-power, -power, -power, -power);
}

void carTurnLeft(int8_t power) {
    carSetMotors(-power, power, power, -power);
}

void carTurnRight(int8_t power) {
    carSetMotors(power, -power, -power, power);
}

void carStop() {
    carSetMotors(0, 0, 0, 0);
}