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
                    def projectDir = workspace
                    def venDir = "${projectDir}/venv"
                    sh "python3 -m venv ${venvDir}"
                    
                }
            }
        }
    }
}