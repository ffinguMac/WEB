# vuln_test.py

from flask import Flask, request

app = Flask(__name__)

# 1. 신규 엔드포인트 추가 (New Endpoint)
@app.route('/new-api')
def new_api():
    return "This is a new endpoint"

# 2. XSS 취약점
@app.route('/greet')
def greet():
    name = request.args.get('name')
    # 사용자 입력을 그대로 HTML에 출력 (XSS)
    return f"<h1>Hello {name}</h1>"

# 3. 하드코딩된 시크릿
def connect_db():
    password = "SuperSecretPassword1234"
    # ... DB 연결 코드 ...

# 4. 인증 우회 취약점
def is_admin(user):
    # 인증 우회 취약점 (항상 True 반환)
    return True

# 5. 개인정보(PII) 노출 및 수집
def save_user_info(user):
    # 개인정보(이메일, 전화번호 등) 로그에 노출
    print(f"User email: {user['email']}")
    print(f"User phone: {user['phone']}")

def collect_user_data(request):
    # 개인정보 수집
    user_ssn = request.form['ssn']
    user_address = request.form['address']
    # ... 저장 로직 ...
