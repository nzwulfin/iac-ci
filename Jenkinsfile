pipeline {
  agent {
    docker {
      image 'centos'
      args ''
    }

  }
  stages {
    stage('Molecule deps') {
      environment {
        WORKSPACE = 'iac-ci/ansible/roles/webserver'
      }
      steps {
        sh '''yum -y install epel-release && \\
    yum -y install gcc python-pip python-devel openssl-devel && \\
    pip install docker molecule testinfra && \\
    yum clean all'''
      }
    }
    stage('Role lint') {
      steps {
        sh 'molecule lint'
      }
    }
    stage('Role dependecies') {
      steps {
        sh 'molecule dependency'
      }
    }
    stage('Role destroy') {
      steps {
        sh 'molecule destroy'
      }
    }
    stage('Role syntax') {
      steps {
        sh 'molecule syntax'
      }
    }
  }
}