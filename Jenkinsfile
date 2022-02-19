pipeline {
    agent any
    environment {
        DOCKER_CREDENTIALS = credentials("docker-credentials")
    }

    stages {
        stage('Build') {
            steps {
                docker.build('whatisbyandby1/brewhouse-backend')
            }
        }
        stage('Test') {
            steps {
                sh 'docker run --entrypoint pytest brewhouse_backend'
            }
        }
        stage('Push') {
            docker.withRegistry("https://registry.hub.docker.com", 'docker-credentials'){
                steps {
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    sh 'docker push brewhouse_backend:latest'
                }
            }
        }
    }
}