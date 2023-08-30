# crackme_challenges
Most challenges originate from [picoCTF](https://play.picoctf.org/practice?category=6&page=1)

| Background | link |
| -------- | :------: |
| This was my first challenge where I had to craft a keygen, </br>reminiscent of the ones we used to create back in the year 2000.    | [challenge 1](./challenge_1/README.md)     |
| I utilized a ROPchain and managed to leak the system and /bin/sh addresses.     | [Here's a LIBC](./Here's%20a%20LIBC/README.md)     |
| A simple example of printf formatting vulnerability  | [Stonks](./Stonks/README.md)     |
| Exploiting a vulnerability in glibc 2.27's tcache mechanism. | [Cache Me Outside](./Cache%20Me%20Outside/README.md)     |
| Use after free    | [Unsubscriptions Are Free](./Unsubscriptions%20Are%20Free/README.md)     |
| Buffer under flow    | [babygame01](./babygame01/README.md)     |
| In-depth Explanation of Buffer Overflow  | [Clutter Overflow](./clutter-overflow/README.md)     |
| Just another BOF    | [Simple buffer overflow](./bof1/README.md)     |

## PRO TIP
You're interested in crafting your own Python automation scripts for the exploits. However, you're also keen on debugging your code as it runs. Wondering how you can effectively achieve this?
This is a cool life hack on how to run the binary as server and attach gdb.

Make fifo file
```bash
mkfifo fifo
```
run netcat and redirect the input from fifo:
```bash
nc -l -p 8080 < fifo | ./vuln >fifo
```

gdb to fun process:
```bash
process_name="vuln"; pid=$(pgrep "$process_name"); [[ -n $pid ]] && gdb -p "$pid" -x .gdbinit
```

cat the content of a file into the running process:
```bash
cat buff | nc localhost 8080
```
