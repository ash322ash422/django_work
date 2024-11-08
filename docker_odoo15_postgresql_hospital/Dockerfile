FROM odoo:15.0

USER root

# Update system, install wget and pip, and clean up
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y wget && \
    pip install --upgrade pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Custom Package Directory
RUN mkdir /custom_packages

# Fetch Arguments from docker-compose.yml or CLI
ARG CI_JOB_TOKEN
ARG GITLAB_PRIVATE_ACCESS_TOKEN

# Copy requirements file and install Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Create backups directory and set permissions
RUN mkdir /mnt/backups && \
    chown -R odoo:odoo /mnt/backups && \
    chmod 755 /mnt/backups

USER odoo