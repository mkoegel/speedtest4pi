Run Speedtest on Raspberry PI4 and create a linechart from your data

Uses:
- Python3
- Flask
- Chart.js
- SQLite3
- Cron

Speedtest part based on https://pimylifeup.com/raspberry-pi-internet-speed-monitor/
and adopted to use SQLite3 as database instead of CSV file.

Flask part based on https://github.com/johnsliao/flask-sqlite3-chartjs-toy

# How to set up:  

1. Clone repository `git clone https://github.com/mkoegel/speedtest4pi.git`
2. Install dependencies `pip3 install -r requirements.txt`
3. Create Database `sqlite3 speedtest.db < schema.sql`
4. Setup your crontab with `sudo crontab -e``
5. Enter `0 * * * * python3 /home/pi/speedtest4pi/speedtestdb.py` to run the test every hour.
6. Start the Flask app with `flask run`
7. Open browser to `http://127.0.0.1:5000/`. You should see the linechart with your Internet Data.

