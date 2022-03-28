import streamlit as st
st.title("what")
st.header("????")
if st.button("第一题"):
    st.write("找规律")
    st.markdown("- 1 3 7 _")
    st.markdown("- 2 4 6 _")
    st.markdown("- 5 9 _")
answer1 = st.selectbox(
    '8填第几行？',
    ('第三行', '第二行', '第一行'))
if answer1 == "第一行":
    st.write("对啦！")
if st.button("第二题"):
    st.write("一个屋子有很多桌子和人，已知2人一桌多1人，3人一桌多2人，4人一桌\
             多3人，5人一桌多4人，6人一桌多5人，7人一桌多6人，8人一桌多7人，9人一桌\
             多8人，10人一桌多9人，11人一桌刚好，问一共几人？")
answer2 = st.text_input("输入至少人数的数字")
if answer2 == "2519":
    st.write("对啦！")
if st.button("第三题"):
    st.write("F(1)=9, F(2)=25, F(3)=49, f(1)=3, f(2)=5 ,f(3)=7, F(4)= ?")
answer3 = st.text_input("输入数字")
if answer3 == "81":
    st.write("对啦！")
if answer1 == "第一行" and answer2 == "2519" and answer3 == "81":
    st.subheader("赢啦！")
    st.balloons()
    st.write("口令红包是：嘿嘿俺赢得胜利啦")
else:
    st.subheader("还没全答对哦")
