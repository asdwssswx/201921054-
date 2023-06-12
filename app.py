import streamlit as st
st.title("201921054 임아무개")

st.header("201921054 임아무개")
st.subheader("전달함수")
st.text("안녕하세요~~")

# 이미지
from PIL import Image
image = Image.open('image.png')
st.image(image, caption='이미지 캡션')

# 데이터프레임
import pandas as pd
df = pd.read_csv('data.csv')
st.dataframe(df)

# 차트
import matplotlib.pyplot as plt
import seaborn as sns
fig, ax = plt.subplots()
sns.histplot(df['column'], ax=ax)
st.pyplot(fig)

