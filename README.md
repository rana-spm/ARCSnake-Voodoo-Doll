# Encoder Interface

## Overview
This package lets a ROS2 system get and use encoder data from an Arduino. It turns this data into joint states in a virtual environment, copying real movements into a computer model.

## How to Set Up
Make sure your Arduino is connected. You might need to change the serial port setting in `encoder_publisher.py` to match your setup:

```python
self.serial_port = serial.Serial('/dev/ttyACM0', 9600, timeout=2)  # Change this port if needed
```

## How to Use
To run the node, first make sure your ROS2 environment is ready. Then, run:

```bash
ros2 run encoder_interface encoder_publisher
```

This starts the `encoder_publisher` node. It reads encoder data and sends it as joint states to the `joint_states` topic.

## Needed Libraries
You need `rclpy` and `sensor_msgs` in ROS2, and the `serial` library in Python.

## Additional Steps for WSL Users

If you're running this on WSL, you need to do these extra steps:

### Step 1: Install usbipd-win

Open PowerShell as Administrator:

- Press **Win + X** and select **"Windows PowerShell (Admin)"** or **"Terminal (Admin)"**.

Install usbipd-win using Windows Package Manager:

Run the following command:

```powershell
winget install usbipd
```

This installs usbipd-win, which allows sharing USB devices with WSL.

### Step 2: Share the Arduino Device with WSL

List the connected USB devices:

In the PowerShell window, run:

```powershell
usbipd list
```

Find the `BUSID` associated with your Arduino (it should be something like `2-3`).

Attach the Arduino to WSL:

Use the `BUSID` found in the previous step:

```powershell
usbipd attach --wsl --busid <BUSID>
```

Replace `<BUSID>` with the actual `BUSID` (e.g., `2-3`).

### Step 3: Run the ROS2 Package

Run the command from earlier:

```bash
ros2 run encoder_interface encoder_publisher
```

You may need to do steps 2 and 3 every time you want to run the node again.
