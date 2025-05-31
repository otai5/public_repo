# UI 자동화 테스트 - 로그인 & 메인 페이지 플로우

App(Android만 대표로 작성) / Web 환경에서의 **로그인 → 메인 페이지 진입** 플로우를 검증하는 UI 자동화 테스트 스크립트입니다.  
테스트 대상 앱은 최신 버전이 설치되어 있다고 가정합니다.

---

## 주요 특징

## POM(Page Object Model) 구조
- 각 페이지별 UI 요소 및 액션을 별도 클래스로 분리
- 코드 중복 제거 및 유지보수성 향상
- 테스트 코드에서 객체 재사용 가능

---

## 디렉토리 구조
```
android-main
│── conftest.py            # 설정 정보 (드라이버, 서버 정보 등)
│── pages/               # 페이지 객체 모델(POM) 폴더
│   ├── import_list.py     # 기본 import 통합 관리
│   └── object_setting.py    # 공통 요소/ 함수 정의
│── Testcase/               # 테스트 케이스/시나리오
│   └── test_login.py    # 로그인 테스트
│── requirements.txt     # 필수 라이브러리 목록 (생략)
```
