# Data Science Project
<!-- TODO: Update title -->

---

⚠️⚠️⚠️

**NOTE:**

The logical root directory of the present location actually corresponds to the physical root of [this repository](https://github.com/kvn-dtrx/ds-project-template).

This note should be removed prior to project submission, of course.

⚠️⚠️⚠️

---

## Synopsis

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

The organisation of the repository follows common conventions and therefore requires little explanation. Our analysis notebooks (with technical details) are subordinated to [`notebooks/`](./notebooks/).

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

2. Choose the right setup option based on your operating system:

   - `make unix`: macOS/Linux.
   - `make win`: Windows (PowerShell).

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

**Template:** This repository was instantiated from this [Data Science Project Template](https://github.com/kvn-dtrx/ds-project-template).

**License:** [MIT License](license.txt)

**Acknowledgements:** The second author would also like to thank his ghostwriter [Gregory Peter Taylor](https://chatgpt.com).
