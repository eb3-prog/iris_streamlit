# 基本ライブラリ
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# データセット読み込み
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# 目標値
df['target'] = iris.target

df.shape

df.tail(5)

df

# 目標値を数字から花の名前に変更
df.loc[df['target'] == 0, 'target'] = 'setosa'
df.loc[df['target'] == 1, 'target'] = 'versicolor'
df.loc[df['target'] == 2, 'target'] = 'virginica'

df

#予測モデル構築
x = iris.data[:,[0,2]]  #すべての行の０番目と２番目の列を取得する
y = iris.target

x
y

#ロジスティック回帰
clf = LogisticRegression()
clf.fit(x,y)

#　サイドバー（入力画面）
st.sidebar.header('Input Features')

sepalValue = st.sidebar.slider('sepal length (cm)',min_value=0.0,max_value=10.0,step=0.1)
petalValue = st.sidebar.slider('petal length (cm)',min_value=0.0,max_value=10.0,step=0.1)

# メインパネル
st.title('Iris Classifier')
st.write('## Input Value')

# インプットデータ（1行のデータフレーム）
value_df = pd.DataFrame({'data':'data','sepal length(cm)':sepalValue,'petal length(cm)':petalValue},index=[0])
value_df.set_index('data',inplace=True)

#入力値の値
st.write(value_df)

# 予測値のデータフレーム
pred_prods = clf.predict_proba(value_df)
pred_df = pd.DataFrame(pred_prods,columns=['setosa','versicolor','virginica'],index=['probability'])

st.write('## Prediction')
st.write(pred_df)

# 予測結果の出力
name = pred_df.idxmax(axis=1).tolist()
st.write('## Result')
st.write('このアイリスはきっと',str(name[0]),'です！')