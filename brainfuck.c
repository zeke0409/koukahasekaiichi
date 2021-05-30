#define PTR_INCREMENT '>'
#define PTR_DECREMENT '<'
#define BYTE_INCREMENT '+'
#define BYTE_DECREMENT '-'
#define OUTPUT '.'
#define INPUT ','
#define LOOP_START '['
#define LOOP_END ']'
#include <stdint.h>
#include <stdio.h>
int main(){
    uint64_t *tape;
    uint8_t head=0;
    char *code;
    uint8_t code_head=0;

    tape = calloc((1 << 8), sizeof(uint64_t));
    code=calloc((1<<8),sizeof(char));
    scanf("%s",code);
    
    /*while(1){
        if(code_head<0){
            perror("not valid code_head");
            exit(1);
        }
        code_head++;
    }*/
}