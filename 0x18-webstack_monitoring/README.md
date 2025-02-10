# Curriculum: Webstack Monitoring Project

## Overview
This project is part of the Curriculum in SE Foundations, focusing on Webstack Monitoring.

### Concepts
- Monitoring
- Server

## Background Context
Monitoring is crucial in the tech industry. In this project, we implement tools to measure server performance.

### Learning Objectives
- Why monitoring is needed
- The two main areas of monitoring
- Purpose of access and error logs for a web server

### Materials
- [What is server monitoring](https://example.com/server_monitoring)
- [What is application monitoring](https://example.com/application_monitoring)
- [System monitoring by Google](https://example.com/system_monitoring_google)
- [Nginx logging and monitoring](https://example.com/nginx_logging_monitoring)

## Requirements
- README.md file is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck without error

### Servers
| Name          | Username | IP             | State   |
|---------------|----------|----------------|---------|
| 420588-web-01 | ubuntu   | 54.144.139.197| running |
| 420588-web-02 | ubuntu   | 34.203.29.50  | running |
| 420588-lb-01  | ubuntu   | 100.26.155.176| running |

## Tasks
### 0. Sign up for Datadog and install datadog-agent
Sign up for a free Datadog account, install the agent on web-01, and create an application key.

### 1. Monitor some metrics
Set up monitors in the Datadog dashboard to monitor read and write requests per second.

### 2. Create a dashboard
Create a dashboard with at least 4 widgets to monitor various metrics.
