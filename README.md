# Data Warehouse on AWS
## Introduction
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

The task is to build an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to.


## Project Datasets
* Song data: 's3://udacity-dend/song_data'  
* Log data: 's3://udacity-dend/log_data'  

#### Song Dataset
The first dataset contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.  
* song_data/A/B/C/TRABCEI128F424C983.json  
* song_data/A/A/B/TRAABJL12903CDCF1A.json

And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.  
> {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}

#### Log Dataset
The log files in the dataset you'll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.  
* log_data/2018/11/2018-11-12-events.json   
* log_data/2018/11/2018-11-13-events.json     

And below is an example of what the data in a log file, 2018-11-12-events.json, looks like.  
> {"artist":null,"auth":"Logged In","firstName":"Walter","gender":"M","itemInSession":0,"lastName":"Frye","length":null,"level":"free","location":"San Francisco-Oakland-Hayward, CA","method":"GET","page":"Home","registration":1540919166796.0,"sessionId":38,"song":null,"status":200,"ts":1541105830796,"userAgent":"\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"","userId":"39"}


## Schema for Song Play Analysis
Using the song and log datasets(json), you'll need to create a star schema optimized for queries on song play analysis. This includes the following tables.

### Fact Table
1. **songplays** - records in log data associated with song plays i.e. records with page NextSong (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
### Dimension Tables
2. **users** - users in the app (user_id, first_name, last_name, gender, level)   
3. **songs** - songs in music database (song_id, title, artist_id, year, duration)  
4. **artists** - artists in music database (artist_id, name, location, latitude, longitude)  
5. **time** - timestamps of records in songplays broken down into specific units (start_time, hour, day, week, month, year, weekday)


## Project Template
1. **create_table.py** is where you'll create your fact and dimension tables and staging tables for the star schema in Redshift.  
2. **etl.py** is where you'll load data from S3 into staging tables on Redshift and then process that data into your analytics tables on Redshift.  
3. **sql_queries.py** is where you'll define you SQL statements, which will be imported into the two other files above.  
4. **create_redshift_cluster.ipynb** is where you'll create redshift cluster and create an IAM role that has read access to S3.  
5. **analytics.ipynb** to check the tables.  
6. **analytics.py** another way to check the tables.  
7. **README.md** is where you'll provide discussion on your process and decisions for this ETL pipeline.      


## Project Steps
### Create Tables
* Write CREATE/DROP statements in sql_queries.py to specify all columns for each of the five tables with the right data types and conditions. Also specify the staging tables, and describe how to generate staging tables from files on s3.
* Launch a redshift cluster and create an IAM role that has read access to S3 in create_redshift_cluster.ipynb.
* Add redshift database and IAM role info to dwh.cfg.
* Complete the logic in create_tables.py to connect to the database and create these tables.
* Test by running create_tables.py and checking the table schemas in your redshift database. You can use Query Editor in the AWS Redshift console for this.

### Build ETL Pipeline
* Implement the logic in etl.py to load data from S3 to staging tables on Redshift.
* Implement the logic in etl.py to load data from staging tables to analytics tables on Redshift.
* Test by running etl.py after running create_tables.py and running the analytic queries on your Redshift database to compare your results with the expected results.
* Delete your redshift cluster when finished.

### Validate the tables
#### Method 1:
* open the Amazon Redshift and use the database info to make a connection.
* run query in Query Editor to check the tables.
#### Method 2:
* run analytics.ipynb
#### Method 3:
* run analytics.py in terminal

