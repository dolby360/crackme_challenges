# mind your ps and qs

In this [CTF](https://play.picoctf.org/practice/challenge/162?category=2&page=1) challange challenge, I encountered the following details:
```
Decrypt my super sick RSA:
c: 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n: 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e: 65537
```
It appears that the only way to solve this is through a brute-force technique to find the values of p and q. I won't deny that I attempted to write my own brute-force algorithm (I even utilized C and [primesieve](https://github.com/kimwalisch/primesieve)), but it turned out to be more challenging to implement than I initially thought.

Subsequently, I conducted an online search for a penetration testing tool and stumbled upon [this](https://github.com/RsaCtfTool/RsaCtfTool) fantastic project. It promptly resolved my issue using the following command:
```
python RsaCtfTool.py -n 1311097532562595991877980619849724606784164430105441327897358800116889057763413423 -e 65537 --uncipher 861270243527190895777142537838333832920579264010533029282104230006461420086153423
```
Apperentlly this tool is using [factordb](http://factordb.com/res.php) which is a platform for individuals and researchers to collaborate on the factorization of large numbers by sharing their progress and findings.
