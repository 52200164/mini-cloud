LyThanhVinhMinicloudDemo - Quickstart
Prerequisites:
  - Docker Desktop installed and running on Windows
  - PowerShell (run as Administrator if ports or permissions require)
How to build & run:
  1) In this folder, build images:
     docker compose build --no-cache
  2) Start all services:
     docker compose up -d
  3) Check running containers:
     docker compose ps
Useful URLs:
  - Web frontend:     http://localhost:8080
  - App (direct):     http://localhost:8085/hello
  - App via proxy:    http://localhost/api/hello
  - Keycloak admin:   http://localhost:8081   (admin/admin)
  - MinIO console:    http://localhost:9001   (minioadmin/minioadmin)
  - Prometheus:       http://localhost:9090
  - Grafana:          http://localhost:3000   (admin/admin)
Notes:
  - Images are tagged as lythanhvinh/<service>:dev
  - If you need to push to Docker Hub, docker login then:
      docker push lythanhvinh/web:dev
