
float mq6_threshold = 200000000;
const int ledPin = 2;
int status_flag = 0;

#define RO_VALUE_CLEAN_AIR (9.83)
#define RL_VALUE (10)
#define MQ3_PIN 34

float Ro =  0;
float MQ6_curve[3]  = {2.3, 0.30, -0.41};



void valve_on() {
  // Relay off
  digitalWrite (4, LOW);
}

void valve_off() {
  // Relay off
  digitalWrite (4, HIGH);
}


void led_red(){
  digitalWrite (18, HIGH);
  digitalWrite (19, LOW);
}

void led_green(){
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


void setup() {
  Serial.begin(115200);
  //pinMode (ledPin, OUTPUT);
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
    status_flag = 1;
  } else if (status_flag == 1) {
    status_flag = 0;
    //digitalWrite (ledPin, HIGH);
    //digitalWrite (4 , HIGH);
    valve_on();
    led_green();
  }
  delay(4000);
}
