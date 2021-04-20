FROM alpine:edge

RUN mkdir ./app
RUN chmod 777 ./app
RUN chmod 777 /app
WORKDIR /app

RUN sed -e 's;^#http\(.*\)/edge/community;http\1/edge/community;g' -i /etc/apk/repositories
RUN apk update && apk add --no-cache -q \
    python3-dev python3 py3-pip aria2 \
    ffmpeg unzip unrar tar wget curl bash git && \
    apk add -qq --no-cache --virtual .build-deps \
    build-base zlib-dev jpeg-dev gcc musl-dev \
    libffi-dev libxml2-dev libxslt-dev openssl-dev cargo && \
    wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    wget -q https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.32-r0/glibc-2.32-r0.apk && \
    apk add -q glibc-2.32-r0.apk && \
    rm /etc/apk/keys/sgerrand.rsa.pub && \
    rm glibc-2.32-r0.apk && \
    rm -r /var/cache/apk/APKINDEX.* && \
    rm -rf /tmp/* /var/cache/apk/* /var/tmp/*
#RUN python3 -m pip install -U pip

#COPY . .
#COPY setup.sh .
#RUN bash setup.sh

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .

#RUN apk del .build-deps
RUN chmod +x extract
CMD ["bash","start.sh"]
