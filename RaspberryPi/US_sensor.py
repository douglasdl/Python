#include <Arduino.h>
#include <Servo.h>

int leftLED = 2;
int rightLED = 3;

int buzzer = 7;

int irRecv = 13;

int leftIR = A0;
int rightIR = A1;

int trig = A2;
int echo = A3;

Servo myservo;

int distanceCm, distanceIn, duration;
int i = 0;
int time;
int left_distance =0;
int right_distance = 0;
int center_distance = 0;
const int stop_time = 5;

// Motors
#define ENL 5
#define L1 8
#define L2 9

#define ENR 6
#define R1 10
#define R2 12

#define OFF 0
#define QUARTERSPEED 64
#define HALFSPEED 127
#define FULLSPEED 255

#define SERVO_CENTER 25

int threshold = 10;
int obstacle;

String direction;

void ctrlLEDs(int state){
  if(state == 1){
    digitalWrite(leftLED, HIGH);
    digitalWrite(rightLED, HIGH);
  }
  else if(state == 0){
    digitalWrite(leftLED, LOW);
    digitalWrite(rightLED, LOW);
  }
}

void flashLEDs(int rate1, int rate2){
  ctrlLEDs(HIGH);
  delay(rate1);
  ctrlLEDs(LOW);
  delay(rate2);
}

void setup() {
    // put your setup code here, to run once:
    pinMode(leftLED, OUTPUT);
    pinMode(rightLED, OUTPUT);

    pinMode(trig, OUTPUT);
    pinMode(echo, INPUT);
    //pinMode(buzzer, OUTPUT);

    pinMode(irRecv, INPUT);
    digitalWrite(buzzer,LOW);

    myservo.attach(11);
    myservo.write(SERVO_CENTER);

    pinMode(ENL, OUTPUT);
    pinMode(L1, OUTPUT);
    pinMode(L2, OUTPUT);

    pinMode(ENR, OUTPUT);
    pinMode(R1, OUTPUT);
    pinMode(R2, OUTPUT);

    Serial.begin(9600);

    for(int i=0; i<3; i++){
      flashLEDs(500,500);
      i+=1;
    }
}


void scanServo(){
  int pos;
  //int obj = abs(getUltrasonic("in"));

  for(pos = 0; pos <= 100; pos += 1) // goes from 0 degrees to 180 degrees
  {                                  // in steps of 1 degree
   Serial.print("Postion = ");
   Serial.println(pos);
   myservo.write(pos);              // tell servo to go to position in variable 'pos'
   delay(15);                       // waits 15ms for the servo to reach the position
  }
  for(pos = 100; pos>=0; pos-=1)     // goes from 180 degrees to 0 degrees
  {
   Serial.print("Postion = ");
   Serial.println(pos);
   myservo.write(pos);              // tell servo to go to position in variable 'pos'
   delay(15);                       // waits 15ms for the servo to reach the position
  }
}

int captureUltrasonic(){
  digitalWrite(trig, LOW);
  delayMicroseconds(2);

  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  duration = pulseIn(echo, HIGH);
  return duration;
}

void printUltrasonic(){
  duration = captureUltrasonic();

  distanceCm = duration*0.034/2;
  distanceIn = duration*0.0133/2;

  Serial.print("Distance = ");
  Serial.print(distanceCm);
  Serial.print(" cm ");

  Serial.print("Distance = ");
  Serial.print(distanceIn);
  Serial.println(" in ");

  delay(1000);
}

int getUltrasonic(String units){
  duration = captureUltrasonic();
  if(units == "cm"){
    return duration*0.034/2;
  }
  else if(units == "in"){
    return duration*0.0133/2;
  }
  else {
    return -1;
  }
}

void backward(){
  direction = "Backing up ... ";
  Serial.println(direction);
  digitalWrite(L1, LOW);
  digitalWrite(L2, HIGH);

  digitalWrite(R1, LOW);
  digitalWrite(R2, HIGH);
}

void forward(){
  direction = "Driving Forward ... ";
  Serial.println(direction);
  myservo.write(SERVO_CENTER);
  digitalWrite(L1, HIGH);
  digitalWrite(L2, LOW);

  digitalWrite(R1, HIGH);
  digitalWrite(R2, LOW);

}

void stop(){
  direction = "Stopping ... ";
  Serial.println(direction);
  digitalWrite(L1, LOW);
  digitalWrite(L2, LOW);

  digitalWrite(R1, LOW);
  digitalWrite(R2, LOW);
}

