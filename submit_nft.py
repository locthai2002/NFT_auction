
import streamlit as st
import pandas as pd
from PIL import Image
import os
from datetime import datetime,timezone,timedelta
import sqlalchemy
#import nft_functions.py

# EH: Set layout as wide
st.set_page_config(page_title="NFT Submission",layout="wide")
# EH: set max screen width.
st.markdown(
        f"""<style>.main .block-container{{ max-width: 1600px }} </style> """,
        unsafe_allow_html=True,
)

# Create the connection string for your SQLite database
database_connection_string = 'sqlite:///'

# Pass the connection string to the SQLAlchemy create_engine function
engine = sqlalchemy.create_engine(database_connection_string, echo=True)

create_nft_table = """
CREATE TABLE nft_info (
    "filename"             VARCHAR(50),
    "filepath"             VARCHAR(50),
    "filesize"             VARCHAR(50),
    "Owner_Name"           VARCHAR(50),
    "Public_Key"           VARCHAR(200),
    "Asset_name"           VARCHAR(50),
    "bid_start_amount"     INT,
    "Bid_close_date"       VARCHAR(50)
  );
 """

engine.execute(create_nft_table)



#EH: Get seller information
st.header('NFT Submission for Auction Application')


username=st.text_input(label='Username')
public_key=st.text_input(label='Public Key')
asset_caption=st.text_input(label='Asset Name')
bid_start=st.number_input("Enter Desired Bid Start amount in Token",min_value=1000,step=1000)

close_date_request = st.date_input(
     "Please enter bid close date(UTC)",
     datetime.now()+timedelta(days=7),min_value=datetime.now() +timedelta(days=7))
st.write('Your close date (UTC) request is:', close_date_request)


def load_image(image_file):
	img = Image.open(image_file)
	return img

def insert_data(nft_df):
    for index, row in nft_df.iterrows():
         engine.execute("INSERT INTO nft_info(filename, filepath, filesize, Owner_Name, Public_Key, Asset_name, bid_start_amount, Bid_close_date) values(?,?,?,?,?,?,?,?)", row.filename, row.filepath,                                                  row.filesize,row.Owner_Name, row.Public_Key, row.Asset_name, row.bid_start_amount, row.Bid_close_date)
    
    sql_nft_info_df = pd.read_sql_table('nft_info', con=engine)
    
    st.write(sql_nft_info_df)
    
def select_data():
##    query_info=f"""
##    SELECT '{select_what}'
##    FROM '{from_table}'
##    WHERE '{where_condition}'
##    """
    
    sql_nft_info_df = pd.read_sql_table('nft_info', con=engine)
    st.write(sql_nft_info_df)
    
def update_data(Public_Key):
    update_data = """
    UPDATE nft_info
    SET 'filename' = '{nft_df.filename}',
        'filepath' = '{nft_df.filepath}',
        'filesize' = 'fileDir/'+'{nft_df.filename}',
        'Owner_Name' = '{nft_df.Owner_Name}',
        'Asset_name' = '{nft_df.Asset_name}',
        'bid_start_amount' = '{nft_df.bid_start_amount}',
        'Bid_close_date' = '{nft_df.Bid_close_date}'
    WHERE 'Public_Key' = '{nft_df.Public_Key}'
    """
    
    engine.execute(update_data)
    read_all_data = """
    SELECT * FROM nft_info
    """
    engine.execute(read_all_data)
    sql_nft_info_df = pd.read_sql_table('nft_info', con=engine)
    st.write(sql_nft_info_df)    
##    list(results)
    
st.subheader("NFT Image")

#EH: upload nft file
image_file = st.file_uploader("Upload Images",
     type=["png","jpg","jpeg"])

if image_file is not None and (len(username) > 0) and (len(public_key)>0) and (len(asset_caption)>0):
          # TO See details
          file_details = {"filename":image_file.name, "filepath":image_file.type,
                    "filesize":image_file.size,"Owner_Name":username,'Public_Key':public_key,'Asset_name':asset_caption,'bid_start_amount':bid_start,"Bid_close_date":close_date_request.isoformat()}

          st.write("Please preview transaction detail before submission.")
          st.write(file_details)
          st.image(load_image(image_file), width=1000)
          
          #Saving upload
          with open(os.path.join("fileDir",image_file.name),"wb") as f:
               f.write((image_file).getbuffer())
          
          
          st.success("File Saved to local fileDir folder")

          #EH: Submit NFT for auction  
          submit=st.button("Submit Auction Request")
          st.write('By click this button, you agree and subject to T&C of auction company.')

          if submit:

              #EH: provide trx hash and asset hash
              #EH: Need to write more exception syntax on this part
               st.write('transaction hash#')
               st.write('Asset hash#')

               #EH: display transaction confirmation
               trx_df=pd.DataFrame(file_details,index=[0])
               st.dataframe(trx_df)
               insert_data(trx_df)

else:
     st.write("Please check inputs.") 

