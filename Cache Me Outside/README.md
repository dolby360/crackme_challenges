# Cache Me Outside
In this challenge, picoCTF provides a binary and the libc library. Let's begin with our usual routine to get an understanding of what's happening.

Check the binary security 
```bash
> checksec ./heapedit

Arch:     amd64-64-little
RELRO:    Partial RELRO
Stack:    Canary found
NX:       NX enabled
PIE:      No PIE (0x400000)
RUNPATH:  b'./'
```
Now, let's ensure that this binary is configured to run with a nearby libc. If it's not, we will need to use patchelf to make the necessary changes.

```bash
> ldd ./heapedit 

linux-vdso.so.1 (0x00007ffe8c8ae000)
libc.so.6 => ./libc.so.6 (0x00007f27eb282000) # great
/lib64/ld-linux-x86-64.so.2 (0x00007f27eb673000)
```

Alright, the next step is to execute the binary.
```bash
> ./heapedit

Segmentation fault
```
:slightly_frowning_face:	

Let's open this code with Ghidra and analyze what is happening.

```C

undefined8 main(void){
  long in_FS_OFFSET;
  undefined decimal_num_to_assign_to_addr;
  int address_to_edit;
  int i;
  undefined8 *pointer_to_flag;
  undefined8 *heap_pointer;
  FILE *flag_fd;
  undefined8 *heap_pointer_2;
  void *local_80;
  undefined8 local_78;
  undefined8 local_70;
  undefined8 local_68;
  undefined local_60;
  char flag_content [72];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  setbuf(stdout,(char *)0x0);
  flag_fd = fopen("flag.txt","r");
  fgets(flag_content,0x40,flag_fd);
  local_78 = 0x2073692073696874;
  local_70 = 0x6d6f646e61722061;
  local_68 = 0x2e676e6972747320;
  local_60 = 0;
  pointer_to_flag = (undefined8 *)0x0;
  for (i = 0; i < 7; i = i + 1) {
    // 1. allocating 0x80 bytes
    heap_pointer = (undefined8 *)malloc(0x80);
    if (pointer_to_flag == (undefined8 *)0x0) {
      pointer_to_flag = heap_pointer;
    }
    *heap_pointer = 0x73746172676e6f43;
    heap_pointer[1] = 0x662072756f592021;
    heap_pointer[2] = 0x203a73692067616c;
    *(undefined *)(heap_pointer + 3) = 0;
    // 2. copy the flag content
    strcat((char *)heap_pointer,flag_content); 
  }
  heap_pointer_2 = (undefined8 *)malloc(0x80);
  *heap_pointer_2 = 0x5420217972726f53;
  heap_pointer_2[1] = 0x276e6f7720736968;
  heap_pointer_2[2] = 0x7920706c65682074;
  *(undefined4 *)(heap_pointer_2 + 3) = 0x203a756f;
  *(undefined *)((long)heap_pointer_2 + 0x1c) = 0;
  strcat((char *)heap_pointer_2,(char *)&local_78);
  // Now the pointer that contain the flag is free
  free(heap_pointer);
  // And something else that is not relevant is freed as well.
  free(heap_pointer_2);
  address_to_edit = 0;
  decimal_num_to_assign_to_addr = 0;
  puts("You may edit one byte in the program.");
  printf("Address: ");
  __isoc99_scanf("%d",&address_to_edit);
  printf("Value: ");
  __isoc99_scanf(" %c",&decimal_num_to_assign_to_addr);
  *(undefined *)((long)address_to_edit + (long)pointer_to_flag) = decimal_num_to_assign_to_addr;
  local_80 = malloc(0x80);
  puts((char *)((long)local_80 + 0x10));
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
    __stack_chk_fail();
  }
  return 0;
}
```

From the following line, we can conclude that the program is reading from a file called flag.txt that I don't have. 
```C
flag_fd = fopen("flag.txt","r");
```
So I just created one with random string.
```bash
# AAAA because it's 0x41 in hex so it will be clear to see that in memory.
echo "AAAAA" > flag.txt
```
Now let's run the program
```bash
> ./heapedit

You may edit one byte in the program.
Address: # waiting for imput
Value: # waiting for imput
t help you: this is a random string.
```

