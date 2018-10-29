FROM python:3

#WORKDIR /usr/src/app

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

#COPY . .

#CMD [ "python", "./your-daemon-or-script.py" ]

#USER ql261
RUN apt-get update
RUN apt-get install sudo -y
RUN useradd -m ql261 && echo "ql261:ql261" | chpasswd && adduser ql261 sudo


USER ql261
