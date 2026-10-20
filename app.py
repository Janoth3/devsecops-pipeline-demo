import json
import sys

def main():
    health_data = {
        "status": "healthy",
        "service": "secure-container-pipeline",
        "environment": "production-mock"
    }
    print(json.dumps(health_data, indent=2))
    sys.exit(0)

if __name__ == "__main__":
    main()