# Dockerfile for PostgreSQL with User table and initial data

FROM postgres:14

# Set environment variables
ENV POSTGRES_DB=product_catalog
ENV POSTGRES_USER=catalog_user
ENV POSTGRES_PASSWORD=password

# Copy SQL script to initialize the database
COPY ./postgres/init.sql /docker-entrypoint-initdb.d/

# Change the default user and database to the ones specified above
USER postgres

# Create directory and run command to update pg_hba.conf
RUN mkdir -p /etc/postgresql/$PG_MAJOR/main/ \
    && echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/$PG_MAJOR/main/pg_hba.conf

# Expose the PostgreSQL port
EXPOSE 5432
