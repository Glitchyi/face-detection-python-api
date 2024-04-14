# Masuku - Face Detection ML Model

Masuku is a API service that utilizes a custom trained YOLO V5 object detection model to detect human faces and determine the presence of face coverings. It provides an API which can be used for web or mobile applications. This application is intended to assist in environments where face coverings are required for safety and compliance purposes.

The application works by capturing images in real-time using the device's camera. These images are then analyzed using the YOLO V5 object detection model to detect human faces and identify whether the face is covered, partially covered, or not covered. The application also logs detection events with timestamps and generates reports summarizing the detection events.

A Rust version of this project is currently in development. You can follow its progress [here](<https://github.com/masukuapi/masuku-rs>).

## Features

- Real-time face detection
- Identification of face coverings
- User-friendly interface for non-technical users
- Reporting and logging of detection events

## Prerequisites

- Python 3.11+
- Node.js
- Docker

## Installation

1. Clone the repository:

    ```sh
    git clone <repository-url>
    ```

2. Build the Docker image:

    ```sh
    docker build -t masuku .
    ```

3. Run the Docker container:

    ```sh
    docker run -p 5000:5000 masuku
    ```

## Usage

Navigate to `http://localhost:5000` on your browser. You should see a form where you can upload an image file. After uploading, the server will process the image.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## References

- YOLO V5 Official Documentation: <https://github.com/ultralytics/yolov5>

- IEEE Software Requirements Specification Standard
