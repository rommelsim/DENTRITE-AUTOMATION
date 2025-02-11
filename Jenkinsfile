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
                sh '''
                    # Create the virtual environment (if it doesn't exist)
                    if [ ! -d ".venv" ]; then  # Check for the .venv directory
                        python3 -m venv .venv
                    fi

                    # Activate the virtual environment
                    source .venv/bin/activate  # Linux/macOS
                    # .venv\\Scripts\\activate   # Windows (adjust if needed)

                    # Install dependencies (from requirements.txt)
                    pip install -r requirements.txt
                '''
                robot framework: 'MyRobotFramework',  // Important: Configure this (see below)
                      source: 'driver.robot',         // Path to your test file
                      outputDirectory: 'robot_reports'
            }
        }
    }
}