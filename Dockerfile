FROM debian:latest

MAINTAINER Ysicing Zheng "root@ysicing.net"

RUN echo "deb http://mirrors.aliyun.com/debian sid main" > /etc/apt/sources.list && \
    apt-get update -y && \
    apt-get install -y python-pip python-dev build-essential

COPY . /app
#WORKDIR /app

RUN pip install -r /app/requirements.txt

RUN chmod +x /app/docker.py

#change timezone
RUN echo "Asia/Shanghai" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["/app/docker.py"]
