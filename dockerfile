FROM perl:5.40-threaded-buster

RUN apt-get update && \
    apt-get install -y apache2 libapache2-mod-perl2 && \
    a2enmod cgi && \
    apt-get clean

WORKDIR /var/www/html
COPY ffaicu/ /var/www/html/
COPY apache/apache2.conf /etc/apache2/
RUN chown -R www-data:www-data /var/www/html

RUN find /var/www/html -type f -iregex ".*\.\(cgi\|pl\)$" -exec chmod 755 {} \;
RUN find /var/www/html -type d -exec chmod 755 {} \;
RUN find /var/www/html -type f -iregex ".*\.\(dat\|ini\)$" -exec chmod 666 {} \;

ENV TZ=Asia/Tokyo

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]
