# Secure Container Pipeline

[![CI Pipeline](https://github.com/Janoth3/devsecops-pipeline-demo/actions/workflows/main.yml/badge.svg)](https://github.com/Janoth3/devsecops-pipeline-demo/actions/workflows/main.yml)

A containerised Python application utilizing GitHub Actions CI/CD to enforce automated testing and security vulnerability scanning.

## Overview
This project demonstrates a foundational DevSecOps pipeline built from scratch. It bridges software development, automated testing, and security governance by integrating:
- **Docker:** Containerising a lightweight Python mock API.
- **GitHub Actions:** Automating CI/CD builds and runtime testing on every push.
- **Trivy:** Enforcing automated security scanning to detect container vulnerabilities and misconfigurations early in the software lifecycle.

## Pipeline Architecture
1. **Build Job:** Checks out code, compiles the Docker image using Buildx, loads it locally, and executes a health-check test container.
2. **Security-Scan Job:** Spins up Trivy to inspect the container image against known CVEs and security best practices before deployment.