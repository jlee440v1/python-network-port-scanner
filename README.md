# Python Network Port Scanner

## Overview

A Python-based TCP port scanner developed as a cybersecurity learning project. The tool scans a specified range of TCP ports on an authorized target and identifies open ports and commonly associated services.

## Features

- Accepts a target IP address or hostname
- Allows the user to specify a port range
- Identifies open TCP ports
- Attempts to identify common services
- Measures scan duration
- Validates user input
- Handles invalid targets and port ranges

## Technologies

- Python 3
- Python socket library
- TCP/IP networking
- Linux/Ubuntu

## Usage

```bash
python3 port_scanner.py <target> <start_port> <end_port>

