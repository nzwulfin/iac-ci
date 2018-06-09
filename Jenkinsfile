pipeline {
  agent {
    docker {
      args ''
      image 'molecule-base'
    }

  }
  stages {
    stage('Role dependecies') {
      steps {
        sh '''cd $ROLEDIR
molecule dependency'''
      }
    }
    stage('Role create') {
      steps {
        sh '''cd $ROLEDIR
molecule create'''
      }
    }
    stage('Role prepare') {
      steps {
        sh '''cd $ROLEDIR
molecule prepare'''
      }
    }
    stage('Role converge') {
      steps {
        sh '''cd $ROLEDIR
molecule converge'''
      }
    }
    stage('Role verify') {
      steps {
        sh '''cd $ROLEDIR
molecule verify'''
      }
    }
  }
  environment {
    ROLEDIR = 'ansible/roles/webserver'
  }
}