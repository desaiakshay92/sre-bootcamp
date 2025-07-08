#!/bin/bash

set -e

install_docker() {
  echo "🔧 Installing Docker..."
  apt-get update
  apt-get install -y docker.io
  systemctl start docker
  systemctl enable docker
}

install_docker_compose() {
  echo "🔧 Installing Docker Compose..."
  curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  chmod +x /usr/local/bin/docker-compose
}

install_make() {
  echo "🔧 Installing Make..."
  apt-get install -y make
}

main() {
  echo "🚀 Starting provisioning..."
  install_docker
  install_docker_compose
  install_make
  echo "✅ Provisioning complete."
}

main