void right(){
  direction = "Turning RIGHT ... ";
  Serial.println(direction);
  digitalWrite(L1, HIGH);
  digitalWrite(L2, LOW);

  digitalWrite(R1, LOW);
  digitalWrite(R2, HIGH);
}


void left(){
  direction = "Turning LEFT ... ";
  Serial.println(direction);
  digitalWrite(L1, LOW);
  digitalWrite(L2, HIGH);

  digitalWrite(R1, HIGH);
  digitalWrite(R2, LOW);
}

void setSpeed(int lspeed, int rspeed){
  analogWrite(ENL, lspeed); //lspeed:0-255
  analogWrite(ENR, rspeed); //rspeed:0-255

  if(lspeed > 0){
    digitalWrite(ENL, HIGH);
  }
  else{
    digitalWrite(ENL, LOW);
  }

  if(rspeed > 0){
    digitalWrite(ENR, HIGH);
  }
  else{
    digitalWrite(ENR, LOW);
  }

}

void executeTankTest(){
  while(i==0){
    setSpeed(127, 127);
    forward();
    delay(5000);
    stop();
    backward();
    delay(5000);
    stop();
    left();
    delay(2500);
    right();
    delay(2500);
    stop();
    i = 1;

    Serial.println("Program complete!");
  }
}

void avoidObj(){
  setSpeed(HALFSPEED,HALFSPEED);
  obstacle = abs(getUltrasonic("in"));
  Serial.print("Distance = ");
  Serial.println(obstacle);

  while(obstacle > threshold){
    ctrlLEDs(LOW);
    forward();
    obstacle = abs(getUltrasonic("in"));
  }

  while(obstacle <= threshold){
    ctrlLEDs(HIGH);
    stop();
    setSpeed(QUARTERSPEED,QUARTERSPEED);
    backward();
    delay(1500);
    right();
    delay(1500);
    obstacle = abs(getUltrasonic("in"));
  }

  Serial.print("Distance = ");
  Serial.println(obstacle);
}

void sweepServo(){

  int pos;
  for(pos = -10; pos <= 90; pos += 1) // goes from 0 degrees to 180 degrees
  {                                  // in steps of 1 degree
   Serial.print("Postion = ");
   Serial.println(pos);
   myservo.write(pos);              // tell servo to go to position in variable 'pos'
   delay(15);                       // waits 15ms for the servo to reach the position

  }
  for(pos = 90; pos>=-10; pos-=1)     // goes from 180 degrees to 0 degrees
  {
   Serial.print("Postion = ");
   Serial.println(pos);
   myservo.write(pos);              // tell servo to go to position in variable 'pos'
   delay(15);                       // waits 15ms for the servo to reach the position
  }
}

void avoidObjServo(){
  setSpeed(HALFSPEED,HALFSPEED);

  center_distance = abs(getUltrasonic("in"));
  Serial.print("Center distance: ");
  Serial.println(center_distance);

  while(center_distance > threshold){
    ctrlLEDs(LOW);
    forward();
    center_distance = abs(getUltrasonic("in"));
  }

  if(center_distance <= threshold){
    ctrlLEDs(HIGH);
    setSpeed(QUARTERSPEED,QUARTERSPEED);
    stop();
    delay(500);

    // scan right side the robot for obstacles
    for(i=90;i>=-10;i--){
      myservo.write(i);
      delay(stop_time);
    }
    right_distance = abs(getUltrasonic("in"));
    Serial.print("Right distance: ");
    Serial.println(right_distance);
    delay(50);

    // scan left side
    for(i=-10;i<=90;i++){
      myservo.write(i);
      delay(stop_time);
    }
    left_distance = abs(getUltrasonic("in"));
    Serial.print("Left distance: ");
    Serial.println(left_distance);
    delay(50);

    // go back to center
    myservo.write(SERVO_CENTER);

    if(right_distance == left_distance){
      ctrlLEDs(HIGH);
      stop();
      setSpeed(QUARTERSPEED,QUARTERSPEED);
      backward();
      delay(1500);
      right();
      delay(2500);
      forward();
      delay(500);
    }
    else if(right_distance < left_distance){ //on the right side
      backward();
      delay(1500);
      left();
      delay(1400);
      stop();
      forward();
      delay(500);
    }
    else{ //on the left side
     backward();
     delay(1500);
     right();
     delay(1400);
     stop();
     forward();
     delay(500);
    }

    forward();
    center_distance = abs(getUltrasonic("in"));

  }

}

void loop() {
  avoidObjServo();
}

