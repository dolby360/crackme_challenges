#include <inttypes.h>
#include <stdio.h>

void execute(char *buffer,int index){
  int iVar1;
  char auStack_2c [8];
  uintptr_t *local_24;
  uintptr_t *local_20;
  int local_1c;
  int size;
  int low_counter;
  uint16_t i;
  int buf_ind;
  
  if ((buffer != NULL) && (index != 0)) {
    size = index * 2;
    local_1c = size;
    iVar1 = ((size + 0x10) / 0x10) * -0x10;
    local_20 = auStack_2c + iVar1;
    low_counter = 0;
    for (i = 0; buf_ind = low_counter, i < size; i = i + 1) {
      if ((int)i % 4 < 2) {
        low_counter = low_counter + 1;
        auStack_2c[i + iVar1] = buffer[buf_ind];
      }
      else {
        auStack_2c[i + iVar1] = 0x90;
      }
    }
    auStack_2c[size + iVar1] = 0xc3;
    local_24 = auStack_2c + iVar1;
    *(char *)(auStack_2c + iVar1 + -4) = 0x80485cb;
    printf("%p\n", auStack_2c + iVar1);
    return;
  }
                    /* WARNING: Subroutine does not return */
  exit(1);
}

int main(void){
  int input;
  char buffer [1000];
  char input_to_char;
  uint16_t index;
  setbuf(stdout, NULL);
  index = 0;
  input_to_char = 0;
  puts("Give me code to run:");
  input = fgetc(stdin);
  input_to_char = (char)input;
  for (; (input_to_char != '\n' && (index < 1000)); index = index + 1) {
    buffer[index] = input_to_char;
    input = fgetc(stdin);
    input_to_char = (char)input;
  }
  if ((index & 1) != 0) {
    buffer[index] = -0x70;
    index = index + 1;
  }
  execute(buffer,index);
  return 0;
}
