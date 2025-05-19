pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/krishmakadia/DockerHeart.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run FastAPI App') {
            steps {
                sh '''
                nohup uvicorn server:app --host 0.0.0.0 --port 8000 > output.log 2>&1 &
                '''
            }
        }
    }
}
