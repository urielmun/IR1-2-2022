//1,2,3 단 stop이 잘안됨

#define RightMotorA_forward 6
#define RightMotorA_backward 5
#define LeftMotorB_forward 10
#define LeftMotorB_backward 11

#define Trig 8
#define Echo 7

//LED모듈
#define BLUE 3
#define GREEN 2
#define RED 1
int  speed = 100;

#define IR_right 13
#define IR_left 12


// 로직 설정
int flag_right = 0; // 1
int flag_left = 0; // 1

void setup() {
    pinMode(RED, OUTPUT);
    pinMode(GREEN, OUTPUT);
    pinMode(BLUE, OUTPUT);
    digitalWrite(RED, 1);
    digitalWrite(GREEN, 1);
    digitalWrite(BLUE, 1);
    //모터
    pinMode(RightMotorA_forward, OUTPUT);
    pinMode(RightMotorA_backward, OUTPUT);
    pinMode(LeftMotorB_forward, OUTPUT);
    pinMode(LeftMotorB_backward, OUTPUT);
    //IR
    pinMode(IR_right, INPUT);
    pinMode(IR_left, INPUT);

    //초음파센서
    pinMode(Trig, OUTPUT); // 9번핀 출력(Trig) 설정
    pinMode(Echo, INPUT); // 8번핀 입력(Echo) 설정
    Serial.begin(9600);
}
// 라인트레이서 제어
void motor_control()
{
    //IR 센서
    int Sub_msg_l = digitalRead(IR_left);
    int Sub_msg_r = digitalRead(IR_right);
    // 센서값 수신

    if (Sub_msg_l == 1 || Sub_msg_r == 1)
    {
        //정상으로 판단
        if (Sub_msg_l == 1 && Sub_msg_r == 1) { flag_right = 0; flag_left = 0; }
        // 우측으로 판단
        else if (Sub_msg_l == 0 && Sub_msg_r == 1) {
            flag_right = 0; flag_left = 1; // 왼쪽으로 이동 
            Serial.print("sensor_right : 0 ");
        }
        // 좌측으로 판단
        else if (Sub_msg_l == 1 && Sub_msg_r == 0) {
            flag_right = 1; flag_left = 0; // 오른쪽으로 이동
            Serial.print("sensor_right : 1 ");
        }
        // 직선 주행
        if (flag_left == 0 && flag_right == 0) {
            analogWrite(RightMotorA_forward, speed + 30);
            analogWrite(RightMotorA_backward, 0);
            analogWrite(LeftMotorB_forward, speed);
            analogWrite(LeftMotorB_backward, 0);
        }
        // 좌측 주행
        else if (flag_left == 1 && flag_right == 0) {
            analogWrite(RightMotorA_forward, speed + 20);
            analogWrite(RightMotorA_backward, 0);
            analogWrite(LeftMotorB_forward, speed - 40);
            analogWrite(LeftMotorB_backward, 0);
        }
        // 우측 주행
        else if (flag_right == 1 && flag_left == 0) {
            analogWrite(RightMotorA_forward, speed - 15);
            analogWrite(RightMotorA_backward, 0);
            analogWrite(LeftMotorB_forward, speed + 20);
            analogWrite(LeftMotorB_backward, 0);
        }
    }
}

void jodo_control() {
    int jodo = analogRead(A1);
    //Serial.println(jodo);//확인을 위한 것
    if (jodo > 350)//어두움-(터널진입시,파란색LED ON)
    {
        digitalWrite(RED, LOW);
        digitalWrite(GREEN, LOW);
        digitalWrite(BLUE, HIGH);
        speed = 90;//감속하기 위한 speed 제어
        echo_control();
    }
    else if (jodo <= 350)//밝음-(밖일시, 파란색LED OFF)
    {
        digitalWrite(RED, LOW);
        digitalWrite(GREEN, LOW);
        digitalWrite(BLUE, LOW);
        speed = 100;
        echo_control();
    }
}

double duration;
double cm;
void echo_control() {
    //초음파신호 송신
    digitalWrite(Trig, LOW);
    delayMicroseconds(2);
    digitalWrite(Trig, HIGH);
    delayMicroseconds(2);
    digitalWrite(Trig, LOW);
    // 초음파신호 수신
    duration = pulseIn(Echo, HIGH);
    cm = duration * 340 / 10000 / 2;
    Serial.println(cm);//확인을 위한것

    if (cm < 10.0)//10cm이하일때 정지
    {
        digitalWrite(GREEN, HIGH);
        digitalWrite(BLUE, HIGH);
        speed = 0;
        if (
    }
    else if (cm < 20.0 && cm>10.0)//10cm초과 20cm미만 감속
    {
        digitalWrite(GREEN, HIGH);
            speed = 80;
    }
}

void loop()
{

    jodo_control();
    motor_control();
    delay(9);


}