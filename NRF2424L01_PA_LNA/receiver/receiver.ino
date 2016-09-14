#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

/**
 *
 * Connect your RF's pin follow this definition
 * radio(CE, CSN);
 *
 */
RF24 radio(7, 8);

const byte rxAddr[6] = "00001";

void setup() {
  while (!Serial) {}
  Serial.begin(115200);

  radio.begin();
  radio.openReadingPipe(0, rxAddr);

  radio.startListening();
}

void loop() {
  if (radio.available()) {
    char text[32] = {0};
    radio.read(&text, sizeof(text));

    Serial.println(text);
  }
}
