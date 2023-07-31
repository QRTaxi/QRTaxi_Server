# 🚖 QRTaxi - 큐택 서버

## 💻 기술 스택
<div style='flex'>
<img src="https://img.shields.io/badge/Python3.9.5-3776AB?style=for-the-badge&logo=Python&logoColor=white" >
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
<ing src="https://camo.githubusercontent.com/4590c0af4aeb1b75233885f86e80c1da8cb2afd401173a40e41370f5cad5db20/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a57542d626c61636b3f7374796c653d666f722d7468652d6261646765266c6f676f3d4a534f4e253230776562253230746f6b656e73">

<img src="https://camo.githubusercontent.com/c1fc168684171582321954905e8b9dc4f59810243ed85e645f3b7938ee3145cb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d7973716c2d3434373941313f7374796c653d666f722d7468652d6261646765266c6f676f3d6d7973716c266c6f676f436f6c6f723d7768697465">
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white">
<ing src="https://camo.githubusercontent.com/cb6a8acb6cd719636cea6cce9de8a98986f895d0a4da406400db37f4a115604c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646f636b6572206875622d3234393645443f7374796c653d666f722d7468652d6261646765266c6f676f3d646f636b6572266c6f676f436f6c6f723d7768697465">
<img src="https://img.shields.io/badge/Amazon EC2-FF9900?style=for-the-badge&logo=Amazon EC2&logoColor=white">
<img src="https://img.shields.io/badge/Amazon RDS-527FFF?style=for-the-badge&logo=Amazon RDS&logoColor=white">
</div>

## 🚖 구성원 및 역할분담

</br>

## 🚖 ERD
<img width="785" alt="" src="https://qrtaxi.s3.ap-northeast-2.amazonaws.com/logo/erd.png">
</br>

## 🚖 API 명세서
http://api.qrtaxi.kro.kr/swagger/
</br>


## 📌 컨벤션
### 커밋 메세지
- feat: : 새로운 기능 추가/수정/삭제
- refactor : 버그를 수정하거나 기능 추가가 없는 단순 코드 변경
- fix: 버그, 오류 해결
- test: : 테스트 코드
- chore: 빌드 업무 수정, settings.py 수정 등
- docs: Readme를 비롯한 문서 변경시
- init: initial commit을 할 시
- build: 라이브러리 추가 등
- !HOTFIX: 치명적 버그를 급하게 수정할 때

### 네이밍 규칙
- class: Pascal ex) MyClass, PersonInfo
- Variable: Snake ex) user_name, total_count
- Function: Snake ex) calculate_total, get_user_data
- Constant : Pascal + Snake pascal ex) MAX_SIZE, DEFAULT_TIMEOUT
### 주석
- Docstring을 활용하여 클래스와 함수단위에 설명을 적어주도록 하자.
```python
def delete_post(post_id):
    """
    모든게시판의 Delete를 담당하는 view
    """
```

### 🚷 큐택 서버 규칙

1. 빠른 개발을 위해 각자 branch에서 `main` 브랜치에 PR을 날려요.
2. PR올리면 카톡으로 알려주고, 그 날 자정까지 확인하고 코드 리뷰를 후 승인 뒤에 `merge`해요.
3. DB 관련된 `model` 코드 수정은 한명이 해요. 모델 수정이 필요하면 공유해요.
4. 커밋 메세지를 잘 지켜요.
5. 주석 및 네이밍 규칙도 잘 지켜요.
6. 한 일과, 해야할 일을 솔직하게 공유해요.

</br>
</br>


