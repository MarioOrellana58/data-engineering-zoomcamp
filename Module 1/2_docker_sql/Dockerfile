#FROM: Especify which dockerimage I want to use
FROM python:3.9

#run commands inside the image
RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2 pyarrow

#WORKDIR creates a new directory and also do CD into it 
WORKDIR /app
#COPY a file into the directory
#COPY SourceName DestName
COPY ingest_data.py pipeline.py

#This is the instruction of what I want docker to do after run
ENTRYPOINT [ "python", "pipeline.py"]