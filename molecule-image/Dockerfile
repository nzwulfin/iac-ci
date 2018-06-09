FROM centos

RUN yum -y install epel-release && \
    yum -y install gcc python-pip python-devel openssl-devel docker && \
    pip install docker molecule testinfra && \
    yum clean all

