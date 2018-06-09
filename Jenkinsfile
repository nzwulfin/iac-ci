pipeline {
  agent {
    docker {
      args ''
      image 'molecule-base'
    }

  }
  stages {
    stage('Role syntax') {
      steps {
        sh '''cd $ROLEDIR
molecule syntax'''
      }
    }
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
    stage('Role idempotence') {
      steps {
        sh '''cd $ROLEDIR
molecule idempotence'''
      }
    }
    stage('Role side_effect') {
      steps {
        sh '''cd $ROLEDIR
molecule side-effect'''
      }
    }
    stage('Role verify') {
      steps {
        sh '''cd $ROLEDIR
molecule verify'''
      }
    }
    stage('Stage Ansible run') {
      steps {
        ansiblePlaybook(playbook: 'ansible/site.yml', disableHostKeyChecking: true, colorized: true, inventory: 'ansible/inventory', credentialsId: 'ansiblekey')
      }
    }
  }
  environment {
    ROLEDIR = 'ansible/roles/webserver'
  }
}