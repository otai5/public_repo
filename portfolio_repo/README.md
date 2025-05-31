# UI Automation (Web, App)
UI 자동화 테스트를 수행하는 프로젝트입니다.

## 프로젝트 구조

```plaintext
portfolio_repo/
│── conftest.py            # 설정 정보 (Appium 서버, 앱 정보 등)
│── driver.py            # WebDriver 설정 및 초기화
│── main.py              # 테스트 실행 파일
│── pages/               # 페이지 객체 모델(POM) 관련 파일들
│   ├── conftest.py      # 광고 팝업 처리 관련 클래스
│   ├── import_list.py     # 기본 페이지 클래스 (공통 동작 정의)
│   └── object_setting.py    # 로그인 페이지 관련 동작 정의
│── Testcase/               # 실제 테스트 파일들
│   └── test_login.py    # 로그인 테스트 (예시)
│── utils/               # 공통 함수들 및 유틸리티들
│   └── appium_server.py # Appium 서버 실행/종료 유틸리티 (예: server start/stop 자동화)
│── .gitignore           # Git 무시 파일
│── requirements.txt     # 필수 라이브러리 목록
```

## 문제 해결
Appium 서버가 시작되지 않음: Appium이 정상적으로 설치되었는지 확인하고, npm install -g appium으로 최신 버전을 설치해 주세요.
디바이스 연결 문제: adb devices 명령어로 연결된 디바이스가 확인되지 않는다면, Android SDK 설치가 제대로 되었는지, adb 경로가 제대로 설정되었는지 다시 확인해 주세요.
