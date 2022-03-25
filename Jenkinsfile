pipeline {
    agent { label 'agent_1' }
    stages {
        stage('Checkout Repository'){
            steps{
                sh 'echo Check Repo'
                sh 'git clone https://github.com/ShakedSabo/World-Of-Games.git'
            }
        }
        stage('Build docker image'){
            steps{
                sh 'docker build -t shaked/project:pipeline World-Of-Games'
            }
        }
        stage('Run & Test') {
            agent {
                docker {
                    image "shaked/project:pipeline"
                    reuseNode true
                }
            }
            steps {
                sh 'python3 /app/MainScores.py &'
                sh 'sleep 5'
                sh 'python3 World-Of-Games/tests/e2e.py'
            }
        }
        stage('End container'){
            steps{
                sh 'docker stop shaked/project:pipeline World-Of-Games'
            } 
        }
    }
}

