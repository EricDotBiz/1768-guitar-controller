#include "mbed.h"
#include "mRotaryEncoder.h"

DigitalIn button0(p21); 
DigitalIn button1(p22); 
DigitalIn button2(p23); 
DigitalIn button3(p24); 
DigitalIn button4(p25); 

mRotaryEncoder rotary(p7, p8, p6);
DigitalIn rotary_switch(p6); 

AnalogIn  joystick_x(p20);

int buttons[5] = {0, 0, 0, 0, 0};
float last_joystick = 0.0;
int prev_click = 0;

void print_rotate(){
    printf("c\n\r");
}

int main() {    
    rotary.attachROT(print_rotate);
        
    printf("***ERIC DOT COM GUITAR HERO CONTROLLER***\n\r");
    while(1) {
        if(button0){ 
            if(!buttons[0]){
                printf("a\n\r");
                buttons[0] = 1;
            }
        }else if(buttons[0]){
            printf("a!\n\r");
            buttons[0] = 0;
        }
        
        if(button1){ 
            if(!buttons[1]){
                printf("s\n\r");
                buttons[1] = 1;
            }
        }else if(buttons[1]){
            printf("s!\n\r");
            buttons[1] = 0;
        }
        
        if(button2){ 
            if(!buttons[2]){
                printf("d\n\r");
                buttons[2] = 1;
            }
        }else if(buttons[2]){
            printf("d!\n\r");
            buttons[2] = 0;
        }
        
        if(button3){ 
            if(!buttons[3]){
                printf("f\n\r");
                buttons[3] = 1;
            }
        }else if(buttons[3]){
            printf("f!\n\r");
            buttons[3] = 0;
        }
        
        if(button4){ 
            if(!buttons[4]){
                printf("g\n\r");
                buttons[4] = 1;
            }
        }else if(buttons[4]){
            printf("g!\n\r");
            buttons[4] = 0;
        }
        
        //Strum up
        if(joystick_x < 0.1 && last_joystick >= 0.1){
            printf("h\n\r");
        }
        
        //Strum down
        if(joystick_x > 0.9 && last_joystick <= 0.9){
            printf("j\n\r");
        }
        
        //Pause
        if(rotary_switch && !prev_click){
            printf("p\n\r");
        }
        
        prev_click = rotary_switch;
        last_joystick = joystick_x;
        wait(0.01);
    }
}
