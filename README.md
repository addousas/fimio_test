# Hardware Mockup
details
![Keypad.](dial_pad.png)
![landingpage.](landingpage.png)


# fimio_test

# build docker image
docker build -t sample_device . 
docker run -d --name mycontainer -p 80:80 sample_device