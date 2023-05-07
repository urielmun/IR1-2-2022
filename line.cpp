//1,2,3 �� stop�� �߾ȵ�

#define RightMotorA_forward 6
#define RightMotorA_backward 5
#define LeftMotorB_forward 10
#define LeftMotorB_backward 11

#define Trig 8
#define Echo 7

//LED���
#define BLUE 3
#define GREEN 2
#define RED 1
int  speed = 100;

#define IR_right 13
#define IR_left 12


// ���� ����
int flag_right = 0; // 1
int flag_left = 0; // 1

void setup() {
    pinMode(RED, OUTPUT);
    pinMode(GREEN, OUTPUT);
    pinMode(BLUE, OUTPUT);
    digitalWrite(RED, 1);
    digitalWrite(GREEN, 1);
    digitalWrite(BLUE, 1);
    //����
    pinMode(RightMotorA_forward, OUTPUT);
    pinMode(RightMotorA_backward, OUTPUT);
    pinMode(LeftMotorB_forward, OUTPUT);
    pinMode(LeftMotorB_backward, OUTPUT);
    //IR
    pinMode(IR_right, INPUT);
    pinMode(IR_left, INPUT);

    //�����ļ���
    pinMode(Trig, OUTPUT); // 9���� ���(Trig) ����
    pinMode(Echo, INPUT); // 8���� �Է�(Echo) ����
    Serial.begin(9600);
}
// ����Ʈ���̼� ����
void motor_control()
{
    //IR ����
    int Sub_msg_l = digitalRead(IR_left);
    int Sub_msg_r = digitalRead(IR_right);
    // ������ ����

    if (Sub_msg_l == 1 || Sub_msg_r == 1)
    {
        //�������� �Ǵ�
        if (Sub_msg_l == 1 && Sub_msg_r == 1) { flag_right = 0; flag_left = 0; }
        // �������� �Ǵ�
        else if (Sub_msg_l == 0 && Sub_msg_r == 1) {
            flag_right = 0; flag_left = 1; // �������� �̵� 
            Serial.print("sensor_right : 0 ");
        }
        // �������� �Ǵ�
        else if (Sub_msg_l == 1 && Sub_msg_r == 0) {
            flag_right = 1; flag_left = 0; // ���������� �̵�
            Serial.print("sensor_right : 1 ");
        }
        // ���� ����
        if (flag_left == 0 && flag_right == 0) {
            analogWrite(RightMotorA_forward, speed + 30);
            analogWrite(RightMotorA_backward, 0);
            analogWrite(LeftMotorB_forward, speed);
            analogWrite(LeftMotorB_backward, 0);
        }
        // ���� ����
        else if (flag_left == 1 && flag_right == 0) {
            analogWrite(RightMotorA_forward, speed + 20);
            analogWrite(RightMotorA_backward, 0);
            analogWrite(LeftMotorB_forward, speed - 40);
            analogWrite(LeftMotorB_backward, 0);
        }
        // ���� ����
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
    //Serial.println(jodo);//Ȯ���� ���� ��
    if (jodo > 350)//��ο�-(�ͳ����Խ�,�Ķ���LED ON)
    {
        digitalWrite(RED, LOW);
        digitalWrite(GREEN, LOW);
        digitalWrite(BLUE, HIGH);
        speed = 90;//�����ϱ� ���� speed ����
        echo_control();
    }
    else if (jodo <= 350)//����-(���Ͻ�, �Ķ���LED OFF)
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
    //�����Ľ�ȣ �۽�
    digitalWrite(Trig, LOW);
    delayMicroseconds(2);
    digitalWrite(Trig, HIGH);
    delayMicroseconds(2);
    digitalWrite(Trig, LOW);
    // �����Ľ�ȣ ����
    duration = pulseIn(Echo, HIGH);
    cm = duration * 340 / 10000 / 2;
    Serial.println(cm);//Ȯ���� ���Ѱ�

    if (cm < 10.0)//10cm�����϶� ����
    {
        digitalWrite(GREEN, HIGH);
        digitalWrite(BLUE, HIGH);
        speed = 0;
        if (
    }
    else if (cm < 20.0 && cm>10.0)//10cm�ʰ� 20cm�̸� ����
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