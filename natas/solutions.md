## Natas Level 0
Inspect
![Alt text](image.png)

## 0 → Level 1
Inspect
```
h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7
```

## Level 1 → Level 2
http://natas2.natas.labs.overthewire.org/files/
 
Is accessible.
```
G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q
```

## Level 2 → Level 3
http://natas3.natas.labs.overthewire.org/s3cr3t/  
Is accessible.

```
natas4:tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm
```

## Level 3 → Level 4
I used burp to edit the referer
![Alt text](image-1.png)
```
Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD 
```

## Level 4 → Level 5
Change coockie value to 1
![Alt text](image-2.png)
```
fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR
```

## Level 5 → Level 6
The source indicated we are including a file
```php
include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>

```
So I added to the url path and found the secret there.
![Alt text](image-3.png)
```
jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr
```
## Level 6 → Level 7
```
Following the description in the comments.
?page=/etc/natas_webpass/natas8
```
```
a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB 
```

## Level 7 → Level 8
I just reversed this 
```php
$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>
```
decode of `3d3d516343746d4d6d6c315669563362` is `==QcCtmMml1ViV3b`  
reverse: `b3ViV1lmMmtCcQ==`  
decode the reverse: `oubWYf2kBq`
```
Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd
```
