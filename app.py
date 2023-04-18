import streamlit as st
import pandas as pd


st.write("""
# Greater out of three numbers
""")
#Get Input
st.header('User Input Parameters')
def user_input_features():
	num1=st.number_input("NUM1")
	num2=st.number_input("NUM2")
	num3=st.number_input("NUM3")

	data={'NUM1':num1,'NUM2':num2,'NUM3':num3}
	features = pd.DataFrame(data, index=[0])
	return features
df = user_input_features()
st.write("Result")
#a=features.loc[0,'NUM1']
#st.write(df.iloc[0,0])
if df.iloc[0,0]>df.iloc[0,1] and df.iloc[0,0]>df.iloc[0,2]:
	st.write(df.iloc[0,0],"is greatest")
elif df.iloc[0,1]>df.iloc[0,0] and df.iloc[0,1]>df.iloc[0,2]:
	st.write(df.iloc[0,1],"is greatest" )
else:
	st.write(df.iloc[0,2],"is greatest")
	



