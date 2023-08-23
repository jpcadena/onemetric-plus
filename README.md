# onemetric-plus

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** Markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="assets/static/images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Onemetric plus</h3>

  <p align="center">
    Onemetric plus
    <br />
    <a href="https://github.com/jpcadena/onemetric-plus"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#testing">Testing</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#security">Security</a></li>
    <li><a href="#code-of-conduct">Code of Conduct</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->


![Project][project-screenshot]

## About the Project

This project is dedicated to developing a sophisticated analytical tool for "ABC" to dynamically monitor and forecast store credit demands. This state-of-the-art system harnesses the power of machine learning and real-time streaming to identify and analyze unusual sales peaks, seasonal outliers, unforeseen events, and store-specific outliers.

The project encompasses several pivotal stages:

- **Real-time Data Streaming**: Capturing data in real-time to transform each moment into actionable insights.
- **Data Processing**: Incorporating continuous data, refining it for subsequent stages.
- **Anomaly Detection**: Identifying unusual peaks in sales and other outliers which significantly affect the store credit demand.
- **Seasonality Analysis**: Recognizing patterns corresponding to holidays, festivals, or peak shopping periods.
- **Event Recognition**: Discerning unexpected external events such as concerts or sports that could influence credit demand.
- **Store-specific Analysis**: Zoning in on specific store behavior that can provide a wealth of localized insights.

Crafted with precision, this system offers invaluable information about successful sales initiatives, allowing "ABC" and its affiliate stores to replicate and innovate their credit management strategies. The solution emphasizes adaptability, ensuring that the stores can promptly cater to increased demand, especially during unforeseen events or peak periods.

With its strategic blend of modern technology and analytical prowess, this project is a beacon for retailers, data analysts, and organizations aiming to transform raw data into meaningful, actionable strategies. Its holistic approach reaffirms its adaptability across multiple domains, making it an epitome of innovation and efficiency in the world of data analytics.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built with

