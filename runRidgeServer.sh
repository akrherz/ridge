#!/bin/sh

export JAVA=/usr/bin/java
cd /home/ldm/ridge/RidgeServer-0.0.1

${JAVA} -Xmx1400m -DconnectorName=amqp -jar RidgeServer-0.0.1.jar &
