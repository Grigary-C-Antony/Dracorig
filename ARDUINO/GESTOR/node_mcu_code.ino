/*CONNECT A0-PIR,D0-led,D1-relay */

#include <IFTTTWebhook.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

#define ssid "cjp"
#define password "01B77370"
#define myiot


int PIR_output=A0;
int led=D0;
int relay =D1;

void setup() 
{

pinMode(PIR_output, INPUT);
pinMode(led, OUTPUT);
pinMode(relay , OUTPUT);
Serial.begin(9600);
  
  WiFi.mode(WIFI_STA);  
WiFi.begin(ssid,password);
Serial.begin(9600);
while(WiFi.status()!=WL_CONNECTED)  {
Serial.println("Connecting......");
delay(1000); }
Serial.println( WiFi.localIP() );
int i = 10;
  while(WiFi.status() != WL_CONNECTED && i >=0) {
    delay(1000);
    Serial.print(i);
    Serial.print(", ");
    i--;
  }
  Serial.println(" ");// print an empty line

  //print connection result
  if(WiFi.status() == WL_CONNECTED){
    Serial.print("Connected."); 
    Serial.println(" ");// print an empty line
    Serial.print("NodeMCU ip address: "); 
    Serial.println(WiFi.localIP());
  }
  else {
    Serial.println("Connection failed - check your credentials or connection");
  }

}

 void loop ()
 {
  myiot();
 }

 
 void myiot()
 {
  HTTPClient http;
   int ret = 0;
   Serial.print("[HTTP] begin...\n");
   // configure ifttt server and url  should be HTTP only..not https!!!  (http://)   
/******************************************************************************************************************************/    
   
    if (digitalRead(A0) == HIGH)
   { 
 http.begin("http://maker.ifttt.com/trigger/troubleless/with/key/bDbFkWmNDsCvhg2RmaXjNgP1yGydC6s9vF60abCg3vi"); 
 digitalWrite(D0, HIGH);
 digitalWrite(D1, HIGH);
 delay(10000);
 Serial.println("motion detected");
   }
     else
     {
 digitalWrite(D0, HIGH);
 digitalWrite(D1, HIGH);
 Serial.println("scanning");
     }

/***********************************************************************************************************************************/     
    Serial.print("[HTTP] GET...\n");
    // start connection and send HTTP header
    int httpCode = http.GET();
    // httpCode will be negative on error
    if(httpCode > 0) {
    // HTTP header has been send and Server response header has been handled
    Serial.printf("[HTTP] GET code: %d\n", httpCode);

      if(httpCode == HTTP_CODE_OK) {
        String payload = http.getString();
        Serial.println(payload);
      }
    } else {
        ret = -1;
        Serial.printf("[HTTP] GET failed, error: %s\n", http.errorToString(httpCode).c_str());
        delay(500); // wait for half sec before retry again
    }

    http.end();

 }
 
