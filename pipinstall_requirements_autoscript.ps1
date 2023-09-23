# 사용자로부터 패키지 이름 입력 받기
$packageName = Read-Host "Enter the package name to install"

# 패키지 설치
pip install $packageName

# requirements.txt 업데이트
pip freeze | Out-File -FilePath requirements.txt