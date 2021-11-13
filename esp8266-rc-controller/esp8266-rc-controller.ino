#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
  
// Set WiFi credentials
#define WIFI_SSID "IndiaOscarTango"
#define WIFI_PASS ""

// UDP
WiFiUDP UDP;
char packet[255];
char reply[] = "Packet received!";
char remote_ip = ""
int remote_port = 5000

void setup() {
  // Setup serial port
  Serial.begin(115200);
  Serial.println();
  
  // Begin WiFi
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  
  // Connecting to WiFi...
  Serial.print("Connecting to ");
  Serial.print(WIFI_SSID);
  // Loop continuously while WiFi is not connected
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(100);
    Serial.print(".");
  }
  
  // Connected to WiFi
  Serial.println();
  Serial.print("Connected! IP address: ");
  Serial.println(WiFi.localIP());
 
  
}
 
void loop() {


    left();
    delay(1000);
    left();
    delay(1000);
    left();
    delay(1000);
    left();
    delay(5000);
    right();
    delay(1000);
    right();
    delay(1000);
    right();
    delay(1000);
    right();

}

void right(){
     UDP.beginPacket(REMOTE_IP, REMOTE_PORT);
    UDP.write("right");
    Serial.print("Message sent: right");
    UDP.endPacket();
}

void left(){
     UDP.beginPacket(REMOTE_IP, REMOTE_PORT);
    UDP.write("left");
    Serial.print("Message sent: left");
    UDP.endPacket();
}
