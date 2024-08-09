Small project on downloading youtube video using python

You can run this using `python3 main.py`

OR run it using docker.

`Note:` This is a GUI application, If you want to run this via docker your need to walk an extra mile
-> This is a GUI app which needs to access the hardware of the current device

Follow the below steps
# X11 Forwarding on macOS for Docker GUI Applications

Guide to setting up X11 forwarding on macOS to run Docker GUI apps on your host display.

## Prerequisites

- macOS
- Docker
- [XQuartz](https://www.xquartz.org/)

## Steps

1. **Install XQuartz**
   - Download and install from [XQuartz](https://www.xquartz.org/).
   - Restart your computer.

2. **Configure XQuartz**
   - Open XQuartz.
   - Go to `XQuartz > Preferences` > **Security** tab.
   - Enable `Allow connections from network clients`.

3. **Set DISPLAY Environment Variable**
   - Open the terminal in XQuartz (`Applications > Utilities > Terminal`).
   - Run:
     ```sh
     export DISPLAY=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}'):0
     ```
     Or:
     ```sh
     export DISPLAY=host.docker.internal:0
     ```

4. **Run Docker with X11 Forwarding**
   - Execute:
     ```sh
     docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix your-docker-image
     ```
   - Replace `your-docker-image` with your Docker image name.

5. **Test with a GUI App**
   - Inside the Docker container, test with:
     ```sh
     xclock
     ```

## Troubleshooting

- Check firewall settings.
- Re-export `DISPLAY` if needed.
- Ensure XQuartz is running before starting the Docker container.

## Notes

- Use X11 forwarding with caution due to potential security implications.
- Running GUI apps in Docker is more complex than running them directly on macOS.
