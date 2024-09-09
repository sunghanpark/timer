import streamlit as st
import time

def countdown_timer(seconds):
    placeholder = st.empty()
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        with placeholder.container():
            st.header(f"⏳ 남은 시간: {time_format}")
        time.sleep(1)
        seconds -= 1
    
    placeholder.empty()
    st.balloons()
    st.header("🎉 타이머 종료!")

st.title("카운트다운 타이머")

duration = st.number_input("타이머를 몇 초로 설정하시겠습니까?", min_value=1, value=60, step=1)

if st.button("타이머 시작"):
    countdown_timer(int(duration))
