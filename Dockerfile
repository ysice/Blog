FROM debian:latest

MAINTAINER YsiCing Zheng "root@ysicing.net"

RUN echo "deb http://mirrors.aliyun.com/debian sid main" > /etc/apt/sources.list && \
    apt-get update -y && \
    apt-get install -y sudo git openssl python3 python3-pip python3-dev build-essential

RUN mkdir /data
COPY . /data/blog
WORKDIR /data/blog

#In China
#RUN pip3 install -r requirements.txt -i https://pypi.douban.com/simple
#RUN pip install pymysql -i https://pypi.douban.com/simple
#Outside
RUN pip3 install -r requirements.txt

RUN chmod +x ./run.py

RUN echo "Asia/Shanghai" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

EXPOSE 4000

ENTRYPOINT ["python3"]
CMD ["./run.py"]