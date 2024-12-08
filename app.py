from .serpapi import GoogleSearch
import streamlit as st
import pandas as pd
st.set_page_config(
    layout="centered", page_title="Price Compare", page_icon="🔎",
    initial_sidebar_state="collapsed")
# """--------------------------------------------------------------------------------------------------------------------------------------"""
def compare(name):
    params = {
    "engine": "google_shopping",
    "q": name,
    "api_key": "7b4f1c879e1ceea1cb33f35be6e42637a3c0f9e9687389c37d8a756708bd6348",
    "gl" : "in"
    }

        
    search = GoogleSearch(params)
    results = search.get_dict()
    shopping_results = results["inline_shopping_results"]
    return(shopping_results)

# --------------------------------------------------------------------------------------------------------------------------------------"""

 #header
c1,c2 = st.columns(2)
c1.image("e_pharmacy.png", width= 200)
c2.header("E-Pharmacy Price compairsion system")

# """--------------------------------------------------------------------------------------------------------------------------------------"""
st.sidebar.title("Enter Name of Medicine:")
st.sidebar.markdown(" ")
st.sidebar.markdown(" ")

medicine_name=st.sidebar.text_input(
        "Enter Name here 👇"
    )
med_name=[]
med_price=[]
if medicine_name is not None:
    if st.sidebar.button("show compair"):
        inline_shopping_results=compare(medicine_name)
        st.sidebar.image(inline_shopping_results[0].get("thumbnail"))
        for i in range(4):
            st.title(f"Option {i+1}")
            c1,c2 = st.columns(2)

            c1.write("Company ")
            c2.write(inline_shopping_results[i].get("source"))

            c1.write("Medicine Name")
            c2.write(inline_shopping_results[i].get("title"))
            med_name.append(inline_shopping_results[i].get("source"))
            med_price.append(inline_shopping_results[i].get("price"))

            c1.write("Price")
            c2.write(inline_shopping_results[i].get("price"))

            url= inline_shopping_results[i].get("link")
            print(url)
            c1.write("BUY LINK ")
            c2.write("[link](%s)" % url)
            """-----------------------------"""
        #graph comrasion 
        dic={"company":med_name,"price":med_price}
        df=pd.DataFrame(dic)
        st.title("Chart Comarasion : ")
        st.bar_chart(df)





# st.image("https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcSKcNTwrqkcdsdKPM-ZP-XTwjlpvH4DIfab1vzfPncHNCmkIVrFV3gmAhENR21j2GDX42O_8_mQtGZjCfeM2-P0w15uGGIZ&usqp=CAE")
