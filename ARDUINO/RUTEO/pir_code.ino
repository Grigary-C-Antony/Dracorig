int PIR_output=5;
int po = 11;
int led=13;
int relay =12;
void setup() {
pinMode(PIR_output, INPUT);
pinMode(led, OUTPUT);
pinMode(relay , OUTPUT);
Serial.begin(9600);
 digitalWrite(11, HIGH);
 }
void loop() {
 
if(digitalRead(5) == HIGH)
{
 digitalWrite(13, HIGH);
   digitalWrite(12, LOW);
 delay(10000);
 Serial.println("motion detected");
 
}
else {
 digitalWrite(13, LOW);
 digitalWrite(12, HIGH);
 Serial.println("scanning");
}
}
