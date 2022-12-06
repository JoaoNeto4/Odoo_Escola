FROM odoo:15

USER root

RUN apt-get update && apt-get upgrade -y 
ADD ./requirements.txt /

RUN pip3 install -r requirements.txt
ADD ./addons /mnt/extra-addons

ADD odoo.conf /etc/odoo/odoo.conf
