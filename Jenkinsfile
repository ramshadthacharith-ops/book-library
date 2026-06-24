pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/ramshadthacharith-ops/book-library.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t book-library-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f book-library || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d --name book-library -p 5000:5000 book-library-app'
            }
        }

    }
}
