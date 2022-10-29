# 0x0D-web_stack_debugging_0
---
### Install and configure apache2 on ubuntu:14.04 docker container to return 'Hello Holberton' when curled

```
docker run -p 8080:80 -d -it holbertonschool/265-0
```
### Before configuration:
```
curl 0:8080  returns an error
```
### After configuration:
```
chalo@chalo:~$ sudo curl 0:8080
[sudo] password for chalo: 
Hello Holberton
```
