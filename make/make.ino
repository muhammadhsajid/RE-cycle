#include <Servo.h>
#include <AccelStepper.h>
#define DELAY 7
#define LONGDELAY 500

#define dirPin 4
#define stepPin 5
#define motorInterfaceType 1

#define pin1 2
#define pin2 3

  Servo s_tilt1;
  Servo s_tilt2;
  AccelStepper stepper = AccelStepper(motorInterfaceType, stepPin, dirPin);

void setup() {
  // put your setup code here, to run once:
  s_tilt1.attach(pin1);
  s_tilt2.attach(pin2);

  s_tilt1.write(90);
  s_tilt2.write(90);

  stepper.setMaxSpeed(200);
  stepper.setAcceleration(200);

  Serial.begin(9600);
  Serial.setTimeout(1);

  randomSeed(analogRead(0));

  delay(1000);
}

void tiltright() {
  for (int i = 90; i <= 120; i++) {
    s_tilt1.write(i);
    s_tilt2.write(180 - i);
    delay(DELAY);
  }
  delay(LONGDELAY);
  for (int i = 120; i >= 90; i--) {
    s_tilt1.write(i);
    s_tilt2.write(180 - i);
    delay(DELAY);
  }
}

void tiltleft() {
  for (int i = 90; i >= 60; i--) {
    s_tilt1.write(i);
    s_tilt2.write(180 - i);
    delay(DELAY);
  }
  delay(LONGDELAY);
  for (int i = 60; i <= 90; i++) {
    s_tilt1.write(i);
    s_tilt2.write(180 - i);
    delay(DELAY);
  }
}

void tiltforward() {
  stepper.moveTo(50);
  stepper.runToPosition();
  tiltright();
  stepper.moveTo(0);
  stepper.runToPosition();
}

void direction(int x) {
  if (x == 1) tiltright();
  else if (x == 2) tiltleft();
  else if (x == 3) tiltforward();
}

int list[] = {1, 2, 3, 1, 2, 3};

void loop() {
  // for testing
  /*
  for (int i = 0; i < 6; i++) {
    delay(2000);
    direction(list[i]);
  }
  */
  while (!Serial.available());
  int incoming = Serial.readString().toInt();
  Serial.print(incoming);
  if (incoming == 1) tiltright();
  else if (incoming == 2) tiltleft();
  else if (incoming == 3) tiltforward();
}
