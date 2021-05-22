FROM  continuumio/miniconda3

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . $APP_HOME

#---------------- Prepare the envirennment
RUN  conda env create --file environment.yaml
RUN  conda install -c plotly plotly-orca

SHELL ["conda", "run", "--name", "app", "/bin/bash", "-c"]

# Make sure the environment is activated:
RUN echo "Make sure plotly is installed:"
RUN python -c "import plotly"


ENTRYPOINT ["conda", "run", "--no-capture-output", "--name", "app", "python", "main.py", "-h"]