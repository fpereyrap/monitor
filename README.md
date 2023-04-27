# 5XX HTTP Status Code Monitor Script

The `monitor.py` script is designed to monitor a log file for HTTP status codes in the 5xx range, and send an alert when it detects one.

## Prerequisites

- Python 3.x installed on your system.
- The `requests` library must be installed. You can install it by running the following command in your terminal or command prompt:

```
pip install requests
```


## Usage

To use the script, follow these steps:

1. Update the webhook URL in the line 7 of the script. 
2. Open your terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using the following command:


```
python monitor.py /path/to/your/logfile.log
```


Replace `/path/to/your/logfile.log` with the actual path to the log file you want to monitor.

Optionally, you can use the `--tail` flag to continuously monitor the log file for changes:

```
python monitor.py /path/to/your/logfile.log --tail
```

5. The script will start monitoring the log file and send an alert whenever it detects an HTTP status code in the 5xx range.
6. If you want to stop the script, press `Ctrl + C` in your terminal or command prompt.

## Customization

It is possible to widen the range of errors, currently is set to monitor between 500 and 599 but that can be changed in the line 32 of the script. 