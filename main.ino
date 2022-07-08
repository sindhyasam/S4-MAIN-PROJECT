#include <HTTPClient.h>
#include <WiFi.h>
#include <ESP32Servo.h>

Servo myservo;
const int servo_pin = 13;
int crnt_pos = 0;
int pos;


const char* ssid     = "narzo 50A";
const char* password = "fai9tw36";

char simple_json1[200];
char json[200];

//Your Domain name with URL path or IP address with path
const char* serverName = "http://    192.168.130.79:8000/readings";

float mq6_threshold = 200000000;
const int ledPin = 2;
int status_flag = 0;

#define RO_VALUE_CLEAN_AIR (9.83)
#define RL_VALUE (10)
#define MQ3_PIN 34

float Ro =  0;
float MQ6_curve[3]  = {2.3, 0.30, -0.41};

unsigned long lastTime = 0;
unsigned long timerDelay = 5000;

void valve_on() {
  // Relay off
  digitalWrite (4, LOW);
}

void valve_off() {
  // Relay off
  digitalWrite (4, HIGH);
}


void led_red() {
  digitalWrite (18, HIGH);
  digitalWrite (19, LOW);
}

void led_green() {
  digitalWrite (18, LOW);
  digitalWrite (19, HIGH);
}

int Sensor_read(int pin) {
  return analogRead(pin);
}

float SensorCalibration() {
  int count;
  float val = 0;
  for (count = 0; count < 50; count++) {
    val += calculate_resistance(Sensor_read(MQ3_PIN));
    delay(500);
  }
  val = val / 50;
  val = val / RO_VALUE_CLEAN_AIR;
  return val;
}

float read_mq() {
  int count;
  float rs = 0;
  for (count = 0; count < 5; count++) {
    rs += calculate_resistance(Sensor_read(MQ3_PIN));
    delay(50);
  }
  rs = rs / 5;
  return rs;
}

float calculate_resistance(int adc_channel) {
  return ( ((float)RL_VALUE * (1023 - adc_channel) / adc_channel));
}

int gas_plot_log_scale(float rs_ro_ratio, float *curve) {
  float diff = rs_ro_ratio - curve[1];
  Serial.println(diff);
  float logdiff = log(diff);
  Serial.println(logdiff);
  float divlog = logdiff / curve[2];
  Serial.println(divlog);
  float adddiv = divlog + curve[0];
  Serial.println(adddiv);
  float power = pow(10, adddiv);
  Serial.println(power);
  return power;
}


void send_data(const char* serverName, int gas_value) {
  if ((millis() - lastTime) > timerDelay) {
    //Check WiFi connection status
    if (WiFi.status() == WL_CONNECTED) {
      WiFiClient client;
      HTTPClient http;

      // Your Domain name with URL path or IP address with path
      http.begin(client, serverName);

      // If you need an HTTP request with a content type: application/json, use the following:

      http.addHeader("Content-Type", "application/json");

      sprintf(simple_json1, "{\"device_id\":\"%d\",\"gas_value\":\"%d\"}", 1, gas_value);
      int httpResponseCode1 = http.POST(simple_json1);
      delay(1000);

      Serial.print("Gas value : ");
      Serial.println(gas_value);

      Serial.print("HTTP Response code1: ");
      Serial.println(httpResponseCode1);

      http.end();
    }
    else {
      Serial.println("WiFi Disconnected");
    }
    lastTime = millis();
  }

}

void gas_off() {
  Serial.println("started");
  if (crnt_pos >= 90 ) {
    for (pos = crnt_pos; pos >= 90; pos -= 1) {
      myservo.write(pos);
      delay(15);
      Serial.println(pos);
    }
  } else {
    for (pos = crnt_pos; pos <= 90; pos += 1) {
      myservo.write(pos);
      delay(15);
      Serial.println(pos);
    }
  }
  crnt_pos = pos - 1;
  Serial.println("end");
}



void gas_on() {
  for (pos = crnt_pos; pos >= 50; pos -= 1) {
    myservo.write(pos);
    delay(15);
  }
  crnt_pos = pos - 1;
}

void setup() {
  Serial.begin(115200);
  //pinMode (ledPin, OUTPUT);
  myservo.attach(servo_pin);

    WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  pinMode (4, OUTPUT);
  pinMode (18, OUTPUT);
  pinMode (19, OUTPUT);
  //Ro = SensorCalibration();
  Ro = 6;
  Serial.println(Ro);
  valve_on();
  led_green();
}

void loop() {
  float rs = read_mq();
  Serial.println("value1: " + String(Sensor_read(MQ3_PIN)));
  float ratio = rs / Ro;
  float value = gas_plot_log_scale(ratio, MQ6_curve);
  Serial.println("R0 : " + String(Ro));
  Serial.println("RS : " + String(rs));
  Serial.println("Ratio : " + String(ratio));
  Serial.println("Value " + String(value));


  if (value > mq6_threshold) {
    //digitalWrite (ledPin, LOW);
    // valve close - relay off - HIGH
    valve_off();
    led_red();
    gas_off();
    
    status_flag = 1;
  } else if (status_flag == 1) {
    status_flag = 0;
    //digitalWrite (ledPin, HIGH);
    //digitalWrite (4 , HIGH);
    valve_on();
    led_green();
    gas_on();
    
  }
  delay(5000);
  send_data(serverName, value);
  delay(1000);
}
