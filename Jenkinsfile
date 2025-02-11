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

                    if(fileExist(venDir)){
                        echo "Virtual environment already exists. Skipping creation."
                    }
                    else{
                        echo "Creating virtual environment in ${venvDir}..."
                        sh "python3 -m venv ${venvDir}"
                    }
                }
            }
        }
    }
}