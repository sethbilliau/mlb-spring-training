#Python 3.13
FROM python:3.12

# Now copy over the python requirements and install them
WORKDIR /app
COPY . .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# Now install Jupyter and spin up a server
RUN jupyter lab --generate-config
CMD ["jupyter", "lab", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root"]