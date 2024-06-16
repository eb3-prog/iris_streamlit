#必要なライブラリをインポート
from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
from multiprocessing import Condition
from optparse import Option
import streamlit as st
import numpy as np
import pandas as pd

#タイトルとテキストを記入
st.title('Streamlit 基礎')
st.write('Hello World')

#データフレームの準備
df = pd.DataFrame({
    "1列目":[5,6,7,8],
    "2列目":[10,20,30,40],    
})

#動的なテーブル
st.dataframe(df)

# 引数を使用した動的テーブル
st.dataframe(df.style.highlight_max(axis=0),width=100,height=150)

#静的なテーブル
st.table(df)

# 10行3列のデータフレームを準備
df = pd.DataFrame(
    np.random.rand(10,3),
    columns=['a','b','c']
)

df

#折れ線グラフ
st.line_chart(df)

#面グラフ
st.area_chart(df)

#棒グラフ
st.bar_chart(df)

#　プロットする乱数をデータフレームで用意
df = pd.DataFrame(
    #乱数 + 新宿の緯度と軽度
    np.random.rand(100,2) / [50,50] + [35.69,139.70],
    columns = ['lat','lon']
)

df

#マップをプロット
st.map(df)

#Pilow
from PIL import Image

# 画像の読み込み
img = Image.open('iris.jpg')
st.image(img,caption = 'Iris',use_column_width = True)

# チェックボックス
if st.checkbox('Show Image'):
    img = Image.open('iris.jpg')
    st.image(img,caption = 'Iris',use_column_width = True)


# セレクトボックス
option = st.selectbox(
    '好きな数字を入力してください',
    list(range(1,11))
)

'あなたの好きな数字は' , option , 'です。'

# テキスト入力による値の動的変更
text = st.sidebar.text_input('あなたの好きなスポーツを教えてください。')

'あなたの好きなスポーツ：' , text

# スライダーによる値の動的変更
Condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'コンディション：' , Condition

expander1 = st.expander('質問１')
expander1.write('質問１の回答')
expander2 = st.expander('質問２')
expander2.write('質問２の回答')
expander3 = st.expander('質問3')
expander3.write('質問3の回答')

#プログレスバー
import time
latest_iteration = st.empty()
bar = st.progress(0)

#プログレスバーを0.1秒毎に進める
for i in range(100):
    latest_iteration.text(f'Iteration{i + 1}')
    bar.progress(i + 1)
    time.sleep(1)

'Done'