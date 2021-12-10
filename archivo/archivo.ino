

/*
  No usa la funcion delay(). En lugar de ello utiliza la
  biblioteca NoDelay. Esto permite que otro codigo ejecute al
  mismo tiempo que se encuentra en el periodo de espera.

  La liga para descargar esta biblioteca es:

  https://github.com/M-tech-Creations/NoDelay

  La liga para descargar esta biblioteca es:

  https://bitbucket.org/teckel12/arduino-new-ping/downloads/
*/

#include <NewTone.h>
#include <NewPing.h>
#include <NoDelay.h>

const unsigned int PIN_ROJO = 11;
const unsigned int PIN_AMARILLO = 10;
const unsigned int PIN_VERDE = 9;

const unsigned int PIN_PIR = 3;

const unsigned int R_LED = 6;
const unsigned int B_LED = 5;
const unsigned int G_LED = 4;

const int PIN_TRIGGER = 13;
const int PIN_ECHO = 12;
const int DISTANCIA_MAX = 200;

const int PIN_ZUMBADOR = 2;

const int DISTANCIA_ALERTA = 10;
const unsigned int BAUD_RATE = 9600;

// Periodo en ms que dura encendido o apagado el LED (SEMAFORO)
const long PERIODO = 10000;

// Periodo en ms que dura encendido o apagado el zumbador
const long PERIODO_ZUMBADOR = 1000;

// Estado del zumbador. LOW = apagado, HIGH = encendido
int estadoZum = LOW;

//Estado semaforo auto
int estadoLedRojo = HIGH;
int estadoLedAmarillo = LOW;
int estadoLedVerde = LOW;

void suenaAlarma();

// Crea una instancia de la clase noDelay
// que determina si han transcurrido PERIODO ms
noDelay pausa(PERIODO);

// Crea una instancia de la clase NewPing
NewPing sonar(PIN_TRIGGER, PIN_ECHO, DISTANCIA_MAX);

void setup() {
  pinMode(PIN_ROJO, OUTPUT);
  pinMode(PIN_AMARILLO, OUTPUT);
  pinMode(PIN_VERDE, OUTPUT);
  pinMode(PIN_ZUMBADOR, OUTPUT);

  pinMode(R_LED, OUTPUT);
  pinMode(B_LED, OUTPUT);
  pinMode(G_LED, OUTPUT);

  Serial.begin(BAUD_RATE);
}


void loop() {
  //Encender la luz para el semaforo
  manejarSemaforo();

    //Si el semaforo del carro esta en rojo, se activa la alarma
    if (estadoLedRojo == HIGH) {
      //Alarma si viene carro
      validarVieneCarro();
      prenderSemaforoPeaton();
    } else {
      validarVieneHumano();
      apagarSemaforoPeaton();
    }
}

void manejarSemaforo() {

  // Verifica si es tiempo de prender/apagar la luz del semaforp
  if (pausa.update()) {
    // Prender/apagar el LED
    if (estadoLedVerde == LOW && estadoLedAmarillo == LOW && estadoLedRojo == HIGH) {
      estadoLedVerde = HIGH;
      estadoLedAmarillo = LOW;
      estadoLedRojo = LOW;
    } else if (estadoLedVerde == HIGH && estadoLedAmarillo == LOW && estadoLedRojo == LOW) {
      estadoLedVerde = LOW;
      estadoLedAmarillo = HIGH;
      estadoLedRojo = LOW;
    } else if (estadoLedVerde == LOW && estadoLedAmarillo == HIGH && estadoLedRojo == LOW) {
      estadoLedVerde = LOW;
      estadoLedAmarillo = LOW;
      estadoLedRojo = HIGH;
    }
    digitalWrite(PIN_VERDE, estadoLedVerde);
    digitalWrite(PIN_AMARILLO, estadoLedAmarillo);
    digitalWrite(PIN_ROJO, estadoLedRojo);
  }
}

void validarVieneCarro() {
  const int tonos[] = {200, 500, 200, 500, 200};
  int uS = sonar.ping_median();
  // Calcular la distancia a la que se encuentra el objeto
  int distancia = sonar.convert_cm(uS);
  

  // Si la distancia es menor a DISTANCIA_ALERTA, suena la alarma
  if (distancia <= DISTANCIA_ALERTA && distancia != 0) {
    suenaAlarma(tonos);
    String texto = "Viene automovil ";
    texto += distancia;
    Serial.println(texto);
  } else {
    apagaAlarma();
  }
}

void validarVieneHumano() {
  const int tonos[] = {50, 5500, 50, 5500, 50};
  int value = digitalRead(PIN_PIR);
  if (value == HIGH)
  {
    String texto = "Viene peaton ";
    texto += '0';
    Serial.println(texto);
    suenaAlarma(tonos);
  } else {
    apagaAlarma();
  }

}

void suenaAlarma(int tonos[]) {
  estadoZum = HIGH;
  for (int iTono = 0; iTono < 5; iTono++) {
    NewTone(PIN_ZUMBADOR, tonos[iTono]);
  }
}

void apagaAlarma() {
  estadoZum = LOW;
  // Apaga el zumbador
  noNewTone(PIN_ZUMBADOR);
}

void prenderSemaforoPeaton() {
  digitalWrite(G_LED, LOW);
  digitalWrite(B_LED, HIGH);
  digitalWrite(R_LED, HIGH);
}

void apagarSemaforoPeaton() {
  digitalWrite(G_LED, HIGH);
  digitalWrite(B_LED, HIGH);
  digitalWrite(R_LED, LOW);

}
