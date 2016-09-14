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
  radio.begin();
  radio.setRetries(15, 15);
  radio.openWritingPipe(rxAddr);

  radio.stopListening();
}

void loop() {
  const char text[] = "Hello World";
  radio.write(&text, sizeof(text));

  delay(1000);
}
