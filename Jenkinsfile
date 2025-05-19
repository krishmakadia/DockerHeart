pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/krishmakadia/DockerHeart.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                C:/ProgramData/anaconda3/python.exe -m pip install --upgrade pip
                C:/ProgramData/anaconda3/python.exe -m pip install -r requirements.txt
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
