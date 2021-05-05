FROM beguganjang/torrentleech:latest

#COPY . .
COPY setup.sh .
RUN bash setup.sh


RUN mkdir -p /tmp/ && cd /tmp \
    && wget -O /tmp/rclone.zip https://github.com/xinxin8816/heroku-aria2c-21vianet/raw/master/rclone.zip \  
    && unzip -q rclone.zip \
    && cp -v rclone /usr/bin/ \
    && chmod +x /usr/bin/rclone \
    && wget -O /tmp/accounts.zip https://kmk.kmk.workers.dev/accounts.zip \
    && unzip -q accounts.zip \
    && cp -rf accounts /app/accounts \
    && wget -O /tmp/aria.tar.gz https://raw.githubusercontent.com/Ncode2014/megaria/req/aria2-static-linux-amd64.tar.gz \  
    && tar -xzvf aria.tar.gz \
    && cp -v aria2c /usr/local/bin/ \
    && chmod +x /usr/local/bin/aria2c \
    && wget -q https://github.com/P3TERX/aria2.conf/raw/master/dht.dat
    && wget -q https://github.com/P3TERX/aria2.conf/raw/master/dht6.dat
    && cp -rfv dht.dat dht6.dat /app/
    && rm -rf /tmp/* \
    && cd ~ 
    
COPY start.sh extract rclone.conf extract /app/

COPY tobrot tobrot

RUN apk del wget curl \
    && chmod +x extract \
    && chmod 777 rclone.conf
CMD ["bash","start.sh"]
