pipeline {
    agent any
    environment {
        DOCKER_CREDENTIALS = credentials("docker-credentials")
    }

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t whatisbyandby1/brewhouse-backend:latest ./brewhouse_backend'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run --entrypoint pytest brewhouse_backend'
            }
        }
        stage('Push') {
            steps {
                sh 'docker login -u $DOCKERHUB_CREDENTIALS_USR --password $DOCKERHUB_CREDENTIALS_PWD'
                sh 'docker push whatisbyandby1/brewhouse_backend:latest'
            }
        }
    }
}