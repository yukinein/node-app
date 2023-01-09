pipeline {
    agent any
    environment{
        DOCKER_TAG = getDockerTag()
    }
    stages{
        stage('Build Docker Image'){
            steps{
                bat "docker build . -t yukinein/nodeapp:Dockerfile "
            }
        }
        stage("Docker Hub Push"){
            steps{
            withCredentials([string(credentialsId: 'docker-hub', variable: 'dockerHubPwd')]) {
                bat "docker login -u alpbugra --password-stdin %dockerHubPwd%"
                bat "docker push alpbugra/nodeapp:Dockerfile"
            }
            }
        }
    }
}

def getDockerTag(){
    def tag  = bat script: 'git rev-parse HEAD', returnStdout: true
    return tag
}
