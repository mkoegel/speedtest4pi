# Run Speedtest on Raspberry PI4 and create a linechart from your data

I run this on the same Raspberry PI 4 that hosts Pi-Hole in my local network.
Uses:
- Python3
- Flask
- Chart.js
- SQLite3
- Cron

Speedtest part based on https://pimylifeup.com/raspberry-pi-internet-speed-monitor/
and adopted to use SQLite3 as database instead of CSV file.

Flask part based on https://github.com/johnsliao/flask-sqlite3-chartjs-toy

## How to set up:  

1. Clone repository `git clone https://github.com/mkoegel/speedtest4pi.git`
2. Install dependencies `pip3 install -r requirements.txt`
3. Create Database `sqlite3 speedtest.db < schema.sql`
4. Setup your crontab with `sudo crontab -e``
5. Enter `0 * * * * python3 /home/pi/speedtest4pi/speedtestdb.py` to run the test every hour.
6. Start the Flask app with `flask run -h <hostname or ip>&`. **Note: Flask is not a production webserver. Never use if your PI is exposed to the internet.**
7. Open browser to `http://<hostname or ip>:5000/`. You see the linechart with your Internet Data.

## ToDo:
- Integrate into Pi-Hole UI once Pi-Hole 5 is out of beta.
- Use a full fledged webserver.
