int SW = 2;
int X = A1;
int Y = A0;

void setup() {
  pinMode(SW, INPUT); // port 2 of arduino uno card is an input
  Serial.begin(9600);
}

void loop() {
  Serial.print("X: ");
  Serial.print(analogRead(X));
  Serial.print(" Y: ");
  Serial.print(analogRead(Y));
  Serial.print(" SW: ");
  Serial.println(digitalRead(SW));
  delay(250); 
}
