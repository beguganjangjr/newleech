FROM beguganjang/torrentleech:latest

#COPY . .
COPY setup.sh .
RUN bash setup.sh


COPY start.sh extract rclone.conf extract /app/

COPY tobrot tobrot

RUN apk del wget curl \
    && chmod +x extract
    && chmod 777 rclone.conf
CMD ["bash","start.sh"]
