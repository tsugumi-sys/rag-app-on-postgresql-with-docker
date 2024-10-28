FROM postgres:16

# Install necessary packages
RUN apt-get update && apt-get install -y build-essential git-all postgresql-server-dev-16

# Download and extract pg_bigm
RUN cd /tmp && git clone --branch v0.7.4 https://github.com/pgvector/pgvector.git
RUN cd /tmp/pgvector && make && make install

# Enable pg_bigm extension
RUN echo "shared_preload_libraries = 'vector'" >> "$PGDATA/postgresql.conf"

