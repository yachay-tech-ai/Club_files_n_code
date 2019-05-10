// assign pin num
//int right_pin = 8;
//int left_pin = 9;
//int forward_pin = 10;
//int reverse_pin = 11;

const int rightA = 8,
          rightB = 9,
          leftA = 10,
          leftB = 11;


// duration for output
int Time = 50;
// initial command
int command = 0;

void setup() {
  pinMode(leftA, OUTPUT);
  pinMode(leftB, OUTPUT);
  pinMode(rightA, OUTPUT);
  pinMode(rightB, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  //receive command
  if (Serial.available() > 0){
    command = Serial.read();
  }
  else{
    reset();
  }
   send_command(command,Time);
}

void right(int Time){
  digitalWrite(leftA, LOW);
  delay(Time);
}

void left(int Time){
  digitalWrite(rightA, LOW);
  delay(Time);
}

void forward(int Time){
  digitalWrite(leftA, LOW);
  digitalWrite(rightA,LOW);
  delay(Time);
}

void reverse(int Time){
  digitalWrite(leftB, LOW);
  digitalWrite(rightB,LOW);
  delay(Time);
}


void reset(){
  digitalWrite(rightB, HIGH);
  digitalWrite(rightA, HIGH);
  digitalWrite(leftA, HIGH);
  digitalWrite(leftB, HIGH);
  
}

void send_command(int command, int Time){
  switch (command){

     //reset command
     case 0: reset(); break;

     // single command
     case 6: forward(Time); break;
     case 7: reverse(Time); break;
     case 3: right(Time); break;
     case 4: left(Time); break;

     default: Serial.print("Invalid Command\n");
    }
}
