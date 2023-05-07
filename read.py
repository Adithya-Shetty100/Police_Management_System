import pandas as pd
import streamlit as st
from datetime import time, datetime
from database import view_data_officer, view_data_cases, view_data_complaint, view_data_complainant, \
    view_data_arrest, view_data_criminal


def read():
    result = view_data_officer()
    df = pd.DataFrame(result,
                      columns=['OfficerId', 'FirstName', 'LastName', 'Ranking', 'Department', 'Phone', 'Address',
                               'BloodGrp'])
    with st.expander("View all officers"):
        st.dataframe(df)

    result = view_data_cases()
    df = pd.DataFrame(result, columns=['CaseId', 'Name', 'DOC', 'Location', 'CRIME', 'OfficerId'])
    with st.expander("View all cases"):
        st.dataframe(df)

    result = view_data_complaint()
    df = pd.DataFrame(result, columns=['ComplaintId', 'Type', 'Complainant', 'DOC', 'Solved', 'CaseId', 'OfficerId'])
    with st.expander("View all complaints"):
        st.dataframe(df)
        # st.code(df)

    result = view_data_complainant()
    df = pd.DataFrame(result, columns=['ComplainantId', 'Name', 'Phone', 'Address', 'ComplaintId', 'RelationToVictim'])
    with st.expander("View all complainants"):
        st.dataframe(df)

    result = view_data_arrest()
    df = pd.DataFrame(result, columns=['ArrestId', 'DOC', 'Location', 'CellNo', 'OfficerId', 'CriminalId'])
    with st.expander("View all arrests"):
        st.dataframe(df)

    result = view_data_criminal()
    df = pd.DataFrame(result, columns=['CriminalId', 'Name', 'JailTerm', 'CaseId'])
    with st.expander("View all criminals"):
        st.dataframe(df)