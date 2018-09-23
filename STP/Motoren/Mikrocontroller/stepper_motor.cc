#include <Stepper.h>
 
/* STEPS muss auf die Anzahl der Stepps des verwendeten Motors angepasst werden */
#define STEPS 100
 
// eine Instanz aus der Klasse Stepper wird erzeugt
// sie bekommt die Anzahl der Steps und die Pins, an die der Schrittmotor
// angeschlossen ist übermittelt
Stepper stepper(STEPS, 4, 23, 24);
 
int previous = 0;
 
void setup(){
  stepper.setSpeed(30);  // setzt die Geschwindigkeit des Motors in Umdrehungen pro Minute
}
 
void loop(){
  int val = analogRead(0);
  // dreht den Motor ja nach Sensorwert (Potentiometer)
  stepper.step(val - previous);
  previous = val;
}
