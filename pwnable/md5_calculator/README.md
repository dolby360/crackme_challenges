# md5 hash calculator

## Source
https://pwnable.kr/play.php

md5 calculator - under Rookiss

## Explanation
As usual, I began by trying to force the system, entering a very long input to see what would happen. Immediately, you can notice a segmentation fault with an indication of smashing the canary. This provides two obvious hints: firstly, there is an option for a stack overflow, and secondly, there is a way to leak the canary.

Let's review the breadcrumbs:  
* Using a random number generator with the current time is often a good indication of something insecure.
    ```C
    __seed = time((time_t *)0x0);
    srand(__seed);
    ```
    I Used the rand seed from libc to determine the next rand numbers.

* Using a canary as part of the hash calculation.
    ```C
    int my_hash(void)

    {
    int rand_var;
    int in_GS_OFFSET;
    int i;
    int buff [4];
    int calc3;
    int calc1;
    int calc4;
    int calc2;
    int cannary;
    
    cannary = *(int *)(in_GS_OFFSET + 0x14);
    for (i = 0; i < 8; i = i + 1) {
        rand_var = rand();
        buff[i] = rand_var;
    }
    if (cannary != *(int *)(in_GS_OFFSET + 0x14)) {
        __stack_chk_fail();
    }
    return calc1 + buff[1] + (buff[2] - buff[3]) + cannary + calc2 + (calc3 - calc4);
    }
    ```
* Using the system command for something simple.
    ```C
    system("echo `date` >> log");
    ```


Eventually, this program compiled without NX, so there's no ASLR to worry about. The calculations are pretty straightforward this way.

```bash
gef➤  info address g_buf
Symbol "g_buf" is at 0x804b0e0 in a file compiled without debugging.
```

The program decodes (base64) the provided buffer and copies the global buffer, which is much larger, to a smaller buffer on the stack.

From here, I think reading the [Python exploit](./e.py) will be much easier.

Thanks for reading.