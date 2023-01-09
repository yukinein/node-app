pipeline {
    agent any
    environment{
        DOCKER_TAG = getDockerTag()
    }
    stages{
        stage('Build Docker Image'){
            steps{
                bat "docker build . -t alpbugra/nodeapp:latest"
            }
        }
        stage("Docker Hub Push"){
            steps{
            withCredentials([string(credentialsId: 'docker-hub', variable: 'dockerHubPwd')]) {
                bat "docker login -u alpbugra -p %dockerHubPwd%"
                bat "docker push alpbugra/nodeapp:latest"
            }
            }
        }
        stage('Deploying App to Kubernetes') {
      steps {
        script {
          kubernetesDeploy(configs: "deploymentservice.yml", kubeconfigId: "kubernetes")
        }
      }
    }
    }
}

def getDockerTag(){
    def tag  = bat script: 'git rev-parse HEAD', returnStdout: true
    return tag
}
