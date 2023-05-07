import pandas as pd
import streamlit as st
from datetime import time, datetime

from database import get_officer, view_data_officer, edit_officer_data


def update():
    result = view_data_officer()
    df = pd.DataFrame(result,columns=['OfficerId' , 'FirstName' , 'LastName', 'Ranking', 'Department', 'Phone', 'Address', 'BloodGrp'])
    with st.expander("Officer List"):
        st.dataframe(df)

    list_of_officers = [i[0] for i in view_data_officer()]
    selected_case = st.selectbox("Officer to Edit", list_of_officers)
    selected_result = get_officer(selected_case)
    if selected_result:
        OfficerId = selected_result[0][0]
        Ranking = selected_result[0][3]
        Department = selected_result[0][4]
        Phone = selected_result[0][5]
        Address = selected_result[0][6]

    new_ranking = st.text_input("Ranking:", Ranking)
    new_department = st.text_input("Department:", Department)
    new_phone = st.text_input("Phone:", Phone)
    new_address = st.text_input("Address:", Address)
    if st.button("Update Officer"):
        edit_officer_data(new_ranking, new_department, new_phone, new_address, OfficerId)
        st.success("Officer's Detail has been updated ")