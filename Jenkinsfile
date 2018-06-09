pipeline {
  agent {
    docker {
      image 'centos'
    }

  }
  stages {
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