import os

BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

BUILD_NAME = "ElPais-Scraper-Build"
PROJECT_NAME = "ElPais Automation Assignment"

CAPABILITIES = [

    {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "11",
            "buildName": BUILD_NAME,
            "sessionName": "Windows 11 - Chrome",
            "projectName": PROJECT_NAME
        }
    },

    {
        "browserName": "Firefox",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "10",
            "buildName": BUILD_NAME,
            "sessionName": "Windows 10 - Firefox",
            "projectName": PROJECT_NAME
        }
    },

    {
        "browserName": "Safari",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "OS X",
            "osVersion": "Ventura",
            "buildName": BUILD_NAME,
            "sessionName": "MacOS Ventura - Safari",
            "projectName": PROJECT_NAME
        }
    },

    {
        "browserName": "Chrome",
        "bstack:options": {
            "deviceName": "Samsung Galaxy S23",
            "osVersion": "13.0",
            "realMobile": "true",
            "buildName": BUILD_NAME,
            "sessionName": "Samsung S23 - Chrome",
            "projectName": PROJECT_NAME
        }
    },

    {
        "browserName": "Safari",
        "bstack:options": {
            "deviceName": "iPhone 14",
            "osVersion": "16",
            "realMobile": "true",
            "buildName": BUILD_NAME,
            "sessionName": "iPhone 14 - Safari",
            "projectName": PROJECT_NAME
        }
    }

]