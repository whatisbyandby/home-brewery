pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker-compose bulid'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}