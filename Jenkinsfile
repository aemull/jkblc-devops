pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
        PYTHON = "${env.WORKSPACE}/${env.VIRTUAL_ENV}/bin/python"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/aemull/jkblc-devops.git'
            }
        }
        
        stage('Install python3-venv') {
            steps {
                sh 'sudo apt-get update'
                sh 'sudo apt-get install -y python3-venv'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh '${PYTHON} -m pip install --upgrade pip'
                sh '${PYTHON} -m pip install -r requirements.txt'
            }
        }
        
        stage('Run Application') {
            steps {
                sh '${PYTHON} -m streamlit run app.py'
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
