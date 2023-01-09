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
    }
}

def getDockerTag(){
    def tag  = bat script: 'git rev-parse HEAD', returnStdout: true
    return tag
}
