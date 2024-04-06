<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">TECHTRENDS_UDACITY</h1>
</p>
<p align="center">
    <em><code>► INSERT-TEXT-HERE</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/syarahmadi/Techtrends_Udacity?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/syarahmadi/Techtrends_Udacity?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/syarahmadi/Techtrends_Udacity?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/syarahmadi/Techtrends_Udacity?style=default&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)
</details>
<hr>

##  Overview

<code>► INSERT-TEXT-HERE</code>

---

##  Features

<code>► INSERT-TEXT-HERE</code>

---

##  Repository Structure

```sh
└── Techtrends_Udacity/
    ├── .github
    │   └── workflows
    ├── Dockerfile
    ├── README.md
    ├── Vagrantfile
    ├── argocd
    │   ├── README.md
    │   ├── argocd-server-nodeport.yaml
    │   ├── helm-techtrends-prod.yaml
    │   └── helm-techtrends-staging.yaml
    ├── docker_commands
    ├── helm
    │   ├── Chart.yaml
    │   ├── README.md
    │   ├── templates
    │   ├── values-prod.yaml
    │   ├── values-staging.yaml
    │   └── values.yaml
    ├── kubernetes
    │   ├── README.md
    │   ├── deploy.yaml
    │   ├── namespace.yaml
    │   └── service.yaml
    ├── screenshots
    │   ├── README.md
    │   ├── app.png
    │   ├── argocd-ui.png
    │   ├── ci-dockerhub.png
    │   ├── ci-github-actions.png
    │   ├── doker_run_local.png
    │   ├── healthz.png
    │   ├── k8s-nodes.png
    │   └── metrics.png
    └── techtrends
        ├── .DS_Store
        ├── .Dockerfile.swp
        ├── README.md
        ├── __init__.py
        ├── app.log
        ├── app.py
        ├── database.db
        ├── init_db.py
        ├── requirements.txt
        ├── schema.sql
        ├── static
        └── templates
```

---

##  Modules

<details closed><summary>.</summary>

| File                                                                                            | Summary                         |
| ---                                                                                             | ---                             |
| [Dockerfile](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/Dockerfile)           | <code>► INSERT-TEXT-HERE</code> |
| [docker_commands](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/docker_commands) | <code>► INSERT-TEXT-HERE</code> |
| [Vagrantfile](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/Vagrantfile)         | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>argocd</summary>

| File                                                                                                                             | Summary                         |
| ---                                                                                                                              | ---                             |
| [argocd-server-nodeport.yaml](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/argocd/argocd-server-nodeport.yaml)   | <code>► INSERT-TEXT-HERE</code> |
| [helm-techtrends-prod.yaml](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/argocd/helm-techtrends-prod.yaml)       | <code>► INSERT-TEXT-HERE</code> |
| [helm-techtrends-staging.yaml](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/argocd/helm-techtrends-staging.yaml) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>kubernetes</summary>

| File                                                                                                     | Summary                         |
| ---                                                                                                      | ---                             |
| [deploy.yaml](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/kubernetes/deploy.yaml)       | <code>► INSERT-TEXT-HERE</code> |
| [service.yaml](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/kubernetes/service.yaml)     | <code>► INSERT-TEXT-HERE</code> |
| [namespace.yaml](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/kubernetes/namespace.yaml) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>helm</summary>

| File                                                                                                         | Summary                         |
| ---                                                                                                          | ---                             |
| [Chart.yaml](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/helm/Chart.yaml)                   | <code>► INSERT-TEXT-HERE</code> |
| [values-staging.yaml](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/helm/values-staging.yaml) | <code>► INSERT-TEXT-HERE</code> |
| [values.yaml](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/helm/values.yaml)                 | <code>► INSERT-TEXT-HERE</code> |
| [values-prod.yaml](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/helm/values-prod.yaml)       | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>techtrends</summary>

| File                                                                                                         | Summary                         |
| ---                                                                                                          | ---                             |
| [requirements.txt](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/techtrends/requirements.txt) | <code>► INSERT-TEXT-HERE</code> |
| [schema.sql](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/techtrends/schema.sql)             | <code>► INSERT-TEXT-HERE</code> |
| [app.py](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/techtrends/app.py)                     | <code>► INSERT-TEXT-HERE</code> |
| [init_db.py](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/techtrends/init_db.py)             | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                                                | Summary                         |
| ---                                                                                                                                 | ---                             |
| [techtrends-dockerhub.yml](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/.github/workflows/techtrends-dockerhub.yml) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>helm.templates</summary>

| File                                                                                                         | Summary                         |
| ---                                                                                                          | ---                             |
| [deploy.yaml](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/helm/templates/deploy.yaml)       | <code>► INSERT-TEXT-HERE</code> |
| [service.yaml](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/helm/templates/service.yaml)     | <code>► INSERT-TEXT-HERE</code> |
| [namespace.yaml](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/helm/templates/namespace.yaml) | <code>► INSERT-TEXT-HERE</code> |

</details>

<details closed><summary>techtrends.templates</summary>

| File                                                                                                         | Summary                         |
| ---                                                                                                          | ---                             |
| [post.html](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/techtrends/templates/post.html)     | <code>► INSERT-TEXT-HERE</code> |
| [index.html](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/techtrends/templates/index.html)   | <code>► INSERT-TEXT-HERE</code> |
| [about.html](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/techtrends/templates/about.html)   | <code>► INSERT-TEXT-HERE</code> |
| [base.html](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/techtrends/templates/base.html)     | <code>► INSERT-TEXT-HERE</code> |
| [create.html](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/techtrends/templates/create.html) | <code>► INSERT-TEXT-HERE</code> |
| [404.html](https://github.com/syarahmadi/Techtrends_Udacity/blob/master/techtrends/templates/404.html)       | <code>► INSERT-TEXT-HERE</code> |

</details>

---

##  Getting Started

**System Requirements:**

* **YAML**: `version x.y.z`

###  Installation

<h4>From <code>source</code></h4>

> 1. Clone the Techtrends_Udacity repository:
>
> ```console
> $ git clone https://github.com/syarahmadi/Techtrends_Udacity
> ```
>
> 2. Change to the project directory:
> ```console
> $ cd Techtrends_Udacity
> ```
>
> 3. Install the dependencies:
> ```console
> $ > INSERT-INSTALL-COMMANDS
> ```

###  Usage

<h4>From <code>source</code></h4>

> Run Techtrends_Udacity using the command below:
> ```console
> $ > INSERT-RUN-COMMANDS
> ```

###  Tests

> Run the test suite using the command below:
> ```console
> $ > INSERT-TEST-COMMANDS
> ```

---

##  Project Roadmap

- [X] `► INSERT-TASK-1`
- [ ] `► INSERT-TASK-2`
- [ ] `► ...`

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/syarahmadi/Techtrends_Udacity/issues)**: Submit bugs found or log feature requests for the `Techtrends_Udacity` project.
- **[Submit Pull Requests](https://github.com/syarahmadi/Techtrends_Udacity/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/syarahmadi/Techtrends_Udacity/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/syarahmadi/Techtrends_Udacity
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com{/syarahmadi/Techtrends_Udacity/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=syarahmadi/Techtrends_Udacity">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-overview)

---
