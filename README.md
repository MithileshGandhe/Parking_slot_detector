# Real-Time Parking Management System

This project engineered a real-time parking management system using CCTV footage to monitor and track parking slot availability. The system customizes parking slot detection regions and replaces manual monitoring with automated tracking to improve operational efficiency.

## Features
- **Real-time detection** of vacant and occupied parking slots using CCTV footage.
- **Customizable** pre-defined detection regions to suit various parking layouts.
- **Automated tracking** of parking occupancy for efficient parking management.
- Provides **real-time updates** on parking slot availability.
- User-friendly interface built with **Streamlit** for easy visualization and monitoring.

## Tools Used
- **OpenCV**: For processing CCTV footage and detecting parking slots.
- **Streamlit**: For building the user interface to display real-time parking status.
- **Python**: The main programming language for the project.

# Output
![image](https://github.com/user-attachments/assets/ec5ac608-b12a-46b0-b3b0-e52bef19960b)


## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/parking-management.git
cd parking-management
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv myenv
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```sh
        .\myenv\Scripts\activate.bat
        ```
    - On macOS/Linux:
        ```sh
        source myenv/bin/activate
        ```

4. **Install the dependencies:**
    ```sh
    pip install opencv-python streamlit numpy
    ```

## Run the application

- **For adding or updating parking slots**: Use the `park.py` script to define or delete parking slots.

```bash
python park.py
```
- Use **left-click** to declare a parking slot.

- Use **right-click** to delete a parking slot.

- This will generate a file named `file` where the parking slots will be saved.

- **For viewing real-time parking status**: Use the `park1.py` script to view the parking status on your local server using Streamlit.
```bash
streamlit run park1.py
```
The application will run on `localhost`, and you can see the updates in real-time as parking slots are occupied or vacant.
