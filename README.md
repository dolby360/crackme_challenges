# crackme_challenges
Most challenges originate from [picoCTF](https://play.picoctf.org/practice?category=6&page=1)

* [challenge 1](./challenge_1/README.md)
* [Here's a LIBC](./Here's%20a%20LIBC/README.md)
* [Stonks](./Stonks/README.md)
* [Cache Me Outside](./Cache%20Me%20Outside/README.md)
* [Unsubscriptions Are Free](./Unsubscriptions%20Are%20Free/README.md)
* [babygame01](./babygame01/README.md)
* [Clutter Overflow](./clutter-overflow/README.md)
* [Simple buffer overflow](./bof1/README.md)


This is a cool life hack on how to run the binary as server and attach gdb.

run netcat and redirect the input from fifo:
```bash
nc -l -p 8080 < fifo | ./chall >fifo
```

gdb to fun process:
```bash
process_name="chall"; pid=$(pgrep "$process_name"); [[ -n $pid ]] && gdb -p "$pid" -x .gdbinit
```

cat the content of a file into the running process:
```bash
cat buff | nc localhost 8080
```
