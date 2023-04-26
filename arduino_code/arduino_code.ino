float inputValue=0;
float inputValue1=0;
float inputValue2=0;
float inputValue3=0;
float inputValue4=0;
float inputValue5=0;
int analogOutputPin = 11; 

void setup()
{
    pinMode(11,OUTPUT);
    pinMode(A0,INPUT);
    pinMode(A1,INPUT);
    pinMode(A2,INPUT);
    pinMode(A3,INPUT);
    pinMode(A4,INPUT);
    pinMode(A5,INPUT);
    Serial.begin(9600);
}

void loop()
{
    inputValue = analogRead(A0);
    inputValue1 = analogRead(A1);
    inputValue2 = analogRead(A2);
    inputValue3 = analogRead(A3);
    inputValue4 = analogRead(A4);
    inputValue5 = analogRead(A5);
    float temp = inputValue*5/1023;
    float temp1 = inputValue1*5/1023;
    float temp2 = inputValue2*5/1023;
    float temp3 = inputValue3*5/1023;
    float temp4 = inputValue4*5/1023;
    float temp5 = inputValue5*5/1023;
    // convert all float to string to avoid delay problem in values    
    String str = String(temp, 4);
    String str1 = String(temp1, 4);
    String str2 = String(temp2, 4);
    String str3 = String(temp3, 4);
    String str4 = String(temp4, 4);
    String str5 = String(temp5, 4);
    Serial.println(str+","+str1+","+str2+","+str3+","+str4+","+str5); 
    delay(2000);
}
