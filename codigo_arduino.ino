#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 13, 7, 6, 5, 4);

String ultimoTexto = "";

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Aguardando...");
}

void loop() {
  if (Serial.available() > 0) {
    String texto = Serial.readStringUntil('\n');
    texto.trim();

    if (texto.length() > 0 && texto != ultimoTexto) {
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Pilhas:");
      lcd.setCursor(0, 1);
      lcd.print(texto);
      ultimoTexto = texto;
    }
  }
}
