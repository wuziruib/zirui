import streamlit as st
import pandas as pd
import os

# 设置问卷标题
st.title("调查问卷")

# 问卷说明
st.write("感谢您参与本次问卷调查，请根据您的实际情况填写以下内容。")

# CSV 文件路径
csv_file = "responses.csv"

# 定义一个函数来保存数据
def save_to_csv(data):
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        df = df.append(data, ignore_index=True)
    else:
        df = pd.DataFrame([data])
    df.to_csv(csv_file, index=False)

# 第一个问题: 你是学生还是老师
role = st.radio("1. 你是学生还是老师？", ("学生", "老师"))

# 初始化答案字典
responses = {"身份": role}

# 如果选择学生
if role == "学生":
    st.write("### 学生部分问题")
    
    # 学生问题 1
    q1 = st.radio("1.1. 您的专业是否会被要求去学习计算机语言？", ("是", "否"))
    responses["专业是否要求学习计算机语言"] = q1
    
    # 学生问题 2
    q2 = st.selectbox("1.2. 您认为您的计算机水平是什么样的？", ["初学者", "中级", "高级", "专家"])
    responses["计算机水平"] = q2
    
    # 学生问题 3
    q3 = st.text_area("1.3. 您如何学习计算机语言的？")
    responses["如何学习计算机语言"] = q3
    
    # 学生问题 4
    q4 = st.radio("1.4. 您曾经是否使用过AI来学习计算机语言？", ("是", "否"))
    responses["是否使用过AI学习计算机语言"] = q4
    
    # 如果使用过AI
    if q4 == "是":
        q5 = st.radio("1.4.1. 您认为AI系统对您的学习帮助大不大？", ("帮助很大", "一般", "帮助不大"))
        responses["AI系统对学习的帮助"] = q5
    else:
        q6 = st.radio("1.4.2. 未来的您是否会尝试使用AI系统来学习计算机语言？", ("会", "不会", "不确定"))
        responses["未来是否会尝试使用AI系统"] = q6
    
    # 学生问题 5
    q7 = st.radio("1.5. 您是否使用过ChatGPT、Copilot等AI来询问过一些在您学习计算机时碰到的困难？", ("是", "否"))
    responses["是否使用过ChatGPT等AI询问学习难题"] = q7
    
    # 学生问题 6
    q8 = st.selectbox("1.6. 您正在上大几？", ["大一", "大二", "大三", "大四", "研究生"])
    responses["年级"] = q8
    
    # 学生问题 7
    q9 = st.text_input("1.7. 您学习计算机语言多久了？")
    responses["学习计算机语言时间"] = q9

# 如果选择老师
elif role == "老师":
    st.write("### 老师部分问题")
    
    # 老师问题 1
    q1 = st.radio("2.1. 您认为现在的学生，他们学习计算机代码的能力是增强还是正在退步？", ("增强", "退步"))
    responses["学生学习能力变化"] = q1
    
    # 老师问题 2
    q2 = st.radio("2.2. 您使用过ChatGPT、Copilot等AI来解决在您研究上所碰到的一些计算机语言类难题吗？", ("是", "否"))
    responses["是否使用过AI解决研究难题"] = q2
    
    # 老师问题 3
    q3 = st.radio("2.3. 您是否相信AI学习系统会全方面地帮助学生学习计算机语言，而不是只是让学生短暂学习？", ("相信", "不相信", "不确定"))
    responses["是否相信AI系统全面帮助学生"] = q3

# 提交按钮
if st.button("提交"):
    save_to_csv(responses)
    st.success("感谢您的参与！您的答案已提交。")

# 显示已提交的结果
if os.path.exists(csv_file):
    st.write("### 当前所有提交的答案：")
    df = pd.read_csv(csv_file)
    st.dataframe(df)