[![Python][python-shield]][python-url] [![Pandas][pandas-shield]][pandas-url] [![TensorFlow][tensorflow-shield]][tensorflow-url] [![PyTorch][pytorch-shield]][pytorch-url] [![numpy][numpy-shield]][numpy-url] [![scikit-learn][scikit-learn-shield]][scikit-learn-url] [![Pydantic][pydantic-shield]][pydantic-url] [![Pytest][pytest-shield]][pytest-url] [![isort][isort-shield]][isort-url] [![Black][black-shield]][black-url] [![Ruff][ruff-shield]][ruff-url] [![MyPy][mypy-shield]][mypy-url][![pre-commit][pre-commit-shield]][pre-commit-url] [![GitHub Actions][github-actions-shield]][github-actions-url] [![Pycharm][pycharm-shield]][pycharm-url] [![Visual Studio Code][visual-studio-code-shield]][visual-studio-code-url] [![Markdown][markdown-shield]][markdown-url] [![License: MIT][license-shield]][license-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->

## Getting started

### Prerequisites

- [Python 3.11][python-url]


1. Clone the **repository**
   ```
   git clone https://github.com/jpcadena/onemetric-plus.git
   ```
2. Change the directory to **root project**
   ```
   cd onemetric-plus
   ```
3. Install **Poetry** package manager
   ```
   pip install poetry
   ```
4. Install the project's **dependencies**
   ```
   poetry install
   ```
5. Activate the **environment**
   ```
   poetry shell
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->

## Usage

1. **Setting up environment variables:**

   If you find a `.env.sample` in the project directory, make a copy of it and rename to `.env`.

   ```
   cp .env.sample .env
   ```

2. **Configuring your credentials:**

   Open the `.env` file in a text editor and replace the placeholder values with your actual credentials.

   ```
   # .env file
   POSTGRES_USER=your_database_user
   SECRET_KEY=your_api_key
   ```

3. Execute with console
    ```
    python main.py
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Testing

1. **Running tests:**

   To run all tests, you can simply run the following command in the root directory of the project:

   ```
   pytest
   ```

2. **Running a specific test:**

   If you want to run a specific test, you can do so by specifying the file and test name. For example, the following command will only run the `test_get_users` test in the `test_main.py` file:

   ```
   pytest tests/test_main.py::test_get_users
   ```

3. **Understanding test results:**

   Pytest will provide a summary of the test results in the console. It will tell you how many tests passed and how many failed. For each failed test, Pytest will provide a detailed error message that can help you identify what went wrong.

4. **Writing new tests:**

   When you add new features to the application, you should also write corresponding test cases. Each test case should be a function that starts with the word 'test'. Inside the function, you can use `assert` statements to check that your code is working as expected. For example:

   ```python
   def test_add_user():
       user = add_user("testuser", "testpass")
       assert user.name == "testuser"
       assert user.password == "testpass"
   ```

   This function tests that the `add_user` function correctly creates a new user with the given name and password.

Remember to update your tests whenever you update your code. Maintaining a comprehensive test suite will help ensure the reliability and robustness of your application.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

[![GitHub][github-shield]][github-url]

Please read our [contributing guide](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Security

For security considerations and best practices, please refer to our [Security Guide](SECURITY.md) for a detailed guide. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CODE_OF_CONDUCT -->

## Code of Conduct

We enforce a code of conduct for all maintainers and contributors. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) to understand the expectations before making any contributions.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->

## Contact

- [![LinkedIn][LinkedIn]][linkedin-url]

- [![Outlook][Outlook]](mailto:jpcadena@espol.edu.ec?subject=[GitHub]onemetric-plus)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[project-screenshot]: assets/static/images/project.png

[//]: # "Shields"

[linkedin-shield]: https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white

[outlook-shield]: https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white

[python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54

[pydantic-shield]: https://img.shields.io/badge/Pydantic-FF43A1?style=for-the-badge&logo=pydantic&logoColor=white

[pycharm-shield]: https://img.shields.io/badge/PyCharm-21D789?style=for-the-badge&logo=pycharm&logoColor=white

[markdown-shield]: https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white

[github-shield]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white

[ruff-shield]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json

[black-shield]: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge&logo=appveyor

[mypy-shield]: https://img.shields.io/badge/mypy-checked-2A6DB2.svg?style=for-the-badge&logo=appveyor

[pytest-shield]: https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white

[visual-studio-code-shield]: https://img.shields.io/badge/Visual_Studio_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white

[poetry-shield]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/python-poetry/website/main/static/badge/v0.json

[isort-shield]: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336

[github-actions-shield]: https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white

[pre-commit-shield]: https://img.shields.io/badge/pre--commit-F7B93E?style=for-the-badge&logo=pre-commit&logoColor=white

[license-shield]: https://img.shields.io/badge/License-MIT-yellow.svg

[pandas-shield]: https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white

[numpy-shield]: https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white

[scikit-Learn-shield]: https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white

[pytorch-shield]: https://img.shields.io/badge/PyTorch-red

[tensorflow-shield]: https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white

[//]: # "URL"

[linkedin-url]: https://linkedin.com/in/juanpablocadenaaguilar

[python-url]: https://docs.python.org/3.11/

[python-url]: https://www.python.org/

[pydantic-url]: https://docs.pydantic.dev

[pycharm-url]: https://www.jetbrains.com/pycharm/

[markdown-url]: https://daringfireball.net/projects/markdown/

[github-url]: https://github.com/jpcadena/autochain-bot

[ruff-url]: https://beta.ruff.rs/docs/

[black-url]: https://github.com/psf/black

[mypy-url]: http://mypy-lang.org/

[pytest-url]: https://docs.pytest.org/en/7.2.x/

[visual-studio-code-url]: https://code.visualstudio.com/

[poetry-url]: https://python-poetry.org/

[isort-url]: https://pycqa.github.io/isort/

[github-actions-url]: https://github.com/features/actions

[pre-commit-url]: https://pre-commit.com/

[license-url]: https://opensource.org/licenses/MIT

[pandas-url]: https://pandas.pydata.org/docs/

[numpy-url]: https://numpy.org/

[scikit-learn-url]: https://scikit-learn.org/stable/

[pytorch-url]: https://pytorch.org/

[tensorflow-url]: https://www.tensorflow.org/