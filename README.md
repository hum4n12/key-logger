# Python Key-Logger

Simple key-logger with ability to send intercepted data to the server.
If server is not active, data will be saved to a file.


## Usage
To run key-logger, run main.py file
```bash 
python main.py
```
To run example server with intercepted data, run server.py file
```bash 
python server.py
```
### Server
Your server will be running by default on [localhost (port 5000)](http://127.0.0.1:5000).
Data will be grouped by ip address and date time.

### Logger
Keyboard logging will be saved in the file, if server is active data will be send to the server.
To turn off logger, click **Esc**