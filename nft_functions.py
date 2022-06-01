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
    "from datetime import datetime,timezone"
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
      "text/plain": [
       "Name      object\n",
       "Amount     int64\n",
       "Date      object\n",
       "Image     object\n",
       "dtype: object"
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
    "nft_df.dtypes\n"
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
    "engine = sqlalchemy.create_engine(database_connection_string)\n",
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
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\locth\\AppData\\Local\\Temp/ipykernel_260748/1270096792.py:21: SADeprecationWarning: The Engine.table_names() method is deprecated and will be removed in a future release.  Please refer to Inspector.get_table_names(). (deprecated since: 1.4)\n",
      "  engine.table_names()\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['\\nCREATE TABLE nft_info (\\n  Name VARCHAR(50) NOT NULL,\\n  Amount VARCHAR(10),\\n  Date DATETIME,\\n  Image VARCHAR(200)\\n  );\\n ']"
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
    "  Name VARCHAR(50) NOT NULL,\n",
    "  Amount VARCHAR(10),\n",
    "  Date DATETIME,\n",
    "  Image VARCHAR(200)\n",
    "  );\n",
    " \"\"\"\n",
    "\n",
    "nft_df.to_sql(\n",
    "    create_nft_table, \n",
    "    engine, \n",
    "    index=False, \n",
    "    if_exists='replace'\n",
    ")\n",
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
       "      <th>Name</th>\n",
       "      <th>Amount</th>\n",
       "      <th>Date</th>\n",
       "      <th>Image</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Laker</td>\n",
       "      <td>4000</td>\n",
       "      <td>datetime(2022, 6, 18, 0, 0, tzinfo=timezone.ut...</td>\n",
       "      <td>Images/image1.png</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1990</td>\n",
       "      <td>5000</td>\n",
       "      <td>datetime(2022, 6, 1, 0, 0, tzinfo=timezone.utc...</td>\n",
       "      <td>Images/image2.png</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>AllStar</td>\n",
       "      <td>7000</td>\n",
       "      <td>datetime(2022, 6, 8, 0, 0, tzinfo=timezone.utc...</td>\n",
       "      <td>Images/image3.png</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Atl0</td>\n",
       "      <td>5500</td>\n",
       "      <td>datetime(2022, 6, 8, 0, 0, tzinfo=timezone.utc...</td>\n",
       "      <td>Images/atl0.jpg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Atl12</td>\n",
       "      <td>6000</td>\n",
       "      <td>datetime(2022, 6, 8, 0, 0, tzinfo=timezone.utc...</td>\n",
       "      <td>Images/atl12.jpg</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Name  Amount                                               Date  \\\n",
       "0    Laker    4000  datetime(2022, 6, 18, 0, 0, tzinfo=timezone.ut...   \n",
       "1     1990    5000  datetime(2022, 6, 1, 0, 0, tzinfo=timezone.utc...   \n",
       "2  AllStar    7000  datetime(2022, 6, 8, 0, 0, tzinfo=timezone.utc...   \n",
       "3     Atl0    5500  datetime(2022, 6, 8, 0, 0, tzinfo=timezone.utc...   \n",
       "4    Atl12    6000  datetime(2022, 6, 8, 0, 0, tzinfo=timezone.utc...   \n",
       "\n",
       "               Image  \n",
       "0  Images/image1.png  \n",
       "1  Images/image2.png  \n",
       "2  Images/image3.png  \n",
       "3    Images/atl0.jpg  \n",
       "4   Images/atl12.jpg  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create a new DataFrame by reading in the nft_info table from the database\n",
    "sql_nft_info_df = pd.read_sql_table(create_nft_table, con=engine)\n",
    "\n",
    "# Review the first and last five rows of the DataFrame\n",
    "display(sql_nft_info_df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "fa516b90-6305-46c9-b163-83fb9bbed86f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def insert_data(names, amount, date, image):\n",
    "    insert_data = \"\"\"\n",
    "    INSERT INTO nft_info\n",
    "    VALUES ('names', 'amount', 'date', 'image')\n",
    "    \"\"\"\n",
    "    \n",
    "    print(insert_data)\n",
    "    engine.execute(insert_data)\n",
    "    \n",
    "    sql_nft_info_df = pd.read_sql_table(create_nft_table, con=engine)\n",
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
    "def select_data(select_what, from_table, where_condition):\n",
    "    query_info=\"\"\"\n",
    "    SELECT select_what\n",
    "    FROM from_table\n",
    "    WHERE where_condition\n",
    "    \"\"\"\n",
    "    \n",
    "    results = engine.execute(query_info)\n",
    "    \n",
    "    list(results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "422ad7aa-eb26-4b20-a5de-ea80eafc787b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def update_data(names, amount):\n",
    "    update_data = \"\"\"\n",
    "    UPDATE nft_info\n",
    "    SET Amount = amount\n",
    "    WHERE Names = names\n",
    "    \"\"\"\n",
    "\n",
    "    # Execute the update in the database\n",
    "    engine.execute(update_data)\n",
    "    \n",
    "    results = engine.execute(query_info)\n",
    "    \n",
    "    list(results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "570da1d0-e086-4198-8e89-a1081db8f06d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "    INSERT INTO create_nft_table\n",
      "    VALUES ('names', 'amount', 'date', 'image')\n",
      "    \n"
     ]
    },
    {
     "ename": "OperationalError",
     "evalue": "(sqlite3.OperationalError) no such table: create_nft_table\n[SQL: \n    INSERT INTO create_nft_table\n    VALUES ('names', 'amount', 'date', 'image')\n    ]\n(Background on this error at: https://sqlalche.me/e/14/e3q8)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOperationalError\u001b[0m                          Traceback (most recent call last)",
      "\u001b[1;32m~\\anaconda3\\envs\\dev\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36m_execute_context\u001b[1;34m(self, dialect, constructor, statement, parameters, execution_options, *args, **kw)\u001b[0m\n\u001b[0;32m   1801\u001b[0m                 \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mevt_handled\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1802\u001b[1;33m                     self.dialect.do_execute(\n\u001b[0m\u001b[0;32m   1803\u001b[0m                         \u001b[0mcursor\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstatement\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparameters\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\dev\\lib\\site-packages\\sqlalchemy\\engine\\default.py\u001b[0m in \u001b[0;36mdo_execute\u001b[1;34m(self, cursor, statement, parameters, context)\u001b[0m\n\u001b[0;32m    718\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mdo_execute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcursor\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstatement\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparameters\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 719\u001b[1;33m         \u001b[0mcursor\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstatement\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparameters\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    720\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mOperationalError\u001b[0m: no such table: create_nft_table",
      "\nThe above exception was the direct cause of the following exception:\n",
      "\u001b[1;31mOperationalError\u001b[0m                          Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_260748/2594769380.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0minsert_data\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'42d'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m5000\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'12/05/2012'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m\"321\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_260748/2692028417.py\u001b[0m in \u001b[0;36minsert_data\u001b[1;34m(names, amount, date, image)\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minsert_data\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 8\u001b[1;33m     \u001b[0mengine\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minsert_data\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      9\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m     \u001b[0msql_nft_info_df\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_sql_table\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcreate_nft_table\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcon\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mengine\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<string>\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, statement, *multiparams, **params)\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\dev\\lib\\site-packages\\sqlalchemy\\util\\deprecations.py\u001b[0m in \u001b[0;36mwarned\u001b[1;34m(fn, *args, **kwargs)\u001b[0m\n\u001b[0;32m    399\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mskip_warning\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    400\u001b[0m             \u001b[0m_warn_with_version\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mversion\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mwtype\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstacklevel\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 401\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mfn\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    402\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    403\u001b[0m     \u001b[0mdoc\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__doc__\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m__doc__\u001b[0m \u001b[1;32mor\u001b[0m \u001b[1;34m\"\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\dev\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, statement, *multiparams, **params)\u001b[0m\n\u001b[0;32m   3137\u001b[0m         \"\"\"\n\u001b[0;32m   3138\u001b[0m         \u001b[0mconnection\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mclose_with_result\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 3139\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mconnection\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstatement\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m*\u001b[0m\u001b[0mmultiparams\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   3140\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   3141\u001b[0m     @util.deprecated_20(\n",
      "\u001b[1;32m~\\anaconda3\\envs\\dev\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, statement, *multiparams, **params)\u001b[0m\n\u001b[0;32m   1272\u001b[0m             )\n\u001b[0;32m   1273\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1274\u001b[1;33m             return self._exec_driver_sql(\n\u001b[0m\u001b[0;32m   1275\u001b[0m                 \u001b[0mstatement\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1276\u001b[0m                 \u001b[0mmultiparams\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\dev\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36m_exec_driver_sql\u001b[1;34m(self, statement, multiparams, params, execution_options, future)\u001b[0m\n\u001b[0;32m   1576\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1577\u001b[0m         \u001b[0mdialect\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdialect\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1578\u001b[1;33m         ret = self._execute_context(\n\u001b[0m\u001b[0;32m   1579\u001b[0m             \u001b[0mdialect\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1580\u001b[0m             \u001b[0mdialect\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecution_ctx_cls\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_init_statement\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\dev\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36m_execute_context\u001b[1;34m(self, dialect, constructor, statement, parameters, execution_options, *args, **kw)\u001b[0m\n\u001b[0;32m   1843\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1844\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mBaseException\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1845\u001b[1;33m             self._handle_dbapi_exception(\n\u001b[0m\u001b[0;32m   1846\u001b[0m                 \u001b[0me\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstatement\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparameters\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcursor\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1847\u001b[0m             )\n",
      "\u001b[1;32m~\\anaconda3\\envs\\dev\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36m_handle_dbapi_exception\u001b[1;34m(self, e, statement, parameters, cursor, context)\u001b[0m\n\u001b[0;32m   2024\u001b[0m                 \u001b[0mutil\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mraise_\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnewraise\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mwith_traceback\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mexc_info\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfrom_\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2025\u001b[0m             \u001b[1;32melif\u001b[0m \u001b[0mshould_wrap\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 2026\u001b[1;33m                 util.raise_(\n\u001b[0m\u001b[0;32m   2027\u001b[0m                     \u001b[0msqlalchemy_exception\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mwith_traceback\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mexc_info\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m2\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfrom_\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0me\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   2028\u001b[0m                 )\n",
      "\u001b[1;32m~\\anaconda3\\envs\\dev\\lib\\site-packages\\sqlalchemy\\util\\compat.py\u001b[0m in \u001b[0;36mraise_\u001b[1;34m(***failed resolving arguments***)\u001b[0m\n\u001b[0;32m    205\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    206\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 207\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mexception\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    208\u001b[0m         \u001b[1;32mfinally\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    209\u001b[0m             \u001b[1;31m# credit to\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\dev\\lib\\site-packages\\sqlalchemy\\engine\\base.py\u001b[0m in \u001b[0;36m_execute_context\u001b[1;34m(self, dialect, constructor, statement, parameters, execution_options, *args, **kw)\u001b[0m\n\u001b[0;32m   1800\u001b[0m                             \u001b[1;32mbreak\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1801\u001b[0m                 \u001b[1;32mif\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mevt_handled\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1802\u001b[1;33m                     self.dialect.do_execute(\n\u001b[0m\u001b[0;32m   1803\u001b[0m                         \u001b[0mcursor\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstatement\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparameters\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1804\u001b[0m                     )\n",
      "\u001b[1;32m~\\anaconda3\\envs\\dev\\lib\\site-packages\\sqlalchemy\\engine\\default.py\u001b[0m in \u001b[0;36mdo_execute\u001b[1;34m(self, cursor, statement, parameters, context)\u001b[0m\n\u001b[0;32m    717\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    718\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mdo_execute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcursor\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstatement\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparameters\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 719\u001b[1;33m         \u001b[0mcursor\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstatement\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparameters\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    720\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    721\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mdo_execute_no_params\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcursor\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstatement\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcontext\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mOperationalError\u001b[0m: (sqlite3.OperationalError) no such table: create_nft_table\n[SQL: \n    INSERT INTO create_nft_table\n    VALUES ('names', 'amount', 'date', 'image')\n    ]\n(Background on this error at: https://sqlalche.me/e/14/e3q8)"
     ]
    }
   ],
   "source": [
    "insert_data('42d', 5000, '12/05/2012', \"321\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6874d363-a43a-42d7-8bbe-26779b69f586",
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
