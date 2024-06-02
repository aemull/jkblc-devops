pipeline {
    agent any

    environment {
        REPO = 'aemull/jkblc-devops'
        BRANCH = 'main'
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
                    def customImage = docker.build("${env.IMAGE_NAME}:${env.BUILD_ID}")
                }
            }
        }

       // stage('Push Docker Image') {
       //     steps {
       //         script {
       //             docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials-id') {
       //                 def customImage = docker.image("${env.IMAGE_NAME}:${env.BUILD_ID}")
       //                 customImage.push()
       //             }
       //         }
       //     }
       // }

        stage('Deploy') {
            steps {
                script {
                    sh "docker run -d -p 8501:8501 ${env.IMAGE_NAME}:${env.BUILD_ID}"
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    sh "docker rm -f $(docker ps -a -q --filter ancestor=${env.IMAGE_NAME}:${env.BUILD_ID})"
                    sh "docker rmi ${env.IMAGE_NAME}:${env.BUILD_ID}"
                }
            }
        }
    }
}
