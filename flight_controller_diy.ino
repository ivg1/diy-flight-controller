int eng_right = 2, eng_left = 3, gears = 4;

int throttle = A0;
int joyX = A1, joyY = A2, joyBtn = 5;

void setup() {
  Serial.begin(9600);
  pinMode(eng_right, INPUT_PULLUP);
  pinMode(eng_left, INPUT_PULLUP);
  pinMode(gears, INPUT_PULLUP);
  pinMode(joyBtn, INPUT_PULLUP);
}

float throt_value(float val) {
  return -1 + (2.0 * val / 660.0);
}

float value_x(float val) {
  return float(val - 520) / 520;
}

float value_y(float val) {
  return (520 - val) / 520;
}

void loop() {
  if (digitalRead(gears) == LOW) {
    Serial.print("1;");
  } else {
    Serial.print("0;");
  }
  if (digitalRead(eng_left) == LOW) {
    Serial.print("1;");
  } else {
    Serial.print("0;");
  }
  if (digitalRead(eng_right) == LOW) {
    Serial.print("1;");
  } else {
    Serial.print("0;");
  }
  if (digitalRead(joyBtn) == LOW) {
    Serial.print("1;");
  } else {
    Serial.print("0;");
  }

  Serial.print(throt_value(analogRead(throttle)));
  Serial.print(";");

  Serial.print(value_x(analogRead(joyX)));
  Serial.print(";");
  Serial.println(value_y(analogRead(joyY)));


  delay(10);
}
