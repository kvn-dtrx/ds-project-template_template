# Data Science Project
<!-- TODO: Update title -->

---

⚠️⚠️⚠️ **NOTE** ⚠️⚠️⚠️

This repository represents the
To The logical root directory of this repository is moved to [`meta/`](./meta/)!

Won't employ  we decided to move the TO make templating for the user as convenient as possible (and submodules subtrees or dedicated documentation branches), the logical root of 

This note is intended to be removed before project submission.

---

## Synopsis

### Problem Description

<!-- 
TODO: Write this section 

Aspects which can be addressed here:

- Problem:
  - The business/research problem.
  - The objective of the project.
  - Key questions answered.
- Data:
  - Source(s) of data.
  - How to access (if public).
  - Description of columns/features.
  - Size and format.
- Results:
  - Summary of findings (accuracy, metrics, charts).
  - Visuals or links to reports (e.g., PDF, dashboard).
  - Key insights.
-->

## Repository Organisation

The organisation of the repository follows common conventions and therefore requires little explanation. Our analysis notebooks (with technical details) are subordinated to [`notebooks/`](./notebooks/)

## Installation

### Requirements

- Python 3.11.3
- pyenv

### Setup

1. Navigate to a working directory of your choice, then clone the repository and enter it:

   ``` shell
   git clone https://github.com/<username>/<reponame>.git &&
       cd <reponame>
   ```

2. Choose a setup option based on your operating system and intended use:

   - `make basic-unix` / `make basic-win`: for general use or exploration (core dependencies only).
   - `make dev-unix` / `make dev-win`: for contributors (includes development tools like linters and pre-commit hooks).

   If you prefer to run the commands manually yourself or want to inspect what each `make` target does first, use the `-n` flag for a dry run. This prints the commands without executing them:

   ``` shell
   make -n <target>
   ```

3. Activate the virtual environment:

   - On macOS/Linux, run:

     ```shell
     source .venv/bin/activate
     ```

   - On Windows (PowerShell), run:

     ``` powershell
     .\.venv\Scripts\Activate.ps1
     ```

---

## Colophon
<!-- TODO: Update section -->

**Authors:** [The Octocat](https://github.com/octocat), [Ghost](https://github.com/ghost)

**Template:** This repository was created from the [10NN DS/ML Project Template](https://github.com/neuefische/ds-take-me-home_template).

**License:** [MIT License](license.txt)

**Acknowledgements:** The first author would also like to thank his ghostwriter [Gregory Peter Thompson](https://chatgpt.com).
