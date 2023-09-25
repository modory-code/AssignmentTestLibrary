# 과제

## 수행 환경 및 기술 버전

-   운영체제: Windows 11 pro
-   언어: Python v3.10.5
-   웹 프레임워크: FastAPI v0.103.1
-   데이터베이스: MariaDB v11.3.0
-   ORM: SQLAlchemy v2.0.21

## 명령어

### 패키지 설치

```shell
pip install -r requirements.txt
```

### 앱 실행

```shell
uvicorn main:app --reload
```

## pip install & pip requirements.txt 자동화 사용법

### 윈도우

1. 실행 정책 설정 (옵션): PowerShell은 스크립트 실행을 기본적으로 제한합니다. 스크립트를 실행하려면 실행 정책을 변경해야 할 수 있습니다. 다음 명령어를 사용하여 실행 정책을 변경할 수 있습니다. 이 단계는 처음 한 번만 수행하면 됩니다.

```shell
Set-ExecutionPolicy RemoteSigned
```

만약 아래와 같은 에러가 뜬다면,

```shell
Set-ExecutionPolicy : 레지스트리 키 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell'
에 대한 액세스가 거부되었습니다. 기본(LocalMachine) Scope에 대한 실행 정책을 변경하려면 "관리자 권한으로 실행" 옵션으로
 Windows PowerShell을 시작하십시오. 현재 사용자에 대한 실행 정책을 변경하려면 "Set-ExecutionPolicy -Scope CurrentUser"
를 실행하십시오.
위치 줄:1 문자:1
+ Set-ExecutionPolicy RemoteSigned
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (:) [Set-ExecutionPolicy], UnauthorizedAccessException
    + FullyQualifiedErrorId : System.UnauthorizedAccessException,Microsoft.PowerShell.Commands.SetExecutionPolicyComma
   nd
```

PowerShell을 관리자 권한으로 실행 후 다음 명령어를 입력합니다.

```shell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

`Get-ExecutionPolicy -List`를 통해 아래와 같이 CurrentUser에 대해 권한 변경이 되었다면 2번으로 넘어갑니다.

```shell
        Scope ExecutionPolicy
        ----- ---------------
MachinePolicy       Undefined
   UserPolicy       Undefined
      Process       Undefined
  CurrentUser    RemoteSigned
 LocalMachine    RemoteSigned
```

2. 다음 명령어를 입력합니다.

```shell
.\pipinstall_requirements_autoscript.ps1
```

아래와 같이 뜬다면 설치할 pip 라이브러리명을 입력하고 enter 키를 누릅니다.

```shell
Enter the package name to install:
```

3. 입력한 pip 라이브러리가 설치되고 requirements.txt가 자동으로 업데이트됩니다.
