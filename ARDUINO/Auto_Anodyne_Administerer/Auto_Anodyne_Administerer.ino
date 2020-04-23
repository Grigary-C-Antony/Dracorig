

String Name,Age,Num1,Num2,Result,Cal,date,onnulla;

void setup() {
 
pinMode(A0,OUTPUT);
  Serial.begin(9600);
    while (Serial.available() == 0)
    {}    
    onnulla = Serial.readString();
    Serial.println(onnulla);
    Serial.println(" ");
    Serial.println("########################################################################################");
    Serial.println("                                AUTO ANODYNE ADMINISTERER");
    Serial.println("                                       S5 PROJECT ");
    Serial.println("*****************************************************************************************");
    Serial.println(" ");    
    Serial.print("Date :");
    while (Serial.available() == 0)
    {}    
    date = Serial.readString();
    Serial.println(date);
     Serial.println(" ");
    

    Serial.println("What is Patient's Name?");
    while (Serial.available() == 0)
    {}
    
    Name = Serial.readString();
    Serial.print("NAME:");
    Serial.println(Name);
     Serial.println(" ");


    Serial.println("What is Patient's age?");
    while (Serial.available() == 0)
    {}
    Age = Serial.readString();
    Serial.print("Patient's age is : ");
    Serial.println(Age.toInt());

    if (Age.toInt() > 18)
    {
      
      Serial.println("It's an Adult!");
      
      }

     else {
      
      Serial.println("It's a Child!!!!");
     
      }
       Serial.println(" ");

     Serial.println("Enter Dose : ");
      while (Serial.available() == 0)
    {}

    Num1 = Serial.readString();
    Serial.print(Num1.toInt());
    Serial.println(" ml");
     Serial.println(" ");

    Serial.println("Enter Interval : ");
    while (Serial.available() == 0)
    {}
    Num2 = Serial.readString();
    Serial.print(Num2.toInt());
    Serial.println("0 s");
     Serial.println(" ");
      Serial.println(" ");
      
    


    Serial.println("                                    ANASTHESIA IS STARTING");
        

}

void loop() {
  
if (Num1.toInt()<=5&&Num2.toInt()<=5)
{
  digitalWrite(A0,HIGH);
      delay(5000);
       Serial.print("Anasthesia at  : ");
       Serial.print(Num1.toInt());
       Serial.print("-*-");
       Serial.println(Num2.toInt()); 
        Serial.println(" ");  
      digitalWrite(A0,LOW);
      delay(10000);
  }
  else if (Num1.toInt()<=5&&Num2.toInt()==5)
{
  digitalWrite(A0,HIGH);
      delay(3000);
       Serial.print("Anasthesia at  : ");
       Serial.print(Num1.toInt());
       Serial.print("-*-");
       Serial.println(Num2.toInt()); 
        Serial.println(" ");  
      digitalWrite(A0,LOW);
      delay(10000);
  }
   else if (Num1.toInt()==5&&Num2.toInt()==5)
{
  digitalWrite(A0,HIGH);
      delay(5000);
       Serial.print("Anasthesia at  : ");
       Serial.print(Num1.toInt());
       Serial.print("-*-");
       Serial.println(Num2.toInt());
        Serial.println(" ");   
      digitalWrite(A0,LOW);
      delay(10000);
  }
   else if (Num1.toInt()==5&&Num2.toInt()<=5)
{
  digitalWrite(A0,HIGH);
      delay(5000);
       Serial.print("Anasthesia at  : ");
       Serial.print(Num1.toInt());
       Serial.print("-*-");
       Serial.println(Num2.toInt());
        Serial.println(" ");   
      digitalWrite(A0,LOW);
      delay(20000);
  }
   else if (Num1.toInt()>=5&&Num2.toInt()>=5)
{
  digitalWrite(A0,HIGH);
      delay(10000);
       Serial.print("Anasthesia at  : ");
       Serial.print(Num1.toInt());
       Serial.print("-*-");
       Serial.println(Num2.toInt()); 
        Serial.println(" ");  
      digitalWrite(A0,LOW);
      delay(20000);
  }
   else if (Num1.toInt()>=5&&Num2.toInt()==5)
{
  digitalWrite(A0,HIGH);
      delay(10000);
       Serial.print("Anasthesia at  : ");
       Serial.print(Num1.toInt());
       Serial.print("-*-");
       Serial.println(Num2.toInt()); 
        Serial.println(" ");  
      digitalWrite(A0,LOW);
      delay(10000);
  }
   else(Num1.toInt()==5&&Num2.toInt()>=5);
{
  digitalWrite(A0,HIGH);
      delay(5000);
       Serial.print("Anasthesia at  : ");
       Serial.print(Num1.toInt());
       Serial.print("-*-");
       Serial.println(Num2.toInt()); 
        Serial.println(" ");  
      digitalWrite(A0,LOW);
      delay(20000);
  }
}
