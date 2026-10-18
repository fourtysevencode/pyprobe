#include <WiFi.h>

// Replace these with your Wi-Fi credentials
const char* ssid = "-";
const char* password = "-";

WiFiServer httpServer(80);
WiFiServer bannerServer(2323);
WiFiServer customServer(8080);

void setup() {
  Serial.begin(115200);
  delay(1000);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected!");
  Serial.print("ESP32 IP: ");
  Serial.println(WiFi.localIP());

  httpServer.begin();
  bannerServer.begin();
  customServer.begin();

  Serial.println("TCP servers started:");
  Serial.println("Port 80   - HTTP");
  Serial.println("Port 2323 - Banner");
  Serial.println("Port 8080 - Custom");
}

void loop() {
  // Port 80: HTTP server
  WiFiClient httpClient = httpServer.available();

  if (httpClient) {
    unsigned long start = millis();

    while (httpClient.connected() &&
           !httpClient.available() &&
           millis() - start < 2000) {
      delay(1);
    }

    if (httpClient.available()) {
      String request = httpClient.readStringUntil('\n');

      httpClient.println("HTTP/1.1 200 OK");
      httpClient.println("Server: ESP32-WebServer");
      httpClient.println("Content-Type: text/plain");
      httpClient.println("Connection: close");
      httpClient.println();
      httpClient.println("ESP32 HTTP server is online!");

      Serial.println("HTTP request received");
    }

    httpClient.stop();
  }

  // Port 2323: TCP banner server
  WiFiClient bannerClient = bannerServer.available();

  if (bannerClient) {
    bannerClient.println("ESP32-BANNER-SERVER");
    bannerClient.println("Device: ESP32-WROOM");
    bannerClient.stop();

    Serial.println("Banner connection received");
  }

  // Port 8080: Custom TCP server
  WiFiClient customClient = customServer.available();

  if (customClient) {
    customClient.println("PYPROBE-TEST-SERVICE");
    customClient.println("Send a message to test this port.");

    unsigned long start = millis();

    while (customClient.connected() &&
           millis() - start < 3000) {
      if (customClient.available()) {
        String message = customClient.readStringUntil('\n');
        Serial.print("Received: ");
        Serial.println(message);

        customClient.println("Message received by ESP32");
        break;
      }

      delay(1);
    }

    customClient.stop();
    Serial.println("Custom connection closed");
  }

  delay(1);
}