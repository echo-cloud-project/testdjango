from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import mysql.connector
from django.contrib import messages

# Create your views here.
# main page
def index(request):
    return render(request, "index.html")

def elements(request):
    return render(request, "elements.html")

def generic(request):
    return render(request, "generic.html")

# login page
def login_view(request):
    if request.method == "POST":
        user_id = request.POST['id']
        password = request.POST['password']

        # MySQL 데이터베이스 연결
        db = mysql.connector.connect(
            host="10.10.100.150",  # MySQL 서버 주소
            user="echo",          # MySQL 사용자 이름
            password="test123",   # MySQL 비밀번호
            database="dg"         # 사용할 데이터베이스 이름
        )
        cursor = db.cursor(dictionary=True)

        try:
            # 사용자 확인 쿼리
            query = "SELECT * FROM users WHERE id = %s AND password = %s"
            cursor.execute(query, (user_id, password))
            user = cursor.fetchone()

            if user:
                # 로그인 성공
                messages.success(request, f"Welcome back, {user['id']}!")
                return redirect('index')  # 메인 페이지로 이동
            else:
                # 로그인 실패
                messages.error(request, "Invalid ID or password.")
                return redirect('login')

        except Exception as e:
            messages.error(request, f"Error during login: {e}")
            return redirect('login')

        finally:
            cursor.close()
            db.close()

    return render(request, "login_view.html")

def login_process(request):
    if request.method == "POST":
        user_id = request.POST['id']
        password = request.POST['password']

        # MySQL 데이터베이스 연결
        db = mysql.connector.connect(
            host="10.10.100.150",  # MySQL 서버 주소
            user="echo",          # MySQL 사용자 이름
            password="test123",   # MySQL 비밀번호
            database="dg"         # 사용할 데이터베이스 이름
        )
        cursor = db.cursor(dictionary=True)

        try:
            # 사용자 확인 쿼리
            query = "SELECT * FROM users WHERE id = %s AND password = %s"
            cursor.execute(query, (user_id, password))
            user = cursor.fetchone()

            if user:
                # 로그인 성공, 세션 설정
                request.session['user_id'] = user['id']
                request.session['username'] = user['username']
                messages.success(request, f"Welcome back, {user['username']}!")
                return redirect('index')  # 메인 페이지로 이동
            else:
                # 로그인 실패
                messages.error(request, "Invalid ID or password.")
                return redirect('login')

        except Exception as e:
            messages.error(request, f"Error during login: {e}")
            return redirect('login')

        finally:
            cursor.close()
            db.close()
    else:
        return redirect('login')

# logout success
def logout_view(request):
    request.session.flush()  # 세션 초기화
    messages.success(request, "You have been logged out.")
    return redirect('index')


# signup page
def signup_view(request):
    if request.method == "POST":
        user_id = request.POST['id']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        # 데이터베이스 연결
        db = mysql.connector.connect(
            host="10.10.100.150",  # MySQL 서버 주소
            user="echo",          # MySQL 사용자 이름
            password="test123",   # MySQL 비밀번호
            database="dg"         # 사용할 데이터베이스 이름
        )
        cursor = db.cursor()

        try:
            # ID 중복 확인
            cursor.execute("SELECT COUNT(*) FROM users WHERE id = %s", (user_id,))
            if cursor.fetchone()[0] > 0:
                messages.error(request, "This ID already exists. Please choose another!!!")
                return redirect('signup')

            # 데이터 삽입
            query = """
                INSERT INTO users (id, username, email, phone, password)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (user_id, username, email, phone, password))
            db.commit()
            messages.success(request, "Sign-up successful!")
            return redirect('index')

        except Exception as e:
            messages.error(request, f"Error during signup: {e}")
            return redirect('signup')

        finally:
            cursor.close()
            db.close()

    return render(request, "signup_view.html")