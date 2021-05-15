FROM tensorflow/tensorflow:latest-gpu

RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev wget vim

RUN pip install keras numpy pillow flask gunicorn

WORKDIR root
COPY ./app.py ./app.py
COPY ./auto_painter.py ./auto_painter.py
COPY ./image_preprocessor.py ./image_preprocessor.py
COPY ./templates/index.html ./templates/index.html
COPY ./images/sample_image.png ./images/sample_image.png

RUN mkdir model
RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=10z10M6qV8KPv5XCOtdkhIE1x9pzgBcvs' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=10z10M6qV8KPv5XCOtdkhIE1x9pzgBcvs" -O auto_painter_model.h5 && rm -rf /tmp/cookies.txt
RUN mv auto_painter_model.h5 model/

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
