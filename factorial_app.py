import streamlit as st

USERS = ["admin"]
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def login():
    st.title("Trang đăng nhập")
    username = st.text_input("Nhập tên người dùng")
    if st.button("Đăng nhập"):
        if username:
            if username in USERS:
                st.session_state.logged_in = True
                st.session_state.user_name = username
            else: 
                st.session_state.logged_in = False
                st.session_state.user_name = username
                st.warning(f"{st.session_state.user_name} không có quyền đăng nhập")
        else: 
            st.warning("Nhập tên người dùng")

def factorial_calculator():
    st.write(f"Xin chào {st.session_state.user_name}")
    # Đăng xuất
    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.session_state.user_name = ""
        st.rerun()
    
    number = st.number_input("Nhập vào một số", min_value=0, max_value=900)
    if st.button("Tính giai thừa"):
        result = factorial(int(number))
        st.write(f"Giai thừa của {number} = {result}")
        
def main():
    st.title("Ứng dụng tính giai thừa")
    # Khởi tạo tham số session
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.user_name = ""

    if st.session_state.logged_in:
        factorial_calculator()
    else:
        login()

if __name__ == "__main__":
    main()