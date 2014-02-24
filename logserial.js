/*
  Simple example that takes a command line provided serial port destination and routes the output to a file of the same name with .log appended to the port name.
  
  usage: node logger.js /dev/tty.usbserial <baudrate>
  
*/

var SerialPort = require("serialport");
var fs = require("fs");
var port = process.argv[2];
var baudrate = process.argv[3];
var active = false;

function attemptLogging(fd, port, baudrate) {
  if (!active) {
    fs.stat(port,  function (err, stats) {
      if (!err) {
        active = true;
        lineno = 0; 
        var serialPort = new SerialPort.SerialPort(port, {
          baudrate: baudrate ,  parser: SerialPort.parsers.readline("\n")
        });
        //var serialPort = new SerialPort.SerialPort(port, {
         // baudrate: baudrate 
        //});
        serialPort.on("data", function (data) {
	  if ( ++lineno > 1 ) {
	  var d = new Date();
          fs.write(fd, d.toLocaleString() + ": " + data.toString() + "\n");
	  }
        });
        serialPort.on("close", function (data) {
          active = false;
        });
      }
    });
  }
}

if (!port) {
  console.log("You must specify a serial port location.");
} else {
  var target = port.split("/");
  target = target[target.length-1]+".log";
  if (!baudrate) {
    baudrate = 115200;
  }
  fs.open("./"+target, 'w', function (err, fd) {
      console.log("Opened file " + target);
      if (!active) {
        try {
	  console.log("Going to try listening.");
          attemptLogging(fd, port, baudrate);  
        } catch (e) {
          // Error means port is not available for listening.
          active = false;
        }
      }
  });
}



