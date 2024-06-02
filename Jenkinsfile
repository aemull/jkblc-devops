pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/aemull/jkblc-devops.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("my-streamlit-app")
                }
            }
        }
        
        stage('Run Docker Container') {
            steps {
                script {
                    docker.image("my-streamlit-app").inside('-p 8501:8501') {
                        sh 'streamlit run app.py'
                    }
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
