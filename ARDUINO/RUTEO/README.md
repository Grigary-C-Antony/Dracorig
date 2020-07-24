# RUTEO

This is a project done in my first year design project for the academics in my college.

Actually this project will make the human detection and will actuate a  light to turn on when a person get detected and also if he goes out then the light will turn off. 

Using this basic project we can automate any bulb fan or other stuff without hustle 


## Materials Required

* [PIR sensor](https://www.amazon.in/Generic-HC-SR501-Sensor-Pyroelectric-Infrared/dp/B00VNWWZM0/ref=sr_1_4?dchild=1&keywords=pir&qid=1595614569&sr=8-4)
* [Relay Module](https://www.amazon.in/SunRobotics-Single-Channel-Arduino-RaspberryPI/dp/B0731F48HN/ref=sr_1_22?crid=JM4BZH3ZV4CA&dchild=1&keywords=relay+module+single+channel&qid=1595614649&sprefix=relay+module+single+%2Caps%2C491&sr=8-22)
* [Arduino](https://www.amazon.in/Robotbanao-Atmega328p-Cable-Length-Black/dp/B06XBMB9T1/ref=sxin_7_ac_d_rm?ac_md=0-0-YXJkdWlubyB1bm8%3D-ac_d_rm&crid=DET8IO2B69E0&cv_ct_cx=arduino+uno&dchild=1&keywords=arduino+uno&pd_rd_i=B06XBMB9T1&pd_rd_r=028fc224-284e-4f8f-aff0-dcca471a8f37&pd_rd_w=DEYYD&pd_rd_wg=x5Uwg&pf_rd_p=66a0eddc-0d01-4352-8c36-110e50afc8ce&pf_rd_r=Q9Q8RH6SNH5B3625HN9B&psc=1&qid=1595614714&sprefix=ard%2Caps%2C382&sr=1-1-fe323411-17bb-433b-b2f8-c44f2e1370d4)
* [Jumper Wires](https://www.amazon.in/Jumper-Wires-Male-female-Pieces/dp/B00ZYFX6A2/ref=sr_1_2?crid=2VVUFH8F04QM8&dchild=1&keywords=jumper+wires&qid=1595614747&sprefix=jumber%2Caps%2C463&sr=8-2)


## How to Make Connections


![2020-07-24 23_58_03-Circuit Design App for Makers- circuito io](https://user-images.githubusercontent.com/62613560/88424745-ba132380-ce0b-11ea-8e99-b5b10f4b1f64.png)


## Coding Part

```
int PIR_output=5;              // output of pir sensor
int led=13;                   // led pin
int relay =12;               // relay pin
void setup() {

    pinMode(PIR_output, INPUT); // setting pir output as arduino input
    pinMode(led, OUTPUT);      //setting led as output
    pinMode(relay , OUTPUT);  //setting relay as output
   
 Serial.begin(9600);     //serial communication between arduino and pc
}

void loop() {

if(digitalRead(5) == HIGH)        // reading the data from the pir sensor
{

     digitalWrite(13, HIGH);   // setting led to high
     digitalWrite(12, HIGH);  // setting relay to high
     delay(10000);           // use this delay otherwise sensor will misbehave

 Serial.println("motion detected");
 
}

else {

      digitalWrite(13, LOW);  // setting led to low
      digitalWrite(12, LOW); // setting relay to low

 Serial.println("scanning");

}
}
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
