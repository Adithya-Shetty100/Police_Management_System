import streamlit as st
from database import add_data_officer, add_data_cases, add_data_complaint, add_data_complainant, \
    add_data_arrest, add_data_criminal
from datetime import time, datetime


def create():
    with st.expander("Add Data to Officer table"):
        Id = st.text_input("OfficerId", key="OfficerId_create")
        FirstName = st.text_input("First Name", key="FirstName_create")
        LastName = st.text_input("Last Name", key="LastName_create")
        Ranking = st.text_input("Ranking", key="Ranking_create")
        Department = st.text_input("Department", key="Department_create")
        Phone = st.text_input("Phone", key="Phone_create1")
        Address = st.text_input("Address", key="Address_create1")
        BloodGrp = st.text_input("BloodGrp", key="BloodGrp_create")

        if st.button("Add Officer"):
            add_data_officer(Id, FirstName, LastName, Ranking, Department, Phone, Address, BloodGrp)
            st.success("Officer added successfully")

    with st.expander("Add Data to Cases table"):
        # CaseId = st.text_input("CaseId", key="CaseId_create1")
        Name = st.text_input("Case Name", key="Name_create1")
        DOC = st.date_input("DOC", key="DOC_create1")
        # TOC = st.time_input("TOC", key="TOC_create1")
        Location = st.text_input("Location", key="Location_create1")
        CRIME = st.text_input("CRIME", key="CRIME_create")
        OfficerId = st.text_input("OfficerId", key="OfficerId_create1")

        if st.button("Add Cases"):
            add_data_cases(Name, DOC, Location, CRIME, OfficerId)
            st.success("Case added successfully")

    with st.expander("Add Data to Complaint table"):
        # ComplaintId = st.text_input("ComplaintId", key="ComplaintId_create1")
        Type = st.text_input("Type", key="Type_create")
        Complainant = st.text_input("Complainant", key="Complainant_create")
        DOC = st.date_input("DOC", key="DOC_create2")
        Solved = st.text_input("Solved", key="Solved_create")
        CaseId = st.text_input("CaseId", key="CaseId_create2")
        OfficerId = st.text_input("OfficerId", key="OfficerId_create2")

        if st.button("Add Complaints"):
            add_data_complaint(Type, Complainant, DOC, Solved, CaseId, OfficerId)
            st.success("Complaint added successfully")

    with st.expander("Add Data to Complainant table"):
        # ComplainantId = st.text_input("ComplainantId", key="ComplainantId_create2")
        Name = st.text_input("Name", key="Name_create2")
        Phone = st.text_input("Phone", key="Phone_create2")
        Address = st.text_input("Address", key="Address_create2")
        ComplaintId = st.text_input("ComplaintId", key="ComplaintId_create")
        RelationToVictim = st.text_input("RelationToVictim", key="RelationToVictim_create")

        if st.button("Add Complainant"):
            add_data_complainant(Name, Phone, Address, ComplaintId, RelationToVictim)
            st.success("Complainant added successfully")

    with st.expander("Add Data to Arrest table"):
        ArrestId = st.text_input("ArrestId", key="ArrestId_create")
        DOC = st.date_input("DOC", key="DOC_create3")
        Location = st.text_input("Location", key="Location_create2")
        CellNo = st.text_input("Cell No.", key="cell_create")
        OfficerId = st.text_input("OfficerId", key="OfficerId_create3")
        CriminalId = st.text_input("CriminalId", key="CriminalId_create1")

        if st.button("Add Arrest"):
            add_data_arrest(ArrestId, DOC, Location, CellNo, OfficerId, CriminalId)
            st.success("Arrest added successfully")

    with st.expander("Add Data to Criminal table"):
        # CriminalId = st.text_input("CriminalId", key="CriminalId_create2")
        Name = st.text_input("Name", key="Name_create3")
        JailTerm = st.text_input("JailTerm", key="JailTerm_create")
        CaseId = st.text_input("CaseId", key="CaseId_create3")

        if st.button("Add Criminal"):
            add_data_criminal(Name, JailTerm, CaseId)
            st.success("Criminal added successfully")