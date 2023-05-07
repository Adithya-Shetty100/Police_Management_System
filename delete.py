import pandas as pd
import streamlit as st
from datetime import time, datetime
from database import delete_data, view_data_cases,view_only_CaseID

def delete():
    result=view_data_cases()
    df = pd.DataFrame(result, columns=['CaseId', 'Name' , 'DOC', 'Location', 'CRIME' , 'OfficerId' ])
    with st.expander("Current data"):
        st.dataframe(df)
    list_of_cases = [i[0] for i in view_only_CaseID ()]
    selected_case= st.selectbox("Task to Delete", list_of_cases)
    st.warning("Do you want to delete ::{}".format(selected_case))
    if st.button("Delete Case"):
        delete_data(selected_case)
        st.success("Case has been solved successfully")