# Context
After downloading the .raw file a simple
```
file file.raw
```
permit to obtain some informations about the file.\
We can undertsand that is a partition file and we need to mount it.\

# Exploit
The first part is to exec:
```
binwalk file.raw
```
Then, with the result we can see the offset and the size of the partition.\
With these infos, we can use:
```
dd if=file.raw of=challenge3 skip=128 count=198656
```
Now we have a new output file name challenge3.\
we try to mount it but we can see an error with bitlocker.\
So we need to remove the bitlocker auth.\
```
mkdir media
sudo dislocker challenge3 -upassword -- media
mkdir mount
sudo mount -o media/dislocker-file mount
```
Then we tried to cat the file flag.txt but it's a fake... So what can we do?\
The answer is simple:
```
sudo binwalk media/dislocker-file
```
Then we can some file named fic.txt. Now how to open/find them?\
There is a good tool:
```
sudo foremost media/dislocker-file
```
Then a all files are present in a folder named output.
```
unzip name.zip
less name.txt
```
There is a github link!\
GO TO THE WEBSITE -> there is a repo "flag" with some base64 encode text. Assimple base64 decode and the flag is here.
