{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2055f9fa-711c-4d61-a003-7f480b2b6cf8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import the required libraries and dependencies\n",
    "import pandas as pd\n",
    "from pathlib import Path\n",
    "import sqlalchemy\n",
    "from datetime import datetime,timezone,tzinfo\n",
    "from sqlalchemy import MetaData, Table, Column, Integer, String"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bd3fb86b-faa2-493a-a945-07ead4e93a41",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>filename</th>\n",
       "      <th>filetype</th>\n",
       "      <th>filesize</th>\n",
       "      <th>Owner_Name</th>\n",
       "      <th>Public_Key</th>\n",
       "      <th>Asset_name</th>\n",
       "      <th>bid_start_amount</th>\n",
       "      <th>Bid_close_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Laker</td>\n",
       "      <td>Images/image1.png</td>\n",
       "      <td>253020</td>\n",
       "      <td>Images/image1.png</td>\n",
       "      <td>0xc852Ab4073FF57c7Fa824D158A3Cdd5CC6707399</td>\n",
       "      <td>Laker_asset</td>\n",
       "      <td>4000.0</td>\n",
       "      <td>6/4/2002</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1990</td>\n",
       "      <td>Images/image2.png</td>\n",
       "      <td>253020</td>\n",
       "      <td>Images/image2.png</td>\n",
       "      <td>0x408e647764abbAB762fFc730afd3888552660C35</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>AllStar</td>\n",
       "      <td>Images/image3.png</td>\n",
       "      <td>253020</td>\n",
       "      <td>Images/image3.png</td>\n",
       "      <td>0x949cD3e57F62499ca874F3C59D456F18b9CeBd8F</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Atl0</td>\n",
       "      <td>Images/atl0.jpg</td>\n",
       "      <td>253020</td>\n",
       "      <td>Images/atl0.jpg</td>\n",
       "      <td>0x23f86eA3f98701A05E8eB6596AAc1F01E3600771</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Atl12</td>\n",
       "      <td>Images/atl12.jpg</td>\n",
       "      <td>253020</td>\n",
       "      <td>Images/atl12.jpg</td>\n",
       "      <td>0x15784317248d616AFf662f512963e35950743Df4</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  filename           filetype  filesize         Owner_Name  \\\n",
       "0    Laker  Images/image1.png    253020  Images/image1.png   \n",
       "1     1990  Images/image2.png    253020  Images/image2.png   \n",
       "2  AllStar  Images/image3.png    253020  Images/image3.png   \n",
       "3     Atl0    Images/atl0.jpg    253020    Images/atl0.jpg   \n",
       "4    Atl12   Images/atl12.jpg    253020   Images/atl12.jpg   \n",
       "\n",
       "                                   Public_Key   Asset_name  bid_start_amount  \\\n",
       "0  0xc852Ab4073FF57c7Fa824D158A3Cdd5CC6707399  Laker_asset            4000.0   \n",
       "1  0x408e647764abbAB762fFc730afd3888552660C35          NaN               NaN   \n",
       "2  0x949cD3e57F62499ca874F3C59D456F18b9CeBd8F          NaN               NaN   \n",
       "3  0x23f86eA3f98701A05E8eB6596AAc1F01E3600771          NaN               NaN   \n",
       "4  0x15784317248d616AFf662f512963e35950743Df4          NaN               NaN   \n",
       "\n",
       "  Bid_close_date  \n",
       "0       6/4/2002  \n",
       "1            NaN  \n",
       "2            NaN  \n",
       "3            NaN  \n",
       "4            NaN  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Using the Pandas read_csv funcion and the Path module, \n",
    "# read \"nft.csv\" file into a Pandas DataFrame\n",
    "\n",
    "nft_df = pd.read_csv(\n",
    "    Path(\"./Resources/nft.csv\")\n",
    ")\n",
    " \n",
    "# Review the DataFrame\n",
    "nft_df.head()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4a2f2793-1dd6-4232-87fe-c976ad701977",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Engine(sqlite:///)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create the connection string for your SQLite database\n",
    "database_connection_string = 'sqlite:///'\n",
    "\n",
    "# Pass the connection string to the SQLAlchemy create_engine function\n",
    "engine = sqlalchemy.create_engine(database_connection_string, echo=True)\n",
    "\n",
    "# Confirm that the database engine was created.\n",
    "engine"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "789ea6f3-aabf-4bc0-85f8-85b71fffee7b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2022-06-05 12:24:07,657 INFO sqlalchemy.engine.Engine \n",
      "CREATE TABLE nft_info (\n",
      "    \"filename\"             VARCHAR(50),\n",
      "    \"filetype\"             VARCHAR(50),\n",
      "    \"filesize\"             INT,\n",
      "    \"Owner_Name\"           VARCHAR(50),\n",
      "    \"Public_Key\"           VARCHAR(200),\n",
      "    \"Asset_name\"           VARCHAR(50),\n",
      "    \"bid_start_amount\"     INT,\n",
      "    \"Bid_close_date\"       VARCHAR(50)\n",
      "  );\n",
      " \n",
      "2022-06-05 12:24:07,660 INFO sqlalchemy.engine.Engine [raw sql] ()\n",
      "2022-06-05 12:24:07,661 INFO sqlalchemy.engine.Engine COMMIT\n",
      "2022-06-05 12:24:07,663 INFO sqlalchemy.engine.Engine SELECT name FROM sqlite_master WHERE type='table' ORDER BY name\n",
      "2022-06-05 12:24:07,664 INFO sqlalchemy.engine.Engine [raw sql] ()\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\locth\\AppData\\Local\\Temp/ipykernel_320232/392259621.py:20: SADeprecationWarning: The Engine.table_names() method is deprecated and will be removed in a future release.  Please refer to Inspector.get_table_names(). (deprecated since: 1.4)\n",
      "  engine.table_names()\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['nft_info']"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Using the nft_info_df DataFrame, create a table called nft_info \n",
    "# inside your newly created database\n",
    "# Be sure include the parameters for the engine, the index, and if_exists with the function\n",
    "create_nft_table = \"\"\"\n",
    "CREATE TABLE nft_info (\n",
    "    \"filename\"             VARCHAR(50),\n",
    "    \"filetype\"             VARCHAR(50),\n",
    "    \"filesize\"             INT,\n",
    "    \"Owner_Name\"           VARCHAR(50),\n",
    "    \"Public_Key\"           VARCHAR(200),\n",
    "    \"Asset_name\"           VARCHAR(50),\n",
    "    \"bid_start_amount\"     INT,\n",
    "    \"Bid_close_date\"       VARCHAR(50)\n",
    "  );\n",
    " \"\"\"\n",
    "\n",
    "engine.execute(create_nft_table)\n",
    "\n",
    "# Confirm that the table was created by calling the table_names function\n",
    "engine.table_names()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ab169052-9599-4838-b93f-4f321f797d6f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2022-06-05 12:24:07,670 INFO sqlalchemy.engine.Engine SELECT name FROM sqlite_master WHERE type='table' ORDER BY name\n",
      "2022-06-05 12:24:07,671 INFO sqlalchemy.engine.Engine [raw sql] ()\n",
      "2022-06-05 12:24:07,672 INFO sqlalchemy.engine.Engine SELECT name FROM sqlite_master WHERE type='view' ORDER BY name\n",
      "2022-06-05 12:24:07,673 INFO sqlalchemy.engine.Engine [raw sql] ()\n",
      "2022-06-05 12:24:07,674 INFO sqlalchemy.engine.Engine PRAGMA main.table_xinfo(\"nft_info\")\n",
      "2022-06-05 12:24:07,675 INFO sqlalchemy.engine.Engine [raw sql] ()\n",
      "2022-06-05 12:24:07,678 INFO sqlalchemy.engine.Engine SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type = 'table'\n",
      "2022-06-05 12:24:07,679 INFO sqlalchemy.engine.Engine [raw sql] ('nft_info',)\n",
      "2022-06-05 12:24:07,681 INFO sqlalchemy.engine.Engine PRAGMA main.foreign_key_list(\"nft_info\")\n",
      "2022-06-05 12:24:07,682 INFO sqlalchemy.engine.Engine [raw sql] ()\n",
      "2022-06-05 12:24:07,683 INFO sqlalchemy.engine.Engine PRAGMA temp.foreign_key_list(\"nft_info\")\n",
      "2022-06-05 12:24:07,683 INFO sqlalchemy.engine.Engine [raw sql] ()\n",
      "2022-06-05 12:24:07,683 INFO sqlalchemy.engine.Engine SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type = 'table'\n",
      "2022-06-05 12:24:07,684 INFO sqlalchemy.engine.Engine [raw sql] ('nft_info',)\n",
      "2022-06-05 12:24:07,685 INFO sqlalchemy.engine.Engine PRAGMA main.index_list(\"nft_info\")\n",
      "2022-06-05 12:24:07,686 INFO sqlalchemy.engine.Engine [raw sql] ()\n",
      "2022-06-05 12:24:07,686 INFO sqlalchemy.engine.Engine PRAGMA temp.index_list(\"nft_info\")\n",
      "2022-06-05 12:24:07,687 INFO sqlalchemy.engine.Engine [raw sql] ()\n",
      "2022-06-05 12:24:07,687 INFO sqlalchemy.engine.Engine PRAGMA main.index_list(\"nft_info\")\n",
      "2022-06-05 12:24:07,688 INFO sqlalchemy.engine.Engine [raw sql] ()\n",
      "2022-06-05 12:24:07,688 INFO sqlalchemy.engine.Engine PRAGMA temp.index_list(\"nft_info\")\n",
      "2022-06-05 12:24:07,689 INFO sqlalchemy.engine.Engine [raw sql] ()\n",
      "2022-06-05 12:24:07,689 INFO sqlalchemy.engine.Engine SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type = 'table'\n",
      "2022-06-05 12:24:07,690 INFO sqlalchemy.engine.Engine [raw sql] ('nft_info',)\n",
      "2022-06-05 12:24:07,695 INFO sqlalchemy.engine.Engine SELECT nft_info.filename, nft_info.filetype, nft_info.filesize, nft_info.\"Owner_Name\", nft_info.\"Public_Key\", nft_info.\"Asset_name\", nft_info.bid_start_amount, nft_info.\"Bid_close_date\" \n",
      "FROM nft_info\n",
      "2022-06-05 12:24:07,697 INFO sqlalchemy.engine.Engine [generated in 0.00161s] ()\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>filename</th>\n",
       "      <th>filetype</th>\n",
       "      <th>filesize</th>\n",
       "      <th>Owner_Name</th>\n",
       "      <th>Public_Key</th>\n",
       "      <th>Asset_name</th>\n",
       "      <th>bid_start_amount</th>\n",
       "      <th>Bid_close_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [filename, filetype, filesize, Owner_Name, Public_Key, Asset_name, bid_start_amount, Bid_close_date]\n",
       "Index: []"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create a new DataFrame by reading in the nft_info table from the database\n",
    "sql_nft_info_df = pd.read_sql_table('nft_info', con=engine)\n",
    "\n",
    "# Review the first and last five rows of the DataFrame\n",
    "display(sql_nft_info_df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "fa516b90-6305-46c9-b163-83fb9bbed86f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def insert_data(nft_df):\n",
    "          # TO See details\n",
    "##          file_details = {\"filename\":image_file.name, \"filetype\":image_file.type,\n",
    "##                    \"filesize\":image_file.size,\"Owner Name\":username,'Public Key':public_key,'Asset Name':asset_caption,'bid start amount':bid_start,\"Bid close date\":close_date_request.isoformat()}\n",
    "    \n",
    "##    insert_data = f\"\"\"\n",
    "##    INSERT INTO nft_info\n",
    "##    VALUES ('{names}', {amount}, {date}, '{image}')\n",
    "##    \"\"\"\n",
    "    \n",
    "##    print(insert_data)\n",
    "##    engine.execute(insert_data)\n",
    "    for index, row in nft_df.iterrows():\n",
    "         engine.execute(\"INSERT INTO nft_info(filename, filetype, filesize, Owner_Name, Public_Key, Asset_name, bid_start_amount, Bid_close_date) values(?,?,?,?,?,?,?,?)\", row.filename, row.filetype, row.filesize,row.Owner_Name, row.Public_Key, row.Asset_name, row.bid_start_amount, row.Bid_close_date)\n",
    "    \n",
    "    sql_nft_info_df = pd.read_sql_table('nft_info', con=engine)\n",
    "    \n",
    "    display(sql_nft_info_df.tail())\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "086ab524-440a-4fff-b87e-b7869f6a6cc9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def select_data():\n",
    "##    query_info=f\"\"\"\n",
    "##    SELECT '{select_what}'\n",
    "##    FROM '{from_table}'\n",
    "##    WHERE '{where_condition}'\n",
    "##    \"\"\"\n",
    "    \n",
    "    sql_nft_info_df = pd.read_sql_table('nft_info', con=engine)\n",
    "    display(sql_nft_info_df.tail())\n",
    "##    results = engine.execute(query_info)\n",
    "    \n",
    "##    list(results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "422ad7aa-eb26-4b20-a5de-ea80eafc787b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def update_data(Public_Key):\n",
    "    update_data = \"\"\"\n",
    "    UPDATE nft_info\n",
    "    SET 'filename' = '{nft_df.filename}',\n",
    "        'filetype' = '{nft_df.filetype}',\n",
    "        'filesize' = '{nft_df.filesize}',\n",
    "        'Owner_Name' = '{nft_df.Owner_Name}',\n",
    "        'Asset_name' = '{nft_df.Asset_name}',\n",
    "        'bid_start_amount' = '{nft_df.bid_start_amount}',\n",
    "        'Bid_close_date' = '{nft_df.Bid_close_date}'\n",
    "    WHERE 'Public_Key' = '{nft_df.Public_Key}'\n",
    "    \"\"\"\n",
    "##    for index, row in nft_df.iterrows():\n",
    "##         engine.execute(\"UPDATE nft_info SET (filename = 'row.filename' , filetype = ?, filesize = ?, Owner_Name = ?, Asset_name = ?, bid_start_amount = ?, Bid_close_date = ?) WHERE Public_Key = ?\", , row.filetype, row.filesize,row.Owner_Name, row.Asset_name, row.bid_start_amount, row.Bid_close_date, row.Public_Key)\n",
    "    \n",
    "    \n",
    "    # Execute the update in the database\n",
    "##    engine.execute(update_data)\n",
    "##    sql_nft_info_df = pd.read_sql_table('nft_info', con=engine)\n",
    "    \n",
    "##    display(sql_nft_info_df.tail())    \n",
    "    engine.execute(update_data)\n",
    "    read_all_data = \"\"\"\n",
    "    SELECT * FROM nft_info\n",
    "    \"\"\"\n",
    "    results = engine.execute(read_all_data)\n",
    "    sql_nft_info_df = pd.read_sql_table('nft_info', con=engine)\n",
    "    display(sql_nft_info_df.tail())    \n",
    "    list(results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37d506a4-876b-477d-92dc-03a1755100d7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
