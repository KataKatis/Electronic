int X = A1;
int Y = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.print("X: ");
  Serial.print(analogRead(X));
  Serial.print(" Y: ");
  Serial.println(analogRead(Y));
}
