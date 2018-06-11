FROM centos/systemd

RUN yum -y install epel-release && \
    yum -y install gcc python-pip python-devel openssl-devel docker firewalld && \
    pip install docker molecule testinfra && \
    systemctl enable firewalld --now && \
    yum clean all

