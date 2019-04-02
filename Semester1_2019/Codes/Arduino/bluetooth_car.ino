char command;
const int leftForward = 4, leftReverse = 5, rightForward = 6, rightReverse = 7;

void setup(){
  pinMode(leftForward,OUTPUT);   
  pinMode(leftReverse,OUTPUT);   
  pinMode(rightForward,OUTPUT);   
  pinMode(rightReverse,OUTPUT);   
  Serial.begin(9600); 
}
 
void loop(){
  if(Serial.available()>0){
    command = Serial.read();
    Serial.println(command);
  }
   
  if(command == 'a'){//GO FORWARD
    digitalWrite(leftForward,HIGH);
    digitalWrite(leftReverse,LOW);
    digitalWrite(rightForward,HIGH);
    digitalWrite(rightReverse,LOW);
  }
   
  else if(command == 'e'){//GO REVERSE
    digitalWrite(leftForward,LOW);
    digitalWrite(leftReverse,HIGH);
    digitalWrite(rightForward,LOW);
    digitalWrite(rightReverse,HIGH);
  }
   
  else if(command == 'd'){//TURN RIGHT
    digitalWrite(leftForward,LOW);
    digitalWrite(leftReverse,LOW);
    digitalWrite(rightForward,HIGH);
    digitalWrite(rightReverse,LOW);
  }
   
  else if(command == 'b'){//TURN LEFT
    digitalWrite(leftForward,HIGH);
    digitalWrite(leftReverse,LOW);
    digitalWrite(rightForward,LOW);
    digitalWrite(rightReverse,LOW);
  }
   
  else if(command == 'c'){//STOP
    digitalWrite(leftForward,LOW);
    digitalWrite(leftReverse,LOW);
    digitalWrite(rightForward,LOW);
    digitalWrite(rightReverse,LOW);
  }
  delay(70);
}
