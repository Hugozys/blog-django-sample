# HugoBlog - A Simple Django Web Application for Personal Website
  This web application is a skill refresh for TAing Duke ECE568 ERSS course. It is also the same code that I used to maintain my first personal blog webiste. The github repository contains all the development code. You could see a development demo via docker. To visit actual deployed web, go [here](https://hugozh.com)

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
  