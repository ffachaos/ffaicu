FROM perl:5.8-threaded-buster

RUN apt-get update && \
    apt-get install -y apache2 libapache2-mod-perl2 && \
    a2enmod cgi && \
    apt-get clean

WORKDIR /var/www/html
COPY ffaicu/ /var/www/html/
COPY apache/apache2.conf /etc/apache2/

RUN find /var/www/html -name "*.cgi" -type f -exec chmod 755 {} \;
RUN find /var/www/html -type d -exec chmod 755 {} \;
RUN find /var/www/html -type f -iregex ".*\.\(dat\|ini\)$" -exec chmod 666 {} \;

ENV TZ=Asia/Tokyo

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]
