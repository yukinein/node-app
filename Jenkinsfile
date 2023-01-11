pipeline {
    agent any
    environment{
        DOCKER_TAG = getDockerTag()
    }
    stages{
        stage('Build Docker Image'){
            steps{
                sh "docker build . -t alpbugra/example:latest"
            }
        }
        stage("Docker Hub Push"){
            steps{
            withCredentials([string(credentialsId: 'docker-hub', variable: 'dockerHubPwd')]) {
                sh "docker login -u alpbugra -p %dockerHubPwd%"
                sh "docker push alpbugra/example:latest"
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
