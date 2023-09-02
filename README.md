# QR Code Shopping List Integration for Home Assistant

## Introduction

This project provides a simple Flask service that integrates with Home Assistant's shopping list component. 
By scanning a QR code, you can add an item to your shopping list directly in Home Assistant.

## Prerequisites

- Docker installed on your system
- Home Assistant running in a Docker container
- Python 3.x
- Flask and requests Python libraries

## Installation

### Step 1: Clone the Repository

Clone this GitHub repository to your local machine.

```
git clone https://github.com/borisdering/qrcode-shopping.git
```

### Step 2: Build the Docker Image

Navigate to the directory where the `Dockerfile` is located.

```
cd path/to/your/repository
```

Build the Docker image.

```
docker build -t qrcode-shopping .
```

### Access Token
```
export ACCESS_TOKEN=<home_assistant_access_token>
```

### Step 3: Run the Docker Container

Run the Docker container on port 5000.

```
docker run -p 5000:5000 -e ACCESS_TOKEN=${ACCESS_TOKEN} qrcode-shopping
```

## Usage

Scan the generated QR code using your mobile device. This will add the item to your Home Assistant shopping list.

## Troubleshooting

If you encounter any issues, check the Flask app logs for debugging information.
