FROM python:3.11.2

# Copy your application code
COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# Set the entrypoint and default command
# ENTRYPOINT [ "python" ]
CMD ["python","-u","app.py"]