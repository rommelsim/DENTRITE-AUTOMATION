pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/rommelsim/DENTRITE-AUTOMATION.git'
            }
        }
        stage('Run Robot Tests') {
            steps {  // The 'steps' block is now correctly inside the 'stage'
                sh '''
                    # Install Python if it's not already on the agent (important!)
                    if [ ! -x "/usr/bin/python3" ]; then  # Check if python3 is installed
                        sudo apt-get update  # Update package lists (Debian/Ubuntu)
                        sudo apt-get install -y python3 python3-venv  # Install Python and venv
                    fi

                    # Create the virtual environment
                    python3 -m venv .venv

                    # Activate the virtual environment
                    source .venv/bin/activate

                    # Install dependencies
                    pip install -r requirements.txt

                    # Install Robot Framework (if not in requirements.txt)
                    pip install robotframework # If not in requirements.txt

                    # Verify installations
                    pip list
                    robot --version

                    # Run Robot Framework (path to robot is now within the venv)
                    .venv/bin/robot driver.robot # Linux/macOS
                    # .venv\\Scripts\\robot.exe driver.robot # Windows (adjust slashes)
                '''
            }
        }
    }
}