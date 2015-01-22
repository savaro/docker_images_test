FROM index.alauda.io/chennanfei/mathilde_env

ADD gondar_start.sh /gondar_start.sh
RUN chmod +x /gondar_start.sh

ADD gondar /app
WORKDIR /app

CMD ["/gondar_start.sh"]
