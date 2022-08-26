void setup(){
    Serial.begin(9600);
}
void loop(){
    if(Serial.available()){
        uint8_t x= Serial.read();
        Serial.print("Data Received is ");
        Serial.println(x);
    }
}