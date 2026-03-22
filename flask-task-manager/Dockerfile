# base image -> python , slim -> small size
FROM python:3.11-slim

#create a non-root user
RUN useradd -m appuser

# create working directory for code
WORKDIR /app

# copy the source code
COPY . .

# install the depedendicies 
RUN pip install --no-cache-dir -r requirements.txt

# change ownership to the non-root user
RUN chown -R appuser:appuser /app

# switch to non-root user
USER appuser
# expose the port number where application is available
EXPOSE  5000

# run the applicatio
CMD ["python", "app.py"]
