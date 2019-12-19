bool on = true;

int light = 0;
int light_threshold = 100;

int mode = 0;
bool mode_1_state = LOW;
bool mode_2_state = LOW;
unsigned long lastModeTime = 0;
int speed = 1000;

const int buttonPin = 6;
int buttonState;
int lastButtonState = LOW;
unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 50;

int led1_pin = 2;
int led2_pin = 3;
int led3_pin = 4;
int led4_pin = 5;

int ldr_pin = A0;

void setup()
{ 
  Serial.begin(9600);
  pinMode(ldr_pin, INPUT);
  pinMode(buttonPin, INPUT);
  pinMode(led1_pin, OUTPUT);
  pinMode(led2_pin, OUTPUT);
  pinMode(led3_pin, OUTPUT);
  pinMode(led4_pin, OUTPUT);
}

void loop()
{ 
  light = analogRead(ldr_pin);
  int reading = digitalRead(buttonPin);
  
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }
  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;
      if (buttonState == HIGH) {
        mode++;
        digitalWrite(led1_pin, LOW);
        digitalWrite(led2_pin, LOW);
        digitalWrite(led3_pin, LOW);
        digitalWrite(led4_pin, LOW);
        if (mode>2){
          mode=1;
        }
        lastModeTime = millis();
        Serial.print(mode);
      }
    }
  }
  lastButtonState = reading;

  if (light<light_threshold){
    on=true;
  }
  else {
    on=false;
  }
   
  if (on){
    switch (mode) {
      case 1:
      if ((millis()-lastModeTime) > speed){
          digitalWrite(led1_pin, mode_1_state);
          digitalWrite(led2_pin, !mode_1_state);
          digitalWrite(led3_pin, mode_1_state);
          digitalWrite(led4_pin, !mode_1_state);
          mode_1_state = !mode_1_state;
          lastModeTime=millis();
      }
      break;
      case 2:
      if ((millis()-lastModeTime) > speed){
          digitalWrite(led1_pin, mode_2_state);
          digitalWrite(led2_pin, mode_2_state);
          digitalWrite(led3_pin, mode_2_state);
          digitalWrite(led4_pin, mode_2_state);
          mode_2_state = !mode_2_state;
          lastModeTime=millis();
      }
      break;
      default:
      digitalWrite(led1_pin, HIGH);
      digitalWrite(led2_pin, HIGH);
      digitalWrite(led3_pin, HIGH);
      digitalWrite(led4_pin, HIGH);
      break;
    }
  }
  else {
    digitalWrite(led1_pin, LOW);
    digitalWrite(led2_pin, LOW);
    digitalWrite(led3_pin, LOW);
    digitalWrite(led4_pin, LOW);
    on = false;
  }
}
