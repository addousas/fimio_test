FROM python:3.13.0


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./generic_device /code/generic_device


CMD ["fastapi", "run", "generic_device/device.py", "--port", "80"]