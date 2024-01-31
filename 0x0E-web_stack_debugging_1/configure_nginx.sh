# This script configures Nginx to listen on port 80 for all active IPv4 IPs

# Install Nginx if not already installed
apt-get update
apt-get install -y nginx

# Remove the problematic "server_name" directive
sed -i '/server_name/d' /etc/nginx/sites-available/default

# Add the necessary "listen" directive for port 80
sed -i '/listen 80;/a\    listen 80 default_server;' /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart
