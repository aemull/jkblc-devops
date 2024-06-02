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
                    // Hentikan dan hapus container jika sudah ada
                    sh 'docker stop my-streamlit-app-container || true'
                    sh 'docker rm my-streamlit-app-container || true'
                    // Jalankan container baru di latar belakang
                    sh 'docker run -d -p 8501:8501 --name my-streamlit-app-container my-streamlit-app'
                }
            }
        }
    }
    
    post {
        succes {
            script {
                // Hentikan dan hapus container setelah selesai
                sh 'docker image prune -f'
            }
        }
    }
}
