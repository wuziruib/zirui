import streamlit as st
import pandas as pd
import os

# 设置问卷标题
st.title("调查问卷：对AI系统学习计算机语言的看法")

# 问卷说明
st.write("感谢您参与本次问卷调查，旨在了解学生和老师对于使用AI系统学习计算机语言的看法。请根据您的实际情况填写以下内容。")

# CSV 文件路径
csv_file = "responses.csv"

# 定义一个函数来保存数据
def save_to_csv(data):
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    else:
        df = pd.DataFrame([data])
    df.to_csv(csv_file, index=False)

# 初始化答案字典
responses = {}

# 第一个问题: 你是学生还是老师
role = st.selectbox("1. 您的身份是？", ["请选择", "学生", "老师"])

if role != "请选择":
    responses["身份"] = role
    
    # 如果选择学生
    if role == "学生":
        st.write("### 学生部分问题")

        # 学生问题 1
        q1 = st.selectbox("1.1. 您的专业是否需要学习计算机语言来完成课程或项目？", ["请选择", "必修", "选修", "不需要"])
        if q1 != "请选择":
            responses["专业是否要求学习计算机语言"] = q1

            # 学生问题 2
            q2 = st.selectbox("1.2. 您如何评价自己在计算机编程方面的熟练程度？", ["请选择", "完全不会编程", "初学者（了解基础语法）", "中级（能够独立完成简单项目）", "高级（熟悉多种语言，能解决复杂问题）", "专家（深入了解算法与系统设计）"])
            if q2 != "请选择":
                responses["计算机水平"] = q2

                # 学生问题 3
                q3 = st.multiselect("1.3. 您主要通过哪些方式学习计算机语言？", ["课堂学习", "自学教程/书籍", "在线课程", "与同学或朋友讨论", "AI工具或软件"], [])
                if q3:
                    responses["如何学习计算机语言"] = ', '.join(q3)

                    # 学生问题 4
                    q4 = st.selectbox("1.4. 您曾经使用过AI工具（如ChatGPT、Copilot等）辅助学习计算机语言吗？", ["请选择", "是", "否"])
                    if q4 != "请选择":
                        responses["是否使用过AI学习计算机语言"] = q4

                        # 如果使用过AI
                        if q4 == "是":
                            q5 = st.select_slider("1.4.1. 在使用AI工具学习计算机语言时，您觉得它对以下方面的帮助有多大？（1表示帮助不大，5表示帮助很大）", options=[1, 2, 3, 4, 5])
                            responses["AI系统对学习的帮助程度（1-5）"] = q5
                        else:
                            q6 = st.selectbox("1.4.2. 如果您从未使用过AI工具，未来您是否愿意尝试？", ["请选择", "很愿意", "可能会", "不确定", "不太可能", "绝不会"])
                            if q6 != "请选择":
                                responses["未来是否会尝试使用AI系统"] = q6

                        # 学生问题 5
                        q7 = st.selectbox("1.5. 在学习过程中，您是否曾使用AI工具来解决遇到的编程问题？", ["请选择", "经常使用", "偶尔使用", "很少使用", "从未使用"])
                        if q7 != "请选择":
                            responses["是否使用过AI解决编程问题"] = q7

                            # 学生问题 6
                            q8 = st.selectbox("1.6. 您正在上大几？", ["请选择", "大一", "大二", "大三", "大四", "研究生"])
                            if q8 != "请选择":
                                responses["年级"] = q8

                                # 学生问题 7
                                q9 = st.selectbox("1.7. 您学习计算机语言多久了？", ["请选择", "少于6个月", "6-12个月", "1-2年", "2-4年", "4年以上"])
                                if q9 != "请选择":
                                    responses["学习计算机语言时间"] = q9

    # 如果选择老师
    elif role == "老师":
        st.write("### 老师部分问题")

        # 老师问题 1
        q1 = st.selectbox("2.1. 与过去相比，您认为现在的学生在学习计算机语言时的能力和效率有何变化？", ["请选择", "明显增强", "有所增强", "保持不变", "有所退步", "明显退步"])
        if q1 != "请选择":
            responses["学生学习能力变化"] = q1

            # 老师问题 2
            q2 = st.selectbox("2.2. 您是否使用过AI工具（如ChatGPT、Copilot等）来帮助解决研究中遇到的编程难题？", ["请选择", "经常使用", "偶尔使用", "很少使用", "从未使用"])
            if q2 != "请选择":
                responses["是否使用过AI解决研究难题"] = q2

                # 老师问题 3
                q3 = st.selectbox("2.3. 您认为AI系统能否长期有效地帮助学生学习和掌握计算机语言？", ["请选择", "非常相信", "比较相信", "不确定", "不太相信", "完全不相信"])
                if q3 != "请选择":
                    responses["是否相信AI系统全面帮助学生"] = q3

# 提交按钮
if st.button("提交") and responses:
    save_to_csv(responses)
    st.success("感谢您的参与！您的答案已提交。")

# 提示用户输入密码查看数据
st.write("### 输入密码以查看数据")
password = st.text_input("请输入密码", type="password")

# 检查密码并显示数据
if password == "Aa110426!":
    st.success("密码正确，正在显示数据")
    if os.path.exists(csv_file):
        st.write("### 当前所有提交的答案：")
        df = pd.read_csv(csv_file)
        st.dataframe(df)
else:
    if password != "":
        st.error("密码错误，请重试")
