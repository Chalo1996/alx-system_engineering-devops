# 0x0E-web_stack_debugging_1
---
### Install and configure nginx on ubuntu:14.04 docker container to be exposed on port 80
```
sudo apt-get -y update && sudo apt-get -y install nginx
sudo apt-get -y install ufw curl
sudo ufw allow 'Nginx HTTP'
sudo service nginx start
curl 0:80
```
