import streamlit as st 
import random as rd

st.title("Üdvözöllek a számkitaláló játékban!")
st.write("Ahol számokat találsz ki.")

number = rd.randint(1, 10)


txt_guess = int(st.text_input('Írj be egy számot 1 és 10 között', 1))


btn_start = st.button("Számold újra!")

btn_guess = st.button("Tippeld meg a számot!")

if btn_guess:
    if txt_guess == number:
        st.write("Te nyertél.")
        st.balloons()
    else:
        st.write("Bocsi, rossz szám, próbáld újra!")

btn_show = st.button('Mutasd a számot!')
if btn_show:
    st.write('A szám, nem más mint: ', number)
    
with st.expander('Segítség..'):
    st.write('''Ebben a játékban egy számot generálok 1 és 10 között. Te beírhatod a tippedet, s kitalálhatod a Tippeld meg a számot gombbal.)''')