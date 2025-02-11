pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/rommelsim/DENTRITE-AUTOMATION.git'
            }
        }

        stage('Run Robot Tests') {
            steps {
                sh 'robot driver.robot'
            }
        }
    }
}