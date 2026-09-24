# Python Network Port Scanner

## Overview

A Python-based TCP port scanner developed as a cybersecurity learning project. The tool scans a specified range of TCP ports on an authorized target and identifies open ports and commonly associated services.

## Features

- Accepts an IP address or hostname as the target
- Allows configurable start and end ports
- Identifies open TCP ports
- Attempts to identify common services
- Measures scan duration
- Validates port ranges and user input
- Handles invalid targets and input errors
- Provides command-line output for scan results

## Technologies

- Python 3
- Python `socket` library
- TCP/IP networking
- Linux/Ubuntu
- Git/GitHub

## Usage

```bash
python3 port_scanner.py <target> <start_port> <end_port>
