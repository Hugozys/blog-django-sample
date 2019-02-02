# HugoBlog - A Simple Django Web Application for Personal Website
  This web application is a skill refresh for TAing Duke ECE568 ERSS course. It is also the same code that I used to maintain my first personal blog webiste. The github repository contains all the development code. You could see a development demo via docker. To visit actual deployed web, go [here](https://hugozh.com)
  The development version is configured in such a way that you may only successfully run the demo if you are on a Duke Virtual Machine. If you are on other other VM or Linux host. You need to change the following configuration in `development.py` before running docker:
  * ALLOWED_HOST should be the FQDN or public ip address associated with your host
  * Configure Email Backend parameters with whatever smtp service you are using

# How To Run Demo
  To run the demo, simply install docker on your Linux VM
  `sudo apt install docker.io docker-compose`
  `sudo chmod -aG docker $USER`
  After you successfully install the docker, you can initiate the web applicaiton by launching
  `docker-compose up`
  Then open the web browser and visit URL: $(VM-DOMAIN):8000/

# Resources
  I used bootstrap for all the CSS declorations and post template. For text editor, I simply integrate martor.
  You could find the source code and documentation here:
  [Bootstrap](https://startbootstrap.com/template-overviews/clean-blog/)
  [martor](https://github.com/agusmakmun/django-markdown-editor)
  