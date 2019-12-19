int counter = 0;

int mode = 1;
bool mode_1_state = LOW;
bool mode_2_state = LOW;
unsigned long lastModeTime = 0;
int speed = 1000;

int led1_pin = 0;
int led2_pin = 1;
int led3_pin = 2;
int led4_pin = 3;

void setup()
{ 
  pinMode(led1_pin, OUTPUT);
  pinMode(led2_pin, OUTPUT);
  pinMode(led3_pin, OUTPUT);
  pinMode(led4_pin, OUTPUT);
}

void loop()
{ 
  switch (mode) {
    case 1:
    if ((millis()-lastModeTime) > speed){
        digitalWrite(led1_pin, mode_1_state);
        digitalWrite(led2_pin, !mode_1_state);
        digitalWrite(led3_pin, mode_1_state);
        digitalWrite(led4_pin, !mode_1_state);
        mode_1_state = !mode_1_state;
        lastModeTime=millis();
      	counter++;
        if (counter>4) {
          mode++;
          if (mode>2){
            mode=1;
          }
          counter=0;
        }
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
      	counter++;
        if (counter>4) {
          mode++;
          if (mode>2){
            mode=1;
          }
          counter=0;
        }
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
