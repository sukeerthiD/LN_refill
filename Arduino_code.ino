int out = 12;


void setup() {
  Serial.begin(9600);
  pinMode(out, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);

}

void loop() {
  if (Serial.available())
  {
    Serial.print(Serial.readStringUntil('\n'));
    delay(1000);
    String receivedChars = Serial.readStringUntil('\n');
    if (receivedChars == "ON")
    {
      digitalWrite(LED_BUILTIN, HIGH);
      digitalWrite(out, HIGH);
    }
    else {
      digitalWrite(LED_BUILTIN, LOW);
      digitalWrite(out, LOW);
    }
  }
}
