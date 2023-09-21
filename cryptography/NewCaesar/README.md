# New Caesar

[Link to CTF](https://play.picoctf.org/practice/challenge/158?category=2&page=1)

## The challenge
AUTHOR: MADSTACKS

### Description
We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) 
```
dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac
```
The provided code.
[new_caesar.py](./new_caesar.py)

## Problem Breakdown
My strategy for tackling this CTF challenge was to break it down into manageable steps. I focused on solving one challenge at a time. When examining the challenge, I identified two main components that needed to be cracked: `b16_encode` and `shift`.

## Deciphering b16_encode
I began by taking a sample of the `b16_encode` function **input** and a sample of the encryption **output**. This helped clarify the challenge and made it evident that my goal was to revert the **output** of the encryption back to its original form.

## Cracking the `shift` Encryption
Similarly, I applied the same approach to the shift encryption. I analyzed the encryption mechanism and worked on reversing it. Once I had successfully deciphered both b16_encode and shift, I proceeded to the final step.

## Determining the Key
The one remaining challenge was determining the key used for the encryption. It was not clear which letter had been chosen as the key. To overcome this obstacle, I brute-forced all possible letter combinations until I found the one that resembled the flag.


Please check out [my Python script](./e.py) to see how I reversed the encryption. If you find any flaws, please don't hesitate to open an issue.



Thanks for reading.
