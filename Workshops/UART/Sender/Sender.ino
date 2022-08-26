
int value= 0;
void setup(){
    Serial.begin(9600);
}
void loop(){
    Serial.write(value++);
    delay(1000);
}