pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/rommelsim/DENTRITE-AUTOMATION.git'
            }
        }
        stage('Run Robot Tests') {
            steps {  
                sh '''
                    python3 -m venv .venv
                    source .venv/bin/activate

                    pip install -r requirements.txt
                    pip install robotframework 

                    pip list
                    robot --version

                '''
            }
        }
    }
}