{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/TheEvergreenStateCollege/week-3-chinchillabob/blob/main/hw/hw3/ds100_utils.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "deletable": false,
        "editable": false,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HtLUf5yWJDxp",
        "outputId": "ff030eb7-816a-49d3-a049-132f38394b24"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: otter-grader in /usr/local/lib/python3.7/dist-packages (3.2.1)\n",
            "Requirement already satisfied: python-on-whales in /usr/local/lib/python3.7/dist-packages (from otter-grader) (0.43.0)\n",
            "Requirement already satisfied: nbformat in /usr/local/lib/python3.7/dist-packages (from otter-grader) (5.3.0)\n",
            "Requirement already satisfied: ipykernel in /usr/local/lib/python3.7/dist-packages (from otter-grader) (4.10.1)\n",
            "Requirement already satisfied: matplotlib in /usr/local/lib/python3.7/dist-packages (from otter-grader) (3.2.2)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.7/dist-packages (from otter-grader) (1.15.0)\n",
            "Requirement already satisfied: google-auth-oauthlib in /usr/local/lib/python3.7/dist-packages (from otter-grader) (0.4.6)\n",
            "Requirement already satisfied: nbconvert in /usr/local/lib/python3.7/dist-packages (from otter-grader) (5.6.1)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from otter-grader) (2.23.0)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.7/dist-packages (from otter-grader) (1.3.5)\n",
            "Requirement already satisfied: dill in /usr/local/lib/python3.7/dist-packages (from otter-grader) (0.3.4)\n",
            "Requirement already satisfied: PyYAML in /usr/local/lib/python3.7/dist-packages (from otter-grader) (3.13)\n",
            "Requirement already satisfied: gspread in /usr/local/lib/python3.7/dist-packages (from otter-grader) (3.4.2)\n",
            "Requirement already satisfied: jupyter-client in /usr/local/lib/python3.7/dist-packages (from otter-grader) (5.3.5)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.7/dist-packages (from otter-grader) (2.11.3)\n",
            "Requirement already satisfied: google-api-python-client in /usr/local/lib/python3.7/dist-packages (from otter-grader) (1.12.11)\n",
            "Requirement already satisfied: pdfkit in /usr/local/lib/python3.7/dist-packages (from otter-grader) (1.0.0)\n",
            "Requirement already satisfied: PyPDF2 in /usr/local/lib/python3.7/dist-packages (from otter-grader) (1.27.9)\n",
            "Requirement already satisfied: google-auth<3dev,>=1.16.0 in /usr/local/lib/python3.7/dist-packages (from google-api-python-client->otter-grader) (1.35.0)\n",
            "Requirement already satisfied: google-auth-httplib2>=0.0.3 in /usr/local/lib/python3.7/dist-packages (from google-api-python-client->otter-grader) (0.0.4)\n",
            "Requirement already satisfied: google-api-core<3dev,>=1.21.0 in /usr/local/lib/python3.7/dist-packages (from google-api-python-client->otter-grader) (1.31.5)\n",
            "Requirement already satisfied: httplib2<1dev,>=0.15.0 in /usr/local/lib/python3.7/dist-packages (from google-api-python-client->otter-grader) (0.17.4)\n",
            "Requirement already satisfied: uritemplate<4dev,>=3.0.0 in /usr/local/lib/python3.7/dist-packages (from google-api-python-client->otter-grader) (3.0.1)\n",
            "Requirement already satisfied: pytz in /usr/local/lib/python3.7/dist-packages (from google-api-core<3dev,>=1.21.0->google-api-python-client->otter-grader) (2022.1)\n",
            "Requirement already satisfied: googleapis-common-protos<2.0dev,>=1.6.0 in /usr/local/lib/python3.7/dist-packages (from google-api-core<3dev,>=1.21.0->google-api-python-client->otter-grader) (1.56.0)\n",
            "Requirement already satisfied: packaging>=14.3 in /usr/local/lib/python3.7/dist-packages (from google-api-core<3dev,>=1.21.0->google-api-python-client->otter-grader) (21.3)\n",
            "Requirement already satisfied: protobuf>=3.12.0 in /usr/local/lib/python3.7/dist-packages (from google-api-core<3dev,>=1.21.0->google-api-python-client->otter-grader) (3.17.3)\n",
            "Requirement already satisfied: setuptools>=40.3.0 in /usr/local/lib/python3.7/dist-packages (from google-api-core<3dev,>=1.21.0->google-api-python-client->otter-grader) (57.4.0)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.7/dist-packages (from google-auth<3dev,>=1.16.0->google-api-python-client->otter-grader) (0.2.8)\n",
            "Requirement already satisfied: cachetools<5.0,>=2.0.0 in /usr/local/lib/python3.7/dist-packages (from google-auth<3dev,>=1.16.0->google-api-python-client->otter-grader) (4.2.4)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.7/dist-packages (from google-auth<3dev,>=1.16.0->google-api-python-client->otter-grader) (4.8)\n",
            "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /usr/local/lib/python3.7/dist-packages (from packaging>=14.3->google-api-core<3dev,>=1.21.0->google-api-python-client->otter-grader) (3.0.8)\n",
            "Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /usr/local/lib/python3.7/dist-packages (from pyasn1-modules>=0.2.1->google-auth<3dev,>=1.16.0->google-api-python-client->otter-grader) (0.4.8)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests->otter-grader) (3.0.4)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests->otter-grader) (2021.10.8)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests->otter-grader) (2.10)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests->otter-grader) (1.24.3)\n",
            "Requirement already satisfied: requests-oauthlib>=0.7.0 in /usr/local/lib/python3.7/dist-packages (from google-auth-oauthlib->otter-grader) (1.3.1)\n",
            "Requirement already satisfied: oauthlib>=3.0.0 in /usr/local/lib/python3.7/dist-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib->otter-grader) (3.2.0)\n",
            "Requirement already satisfied: ipython>=4.0.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel->otter-grader) (5.5.0)\n",
            "Requirement already satisfied: tornado>=4.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel->otter-grader) (5.1.1)\n",
            "Requirement already satisfied: traitlets>=4.1.0 in /usr/local/lib/python3.7/dist-packages (from ipykernel->otter-grader) (5.1.1)\n",
            "Requirement already satisfied: pexpect in /usr/local/lib/python3.7/dist-packages (from ipython>=4.0.0->ipykernel->otter-grader) (4.8.0)\n",
            "Requirement already satisfied: simplegeneric>0.8 in /usr/local/lib/python3.7/dist-packages (from ipython>=4.0.0->ipykernel->otter-grader) (0.8.1)\n",
            "Requirement already satisfied: prompt-toolkit<2.0.0,>=1.0.4 in /usr/local/lib/python3.7/dist-packages (from ipython>=4.0.0->ipykernel->otter-grader) (1.0.18)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.7/dist-packages (from ipython>=4.0.0->ipykernel->otter-grader) (2.6.1)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.7/dist-packages (from ipython>=4.0.0->ipykernel->otter-grader) (0.7.5)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.7/dist-packages (from ipython>=4.0.0->ipykernel->otter-grader) (4.4.2)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.7/dist-packages (from prompt-toolkit<2.0.0,>=1.0.4->ipython>=4.0.0->ipykernel->otter-grader) (0.2.5)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.7/dist-packages (from jinja2->otter-grader) (2.0.1)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.7/dist-packages (from jupyter-client->otter-grader) (2.8.2)\n",
            "Requirement already satisfied: jupyter-core>=4.6.0 in /usr/local/lib/python3.7/dist-packages (from jupyter-client->otter-grader) (4.10.0)\n",
            "Requirement already satisfied: pyzmq>=13 in /usr/local/lib/python3.7/dist-packages (from jupyter-client->otter-grader) (22.3.0)\n",
            "Requirement already satisfied: numpy>=1.11 in /usr/local/lib/python3.7/dist-packages (from matplotlib->otter-grader) (1.21.6)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.7/dist-packages (from matplotlib->otter-grader) (0.11.0)\n",
            "Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.7/dist-packages (from matplotlib->otter-grader) (1.4.2)\n",
            "Requirement already satisfied: typing-extensions in /usr/local/lib/python3.7/dist-packages (from kiwisolver>=1.0.1->matplotlib->otter-grader) (4.2.0)\n",
            "Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->otter-grader) (0.8.4)\n",
            "Requirement already satisfied: testpath in /usr/local/lib/python3.7/dist-packages (from nbconvert->otter-grader) (0.6.0)\n",
            "Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.7/dist-packages (from nbconvert->otter-grader) (1.5.0)\n",
            "Requirement already satisfied: entrypoints>=0.2.2 in /usr/local/lib/python3.7/dist-packages (from nbconvert->otter-grader) (0.4)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.7/dist-packages (from nbconvert->otter-grader) (0.7.1)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.7/dist-packages (from nbconvert->otter-grader) (5.0.0)\n",
            "Requirement already satisfied: jsonschema>=2.6 in /usr/local/lib/python3.7/dist-packages (from nbformat->otter-grader) (4.3.3)\n",
            "Requirement already satisfied: fastjsonschema in /usr/local/lib/python3.7/dist-packages (from nbformat->otter-grader) (2.15.3)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=2.6->nbformat->otter-grader) (0.18.1)\n",
            "Requirement already satisfied: importlib-resources>=1.4.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=2.6->nbformat->otter-grader) (5.7.1)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.7/dist-packages (from jsonschema>=2.6->nbformat->otter-grader) (21.4.0)\n",
            "Requirement already satisfied: importlib-metadata in /usr/local/lib/python3.7/dist-packages (from jsonschema>=2.6->nbformat->otter-grader) (4.11.3)\n",
            "Requirement already satisfied: zipp>=3.1.0 in /usr/local/lib/python3.7/dist-packages (from importlib-resources>=1.4.0->jsonschema>=2.6->nbformat->otter-grader) (3.8.0)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.7/dist-packages (from bleach->nbconvert->otter-grader) (0.5.1)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.7/dist-packages (from pexpect->ipython>=4.0.0->ipykernel->otter-grader) (0.7.0)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.7/dist-packages (from python-on-whales->otter-grader) (4.64.0)\n",
            "Requirement already satisfied: pydantic in /usr/local/lib/python3.7/dist-packages (from python-on-whales->otter-grader) (1.9.0)\n",
            "Requirement already satisfied: typer>=0.4.1 in /usr/local/lib/python3.7/dist-packages (from python-on-whales->otter-grader) (0.4.1)\n",
            "Requirement already satisfied: click<9.0.0,>=7.1.1 in /usr/local/lib/python3.7/dist-packages (from typer>=0.4.1->python-on-whales->otter-grader) (7.1.2)\n"
          ]
        }
      ],
      "source": [
        "# Initialize Otter\n",
        "!pip install otter-grader\n",
        "import otter\n",
        "grader = otter.Notebook(\"hw3.ipynb\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "nbgrader": {
          "grade": false,
          "grade_id": "intro-hw2",
          "locked": true,
          "schema_version": 2,
          "solution": false
        },
        "id": "UfY_N4bGJDxr"
      },
      "source": [
        "# Homework 3: Food Safety\n",
        "## Cleaning and Exploring Data with Pandas\n",
        "## Due Date: Thursday, September 16th, 11:59 PM\n",
        "## Collaboration Policy\n",
        "\n",
        "Data science is a collaborative activity. While you may talk with others about\n",
        "the homework, we ask that you **write your solutions individually**. If you do\n",
        "discuss the assignments with others please **include their names** at the top\n",
        "of your notebook."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fr-BEgYMJDxs"
      },
      "source": [
        "**Collaborators**: *list collaborators here*"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WtpNdjuKJDxt"
      },
      "source": [
        "\n",
        "## This Assignment\n",
        "\n",
        "In this homework, we will investigate restaurant food safety scores for restaurants in San Francisco. The scores and violation information have been [made available by the San Francisco Department of Public Health](https://data.sfgov.org/Health-and-Social-Services/Restaurant-Scores-LIVES-Standard/pyih-qa8i). The main goal for this assignment is to walk through the process of Data Cleaning and EDA. \n",
        "\n",
        "\n",
        "As we clean and explore these data, you will gain practice with:\n",
        "* Reading simple csv files and using Pandas\n",
        "* Working with data at different levels of granularity\n",
        "* Identifying the type of data collected, missing values, anomalies, etc.\n",
        "* Exploring characteristics and distributions of individual variables\n",
        "\n",
        "## Score Breakdown \n",
        "Question | Points\n",
        "--- | ---\n",
        "1a | 1\n",
        "1b | 2\n",
        "1c | 1\n",
        "2a | 2\n",
        "2b | 2\n",
        "2ci | 1\n",
        "2cii | 1\n",
        "2d | 2\n",
        "2e | 2\n",
        "2f | 2\n",
        "3a | 1\n",
        "3bi | 2\n",
        "3bii | 2\n",
        "3biii | 1\n",
        "3ci | 1\n",
        "3cii | 1\n",
        "3ciii | 1\n",
        "3civ | 1\n",
        "3d | 3\n",
        "4a | 2\n",
        "4b | 3\n",
        "4c | 2\n",
        "5a|1\n",
        "5b|2\n",
        "6a|3\n",
        "6b|2\n",
        "6c|2\n",
        "7|0\n",
        "Total | 46"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "G6Aru4GcJDxt"
      },
      "source": [
        "## Before You Start\n",
        "\n",
        "For each question in the assignment, please write down your answer in the answer cell(s) right below the question. \n",
        "\n",
        "We understand that it is helpful to have extra cells breaking down the process towards reaching your final answer. If you happen to create new cells below your answer to run codes, **NEVER** add cells between a question cell and the answer cell below it. It will cause errors when we run the autograder, and it will sometimes cause a failure to generate the PDF file.\n",
        "\n",
        "**Important note: The local autograder tests will not be comprehensive. You can pass the automated tests in your notebook but still fail tests in the autograder.** Please be sure to check your results carefully.\n",
        "\n",
        "Finally, unless we state otherwise, try to avoid using python for loops or list comprehensions.  The majority of this assignment can be done using builtin commands in Pandas and numpy.  \n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "nbgrader": {
          "grade": false,
          "grade_id": "import",
          "locked": true,
          "schema_version": 2,
          "solution": false
        },
        "id": "geH8T0uvJDxu"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "\n",
        "import matplotlib\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "sns.set()\n",
        "plt.style.use('fivethirtyeight')\n",
        "\n",
        "import zipfile\n",
        "from pathlib import Path\n",
        "import os # Used to interact with the file system"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "e2YixWIjJDxu"
      },
      "source": [
        "## Obtaining the Data\n",
        "\n",
        "### File Systems and I/O\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7CgJw6YHJDxv"
      },
      "source": [
        "In general, we will focus on using python commands to investigate files.  However, it can sometimes be easier to use shell commands in your local operating system.  The following cells demonstrate how to do this."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "MILfrwcRJDxv"
      },
      "outputs": [],
      "source": [
        "from pathlib import Path\n",
        "data_dir = Path('.')\n",
        "data_dir.mkdir(exist_ok = True)\n",
        "file_path = data_dir / Path('data.zip')\n",
        "dest_path = file_path"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OXlusD6xJDxw"
      },
      "source": [
        "After running the cell above, if you list the contents of the directory containing this notebook, you should see `data.zip`.\n",
        "\n",
        "*Note*: The command below starts with an `!`. This tells our Jupyter notebook to pass this command to the operating system. In this case, the command is the `ls` Unix command which lists files in the current directory."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Wndj78HUJDxx",
        "outputId": "ae6e05c3-7b0e-4a72-c8ee-4fe6a7e38931"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "sample_data  tests\n"
          ]
        }
      ],
      "source": [
        "!ls"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wY5sAiZeJDxx"
      },
      "source": [
        "## 1: Loading Food Safety Data\n",
        "\n",
        "We have data, but we don't have any specific questions about the data yet. Let's focus on understanding the structure of the data; this involves answering questions such as:\n",
        "\n",
        "* Is the data in a standard format or encoding?\n",
        "* Is the data organized in records?\n",
        "* What are the fields in each record?\n",
        "\n",
        "Let's start by looking at the contents of `data.zip`. It's not just a single file but rather a compressed directory of multiple files. We could inspect it by uncompressing it using a shell command such as `!unzip data.zip`, but in this homework we're going to do almost everything in Python for maximum portability."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1BhzkyMxJDxx"
      },
      "source": [
        "## Looking Inside and Extracting the Zip Files\n",
        "\n",
        "The following codeblocks are setup. Simply run the cells; **do not modify them**. Question 1a is where you will start to write code.\n",
        "\n",
        "Here, we assign `my_zip` to a `zipfile.Zipfile` object representing `data.zip`, and assign `list_names` to a list of all the names of the contents in `data.zip`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uANw9cAAJDxy",
        "outputId": "5ad9a8b8-86b7-4492-a5e8-89f0c4d3270c"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['data/',\n",
              " 'data/bus.csv',\n",
              " 'data/ins.csv',\n",
              " 'data/ins2vio.csv',\n",
              " 'data/vio.csv',\n",
              " 'data/sf_zipcodes.json',\n",
              " 'data/legend.csv']"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ],
      "source": [
        "my_zip = zipfile.ZipFile(dest_path, 'r')\n",
        "list_names = my_zip.namelist()\n",
        "list_names"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6lGsZIHmJDxy"
      },
      "source": [
        "You may notice that we did not write `zipfile.ZipFile('data.zip', ...)`. Instead, we used `zipfile.ZipFile(dest_path, ...)`. In general, we **strongly suggest having your filenames hard coded as string literals only once** in a notebook. It is very dangerous to hard code things twice because if you change one but forget to change the other, you can end up with bugs that are very hard to find."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FatOIIZSJDxy"
      },
      "source": [
        "Now we display the files' names and their sizes."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "N6db6vlhJDxy",
        "outputId": "1658e9c2-f9f1-4eee-e096-b6b55039a261"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "data/\t0\n",
            "data/bus.csv\t665365\n",
            "data/ins.csv\t1860919\n",
            "data/ins2vio.csv\t1032799\n",
            "data/vio.csv\t4213\n",
            "data/sf_zipcodes.json\t474\n",
            "data/legend.csv\t120\n"
          ]
        }
      ],
      "source": [
        "my_zip = zipfile.ZipFile(dest_path, 'r')\n",
        "for info in my_zip.infolist():\n",
        "    print('{}\\t{}'.format(info.filename, info.file_size))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "G69ncAT-JDxz"
      },
      "source": [
        "Often when working with zipped data, we'll never unzip the actual zipfile. This saves space on our local computer. However, for this homework the files are small, so we're just going to unzip everything. This has the added benefit that you can look inside the csv files using a text editor, which might be handy for understanding the structure of the files. The cell below will unzip the csv files into a subdirectory called `data`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Qgcjk04EJDxz",
        "outputId": "a3a68461-1691-4d97-f4e3-756a6c89ab50"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "bus.csv  ins2vio.csv  ins.csv  legend.csv  sf_zipcodes.json  vio.csv\n"
          ]
        }
      ],
      "source": [
        "data_dir = Path('.')\n",
        "my_zip.extractall(data_dir)\n",
        "!ls {data_dir / Path(\"data\")}"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HglZ2CoWJDxz"
      },
      "source": [
        "The cell above created a folder called `data`, and in it there should be five CSV files. Let's open up `legend.csv` to see its contents. To do this, click on the jupyterhub logo on the top left, then navigate to `su21/hw/hw3/data/` and click on `legend.csv`. The file will open up in another tab. You should see something that looks like:\n",
        "\n",
        "    \"Minimum_Score\",\"Maximum_Score\",\"Description\"\n",
        "    0,70,\"Poor\"\n",
        "    71,85,\"Needs Improvement\"\n",
        "    86,90,\"Adequate\"\n",
        "    91,100,\"Good\""
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "djFLrituJDxz"
      },
      "source": [
        "The `legend.csv` file does indeed look like a well-formed CSV file. Let's check the other three files. Rather than opening up each file manually, let's use Python to print out the first 5 lines of each. The `ds100_utils` library has a method called `head` that will allow you to retrieve the first N lines of a file as a list. For example `ds100_utils.head('data/legend.csv', 5)` will return the first 5 lines of \"data/legend.csv\". Try using this function to print out the first 5 lines of all six files that we just extracted from the zipfile."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "n_6cSPgBJDxz",
        "outputId": "55ed77a2-ff9e-4fff-b17d-91fa71d1fceb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['\"business id column\",\"name\",\"address\",\"city\",\"state\",\"postal_code\",\"latitude\",\"longitude\",\"phone_number\"\\n', '\"1000\",\"HEUNG YUEN RESTAURANT\",\"3279 22nd St\",\"San Francisco\",\"CA\",\"94110\",\"37.755282\",\"-122.420493\",\"-9999\"\\n', '\"100010\",\"ILLY CAFFE SF_PIER 39\",\"PIER 39  K-106-B\",\"San Francisco\",\"CA\",\"94133\",\"-9999\",\"-9999\",\"+14154827284\"\\n', '\"100017\",\"AMICI\\'S EAST COAST PIZZERIA\",\"475 06th St\",\"San Francisco\",\"CA\",\"94103\",\"-9999\",\"-9999\",\"+14155279839\"\\n', '\"100026\",\"LOCAL CATERING\",\"1566 CARROLL AVE\",\"San Francisco\",\"CA\",\"94124\",\"-9999\",\"-9999\",\"+14155860315\"\\n'] \n",
            "\n",
            "['\"iid\",\"date\",\"score\",\"type\"\\n', '\"100010_20190329\",\"03/29/2019 12:00:00 AM\",\"-1\",\"New Construction\"\\n', '\"100010_20190403\",\"04/03/2019 12:00:00 AM\",\"100\",\"Routine - Unscheduled\"\\n', '\"100017_20190417\",\"04/17/2019 12:00:00 AM\",\"-1\",\"New Ownership\"\\n', '\"100017_20190816\",\"08/16/2019 12:00:00 AM\",\"91\",\"Routine - Unscheduled\"\\n'] \n",
            "\n",
            "['\"iid\",\"vid\"\\n', '\"97975_20190725\",\"103124\"\\n', '\"85986_20161011\",\"103114\"\\n', '\"95754_20190327\",\"103124\"\\n', '\"77005_20170429\",\"103120\"\\n'] \n",
            "\n",
            "['\"description\",\"risk_category\",\"vid\"\\n', '\"Consumer advisory not provided for raw or undercooked foods\",\"Moderate Risk\",103128\\n', '\"Contaminated or adulterated food\",\"High Risk\",103108\\n', '\"Discharge from employee nose mouth or eye\",\"Moderate Risk\",103117\\n', '\"Employee eating or smoking\",\"Moderate Risk\",103118\\n'] \n",
            "\n",
            "['{\"zip_codes\": [\"94102\", \"94103\", \"94104\", \"94105\", \"94107\", \"94108\", \"94109\", \"94110\", \"94111\", \"94112\", \"94114\", \"94115\", \"94116\", \"94117\", \"94118\", \"94119\", \"94120\", \"94121\", \"94122\", \"94123\", \"94124\", \"94125\", \"94126\", \"94127\", \"94128\", \"94129\", \"94130\", \"94131\", \"94132\", \"94133\", \"94134\", \"94137\", \"94139\", \"94140\", \"94141\", \"94142\", \"94143\", \"94144\", \"94145\", \"94146\", \"94147\", \"94151\", \"94158\", \"94159\", \"94160\", \"94161\", \"94163\", \"94164\", \"94172\", \"94177\", \"94188\"]}'] \n",
            "\n",
            "['\"Minimum_Score\",\"Maximum_Score\",\"Description\"\\n', '0,70,\"Poor\"\\n', '71,85,\"Needs Improvement\"\\n', '86,90,\"Adequate\"\\n', '91,100,\"Good\"\\n'] \n",
            "\n"
          ]
        }
      ],
      "source": [
        "import ds100_utils\n",
        "\n",
        "data_dir = \"./\"\n",
        "for f in list_names:\n",
        "    if not os.path.isdir(f):\n",
        "        print(ds100_utils.head(data_dir + f, 5), \"\\n\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bXUIUXP7JDx0"
      },
      "source": [
        "## Reading in and Verifying Data\n",
        "\n",
        "Based on the above information, let's attempt to load `bus.csv`, `ins2vio.csv`, `ins.csv`, and `vio.csv` into pandas dataframes with the following names: `bus`, `ins2vio`, `ins`, and `vio` respectively.\n",
        "\n",
        "*Note:* Because of character encoding issues one of the files (`bus`) will require an additional argument `encoding='ISO-8859-1'` when calling `pd.read_csv`. At some point in your future, you should read all about [character encodings](https://diveintopython3.problemsolving.io/strings.html). We won't discuss these in detail in Data 100."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "id": "toiw-v69JDx0"
      },
      "outputs": [],
      "source": [
        "# path to directory containing data\n",
        "dsDir = Path('data')\n",
        "\n",
        "bus = pd.read_csv(dsDir/'bus.csv', encoding='ISO-8859-1')\n",
        "ins2vio = pd.read_csv(dsDir/'ins2vio.csv')\n",
        "ins = pd.read_csv(dsDir/'ins.csv')\n",
        "vio = pd.read_csv(dsDir/'vio.csv')\n",
        "\n",
        "#This code is essential for the autograder to function properly. Do not edit\n",
        "ins_test = ins"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rnR-zW-5JDx0"
      },
      "source": [
        "Now that you've read in the files, let's try some `pd.DataFrame` methods ([docs](https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.html)).\n",
        "Use the `DataFrame.head` method to show the top few lines of the `bus`, `ins`, and `vio` dataframes. To show multiple return outputs in one single cell, you can use `display()`. Currently, running the cell below will display the first few lines of the `bus` dataframe. "
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "p4bV5c-hJDx0",
        "outputId": "d16aeb2b-c344-49d3-a363-0aeca982cdb8"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   business id column                         name                 address  \\\n",
              "0                1000        HEUNG YUEN RESTAURANT            3279 22nd St   \n",
              "1              100010        ILLY CAFFE SF_PIER 39        PIER 39  K-106-B   \n",
              "2              100017  AMICI'S EAST COAST PIZZERIA             475 06th St   \n",
              "3              100026               LOCAL CATERING        1566 CARROLL AVE   \n",
              "4              100030             OUI OUI! MACARON  2200 JERROLD AVE STE C   \n",
              "\n",
              "            city state postal_code     latitude    longitude  phone_number  \n",
              "0  San Francisco    CA       94110    37.755282  -122.420493         -9999  \n",
              "1  San Francisco    CA       94133 -9999.000000 -9999.000000   14154827284  \n",
              "2  San Francisco    CA       94103 -9999.000000 -9999.000000   14155279839  \n",
              "3  San Francisco    CA       94124 -9999.000000 -9999.000000   14155860315  \n",
              "4  San Francisco    CA       94124 -9999.000000 -9999.000000   14159702675  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-fe541fac-a388-4206-8f1a-23183f0c0434\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>business id column</th>\n",
              "      <th>name</th>\n",
              "      <th>address</th>\n",
              "      <th>city</th>\n",
              "      <th>state</th>\n",
              "      <th>postal_code</th>\n",
              "      <th>latitude</th>\n",
              "      <th>longitude</th>\n",
              "      <th>phone_number</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1000</td>\n",
              "      <td>HEUNG YUEN RESTAURANT</td>\n",
              "      <td>3279 22nd St</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>94110</td>\n",
              "      <td>37.755282</td>\n",
              "      <td>-122.420493</td>\n",
              "      <td>-9999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>100010</td>\n",
              "      <td>ILLY CAFFE SF_PIER 39</td>\n",
              "      <td>PIER 39  K-106-B</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>94133</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>14154827284</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>100017</td>\n",
              "      <td>AMICI'S EAST COAST PIZZERIA</td>\n",
              "      <td>475 06th St</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>94103</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>14155279839</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>100026</td>\n",
              "      <td>LOCAL CATERING</td>\n",
              "      <td>1566 CARROLL AVE</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>94124</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>14155860315</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>100030</td>\n",
              "      <td>OUI OUI! MACARON</td>\n",
              "      <td>2200 JERROLD AVE STE C</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>94124</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>14159702675</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-fe541fac-a388-4206-8f1a-23183f0c0434')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-fe541fac-a388-4206-8f1a-23183f0c0434 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-fe541fac-a388-4206-8f1a-23183f0c0434');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ],
      "source": [
        "bus.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CL0yTtxjJDx0"
      },
      "source": [
        "The `DataFrame.describe` method can also be handy for computing summaries of numeric columns of our dataframes. Try it out with each of our 4 dataframes. Below, we have used the method to give a summary of the `bus` dataframe. "
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "4Q19hFrpJDx0",
        "outputId": "eaa6a9a5-0e71-453a-a853-0d4501b5d50f"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "       business id column     latitude    longitude  phone_number\n",
              "count         6253.000000  6253.000000  6253.000000  6.253000e+03\n",
              "mean         60448.948984 -5575.337966 -5645.817699  4.701819e+09\n",
              "std          36480.132445  4983.390142  4903.993683  6.667508e+09\n",
              "min             19.000000 -9999.000000 -9999.000000 -9.999000e+03\n",
              "25%          18399.000000 -9999.000000 -9999.000000 -9.999000e+03\n",
              "50%          75685.000000 -9999.000000 -9999.000000 -9.999000e+03\n",
              "75%          90886.000000    37.776494  -122.421553  1.415533e+10\n",
              "max         102705.000000    37.824494     0.000000  1.415988e+10"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-9c4f0720-d8ee-427b-9f80-917068227973\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>business id column</th>\n",
              "      <th>latitude</th>\n",
              "      <th>longitude</th>\n",
              "      <th>phone_number</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>6253.000000</td>\n",
              "      <td>6253.000000</td>\n",
              "      <td>6253.000000</td>\n",
              "      <td>6.253000e+03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>60448.948984</td>\n",
              "      <td>-5575.337966</td>\n",
              "      <td>-5645.817699</td>\n",
              "      <td>4.701819e+09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>36480.132445</td>\n",
              "      <td>4983.390142</td>\n",
              "      <td>4903.993683</td>\n",
              "      <td>6.667508e+09</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>19.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9.999000e+03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>18399.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9.999000e+03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>75685.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9.999000e+03</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>90886.000000</td>\n",
              "      <td>37.776494</td>\n",
              "      <td>-122.421553</td>\n",
              "      <td>1.415533e+10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>102705.000000</td>\n",
              "      <td>37.824494</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.415988e+10</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-9c4f0720-d8ee-427b-9f80-917068227973')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-9c4f0720-d8ee-427b-9f80-917068227973 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-9c4f0720-d8ee-427b-9f80-917068227973');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ],
      "source": [
        "bus.describe()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9x0koPNqJDx1"
      },
      "source": [
        "Now, we perform some sanity checks for you to verify that the data was loaded with the correct structure. Run the following cells to load some basic utilities (you do not need to change these at all):"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5yihfLdQJDx1"
      },
      "source": [
        "First, we check the basic structure of the data frames you created:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "id": "IlpLJxzNJDx1"
      },
      "outputs": [],
      "source": [
        "\n",
        "#assert all(bus.columns == ['bid', 'name', 'address', 'city', 'state', 'postal_code',\n",
        "                           #'latitude', 'longitude', 'phone_number'])\n",
        "assert 6250 <= len(bus) <= 6260\n",
        "\n",
        "assert all(ins.columns == ['iid', 'date', 'score', 'type'])\n",
        "assert 26660 <= len(ins) <= 26670\n",
        "\n",
        "assert all(vio.columns == ['description', 'risk_category', 'vid'])\n",
        "assert 60 <= len(vio) <= 65\n",
        "\n",
        "assert all(ins2vio.columns == ['iid', 'vid'])\n",
        "assert 40210 <= len(ins2vio) <= 40220"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_ZXH3ph7JDx1"
      },
      "source": [
        "Next we'll check that the statistics match what we expect. The following are hard-coded statistical summaries of the correct data."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 450
        },
        "id": "0iQn2zoIJDx1",
        "outputId": "a37ef9ff-f381-4b36-af29-fbc3636d51cd"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "What we expect from your Businesses dataframe:\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "     business id column     latitude  longitude\n",
              "min                19.0 -9999.000000    -9999.0\n",
              "50%             75685.0 -9999.000000    -9999.0\n",
              "max            102705.0    37.824494        0.0"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-bf19a46e-212b-41ae-9ac3-a52b3ffb9161\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>business id column</th>\n",
              "      <th>latitude</th>\n",
              "      <th>longitude</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>19.0</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>75685.0</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>102705.0</td>\n",
              "      <td>37.824494</td>\n",
              "      <td>0.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-bf19a46e-212b-41ae-9ac3-a52b3ffb9161')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-bf19a46e-212b-41ae-9ac3-a52b3ffb9161 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-bf19a46e-212b-41ae-9ac3-a52b3ffb9161');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "What we expect from your Inspections dataframe:\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "     score\n",
              "min   -1.0\n",
              "50%   76.0\n",
              "max  100.0"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-c84836c2-67b9-4b5d-8362-596a4dd1c9bb\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>score</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>-1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>76.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>100.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-c84836c2-67b9-4b5d-8362-596a4dd1c9bb')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-c84836c2-67b9-4b5d-8362-596a4dd1c9bb button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-c84836c2-67b9-4b5d-8362-596a4dd1c9bb');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "What we expect from your Violations dataframe:\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "          vid\n",
              "min  103102.0\n",
              "50%  103135.0\n",
              "max  103177.0"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-404f4ecb-a83b-402b-b63a-13edd00851e2\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>vid</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>103102.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>103135.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>103177.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-404f4ecb-a83b-402b-b63a-13edd00851e2')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-404f4ecb-a83b-402b-b63a-13edd00851e2 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-404f4ecb-a83b-402b-b63a-13edd00851e2');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {}
        }
      ],
      "source": [
        "bus_summary = pd.DataFrame(**{'columns': ['business id column', 'latitude', 'longitude'],\n",
        " 'data': {'business id column': {'50%': 75685.0, 'max': 102705.0, 'min': 19.0},\n",
        "  'latitude': {'50%': -9999.0, 'max': 37.824494, 'min': -9999.0},\n",
        "  'longitude': {'50%': -9999.0,\n",
        "   'max': 0.0,\n",
        "   'min': -9999.0}},\n",
        " 'index': ['min', '50%', 'max']})\n",
        "\n",
        "ins_summary = pd.DataFrame(**{'columns': ['score'],\n",
        " 'data': {'score': {'50%': 76.0, 'max': 100.0, 'min': -1.0}},\n",
        " 'index': ['min', '50%', 'max']})\n",
        "\n",
        "vio_summary = pd.DataFrame(**{'columns': ['vid'],\n",
        " 'data': {'vid': {'50%': 103135.0, 'max': 103177.0, 'min': 103102.0}},\n",
        " 'index': ['min', '50%', 'max']})\n",
        "\n",
        "from IPython.display import display\n",
        "\n",
        "print('What we expect from your Businesses dataframe:')\n",
        "display(bus_summary)\n",
        "print('What we expect from your Inspections dataframe:')\n",
        "display(ins_summary)\n",
        "print('What we expect from your Violations dataframe:')\n",
        "display(vio_summary)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dEwyYpzkJDx1"
      },
      "source": [
        "The code below defines a testing function that we'll use to verify that your data has the same statistics as what we expect. Run these cells to define the function. The `df_allclose` function has this name because we are verifying that all of the statistics for your dataframe are close to the expected values. Why not `df_allequal`? It's a bad idea in almost all cases to compare two floating point values like 37.780435, as rounding error can cause spurious failures."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "id": "E9cD4NYSJDx1"
      },
      "outputs": [],
      "source": [
        "\"\"\"Run this cell to load this utility comparison function that we will use in various\n",
        "tests below (both tests you can see and those we run internally for grading).\n",
        "\n",
        "Do not modify the function in any way.\n",
        "\"\"\"\n",
        "\n",
        "\n",
        "def df_allclose(actual, desired, columns=None, rtol=5e-2):\n",
        "    \"\"\"Compare selected columns of two dataframes on a few summary statistics.\n",
        "    \n",
        "    Compute the min, median and max of the two dataframes on the given columns, and compare\n",
        "    that they match numerically to the given relative tolerance.\n",
        "    \n",
        "    If they don't match, an AssertionError is raised (by `numpy.testing`).\n",
        "    \"\"\"    \n",
        "    # summary statistics to compare on\n",
        "    stats = ['min', '50%', 'max']\n",
        "    \n",
        "    # For the desired values, we can provide a full DF with the same structure as\n",
        "    # the actual data, or pre-computed summary statistics.\n",
        "    # We assume a pre-computed summary was provided if columns is None. In that case, \n",
        "    # `desired` *must* have the same structure as the actual's summary\n",
        "    if columns is None:\n",
        "        des = desired\n",
        "        columns = desired.columns\n",
        "    else:\n",
        "        des = desired[columns].describe().loc[stats]\n",
        "\n",
        "    # Extract summary stats from actual DF\n",
        "    act = actual[columns].describe().loc[stats]\n",
        "\n",
        "    return np.allclose(act, des, rtol)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Gf7Ws1Q2JDx1"
      },
      "source": [
        "We will now explore each file in turn, including determining its granularity and primary keys and exploring many of the variables individually. Let's begin with the businesses file, which has been read into the `bus` dataframe."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "nbgrader": {
          "grade": false,
          "grade_id": "business-data",
          "locked": true,
          "schema_version": 2,
          "solution": false
        },
        "id": "rgjbUCsOJDx2"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "<br/><br/><br/>\n",
        "\n",
        "## Question 1a: Examining the Business Data File"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vv8RMaLSJDx2"
      },
      "source": [
        "From its name alone, we expect the `bus.csv` file to contain information about the restaurants. Let's investigate the granularity of this dataset."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 22,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "-Cw14yVNJDx2",
        "outputId": "10d4903a-2f62-4480-ff33-071f50f6c50b"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   business id column                         name                 address  \\\n",
              "0                1000        HEUNG YUEN RESTAURANT            3279 22nd St   \n",
              "1              100010        ILLY CAFFE SF_PIER 39        PIER 39  K-106-B   \n",
              "2              100017  AMICI'S EAST COAST PIZZERIA             475 06th St   \n",
              "3              100026               LOCAL CATERING        1566 CARROLL AVE   \n",
              "4              100030             OUI OUI! MACARON  2200 JERROLD AVE STE C   \n",
              "\n",
              "            city state postal_code     latitude    longitude  phone_number  \n",
              "0  San Francisco    CA       94110    37.755282  -122.420493         -9999  \n",
              "1  San Francisco    CA       94133 -9999.000000 -9999.000000   14154827284  \n",
              "2  San Francisco    CA       94103 -9999.000000 -9999.000000   14155279839  \n",
              "3  San Francisco    CA       94124 -9999.000000 -9999.000000   14155860315  \n",
              "4  San Francisco    CA       94124 -9999.000000 -9999.000000   14159702675  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-a8615d96-ed12-4583-8242-ba47915b0689\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>business id column</th>\n",
              "      <th>name</th>\n",
              "      <th>address</th>\n",
              "      <th>city</th>\n",
              "      <th>state</th>\n",
              "      <th>postal_code</th>\n",
              "      <th>latitude</th>\n",
              "      <th>longitude</th>\n",
              "      <th>phone_number</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1000</td>\n",
              "      <td>HEUNG YUEN RESTAURANT</td>\n",
              "      <td>3279 22nd St</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>94110</td>\n",
              "      <td>37.755282</td>\n",
              "      <td>-122.420493</td>\n",
              "      <td>-9999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>100010</td>\n",
              "      <td>ILLY CAFFE SF_PIER 39</td>\n",
              "      <td>PIER 39  K-106-B</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>94133</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>14154827284</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>100017</td>\n",
              "      <td>AMICI'S EAST COAST PIZZERIA</td>\n",
              "      <td>475 06th St</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>94103</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>14155279839</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>100026</td>\n",
              "      <td>LOCAL CATERING</td>\n",
              "      <td>1566 CARROLL AVE</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>94124</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>14155860315</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>100030</td>\n",
              "      <td>OUI OUI! MACARON</td>\n",
              "      <td>2200 JERROLD AVE STE C</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>94124</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>14159702675</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a8615d96-ed12-4583-8242-ba47915b0689')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-a8615d96-ed12-4583-8242-ba47915b0689 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-a8615d96-ed12-4583-8242-ba47915b0689');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ],
      "source": [
        "bus.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Txq7Yl4GJDx2"
      },
      "source": [
        "The `bus` dataframe contains a column called `business id column` which probably corresponds to a unique business id.  However, we will first rename that column to `bid` for simplicity.\n",
        "\n",
        "**Note**: In practice we might want to do this renaming when the table is loaded but for grading purposes we will do it here.\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "id": "Z9ZQ4mV2JDx2"
      },
      "outputs": [],
      "source": [
        "bus = bus.rename(columns={\"business id column\": \"bid\"})"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "IfS94u_FJDx2"
      },
      "source": [
        "Examining the entries in `bus`, is the `bid` unique for each record (i.e. each row of data)? Your code should compute the answer, i.e. don't just hard code `True` or `False`.\n",
        "\n",
        "Hint: use `value_counts()` or `unique()` to determine if the `bid` series has any duplicates.\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q1a\n",
        "points: 1\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YdBGmjaKJDx2",
        "outputId": "9f5d0f1e-6d2b-49d9-aa37-e043809b70c6"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 24
        }
      ],
      "source": [
        "is_bid_unique = pd.Series(bus.bid).is_unique\n",
        "is_bid_unique"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 25,
      "metadata": {
        "deletable": false,
        "editable": false,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 47
        },
        "id": "W3OvohffJDx2",
        "outputId": "fbe8dc07-6203-4c58-b031-08d6b896b5f7"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "q1a results: All test cases passed!"
            ],
            "text/html": [
              "<p><strong><pre style='display: inline;'>q1a</pre></strong> passed!</p>"
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ],
      "source": [
        "grader.check(\"q1a\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "L07UIrcVJDx3"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "\n",
        "## Question 1b\n",
        "\n",
        "We will now work with some important fields in `bus`.\n",
        "\n",
        "1. Assign `top_names` to a list containing the top 5 most frequently used business names, from most frequent to least frequent.\n",
        "2. Assign `top_addresses` to a list containing the top 5 addressses where businesses are located, from most popular to least popular.\n",
        "\n",
        "Hint: you may find `value_counts()` helpful.\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q1b\n",
        "points: 2\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 26,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Vc7jrYSgJDx3",
        "outputId": "26671af2-27f5-4693-e870-7ee69d40567c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10\n"
          ]
        }
      ],
      "source": [
        "top_names = bus['name'].value_counts().head()\n",
        "top_addresses = bus['address'].value_counts().head()\n",
        "print(top_names[2])\n",
        "#top_names, top_addresses"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 27,
      "metadata": {
        "deletable": false,
        "editable": false,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 604
        },
        "id": "h3ui8AYFJDx3",
        "outputId": "f28723fc-e3cf-490e-9bff-7e2f2318b218"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "q1b results:\n",
              "    q1b - 1 result:\n",
              "        Test case passed!\n",
              "\n",
              "    q1b - 2 result:\n",
              "        Trying:\n",
              "            assert top_names[0] == \"Peet's Coffee & Tea\"\n",
              "        Expecting nothing\n",
              "        **********************************************************************\n",
              "        Line 1, in q1b 1\n",
              "        Failed example:\n",
              "            assert top_names[0] == \"Peet's Coffee & Tea\"\n",
              "        Exception raised:\n",
              "            Traceback (most recent call last):\n",
              "              File \"/usr/lib/python3.7/doctest.py\", line 1337, in __run\n",
              "                compileflags, 1), test.globs)\n",
              "              File \"<doctest q1b 1[0]>\", line 1, in <module>\n",
              "                assert top_names[0] == \"Peet's Coffee & Tea\"\n",
              "            AssertionError\n",
              "        Trying:\n",
              "            assert top_addresses[0] == 'Off The Grid'\n",
              "        Expecting nothing\n",
              "        **********************************************************************\n",
              "        Line 2, in q1b 1\n",
              "        Failed example:\n",
              "            assert top_addresses[0] == 'Off The Grid'\n",
              "        Exception raised:\n",
              "            Traceback (most recent call last):\n",
              "              File \"/usr/lib/python3.7/doctest.py\", line 1337, in __run\n",
              "                compileflags, 1), test.globs)\n",
              "              File \"<doctest q1b 1[1]>\", line 1, in <module>\n",
              "                assert top_addresses[0] == 'Off The Grid'\n",
              "            AssertionError"
            ],
            "text/html": [
              "<p><strong style='color: red;'><pre style='display: inline;'>q1b</pre> results:</strong></p><p><strong><pre style='display: inline;'>q1b - 1</pre> result:</strong></p><pre>    Test case passed!</pre><p><strong><pre style='display: inline;'>q1b - 2</pre> result:</strong></p><pre>    Trying:\n",
              "        assert top_names[0] == \"Peet's Coffee & Tea\"\n",
              "    Expecting nothing\n",
              "    **********************************************************************\n",
              "    Line 1, in q1b 1\n",
              "    Failed example:\n",
              "        assert top_names[0] == \"Peet's Coffee & Tea\"\n",
              "    Exception raised:\n",
              "        Traceback (most recent call last):\n",
              "          File \"/usr/lib/python3.7/doctest.py\", line 1337, in __run\n",
              "            compileflags, 1), test.globs)\n",
              "          File \"<doctest q1b 1[0]>\", line 1, in <module>\n",
              "            assert top_names[0] == \"Peet's Coffee & Tea\"\n",
              "        AssertionError\n",
              "    Trying:\n",
              "        assert top_addresses[0] == 'Off The Grid'\n",
              "    Expecting nothing\n",
              "    **********************************************************************\n",
              "    Line 2, in q1b 1\n",
              "    Failed example:\n",
              "        assert top_addresses[0] == 'Off The Grid'\n",
              "    Exception raised:\n",
              "        Traceback (most recent call last):\n",
              "          File \"/usr/lib/python3.7/doctest.py\", line 1337, in __run\n",
              "            compileflags, 1), test.globs)\n",
              "          File \"<doctest q1b 1[1]>\", line 1, in <module>\n",
              "            assert top_addresses[0] == 'Off The Grid'\n",
              "        AssertionError\n",
              "</pre>"
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ],
      "source": [
        "grader.check(\"q1b\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "hzXiOUjwJDx3"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "\n",
        "## Question 1c\n",
        "\n",
        "Based on the above exploration, what does each record represent?\n",
        "\n",
        "A. \"One location of a restaurant.\"\n",
        "B. \"A chain of restaurants.\"\n",
        "C. \"A city block.\"\n",
        "\n",
        "Answer in the following cell. Your answer should be a string, either `\"A\"`, `\"B\"`, or `\"C\"`.\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q1c\n",
        "points: \n",
        "- 0\n",
        "- 1\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 28,
      "metadata": {
        "id": "sPF1Y7t9JDx3"
      },
      "outputs": [],
      "source": [
        "# What does each record represent?  Valid answers are:\n",
        "#    \"One location of a restaurant.\"\n",
        "#    \"A chain of restaurants.\"\n",
        "#    \"A city block.\"\n",
        "q1c = \"A\""
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 29,
      "metadata": {
        "deletable": false,
        "editable": false,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 47
        },
        "id": "2O0KtuAUJDx3",
        "outputId": "bcbf7058-29bd-4593-f974-abccadadf00b"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "q1c results: All test cases passed!"
            ],
            "text/html": [
              "<p><strong><pre style='display: inline;'>q1c</pre></strong> passed!</p>"
            ]
          },
          "metadata": {},
          "execution_count": 29
        }
      ],
      "source": [
        "grader.check(\"q1c\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "nbgrader": {
          "grade": false,
          "grade_id": "business-data",
          "locked": true,
          "schema_version": 2,
          "solution": false
        },
        "id": "Vy2271SUJDx3"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "<br/><br/><br/>\n",
        "\n",
        "# 2: Cleaning the Business Data Postal Codes\n",
        "\n",
        "The business data contains postal code information that we can use to aggregate the ratings over regions of the city.  Let's examine and clean the postal code field.  The postal code (sometimes also called a ZIP code) partitions the city into regions:\n",
        "\n",
        "<img src=\"https://www.usmapguide.com/wp-content/uploads/2019/03/printable-san-francisco-zip-code-map.jpg\" alt=\"ZIP Code Map\" style=\"width: 600px\">"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "nbgrader": {
          "grade": false,
          "grade_id": "cell-a4c4a09f1ecf2f4b",
          "locked": true,
          "schema_version": 2,
          "solution": false
        },
        "id": "Sa0MKLXLJDx3"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "\n",
        "## Question 2a\n",
        "\n",
        "How many restaurants are in each ZIP code? \n",
        "\n",
        "In the cell below, create a **series** where the index is the postal code and the value is the number of records with that postal code in descending order of count. You may need to use `groupby()`, `size()`, or `value_counts()`. Do you notice any odd/invalid zip codes?\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q2a\n",
        "points: 2\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 30,
      "metadata": {
        "nbgrader": {
          "grade": false,
          "grade_id": "cell-d2151d673e6c36a1",
          "locked": false,
          "schema_version": 2,
          "solution": true
        },
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "07UIX-hGJDx4",
        "outputId": "b83c3e7d-1377-4b9d-85f4-d945f1feaad7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "94103         562\n",
            "94110         555\n",
            "94102         456\n",
            "94107         408\n",
            "94133         398\n",
            "94109         382\n",
            "94111         259\n",
            "94122         255\n",
            "94105         249\n",
            "94118         231\n",
            "94115         230\n",
            "94108         229\n",
            "94124         218\n",
            "94114         200\n",
            "-9999         194\n",
            "94112         192\n",
            "94117         189\n",
            "94123         177\n",
            "94121         157\n",
            "94104         142\n",
            "94132         132\n",
            "94116          97\n",
            "94158          90\n",
            "94134          82\n",
            "94127          67\n",
            "94131          49\n",
            "94130           8\n",
            "94143           5\n",
            "94301           2\n",
            "94188           2\n",
            "94101           2\n",
            "CA              2\n",
            "94013           2\n",
            "941102019       1\n",
            "941             1\n",
            "95112           1\n",
            "94105-2907      1\n",
            "94102-5917      1\n",
            "94124-1917      1\n",
            "94621           1\n",
            "95122           1\n",
            "95132           1\n",
            "95109           1\n",
            "95133           1\n",
            "95117           1\n",
            "94901           1\n",
            "94105-1420      1\n",
            "94544           1\n",
            "64110           1\n",
            "94122-1909      1\n",
            "00000           1\n",
            "94080           1\n",
            "Ca              1\n",
            "94602           1\n",
            "94129           1\n",
            "94014           1\n",
            "94117-3504      1\n",
            "94518           1\n",
            "94120           1\n",
            "92672           1\n",
            "95105           1\n",
            "941033148       1\n",
            "94123-3106      1\n"
          ]
        }
      ],
      "source": [
        "zip_counts = bus['postal_code'].value_counts()\n",
        "print(zip_counts.to_string())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 31,
      "metadata": {
        "deletable": false,
        "editable": false,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 47
        },
        "id": "krYEM263JDx4",
        "outputId": "d904499e-b141-4c8c-da6a-eecfc75b58c5"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "q2a results: All test cases passed!"
            ],
            "text/html": [
              "<p><strong><pre style='display: inline;'>q2a</pre></strong> passed!</p>"
            ]
          },
          "metadata": {},
          "execution_count": 31
        }
      ],
      "source": [
        "grader.check(\"q2a\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "gfz3CXyLJDx4"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "--- \n",
        "\n",
        "## Question 2b\n",
        "\n",
        "Answer the following questions about the `postal_code` column in the `bus` dataframe.\n",
        "\n",
        "1. The ZIP code column is which of the following type of data:\n",
        "    1. Quantitative Continuous\n",
        "    1. Quantitative Discrete\n",
        "    1. Qualitative Ordinal\n",
        "    1. Qualitative Nominal    \n",
        "1. What Python data type is used to represent a ZIP code?\n",
        "    1. `str`\n",
        "    2. `int`\n",
        "    3. `bool`\n",
        "    4. `float`\n",
        "\n",
        "*Note*: ZIP codes and postal codes are the same thing.\n",
        "\n",
        "Please write your answers in the cell below. Your answer should be a string, either `\"A\"`, `\"B\"`, `\"C\"`, or `\"D\"`.\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q2b\n",
        "points: \n",
        "- 0\n",
        "- 0\n",
        "- 1\n",
        "- 1\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 32,
      "metadata": {
        "id": "uUUUlpUDJDx4"
      },
      "outputs": [],
      "source": [
        "# The ZIP code column is which of the following type of data:\n",
        "q2b_part1 = \"A\"\n",
        "\n",
        "# What Python data type is used to represent a ZIP code? \n",
        "q2b_part2 = \"C\""
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 33,
      "metadata": {
        "deletable": false,
        "editable": false,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 47
        },
        "id": "aHa2LqY4JDx4",
        "outputId": "808f34d2-0049-456a-cfc5-29eb880cbaac"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "q2b results: All test cases passed!"
            ],
            "text/html": [
              "<p><strong><pre style='display: inline;'>q2b</pre></strong> passed!</p>"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ],
      "source": [
        "grader.check(\"q2b\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7v45pKWHJDx4"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "--- \n",
        "\n",
        "## Question 2c\n",
        "\n",
        "In question 2a we noticed a large number of potentially invalid ZIP codes (e.g., \"Ca\").  These are likely due to data entry errors.  To get a better understanding of the potential errors in the zip codes we will:\n",
        "\n",
        "1. Import a list of valid San Francisco ZIP codes by using `pd.read_json` to load the file `data/sf_zipcodes.json` and extract a **series** of type `str` containing the valid ZIP codes.  *Hint: set `dtype` when invoking `read_json`.*\n",
        "1. Construct a `DataFrame` containing only the businesses which DO NOT have valid ZIP codes.  You will probably want to use the `Series.isin` function. \n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "6KGrEEX3JDx4"
      },
      "source": [
        "**Step 1**\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q2ci\n",
        "points: 1\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 34,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9KpValzbJDx4",
        "outputId": "d3db67e9-f865-484f-9d07-f805d7d1c277"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    94102\n",
              "1    94103\n",
              "2    94104\n",
              "3    94105\n",
              "4    94107\n",
              "Name: zip_codes, dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 34
        }
      ],
      "source": [
        "valid_zips = pd.read_json('data/sf_zipcodes.json', dtype=False).squeeze()\n",
        "valid_zips.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 35,
      "metadata": {
        "deletable": false,
        "editable": false,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 47
        },
        "id": "MdQWueM7JDx5",
        "outputId": "1f8831be-5404-4cd2-e256-f196d5f1eb64"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "q2ci results: All test cases passed!"
            ],
            "text/html": [
              "<p><strong><pre style='display: inline;'>q2ci</pre></strong> passed!</p>"
            ]
          },
          "metadata": {},
          "execution_count": 35
        }
      ],
      "source": [
        "grader.check(\"q2ci\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "UVOpyp4oJDx5"
      },
      "source": [
        "**Step 2**\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q2cii\n",
        "points: 1\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 36,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 676
        },
        "id": "Mrl0Wo7eJDx5",
        "outputId": "d846915f-0d45-4c4f-8db8-f00a6034580d"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "        bid                               name  \\\n",
              "22   100126          Lamas Peruvian Food Truck   \n",
              "68   100417                   COMPASS ONE, LLC   \n",
              "96   100660                          TEAPENTER   \n",
              "109  100781                  LE CAFE DU SOLEIL   \n",
              "144  101084                     Deli North 200   \n",
              "156  101129                    Vendor Room 200   \n",
              "177  101192                       Cochinita #2   \n",
              "276  102014       DROPBOX (Section 3, Floor 7)   \n",
              "295  102245         Vessell CA Operations (#4)   \n",
              "298   10227                   The Napper Tandy   \n",
              "320   10372  BERNAL HEIGHTS NEIGBORHOOD CENTER   \n",
              "321   10373                    El Tonayense #1   \n",
              "322   10376                Good Frikin Chicken   \n",
              "324   10406              Sunset Youth Services   \n",
              "357   11416                   El Beach Burrito   \n",
              "381   12199                      El Gallo Giro   \n",
              "384   12344         The Village Market & Pizza   \n",
              "406   13062              Everett Middle School   \n",
              "434   13753                             Taboun   \n",
              "548   17423                  Project Open Hand   \n",
              "\n",
              "                                 address           city state postal_code  \\\n",
              "22                      Private Location  San Francisco    CA       -9999   \n",
              "68                       1 MARKET ST. FL  San Francisco    CA  94105-1420   \n",
              "96                        1518 IRVING ST  San Francisco    CA  94122-1909   \n",
              "109                      200 FILLMORE ST  San Francisco    CA  94117-3504   \n",
              "144  1 Warriors Way Level 300 North East  San Francisco    CA       94518   \n",
              "156  1 Warriors Way Level 300 South West  San Francisco    CA       -9999   \n",
              "177             2 Marina Blvd Fort Mason  San Francisco    CA       -9999   \n",
              "276                        1800 Owens St  San Francisco    CA       -9999   \n",
              "295                      2351 Mission St  San Francisco    CA       -9999   \n",
              "298                         3200 24th St  San Francisco    CA       -9999   \n",
              "320                     515 CORTLAND AVE  San Francisco    CA       -9999   \n",
              "321                     1717 Harrison St  San Francisco    CA       -9999   \n",
              "322                           10 29th St  San Francisco    CA       -9999   \n",
              "324                        3918 Judah St  San Francisco    CA       -9999   \n",
              "357                        3914 Judah St  San Francisco    CA       -9999   \n",
              "381                         3055 23rd St  San Francisco    CA       -9999   \n",
              "384                        750 Font Blvd  San Francisco    CA       -9999   \n",
              "406                        450 Church St  San Francisco    CA       -9999   \n",
              "434                    203 Parnassus Ave  San Francisco    CA       -9999   \n",
              "548                       100 Diamond St  San Francisco    CA       -9999   \n",
              "\n",
              "        latitude    longitude  phone_number  \n",
              "22  -9999.000000 -9999.000000         -9999  \n",
              "68  -9999.000000 -9999.000000   14154324000  \n",
              "96  -9999.000000 -9999.000000   14155868318  \n",
              "109 -9999.000000 -9999.000000   14155614215  \n",
              "144 -9999.000000 -9999.000000         -9999  \n",
              "156 -9999.000000 -9999.000000         -9999  \n",
              "177 -9999.000000 -9999.000000   14150429222  \n",
              "276 -9999.000000 -9999.000000         -9999  \n",
              "295 -9999.000000 -9999.000000         -9999  \n",
              "298    37.752581  -122.416482         -9999  \n",
              "320    37.739110  -122.416404   14155202142  \n",
              "321    37.769426  -122.413446   14155556127  \n",
              "322    37.744369  -122.420967         -9999  \n",
              "324    37.760560  -122.504027         -9999  \n",
              "357    37.760851  -122.503998         -9999  \n",
              "381    37.754218  -122.413285   14155553048  \n",
              "384    37.723462  -122.483012   14155374525  \n",
              "406    37.763794  -122.428617         -9999  \n",
              "434    37.764574  -122.452950         -9999  \n",
              "548    37.760689  -122.437252         -9999  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-dab372a1-9aca-477a-877f-b7e68d98917c\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>bid</th>\n",
              "      <th>name</th>\n",
              "      <th>address</th>\n",
              "      <th>city</th>\n",
              "      <th>state</th>\n",
              "      <th>postal_code</th>\n",
              "      <th>latitude</th>\n",
              "      <th>longitude</th>\n",
              "      <th>phone_number</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>22</th>\n",
              "      <td>100126</td>\n",
              "      <td>Lamas Peruvian Food Truck</td>\n",
              "      <td>Private Location</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>-9999</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>68</th>\n",
              "      <td>100417</td>\n",
              "      <td>COMPASS ONE, LLC</td>\n",
              "      <td>1 MARKET ST. FL</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>94105-1420</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>14154324000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>96</th>\n",
              "      <td>100660</td>\n",
              "      <td>TEAPENTER</td>\n",
              "      <td>1518 IRVING ST</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>94122-1909</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>14155868318</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>109</th>\n",
              "      <td>100781</td>\n",
              "      <td>LE CAFE DU SOLEIL</td>\n",
              "      <td>200 FILLMORE ST</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>94117-3504</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>14155614215</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>144</th>\n",
              "      <td>101084</td>\n",
              "      <td>Deli North 200</td>\n",
              "      <td>1 Warriors Way Level 300 North East</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>94518</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>156</th>\n",
              "      <td>101129</td>\n",
              "      <td>Vendor Room 200</td>\n",
              "      <td>1 Warriors Way Level 300 South West</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>-9999</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>177</th>\n",
              "      <td>101192</td>\n",
              "      <td>Cochinita #2</td>\n",
              "      <td>2 Marina Blvd Fort Mason</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>-9999</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>14150429222</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>276</th>\n",
              "      <td>102014</td>\n",
              "      <td>DROPBOX (Section 3, Floor 7)</td>\n",
              "      <td>1800 Owens St</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>-9999</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>295</th>\n",
              "      <td>102245</td>\n",
              "      <td>Vessell CA Operations (#4)</td>\n",
              "      <td>2351 Mission St</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>-9999</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999.000000</td>\n",
              "      <td>-9999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>298</th>\n",
              "      <td>10227</td>\n",
              "      <td>The Napper Tandy</td>\n",
              "      <td>3200 24th St</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>-9999</td>\n",
              "      <td>37.752581</td>\n",
              "      <td>-122.416482</td>\n",
              "      <td>-9999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>320</th>\n",
              "      <td>10372</td>\n",
              "      <td>BERNAL HEIGHTS NEIGBORHOOD CENTER</td>\n",
              "      <td>515 CORTLAND AVE</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>-9999</td>\n",
              "      <td>37.739110</td>\n",
              "      <td>-122.416404</td>\n",
              "      <td>14155202142</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>321</th>\n",
              "      <td>10373</td>\n",
              "      <td>El Tonayense #1</td>\n",
              "      <td>1717 Harrison St</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>-9999</td>\n",
              "      <td>37.769426</td>\n",
              "      <td>-122.413446</td>\n",
              "      <td>14155556127</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>322</th>\n",
              "      <td>10376</td>\n",
              "      <td>Good Frikin Chicken</td>\n",
              "      <td>10 29th St</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>-9999</td>\n",
              "      <td>37.744369</td>\n",
              "      <td>-122.420967</td>\n",
              "      <td>-9999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>324</th>\n",
              "      <td>10406</td>\n",
              "      <td>Sunset Youth Services</td>\n",
              "      <td>3918 Judah St</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>-9999</td>\n",
              "      <td>37.760560</td>\n",
              "      <td>-122.504027</td>\n",
              "      <td>-9999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>357</th>\n",
              "      <td>11416</td>\n",
              "      <td>El Beach Burrito</td>\n",
              "      <td>3914 Judah St</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>-9999</td>\n",
              "      <td>37.760851</td>\n",
              "      <td>-122.503998</td>\n",
              "      <td>-9999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>381</th>\n",
              "      <td>12199</td>\n",
              "      <td>El Gallo Giro</td>\n",
              "      <td>3055 23rd St</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>-9999</td>\n",
              "      <td>37.754218</td>\n",
              "      <td>-122.413285</td>\n",
              "      <td>14155553048</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>384</th>\n",
              "      <td>12344</td>\n",
              "      <td>The Village Market &amp; Pizza</td>\n",
              "      <td>750 Font Blvd</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>-9999</td>\n",
              "      <td>37.723462</td>\n",
              "      <td>-122.483012</td>\n",
              "      <td>14155374525</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>406</th>\n",
              "      <td>13062</td>\n",
              "      <td>Everett Middle School</td>\n",
              "      <td>450 Church St</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>-9999</td>\n",
              "      <td>37.763794</td>\n",
              "      <td>-122.428617</td>\n",
              "      <td>-9999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>434</th>\n",
              "      <td>13753</td>\n",
              "      <td>Taboun</td>\n",
              "      <td>203 Parnassus Ave</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>-9999</td>\n",
              "      <td>37.764574</td>\n",
              "      <td>-122.452950</td>\n",
              "      <td>-9999</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>548</th>\n",
              "      <td>17423</td>\n",
              "      <td>Project Open Hand</td>\n",
              "      <td>100 Diamond St</td>\n",
              "      <td>San Francisco</td>\n",
              "      <td>CA</td>\n",
              "      <td>-9999</td>\n",
              "      <td>37.760689</td>\n",
              "      <td>-122.437252</td>\n",
              "      <td>-9999</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-dab372a1-9aca-477a-877f-b7e68d98917c')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-dab372a1-9aca-477a-877f-b7e68d98917c button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-dab372a1-9aca-477a-877f-b7e68d98917c');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 36
        }
      ],
      "source": [
        "# has_valid_zip should be a boolean array\n",
        "# A True value would indicate the business has a valid ZIP code\n",
        "\n",
        "#has_valid_zip =bus['postal_code'].isin(valid_zips)\n",
        "#bus['valid_zip'] = has_valid_zip\n",
        "#invalid_zip_bus = bus.loc[bus['valid_zip']==False, 'name'].to_frame()\n",
        "#invalid_zip_bus.head(20)\n",
        "has_valid_zip = bus['postal_code'].isin(values=valid_zips)\n",
        "invalid_zip_bus = bus[~has_valid_zip]\n",
        "invalid_zip_bus.head(20)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 37,
      "metadata": {
        "deletable": false,
        "editable": false,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 47
        },
        "id": "GEojDHvpJDx5",
        "outputId": "4053b4ba-1368-42f8-b192-3cc918863175"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "q2cii results: All test cases passed!"
            ],
            "text/html": [
              "<p><strong><pre style='display: inline;'>q2cii</pre></strong> passed!</p>"
            ]
          },
          "metadata": {},
          "execution_count": 37
        }
      ],
      "source": [
        "grader.check(\"q2cii\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "Gkhb2LWeJDx5"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "--- \n",
        "\n",
        "## Question 2d\n",
        "\n",
        "In the previous question, many of the businesses had a common invalid postal code that was likely used to encode a MISSING postal code.  Do they all share a potentially \"interesting address\"?\n",
        "\n",
        "In the following cell, construct a **series** that counts the number of businesses at each `address` that have this single likely MISSING postal code value.  Order the series in descending order by count. \n",
        "\n",
        "After examining the output, please answer the following question (2e) by filling in the appropriate variable. If we were to drop businesses with MISSING postal code values would a particular class of business be affected?  If you are unsure try to search the web for the most common addresses.\n",
        "\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q2d\n",
        "points: 2\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 38,
      "metadata": {
        "scrolled": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Uqp8YflDJDx5",
        "outputId": "96871be4-deac-4c67-e33a-c54209663373"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "135\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Off The Grid                  39\n",
              "Off the Grid                  10\n",
              "OTG                            4\n",
              "Approved Locations             3\n",
              "Approved Private Locations     3\n",
              "Name: address, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 38
        }
      ],
      "source": [
        "missing_zip_address_count = invalid_zip_bus.loc[invalid_zip_bus['postal_code'] == '-9999', 'address'].value_counts()\n",
        "print(len(missing_zip_address_count))\n",
        "missing_zip_address_count.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 39,
      "metadata": {
        "deletable": false,
        "editable": false,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 47
        },
        "id": "MWKOghULJDx5",
        "outputId": "5b5f5fd4-cc1f-47ca-c12a-21d6ad91ef6d"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "q2d results: All test cases passed!"
            ],
            "text/html": [
              "<p><strong><pre style='display: inline;'>q2d</pre></strong> passed!</p>"
            ]
          },
          "metadata": {},
          "execution_count": 39
        }
      ],
      "source": [
        "grader.check(\"q2d\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "gbJYJcZqJDx5"
      },
      "source": [
        "<!-- BEGIN QUESTION -->\n",
        "\n",
        "<br/><br/><br/>\n",
        "\n",
        "--- \n",
        "\n",
        "## Question 2e\n",
        "\n",
        "If we were to drop businesses with MISSING postal code values, what specific types of businesses would we be excluding? In other words, is there a commonality among businesses with missing postal codes?\n",
        "\n",
        "**Hint**: You may want to look at the names of the businesses with missing postal codes. Feel free to reuse parts of your code from 2d, but we will not be grading your code.\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q2e\n",
        "points: 2\n",
        "manual: True\n",
        "-->"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "BrycBq6vJDx5"
      },
      "source": [
        "Places that are located in areas with no address system. "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "ldnfwWTyJDx6"
      },
      "source": [
        "<!-- END QUESTION -->\n",
        "\n",
        "<br/><br/><br/>\n",
        "\n",
        "--- \n",
        "\n",
        "## Question 2f\n",
        "\n",
        "Examine the `invalid_zip_bus` dataframe we computed above and look at the businesses that DO NOT have the special MISSING ZIP code value. Some of the invalid postal codes are just the full 9 digit code rather than the first 5 digits. Create a new column named `postal5` in the original `bus` dataframe which contains only the first 5 digits of the `postal_code` column.\n",
        "\n",
        "Then, for any of the `postal5` ZIP code entries that were not a valid San Fransisco ZIP Code (according to `valid_zips`), the provided code will set the `postal5` value to `None`.  \n",
        "\n",
        "**Do not modify the provided code!**\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q2f\n",
        "points: 2\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 40,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 240
        },
        "id": "kff3Pz9iJDx6",
        "outputId": "c33c0b78-c22a-4930-94eb-cecd34d9c0af"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-40-7ee87c07b690>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mfive_digit_postal\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpostal_code\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m   \u001b[0;32mreturn\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpostal_code\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;36m6\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mbus\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'postal5'\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mbus\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'postal_code'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mapply\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfive_digit_postal\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0mbus\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'postal5'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mbus\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mloc\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m~\u001b[0m\u001b[0mbus\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'postal5'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0misin\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mvalid_zips\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'postal5'\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: five_digit_postal() missing 1 required positional argument: 'postal_code'"
          ]
        }
      ],
      "source": [
        "def five_digit_postal(postal_code):\n",
        "  return str(postal_code)[:6]\n",
        "bus['postal5'] = bus['postal_code'].apply(five_digit_postal())\n",
        "bus['postal5']\n",
        "bus.loc[~bus['postal5'].isin(valid_zips), 'postal5'] = None\n",
        "# Checking the corrected postal5 column\n",
        "bus.loc[invalid_zip_bus.index, ['bid', 'name', 'postal_code', 'postal5']]"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "2NvHjKLKJDx6"
      },
      "outputs": [],
      "source": [
        "grader.check(\"q2f\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "nbgrader": {
          "grade": false,
          "grade_id": "business-data",
          "locked": true,
          "schema_version": 2,
          "solution": false
        },
        "id": "xiDD08lTJDx6"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "<br/><br/><br/>\n",
        "\n",
        "# 3: Investigate the Inspection Data\n",
        "\n",
        "Let's now turn to the inspection DataFrame. Earlier, we found that `ins` has 4 columns named \n",
        "`iid`, `score`, `date` and `type`.  In this section, we determine the granularity of `ins` and investigate the kinds of information provided for the inspections. "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "nbgrader": {
          "grade": false,
          "grade_id": "cell-174ed23c543ad9da",
          "locked": true,
          "schema_version": 2,
          "solution": false
        },
        "id": "7j_aAXTqJDx6"
      },
      "source": [
        "Let's start by looking again at the first 5 rows of `ins` to see what we're working with."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "nbgrader": {
          "grade": false,
          "grade_id": "cell-f0fbe724a2783e33",
          "locked": true,
          "schema_version": 2,
          "solution": false
        },
        "id": "0EICP43iJDx6"
      },
      "outputs": [],
      "source": [
        "ins.head(5)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "Dhk2Os6CJDx6"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "## Question 3a\n",
        "\n",
        "The column `iid` probably corresponds to an inspection id.  Is it a primary key?  Write an expression (line of code) that evaluates to `True` or `False` based on whether all the values are unique.\n",
        "\n",
        "**Hint:** This is a very similar question to Question 1b.\n",
        "\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q3a\n",
        "points: 1\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "YhfcPSfzJDx6"
      },
      "outputs": [],
      "source": [
        "is_ins_iid_a_primary_key = ...\n",
        "is_ins_iid_a_primary_key"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "Kqx2jlF6JDx6"
      },
      "outputs": [],
      "source": [
        "grader.check(\"q3a\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DvMcei8RJDx6"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "## Question 3b\n",
        "\n",
        "The column `iid` appears to be the composition of two numbers and the first number looks like a business id.  \n",
        "\n",
        "**Part 1.**: Create a new column called `bid` in the `ins` dataframe containing just the business id.  You will want to use `ins['iid'].str` operations to do this.  Also be sure to convert the type of this column to `int`\n",
        "\n",
        "**Part 2.**: Then compute how many values in this new column are invalid business ids (i.e. do not appear in the `bus['bid']` column). This is verifying a foreign key relationship. Consider using the `pd.Series.isin` function.\n",
        "\n",
        "**Part 3.**: Answer True or False, `ins['bid']` is a foreign key reference to `bus['bid']`.\n",
        "\n",
        "\n",
        "**No python `for` loops or list comprehensions required!**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "qJ7gUzmNJDx7"
      },
      "source": [
        "**Part 1**\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q3bi\n",
        "points: 2\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Z5qwVOb1JDx7"
      },
      "outputs": [],
      "source": [
        "...\n",
        "ins.head(5)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "ssLfEcOgJDx7"
      },
      "outputs": [],
      "source": [
        "grader.check(\"q3bi\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "Vw5o0VzDJDx7"
      },
      "source": [
        "**Part 2**\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q3bii\n",
        "points: 2\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "4GWKKpXqJDx7"
      },
      "outputs": [],
      "source": [
        "invalid_bid_count = ..."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "WLM61hsQJDx7"
      },
      "outputs": [],
      "source": [
        "grader.check(\"q3bii\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "WcAUJsMdJDx7"
      },
      "source": [
        "**Part 3**\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q3biii\n",
        "points: 1\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "-s0ae8VzJDx7"
      },
      "outputs": [],
      "source": [
        "# True or False: The column ins['bid'] is a foreign key \n",
        "#   referencing the bus['bid'] primary key.\n",
        "\n",
        "q3b_is_foreign_key = ..."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "Bv4hoeL4JDx7"
      },
      "outputs": [],
      "source": [
        "grader.check(\"q3biii\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RLUTAHupJDx7"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "## Question 3c\n",
        "\n",
        "What if we are interested in a time component of the inspection data?  We need to examine the date column of each inspection. \n",
        "\n",
        "**Part 1:** What is the type of the individual `ins['date']` entries? You may want to grab the very first entry and use the `type` function in python. \n",
        "\n",
        "**Part 2:** Use `pd.to_datetime` to create a new `ins['timestamp']` column containing of `pd.Timestamp` objects.  These will allow us to do more date manipulation.\n",
        "\n",
        "**Part 3:** What are the earliest and latest dates in our inspection data?  *Hint: you can use `min` and `max` on dates of the correct type.*\n",
        "\n",
        "**Part 4:** We probably want to examine the inspections by year. Create an additional `ins['year']` column containing just the year of the inspection.  Consider using `pd.Series.dt.year` to do this.\n",
        "\n",
        "**No python `for` loops or list comprehensions required!**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "12qI59ZUJDx8"
      },
      "source": [
        "**Part 1**\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q3ci\n",
        "points: 1\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "cYLYTqL_JDx8"
      },
      "outputs": [],
      "source": [
        "ins_date_type = ...\n",
        "ins_date_type"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "ioxykF0KJDx8"
      },
      "outputs": [],
      "source": [
        "grader.check(\"q3ci\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "df5cYueVJDx8"
      },
      "source": [
        "**Part 2**\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q3cii\n",
        "points: 1\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "h075wyejJDx8"
      },
      "outputs": [],
      "source": [
        "..."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "SiiWHtzQJDx8"
      },
      "outputs": [],
      "source": [
        "grader.check(\"q3cii\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "3SVlUrYwJDx8"
      },
      "source": [
        "**Part 3**\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q3ciii\n",
        "points: 1\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "XFq1wIdrJDx8"
      },
      "outputs": [],
      "source": [
        "earliest_date = ...\n",
        "latest_date = ...\n",
        "\n",
        "print(\"Earliest Date:\", earliest_date)\n",
        "print(\"Latest Date:\", latest_date)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "BFiksSY2JDx8"
      },
      "outputs": [],
      "source": [
        "grader.check(\"q3ciii\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "CHfPFK9hJDx8"
      },
      "source": [
        "**Part 4**\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q3civ\n",
        "points: 1\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "bjE54Y0VJDx9"
      },
      "outputs": [],
      "source": [
        "..."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "TaEXXSp6JDx9"
      },
      "outputs": [],
      "source": [
        "grader.check(\"q3civ\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "7JqNUPr3JDx9"
      },
      "outputs": [],
      "source": [
        "ins.head()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lPPfWoDoJDx9"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "## Question 3d\n",
        "\n",
        "Let's examine the inspection scores `ins['score']`\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "KDZPufDyJDx9"
      },
      "outputs": [],
      "source": [
        "ins['score'].value_counts().head()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "p63J3g6RJDx9"
      },
      "source": [
        "There are a large number of inspections with the `'score'` of `-1`.   These are probably missing values.  Let's see what type of inspections have scores and which do not. Create the following dataframe using steps similar to the previous question, and assign it to to the variable `ins_missing_score_pivot`.\n",
        "\n",
        "You should observe that inspection scores appear only to be assigned to `Routine - Unscheduled` inspections.\n",
        "\n",
        "\n",
        "<table border=\"1\" class=\"dataframe\">  <thead>    <tr style=\"text-align: right;\">      <th>Missing Score</th>      <th>False</th>      <th>True</th>      <th>Total</th>    </tr>    <tr>      <th>type</th>      <th></th>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>Routine - Unscheduled</th>      <td>14031</td>      <td>46</td>      <td>14077</td>    </tr>    <tr>      <th>Reinspection/Followup</th>      <td>0</td>      <td>6439</td>      <td>6439</td>    </tr>    <tr>      <th>New Ownership</th>      <td>0</td>      <td>1592</td>      <td>1592</td>    </tr>    <tr>      <th>Complaint</th>      <td>0</td>      <td>1458</td>      <td>1458</td>    </tr>    <tr>      <th>New Construction</th>      <td>0</td>      <td>994</td>      <td>994</td>    </tr>    <tr>      <th>Non-inspection site visit</th>      <td>0</td>      <td>811</td>      <td>811</td>    </tr>    <tr>      <th>New Ownership - Followup</th>      <td>0</td>      <td>499</td>      <td>499</td>    </tr>    <tr>      <th>Structural Inspection</th>      <td>0</td>      <td>394</td>      <td>394</td>    </tr>    <tr>      <th>Complaint Reinspection/Followup</th>      <td>0</td>      <td>227</td>      <td>227</td>    </tr>    <tr>      <th>Foodborne Illness Investigation</th>      <td>0</td>      <td>115</td>      <td>115</td>    </tr>    <tr>      <th>Routine - Scheduled</th>      <td>0</td>      <td>46</td>      <td>46</td>    </tr>    <tr>      <th>Administrative or Document Review</th>      <td>0</td>      <td>4</td>      <td>4</td>    </tr>    <tr>      <th>Multi-agency Investigation</th>      <td>0</td>      <td>3</td>      <td>3</td>    </tr>    <tr>      <th>Special Event</th>      <td>0</td>      <td>3</td>      <td>3</td>    </tr>    <tr>      <th>Community Health Assessment</th>      <td>0</td>      <td>1</td>      <td>1</td>    </tr>  </tbody></table>\n",
        "\n",
        "Note that we create a \"Missing Score\" column, which will be `\"True\"` for inspections with a missing score, and `\"False\"` for those with a proper score. This column may be helpful, but you don't need to use it if you don't want to."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "U4WrlinSJDx9"
      },
      "outputs": [],
      "source": [
        "ins['Missing Score'] = (ins['score'] == -1).astype(\"str\")\n",
        "ins_missing_score_pivot = ...\n",
        "\n",
        "..."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "Xv_B8DuGJDx9"
      },
      "outputs": [],
      "source": [
        "grader.check(\"q3d\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fWDlIxMnJDx9"
      },
      "source": [
        "Notice that inspection scores appear only to be assigned to `Routine - Unscheduled` inspections. It is reasonable that for inspection types such as `New Ownership` and `Complaint` to have no associated inspection scores, but we might be curious why there are no inspection scores for the `Reinspection/Followup` inspection type."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "nbgrader": {
          "grade": false,
          "grade_id": "business-data",
          "locked": true,
          "schema_version": 2,
          "solution": false
        },
        "id": "n68Zw6pvJDx9"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "<br/><br/><br/>\n",
        "\n",
        "# 4: Joining Data Across Tables\n",
        "\n",
        "In this question we will start to connect data across mulitple tables.  We will be using the `merge` function. "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ijg27QZVJDx-"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "--- \n",
        "\n",
        "## Question 4a\n",
        "\n",
        "Let's figure out which restaurants had the lowest scores. Before we proceed, let's filter out missing scores from `ins` so that negative scores don't influence our results."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "_UCQySDwJDx-"
      },
      "outputs": [],
      "source": [
        "ins = ins[ins[\"score\"] > 0]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "TjvmER2TJDx-"
      },
      "source": [
        "We'll start by creating a new dataframe called `ins_named`. It should be exactly the same as `ins`, except that it should have the name and address of every business, as determined by the `bus` dataframe. If a `business_id` in `ins` does not exist in `bus`, the name and address should be given as `NaN`. \n",
        "\n",
        "*Hint*: Use the merge method to join the `ins` dataframe with the appropriate portion of the `bus` dataframe. See the official [documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html) on how to use `merge`.\n",
        "\n",
        "*Note*: For quick reference, a pandas 'left' join keeps the keys from the left frame, so if `ins` is the left frame, all the keys from `ins` are kept and if a set of these keys don't have matches in the other frame, the columns from the other frame for these \"unmatched\" key rows contains NaNs.\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q4a\n",
        "points: 2\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "NDUZCz-cJDx-"
      },
      "outputs": [],
      "source": [
        "ins_named = ...\n",
        "\n",
        "...\n",
        "ins_named.head()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "juKIW0CzJDx-"
      },
      "outputs": [],
      "source": [
        "grader.check(\"q4a\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "5vJi9oidJDx-"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "--- \n",
        "\n",
        "## Question 4b\n",
        "\n",
        "Let's look at the 20 businesses with the lowest **median** score.  Order your results by the median score followed by the business name to break ties. The resulting table should look like:\n",
        "\n",
        "\n",
        "*Hint: You may find the `as_index` argument in the `groupby` method important*. [The documentation is linked here!](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)\n",
        "\n",
        "<table border=\"1\" class=\"dataframe\">  <thead>    <tr style=\"text-align: right;\">      <th>bid</th>      <th>name</th>      <th>median score</th>    </tr>  </thead>  <tbody>    <tr>      <th>84590</th>      <td>Chaat Corner</td>      <td>54.0</td>    </tr>    <tr>        <th>90622</th>      <td>Taqueria Lolita</td>      <td>57.0</td>    </tr>    <tr>         <th>94351</th>      <td>VBowls LLC</td>      <td>58.0</td>    </tr>    <tr>          <th>69282</th>      <td>New Jumbo Seafood Restaurant</td>      <td>60.5</td>    </tr>    <tr>         <th>1154</th>      <td>SUNFLOWER RESTAURANT</td>      <td>63.5</td>    </tr>  <tr>          <th>93150</th>      <td>Chez Beesen</td>      <td>64.0</td>    </tr>   <tr>     <th>39776</th>      <td>Duc Loi Supermarket</td>      <td>64.0</td>    </tr>  <tr>         <th>78328</th>      <td>Golden Wok</td>      <td>64.0</td>    </tr>  <tr>          <th>69397</th>      <td>Minna SF Group LLC</td>      <td>64.0</td>    </tr>     <tr>        <th>93502</th>      <td>Smoky Man</td>      <td>64.0</td>    </tr>    <tr>           <th>98995</th>      <td>Vallarta's Taco Bar</td>      <td>64.0</td>    </tr>    <tr>         <th>10877</th>      <td>CHINA FIRST INC.</td>      <td>64.5</td>    </tr>    <tr>        <th>71310</th>      <td>Golden King Vietnamese Restaurant</td>      <td>64.5</td>    </tr>     <tr>          <th>89070</th>      <td>Lafayette Coffee Shop</td>      <td>64.5</td>    </tr>\n",
        "    <tr>          <th>71008</th>      <td>House of Pancakes</td>      <td>65.0</td>    </tr> <tr>         <th>2542</th>      <td>PETER D'S RESTAURANT</td>      <td>65.0</td>    </tr>            <tr>        <th>3862</th>      <td>IMPERIAL GARDEN SEAFOOD RESTAURANT</td>      <td>66.0</td>    </tr>    <tr>         <th>61427</th>      <td>Nick's Foods</td>      <td>66.0</td>    </tr>    <tr>          <th>72176</th>      <td>Wolfes Lunch</td>      <td>66.0</td>    </tr>    <tr>        <th>89141</th>      <td>Cha Cha Cha on Mission</td>      <td>66.5</td>    </tr>  </tbody></table>\n",
        "\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q4b\n",
        "points: 3\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "t-UkJNPMJDx-"
      },
      "outputs": [],
      "source": [
        "twenty_lowest_scoring = ... \n",
        "...\n",
        "\n",
        "twenty_lowest_scoring"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "UMODd2mrJDx-"
      },
      "outputs": [],
      "source": [
        "grader.check(\"q4b\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "lugaPTgVJDx-"
      },
      "source": [
        "### Question 4c\n",
        "\n",
        "Let's figure out which restaurant had the worst score ever (single lowest score). \n",
        "\n",
        "In the cell below, assign `worst_restaurant` to the name of the restaurant with the **lowest inspection score ever**. Feel free to head to yelp.com and look up the reviews page for this restaurant.\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q4c\n",
        "points: 2\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ijMVpUSBJDx_"
      },
      "outputs": [],
      "source": [
        "worst_restaurant = ...\n",
        "worst_restaurant"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "5-vcN0hzJDx_"
      },
      "outputs": [],
      "source": [
        "grader.check(\"q4c\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8bkQIEqlJDx_"
      },
      "source": [
        "<br/><br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "<br/><br/>\n",
        "\n",
        "## 5: Explore Inspection Scores\n",
        "\n",
        "In this part we explore some of the basic inspection score values visually."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "jupyter": {
          "outputs_hidden": true
        },
        "id": "u3ztRfJWJDx_"
      },
      "source": [
        "<!-- BEGIN QUESTION -->\n",
        "\n",
        "<br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "\n",
        "## Question 5a\n",
        "Let's look at the distribution of inspection scores. As we saw before when we called head on this data frame, inspection scores appear to be integer values. The discreteness of this variable means that we can use a bar plot to visualize the distribution of the inspection score. Make a bar plot of the counts of the number of inspections receiving each score.\n",
        "\n",
        "It should look like the image below. It does not need to look exactly the same (e.g., no grid), but make sure that all labels and axes are correct.\n",
        "\n",
        "![](https://github.com/TheEvergreenStateCollege/week-3-chinchillabob/blob/28d867d23f8fb2f55e6096511afe2da6e48efa04/hw/hw3/pics/6a.png?raw=1)\n",
        "\n",
        "You might find this [matplotlib.pyplot tutorial](https://matplotlib.org/tutorials/introductory/pyplot.html) useful. Key syntax that you'll need:\n",
        "\n",
        "```\n",
        "plt.bar\n",
        "plt.xlabel\n",
        "plt.ylabel\n",
        "plt.title\n",
        "```\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q5a\n",
        "points: 1\n",
        "manual: True\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "fQsquzXnJDx_"
      },
      "outputs": [],
      "source": [
        "..."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "KlD40FuUJDx_"
      },
      "source": [
        "<!-- END QUESTION -->\n",
        "\n",
        "<!-- BEGIN QUESTION -->\n",
        "\n",
        "<br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "### Question 5b\n",
        "Describe the qualities of the distribution of the inspections scores based on your bar plot. Consider the mode(s), symmetry, tails, gaps, and anomalous values. Are there any unusual features of this distribution? What do your observations imply about the scores?\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q5b\n",
        "points: 2\n",
        "manual: True\n",
        "-->"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NuSSgmEIJDx_"
      },
      "source": [
        "_Type your answer here, replacing this text._"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fc3albYIJDyA"
      },
      "source": [
        "<!-- END QUESTION -->\n",
        "\n",
        "\n",
        "\n",
        "<br/><br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "<br/><br/>\n",
        "\n",
        "## 6: Restaurant Ratings Over Time\n",
        "\n",
        "Let's consider various scenarios involving restaurants with multiple ratings over time.\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qJZhnCQAJDyA"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "### Question 6a\n",
        "\n",
        "The city would like to know if the state of food safety has been getting better, worse, or about average. This is a pretty vague and broad question, which you should expect as part of your future job as a data scientist! However for the ease of grading for this assignment, we are going to guide you through it and offer some specific directions to consider."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "RE4-L7zRJDyA"
      },
      "source": [
        "Let's see which restaurant has had the most extreme improvement in its scores. Let the \"swing\" of a restaurant be defined as the difference between its highest-ever and lowest-ever score. **Only consider restaurants with at least 3 scores—that is, restaurants that were rated at least 3 times.** Using whatever technique you want to use, assign `max_swing` to the name of restaurant that has the maximum swing.\n",
        "\n",
        "*Note*: The \"swing\" is of a specific business. There might be some restaurants with multiple locations; each location has its own \"swing\".\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q6a\n",
        "points: 3\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "dyNvvm72JDyA"
      },
      "outputs": [],
      "source": [
        "max_swing = ...\n",
        "max_swing"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "nJnUg-CRJDyA"
      },
      "outputs": [],
      "source": [
        "grader.check(\"q6a\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zkH5M3WwJDyA"
      },
      "source": [
        "<br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "\n",
        "### Question 6b\n",
        "\n",
        "What's the relationship between the first and second scores for the businesses with 2 inspections in a year? Do they typically improve? For simplicity, let's focus on only 2018 for this problem, using the `ins2018` DataFrame that will be created for you below.\n",
        "\n",
        "In the following cell, we create a DataFrame called `scores_pairs_by_business` indexed by `bid` (containing only businesses with exactly 2 inspections in 2018). This DataFrame contains the field score_pair consisting of the score pairs ordered chronologically: `[first_score, second_score]`.\n",
        "\n",
        "Then, make a scatter plot to display these pairs of scores. Include on the plot a reference line with slope 1."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Y9yvs1u8JDyA"
      },
      "outputs": [],
      "source": [
        "ins2018 = ins[ins['year'] == 2018]\n",
        "scores_pairs_by_business = (ins2018.sort_values('date')\n",
        "                            .loc[:, ['bid', 'score']]\n",
        "                            .groupby('bid')\n",
        "                            .filter(lambda group: len(group)==2)\n",
        "                            .groupby('bid')\n",
        "                            .agg(list)\n",
        "                            .rename(columns={'score':'score_pair'}))\n",
        "scores_pairs_by_business"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "5r8zM4c0JDyA"
      },
      "source": [
        "<!-- BEGIN QUESTION -->\n",
        "\n",
        "Now, create your scatter plot in the cell below. It does not need to look exactly the same (e.g., no grid) as the sample below, but make sure that all labels, axes and data itself are correct.\n",
        "\n",
        "![](https://github.com/TheEvergreenStateCollege/week-3-chinchillabob/blob/28d867d23f8fb2f55e6096511afe2da6e48efa04/hw/hw3/pics/7c.png?raw=1)\n",
        "\n",
        "Key pieces of syntax you'll need:\n",
        "\n",
        "`plt.scatter` plots a set of points. Use `facecolors='none'` and `edgecolors='b'` to make circle markers with blue borders. \n",
        "\n",
        "`plt.plot` for the reference line.\n",
        "\n",
        "`plt.xlabel`, `plt.ylabel`, `plt.axis`, and `plt.title`.\n",
        "\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q6b\n",
        "points: 2\n",
        "manual: True\n",
        "-->"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "_1hjmlWJJDyB"
      },
      "outputs": [],
      "source": [
        "..."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "7sQ1uWt8JDyB"
      },
      "source": [
        "<!-- END QUESTION -->\n",
        "\n",
        "<!-- BEGIN QUESTION -->\n",
        "\n",
        "<br/><br/><br/>\n",
        "\n",
        "\n",
        "---\n",
        "\n",
        "\n",
        "### Question 6c\n",
        "\n",
        "If restaurants' scores tend to improve from the first to the second inspection, what do you expect to see in the scatter plot that you made in question 6b? What do you oberve from the plot? Are your observations consistent with your expectations? \n",
        "\n",
        "Hint: What does the slope represent?\n",
        "\n",
        "<!--\n",
        "BEGIN QUESTION\n",
        "name: q6c\n",
        "points: 2\n",
        "manual: True\n",
        "-->"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sXekaaUbJDyB"
      },
      "source": [
        "_Type your answer here, replacing this text._"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "B2dbkqJfJDyB"
      },
      "source": [
        "<!-- END QUESTION -->\n",
        "\n",
        "\n",
        "\n",
        "## Summary of Inspections Data\n",
        "\n",
        "We have done a lot in this homework! Below are some examples of what we have learned about the inspections data through some cool visualizations!\n",
        "\n",
        "- We found that the records are at the inspection level and that we have inspections for multiple years.\n",
        "- We also found that many restaurants have more than one inspection a year.\n",
        "- By joining the business and inspection data, we identified the name of the restaurant with the worst rating.\n",
        "- We identified the restaurant that had the largest swing in rating over time.\n",
        "- We also examined the change of scores over time! Many restaurants are not actually doing better."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CJVGjV5sJDyB"
      },
      "source": [
        "<br/><br/><br/><br/>\n",
        "\n",
        "---\n",
        "\n",
        "<br/><br/>\n",
        "\n",
        "# 7: Open Ended Question [OPTIONAL]\n",
        "\n",
        "### Discover something interesting about the data!\n",
        "\n",
        "<br/>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9SB3l51EJDyB"
      },
      "source": [
        "Play with the data, and try to answer one question that you find interesting regarding the data. Show us how you would answer this question through exploratory data analysis. \n",
        "\n",
        "Here are some possible routes you can take in completing your analysis:\n",
        "* Construct a dataframe by computing something interesting about the data with methods such as `merge`/`groupby`/`pivot`, etc.\n",
        "* Create a visualization with the data from which you can draw a conclusion that can answer you question.\n",
        "\n",
        "Here are some possible questions you can ask about the data:\n",
        "* How do the inspection scores relate to the geolocation (latitude, longitude) of a restaurant?\n",
        "* How do all the inspection scores for each type of business change over time? \n",
        "\n",
        "**Note**: You are not limited to the questions we provided above. We actually strongly recommend you to explore something you are personally interested in knowing about the data. On topics such as how the socioeconomic background of the neighborhoods impact all the nearby restaurants, you are welcome to reference external sources (make sure to cite the sources) as well to guide your exploration.\n",
        "\n",
        "Please show your work in the cells below, feel free to use extra cells if you want.\n",
        "\n",
        "**NOTE: This question is optional. It will not be graded. Just make sure any code you use here runs properly, as it might break the autograder if it errors.**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "3KRlpe7wJDyB"
      },
      "outputs": [],
      "source": [
        "# YOUR WORK HERE"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "B0qY9SfhJDyB"
      },
      "source": [
        "## Congratulations! You have finished Homework 3! ##"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "oye0zR9gJDyB"
      },
      "source": [
        "---\n",
        "\n",
        "To double-check your work, the cell below will rerun all of the autograder tests."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "IwZoRQtuJDyB"
      },
      "outputs": [],
      "source": [
        "grader.check_all()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "9xHctQIaJDyC"
      },
      "source": [
        "## Submission\n",
        "\n",
        "Make sure you have run all cells in your notebook in order before running the cell below, so that all images/graphs appear in the output. The cell below will generate a zip file for you to submit. **Please save before exporting!**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "deletable": false,
        "editable": false,
        "id": "RvFP_ggQJDyC"
      },
      "outputs": [],
      "source": [
        "# Save your notebook first, then run this cell to export your submission.\n",
        "grader.export()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "k51mdLUkJDyC"
      },
      "source": [
        " "
      ]
    }
  ],
  "metadata": {
    "celltoolbar": "Create Assignment",
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.9.7"
    },
    "colab": {
      "name": "Copy of hw3.ipynb",
      "provenance": [],
      "collapsed_sections": [
        "Dhk2Os6CJDx6",
        "DvMcei8RJDx6",
        "RLUTAHupJDx7",
        "lPPfWoDoJDx9",
        "ijg27QZVJDx-",
        "5vJi9oidJDx-",
        "lugaPTgVJDx-",
        "8bkQIEqlJDx_",
        "u3ztRfJWJDx_",
        "KlD40FuUJDx_",
        "fc3albYIJDyA",
        "qJZhnCQAJDyA",
        "zkH5M3WwJDyA",
        "7sQ1uWt8JDyB",
        "B2dbkqJfJDyB",
        "B0qY9SfhJDyB",
        "9xHctQIaJDyC"
      ],
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}