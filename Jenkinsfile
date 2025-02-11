pipeline{
    agent any

    stages{
        stage('Checkout'){
            steps{
                checkout scm
            }
        }
        stage('Creating Virtual Env'){
            steps{
                script{
                    sh "python --version"
                }
            }
        }
    }
}