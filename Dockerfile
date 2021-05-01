FROM beguganjang/torrentleech:latest

#COPY . .
COPY setup.sh .
RUN bash setup.sh


ADD https://raw.githubusercontent.com/maple3142/aria2c-ariang/master/aria2c.conf apic.conf
COPY start.sh extract extract /app/

COPY tobrot tobrot

RUN apk del wget curl \
    && chmod +x extract
CMD ["bash","start.sh"]
