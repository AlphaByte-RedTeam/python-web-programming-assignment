import streamlit as st
from supabase import create_client


# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    url = st.secrets["supabase_url"]
    key = st.secrets["supabase_key"]
    return create_client(url, key)


supabase = init_connection()


# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query():
    return supabase.table("mytable").select("*").execute()


rows = run_query()

# Print results.
for row in rows.data:
    st.write(f"{row['name']} has a :{row['pet']}:")
