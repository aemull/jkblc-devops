pipeline {
    agent any

    environment {
        REPO = 'aemull/jkblc-devops'
        BRANCH = 'master'
        //IMAGE_NAME = 'your-dockerhub-username/streamlit-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: "*/${BRANCH}"]],
                          userRemoteConfigs: [[url: "https://github.com/${REPO}.git"]]])
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${env.BUILD_ID}")
                }
            }
        }

       // stage('Push Docker Image') {
         //   steps {
           //     script {
             //       docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials-id') {
               //         docker.image("${IMAGE_NAME}:${env.BUILD_ID}").push()
                 //   }
              //  }
           // }
        //}

        stage('Deploy') {
            steps {
                script {
                    // Deploy steps
                    sh 'docker run -d -p 8501:8501 ${IMAGE_NAME}:${env.BUILD_ID}'
                }
            }
        }
    }
}
