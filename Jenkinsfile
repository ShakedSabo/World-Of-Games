pipline {
    agent {label 'agent_1'}
    stages {
        stage('Checkout Repository'){
            steps{
                sh echo 'Checkout Repository'
                sh git clone 'https://github.com/ShakedSabo/World-Of-Games.git'
            }
        }
        stage('Build'){
            step{
                sh 'docker build -t shaked/project:new .'
            }
        }
        stage('Testing'){
            agent{
                docker{
                image "shaked/project:new"
                reusNode true
            }
        }
            steps {
                sh 'python3 /app/MainScores.py &'
                sh 'sleep 3'
                sh 'python3 e2e.py'
            }
        }
    }
}
        

