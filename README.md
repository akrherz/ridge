ridge
=====

Ridge Server program

#How I setup rabbitmq

1. Install rabbitmq-server from EPEL
2. systemctl enable rabbitmq-server
3. rabbitmq-plugins enable rabbitmq_management
4. systemctl restart rabbitmq-server
5. Log into http://localhost:15672/ as guest/guest
6. Create fanout exchange of ridgeProductExchange