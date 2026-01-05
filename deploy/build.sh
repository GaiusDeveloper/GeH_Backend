# #!/usr/bin/env bash
# # exit on error
# set -o errexit 

# # Install dependencies
# pip install -r requirements.txt

# # Run migrations
# python manage.py migrate

# # Collect static files
# python manage.py collectstatic --no-input


#!/bin/bash
set -e

echo "🚀 Starting deployment..."
echo "========================================"

# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
sudo apt install -y docker.io docker-compose
sudo systemctl enable docker
sudo systemctl start docker

# Add user to docker group
sudo usermod -aG docker $USER

# Create deployment directory
sudo mkdir -p /opt/geh-backend
sudo chown -R $USER:$USER /opt/geh-backend

echo "System preparation complete"