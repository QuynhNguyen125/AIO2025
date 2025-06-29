import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt
from typing import List



def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def is_prime(n): 
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]


def solve_quadratic(a: float, b: float, c: float):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm thực"
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép: x = {x}"
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)
        return f"Hai nghiệm: x1 = {x1}, x2 = {x2}"

def register(new_user=None):
    st.markdown("""
        <h2 style='text-align: center;'>📝 Đăng ký người dùng mới</h2>
    """, unsafe_allow_html=True)

    if new_user:
        st.info(f"Người dùng '{new_user}' chưa tồn tại, vui lòng đăng ký")

    with st.form("register_form"):
        new_username = st.text_input("👤 Nhập tên người dùng mới", value=new_user if new_user else "")
        submitted = st.form_submit_button("Đăng ký")
        if submitted:
            if new_username:
                if new_username in st.session_state.users:
                    st.warning("⚠️ Người dùng đã tồn tại")
                else:
                    st.session_state.users.append(new_username)
                    st.success(f"✅ Tạo tài khoản thành công cho: {new_username}")
            else:
                st.warning("⚠️ Vui lòng nhập tên người dùng")

def login():
    st.markdown("""
        <h2 style='text-align: center;'>🔐 Trang đăng nhập</h2>
    """, unsafe_allow_html=True)

    with st.form("login_form"):
        username = st.text_input("👤 Nhập tên người dùng")
        submitted = st.form_submit_button("Đăng nhập")
        if submitted:
            if username:
                if username in st.session_state.users:
                    st.session_state.logged_in = True
                    st.session_state.user_name = username
                else:
                    st.session_state.new_user = username
                    st.rerun()
            else:
                st.warning("⚠️ Vui lòng nhập tên người dùng")

    if "new_user" in st.session_state:
        register(st.session_state.new_user)

def factorial_calculator():
    number = st.number_input("🔢 Nhập số cần tính giai thừa", min_value=0, max_value=900)
    if st.button("Tính giai thừa"):
        result = factorial(int(number))
        st.success(f"✅ Giai thừa của {int(number)} là: {result}")

def prime_checker():
    number = st.number_input("🔍 Nhập số cần kiểm tra nguyên tố", min_value=0, max_value=100000)
    if st.button("Kiểm tra nguyên tố"):
        if is_prime(int(number)):
            st.success(f"✅ {int(number)} là số nguyên tố")
        else:
            st.warning(f"❌ {int(number)} không phải là số nguyên tố")

def fibonacci_generator():
    count = st.slider("🔢 Số phần tử trong dãy Fibonacci", min_value=1, max_value=100, value=10)
    if st.button("Sinh dãy Fibonacci"):
        seq = fibonacci(count)
        st.success(f"Dãy Fibonacci ({count} phần tử):")
        st.code(seq)

def quadratic_solver():
    a = st.number_input("Hệ số a", value=1.0)
    b = st.number_input("Hệ số b", value=0.0)
    c = st.number_input("Hệ số c", value=0.0)
    if st.button("Giải phương trình"):
        if a == 0:
            st.warning("a phải khác 0")
        else:
            result = solve_quadratic(a, b, c)
            st.success(result)

def function_plotter():
    st.markdown("""
        <h3>📉 Vẽ đồ thị hàm số</h3>
    """, unsafe_allow_html=True)

    func_input = st.text_input("Nhập hàm số theo biến x (VD: sin(x), x**2 + 2*x - 3)", value="x**2")
    x_min = st.number_input("Giá trị x nhỏ nhất", value=-10.0)
    x_max = st.number_input("Giá trị x lớn nhất", value=10.0)
    samples = st.slider("Số điểm mẫu", min_value=100, max_value=2000, value=500)

    if st.button("📊 Vẽ đồ thị"):
        try:
            x = np.linspace(x_min, x_max, samples)
            y = eval(func_input, {"x": x, "np": np, "sin": np.sin, "cos": np.cos, "tan": np.tan, "exp": np.exp, "log": np.log})

            fig, ax = plt.subplots()
            ax.plot(x, y, label=f"y = {func_input}")
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_title("Đồ thị hàm số")
            ax.grid(True)
            ax.legend()
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Lỗi: {e}")

def main():
    st.set_page_config(page_title="Công cụ Toán học", page_icon="➗", layout="centered")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user_name" not in st.session_state:
        st.session_state.user_name = ""
    if "users" not in st.session_state:
        st.session_state.users = ["admin"]

    st.markdown("""
        <style>
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f8f9fa;
        }
        .stButton>button {background-color: #4CAF50; color: white; border-radius: 8px; padding: 0.5em 1em;}
        .stNumberInput>div>div>input {font-size: 18px;}
        </style>
    """, unsafe_allow_html=True)

    if st.session_state.logged_in:
        st.markdown(f"""
            <h3 style='text-align: center;'>👋 Xin chào <span style='color:#4CAF50'>{st.session_state.user_name}</span></h3>
        """, unsafe_allow_html=True)

        if st.button("🔓 Đăng xuất"):
            st.session_state.logged_in = False
            st.session_state.user_name = ""
            st.session_state.pop("new_user", None)
            st.rerun()

        option = st.sidebar.selectbox(
            "Chọn chức năng",
            ["Tính giai thừa", "Kiểm tra số nguyên tố", "Sinh dãy Fibonacci", "Giải phương trình bậc 2", "Vẽ đồ thị hàm số"]
        )

        if option == "Tính giai thừa":
            factorial_calculator()
        elif option == "Kiểm tra số nguyên tố":
            prime_checker()
        elif option == "Sinh dãy Fibonacci":
            fibonacci_generator()
        elif option == "Giải phương trình bậc 2":
            quadratic_solver()
        elif option == "Vẽ đồ thị hàm số":
            function_plotter()
    else:
        login()

if __name__ == "__main__":
    main()