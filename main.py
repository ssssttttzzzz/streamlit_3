import streamlit as st
import random
def compare(a,b):
    sheet1 = {'剪刀': 0, '石头': 1, '布': 2}
    if sheet1[a] - sheet1[b] == 0:
        out_p = ["平局", 2]
    elif sheet1[a] - sheet1[b] == 1 or sheet1[a] - sheet1[b] == -2:
        out_p = ["你赢啦！！", 1]
    else:
        out_p = ["输掉了T.T", 0]
    return out_p
cop_of = ['剪刀', '石头', '布']
st.title("连赢三局拿红包哦！")
st.header("一共十次机会！")
mark = 0
for i in range(10):
    pg = (i+1)/10
    option = st.selectbox(
        '选一个出拳吧！',
        ('剪刀', '石头', '布'))
    cop = random.randint(0, 2)
    cop_o = cop_of[cop]
    st.write('我出的是：', cop_o)
    com = compare(option, cop_o)
    st.write("第", i, "局:", com[0])
    if com[1] == 1:
        mark += 1
    elif com[1] == 0:
        mark = 0
    if mark == 3:
        break
    elif i == 9:
        st.write("机会用完啦")
    else:
        pass
st.write("现在连赢", mark, "局")
if mark == 3:
    st.balloons()
    st.write("口令红包是：俺也能赢得胜利哦")
