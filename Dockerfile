FROM beguganjang/torrentleech:latest

#COPY . .
COPY setup.sh .
RUN bash setup.sh


COPY start.sh extract extract /app/

COPY tobrot tobrot

RUN apk del wget curl \
    && chmod +x extract
CMD ["bash","start.sh"]
