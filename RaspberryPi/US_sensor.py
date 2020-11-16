# Arduino

int captureUltrasonic(){
  digitalWrite(trig, LOW);
  delayMicroseconds(2);

  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  duration = pulseIn(echo, HIGH);
  return duration;
}

int getUltrasonic(String units){
  int duration = captureUltrasonic();
  if(units == "cm"){
    return duration*0.034/2; // these values are from the data sheet
  }
  else if(units == "in"){
    return duration*0.0133/2; //from data sheet
  }
  else {
    return -1;
  }
}


if(right_distance < left_distance){ //on the right side
  backward();
  delay(1500);
  left();
  delay(1400);
  stop();
  forward();
  delay(500);
}

# right < left
# left < right
# object in center
# no object detected