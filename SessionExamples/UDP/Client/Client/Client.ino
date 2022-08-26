//#if defined(__MBED__)
//  #include <mbed.h>
//  #include "mbed/millis.h"
//  #define delay(x) wait_ms(x)
//  #define PROGMEM
//  #include "mbed/Print.h"
//#endif

#include <UIPEthernet.h>
#include "utility/logging.h"

EthernetUDP udp;
          uint8_t buffer[]= {0,0};

uint8_t data[]={0,0};
int value=0;
void setup() {
  Serial.begin(9600);
  uint8_t mac[6] = {0x00, 0x01, 0x02, 0x03, 0x04, 0x05};
  Ethernet.begin(mac, IPAddress(192, 168, 1, 6));

}

void loop() {
          udp.begin(5050);

        int success;

        success = udp.beginPacket(IPAddress(192, 168, 1, 10), 5000);
        //beginPacket fails if remote ethaddr is unknown. In this case an
        //arp-request is send out first and beginPacket succeeds as soon
        //the arp-response is received.
        if(!success){
          Serial.println("Can't locate address!");
          return;
        }
        data[0]= value/256;
        data[1]= value%256;
        success = udp.write(data, 2);
        success = udp.endPacket();
        //Serial.print("Sent!");

        int size= udp.parsePacket();
        if(size>0){
          udp.read(buffer,2);
          Serial.println(buffer[0]*256+buffer[1]);
        }
        udp.stop();
//        delay(5000);
        value+=100;
       // delay(20);
  }
