# 이미지 객체인식 기술을 활용한 애플리케이션 구축
</br>

* as-is 폴더는 최초 제출한 파일들을 모아놓은 폴더입니다.
* 그 외의 폴더 및 파일들이 최종 버전입니다. 
* 현 시간 기준으로 헤로쿠의 서버 오류로 배포가 불가능하여 대기 중입니다. **배포가 완료되는 대로 링크를 추가할 예정입니다.**
* 업로드 한 파일을 기반으로 로컬에서 테스트할 시, static 폴더에 있는 이미지를 테스트용으로 활용해 주시면 되겠습니다.

----
### **12.7 발표 영상 제출 이후 변동 사항 정리**
----
#### 1. 데이터 테이블 스키마 변경
 -> DB를 연동하는 과정에서 데이터 구성이 잘못된 부분을 확인 및 보완 진행
<img width="666" alt="1" src="https://user-images.githubusercontent.com/66727848/145096769-b535495e-3c14-4586-9095-874351214d53.png">
</br></br> 

#### 2. 파일 구성 변경
 -> 기존에는 __init__.py과 routes.py을 하나로 합쳐서 구축하였으나
 
 -> Application Factory 패턴을 유지하기 위해 파일 구성을 변경 (즉, __init__.py과 routes.py을 나누어 구축)
</br></br>

#### 3. SQLite 기반의 DB 연동 진행

 -> 그동안 연동을 실패했던 이유는 Table마다 PK를 지정하지 않았던 것, Migration을 제대로 하지 않았기 때문
 
 -> 이에 데이터 구성 변경 및 Migration을 통해 연동에 성공함
 
 -> 또한 DB 연동을 성공함에 따라 임시로 사용했던 엑셀 파일은 모두 제거
</br></br>

#### 4. CRUD 구현 진행
 -> 다만, 모든 항목을 구현하진 못함 (갱신 및 삭제는 차후 진행 예정)
</br></br>

----
### **이슈 정리**
----
#### 1. 헤로쿠 배포 관련
 -> 현재 해로쿠 서버 문제로 배포를 진행할 수 없음
 
 -> 텐서플로우 라이브러리 용량이 매우 커 이전까지의 배포를 모두 실패함
 
 -> 용량을 줄이기 위해 버전 변경, tensorflow-cpu로 대체 등 다양한 방법을 시도 중
 
 -> 다만, 라이브러리를 바꾸면 애플리케이션이 오류가 나서 시간이 좀 걸릴 것으로 예상됨
 <img width="1021" alt="2" src="https://user-images.githubusercontent.com/66727848/145096791-c9de1386-e24d-4867-b0f0-0ea2eb184021.png">
</br></br>

#### 2. 이미지 객체 인식 모델 관련
 -> 랜드마크 인식을 위해 이미지를 모델에 넣을 경우, 이 이미지가 static 폴더에 없으면 모델이 결과를 내지 못하는 문제가 발생함
 
 -> 우선 원인은 request로 이미지를 받은 후 image_path 변수를 설정하는 과정에 있는 것으로 확인됨
 
 -> 따라서 최소 기능으로 헤로쿠 배포를 완료한 후 해당 문제를 보완할 예정
</br></br>