# PyAutoGUI Docker Demo

This is a demonstration of running PyAutoGUI in a Docker container on Linux. The setup uses Xvfb (X Virtual Framebuffer) to create a virtual display, allowing PyAutoGUI to work in a headless environment.

## Prerequisites

- Docker installed on your Linux server
- Git (optional, for cloning the repository)

## Building and Running

1. Build the Docker image:
```bash
docker build -t pyautogui-demo .
```

2. Run the container:
```bash
docker run --rm pyautogui-demo
```

## How it Works

- The Dockerfile sets up a Python environment with all necessary dependencies
- Xvfb creates a virtual display (1024x768) that PyAutoGUI can use
- The Python script demonstrates basic PyAutoGUI functionality:
  - Getting screen size
  - Moving the mouse
  - Taking a screenshot
  - Typing text

## Notes

- The virtual display is set to 1024x768 resolution
- Screenshots are saved inside the container (you'll need to modify the code to save them to a mounted volume if you want to access them from the host)
- This is a basic demonstration; you may need to adjust the setup based on your specific needs

## Troubleshooting

If you encounter any issues:
1. Make sure all system dependencies are properly installed
2. Check if the virtual display is running correctly
3. Verify that PyAutoGUI can access the display

## Integration with Your Project

To integrate this with your project:
1. Copy the Dockerfile and requirements.txt
2. Modify the Python script to include your specific automation tasks
3. Adjust the virtual display settings if needed
4. Add any additional dependencies your project requires 