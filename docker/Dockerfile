
FROM debian:bookworm

RUN apt-get update \
  && apt-get install -y --no-install-recommends g++ make cmake python3 python3-pip python3-dev python3-setuptools git-lfs python3.11-venv \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy python sources.
COPY ./ ./

# Install virtualenv.
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Instance dependencies.
RUN pip install -r requirements.txt

# Load initial trade db from git LFS (https://git-lfs.github.com/).
# RUN git lfs pull -I lpbook/cost/traded_data.pickled

# Start server.
#CMD python3 -m lpbook.server.server
ENTRYPOINT ["python3","-m","lpbook.server.server"]
