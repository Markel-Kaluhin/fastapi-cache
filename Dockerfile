FROM python:3.11.5

WORKDIR /

RUN apt update

RUN pip install --upgrade pip && pip install pipenv setuptools && pip install --upgrade pipenv

COPY ./ /src/

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --system --deploy

CMD pipenv run app
