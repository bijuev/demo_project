pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the Git repository from the main branch
                git branch: 'main', url: 'https://github.com/bijuev/demo_project.git'
            }
        }

        stage('Build Docker Containers') {
            steps {
                // Build the Docker containers using docker-compose
                sh 'docker compose build'
            }
        }

        stage('Start Docker Containers') {
            steps {
                // Start the Docker containers
                sh 'docker compose up -d'
            }
        }

        stage('Make Migrations') {
            steps {
                // Run makemigrations inside the Django container
                sh 'docker compose exec -T django-app python manage.py makemigrations'
            }
        }

        stage('Migrate') {
            steps {
                // Run migrate inside the Django container
                sh 'docker compose exec -T django-app python manage.py migrate'
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests for the specific Django app 'first_app' inside the container
                sh 'docker compose exec -T django-app python manage.py test first_app'
            }
        }

        stage('Run Server') {
            steps {
                // Optionally run the server (only in development environments)
                sh 'docker compose up -d'
            }
        }
    }

    post {
        always {
            // Clean up or notify after the pipeline finishes
            echo "Pipeline completed"
             sh 'docker compose down'
        }
    }
}
