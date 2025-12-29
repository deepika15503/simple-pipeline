pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/deepika15503/simple-pipeline'
            }
        }

        stage('Run Data Pipeline') {
            steps {
                // Windows: use bat, Linux: use sh
                bat 'python scripts\process_data.py'
            }
        }

        stage('Display Output') {
            steps {
                bat 'type data\output.txt'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Pipeline ran correctly'
        }
        failure {
            echo 'ERROR: Pipeline failed'
        }
    }
}
