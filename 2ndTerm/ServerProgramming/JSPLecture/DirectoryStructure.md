디렉토리 구조 분석
  이 폴더는 Eclipse IDE 기반의 JSP/Servlet 웹 프로젝트 워크스페이스입니다. 
  26.08.19 기준 현재 구조는 다음과 같습니다:

    JSPLecture/                          ← Eclipse 워크스페이스 루트
    │
    ├── .gitignore                       ← 현재 /.metadata/ 만 등록됨
    ├── .project                         ← 워크스페이스 메타 파일 (Eclipse)
    │
    ├── .metadata/                       ← Eclipse 워크스페이스 런타임 데이터 (이미 무시됨)
    │   ├── .lock                        ← 워크스페이스 잠금 파일
    │   ├── .log                         ← Eclipse 런타임 로그 (316KB)
    │   ├── .mylyn/                      ← Mylyn 태스크 관리 플러그인 데이터
    │   ├── .plugins/                    ← Eclipse 플러그인 런타임 상태
    │   └── version.ini                  ← Eclipse 버전 정보
    │
    ├── JSP0819/                         ← 오늘(8/19) 생성한 JSP 프로젝트
    │   ├── .classpath                   ← 클래스패스 설정 (JRE 21, Tomcat 9.0)
    │   ├── .project                     ← Eclipse 프로젝트 메타 파일
    │   ├── .gitignore                   ← 프로젝트 레벨 .gitignore (현재 거의 비어있음)
    │   ├── .settings/                   ← Eclipse 프로젝트별 IDE 설정
    │   │   ├── .jsdtscope
    │   │   ├── org.eclipse.core.resources.prefs
    │   │   ├── org.eclipse.jdt.core.prefs
    │   │   ├── org.eclipse.wst.common.component
    │   │   ├── org.eclipse.wst.common.project.facet.core.xml
    │   │   └── org.eclipse.wst.jsdt.ui.*
    │   ├── build/
    │   │   └── classes/                 ← Java 컴파일 결과물 (.class 파일들, 현재 비어있음)
    │   └── src/main/
    │       ├── java/                    ← Java 소스 루트 (현재 비어있음)
    │       └── webapp/                  ← 웹 애플리케이션 루트
    │           ├── Hello0819.jsp        ← ✅ 실습 파일
    │           ├── Welcome.jsp          ← ✅ 실습 파일
    │           ├── META-INF/
    │           │   └── MANIFEST.MF
    │           └── WEB-INF/
    │               └── lib/             ← 외부 JAR 라이브러리 (현재 비어있음)
    │
    └── Servers/                         ← Eclipse Tomcat 서버 설정
        ├── .project
        ├── .settings/
        └── Tomcat v9.0 Server at localhost-config/
            ├── server.xml               ← Tomcat 서버 설정
            ├── web.xml                  ← Tomcat 기본 웹 설정
            ├── context.xml
            ├── catalina.policy
            ├── catalina.properties
            └── tomcat-users.xml         ← ⚠️ 사용자/비밀번호 정보 포함 가능
  ──────
  ## .gitignore 추천 항목 및 이유

  현재 루트 .gitignore에는 /.metadata/ 하나만 있습니다. 
아래 항목들을 추가로 등록하는 것을 권장합니다:

   항목                                            | 이유
  -------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------
   **/.metadata/                                   | Eclipse 워크스페이스 런타임 데이터. 로그, 잠금파일, 플러그인 상태 등 개인 환경에 종속되어 공유 불필요
   **/build/                                       | Java 컴파일 결과물(.class 파일). 소스로부터 재생성 가능하며 바이너리를 Git에 올리는 건 낭비
   **/WEB-INF/lib/*.jar                            | 외부 JAR 라이브러리. 용량이 크고 Maven/Gradle 등 빌드 도구나 별도 관리가 적절 (지금은 비어있지만 추후 추가될 수 있음)
   **/.settings/                                   | Eclipse 개인 IDE 설정 파일들. 다른 사람/환경에서 열면 충돌날 수 있음. 단, 팀 협업 시 일부 공유 필요할 수 있으므로 선택적 적용
   Servers/                                        | Tomcat 서버 로컬 설정 디렉토리. 로컬 포트, 경로, 사용자 비밀번호(tomcat-users.xml) 등 개인 환경 정보 포함 → 보안상 중요
   **/*.class                                      | 혹시 build 폴더 밖에 생성될 수 있는 컴파일 결과물 이중 방어
   **/.log                                         | Eclipse 런타임 로그파일. 용량이 크고 불필요

  ### 특히 주의: tomcat-users.xml

  Servers/Tomcat v9.0 Server at localhost-config/tomcat-users.xml에는 Tomcat 관리자 계정 정보가 포함될 수 있습니다. Servers/ 폴더 전체를 .gitignore에 추가하거나, 최소한 해당 파일만이라도 제외하세요.
  ──────