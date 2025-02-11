stage('Run Robot Tests') {
    steps {
        sh '''
            if [ ! -d ".venv" ]; then
                python3 -m venv .venv  # Or virtualenv .venv if you prefer
            fi

            source .venv/bin/activate   # Linux/macOS
            # .venv\\Scripts\\activate.bat  # Windows (adjust if needed)

            pip install -r requirements.txt

            pip list  # Lists installed packages - check for your dependencies
            robot --version # Check Robot Framework version
        '''
        robot framework: 'MyRobotFramework',  // Configured in Global Tool Configuration
              source: 'driver.robot',         // Relative path to your test file
              outputDirectory: 'robot_reports'
    }
}