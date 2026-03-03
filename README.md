# EL PAÍS BrowserStack Automation Assignment

## Overview

This project implements an automated scraper for the EL PAÍS Opinion section using Selenium.  
The framework executes in parallel across multiple desktop and real mobile environments using BrowserStack Automate.

---

## Features

- Scrapes latest 5 opinion articles
- Extracts:
  - Title
  - Content preview
  - Image URL
- Downloads article images
- Translates titles to English
- Performs word frequency analysis
- Executes in parallel across 5 environments
- Marks session pass/fail status in BrowserStack
- Public build reporting enabled

---

## Cross-Platform Execution

Executed across:

- Windows 11 – Chrome
- Windows 10 – Firefox
- macOS Ventura – Safari
- Samsung Galaxy S23 – Chrome (real device)
- iPhone 14 – Safari (real device)

Parallel execution implemented using `ThreadPoolExecutor`.

---

## Architecture

```
core/
│
├── scraper.py              # Main scraping logic
├── driver_factory.py       # Local / BrowserStack driver abstraction
├── image_downloader.py     # Image download handler
├── translator.py           # Title translation logic
├── text_analyzer.py        # Word frequency analysis
│
config/
├── browserstack_config.py  # Capability configuration
│
main.py                     # Parallel test runner
```

---

## Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <your-repo-link>
cd elpais-browserstack-automation
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running Locally

```bash
python main.py
```

---

## BrowserStack Integration

The framework supports execution on BrowserStack using capability configuration.

Set your credentials inside:

```
config/browserstack_config.py
```

Then run:

```bash
python main.py
```

---

## BrowserStack Execution Result

### 🔗 Public Build Link

https://automate.browserstack.com/projects/ElPais+Automation+Assignment/builds/ElPais-Scraper-Build/3?public_token=7061173ede10a49acf4d9da87c43af2786c0aada3cf099eeac92cfe475d5f8e1

---

### ✅ Build Summary

- Total Sessions: 5
- Passed: 5
- Failed: 0
- Execution Mode: Parallel
- Real Devices Included: Yes

---

### 📸 Build Dashboard Screenshot

![BrowserStack Build Result](docs/browserstack-build-success.png)

---

## Design Decisions

- Driver abstraction allows local/cloud execution without modifying scraping logic.
- Capability configuration enables scalable cross-browser execution.
- Parallel execution ensures efficient multi-environment testing.
- Explicit session status marking improves dashboard reporting accuracy.

---

## Author

Vallen Dsouza