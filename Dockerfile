FROM centos:7
ENV container docker
RUN yum update -y
RUN yum install --assumeyes python bash openssh-client curl net-tools
COPY server.py /server.py
ENTRYPOINT ["/server.py"]
