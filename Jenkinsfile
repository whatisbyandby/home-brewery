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
                sh 'echo $DOCKER_CREDENTIALS_PSW | docker login -u $DOCKER_CREDENTIALS_USR --password-stdin'
                sh 'docker push whatisbyandby1/brewhouse-backend:latest'
            }
        }
    }
}