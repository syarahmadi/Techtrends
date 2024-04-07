<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">TECHTRENDS</h1>
</p>
<p align="center">
    <em><code>► A pet project to find and showcase techtrends ...</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/syarahmadi/Techtrends?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/syarahmadi/Techtrends?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/syarahmadi/Techtrends?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/syarahmadi/Techtrends?style=default&color=0080ff" alt="repo-language-count">
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

<code>► To be completed ...</code>


---

##  Repository Structure

```sh
└── Techtrends/
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

| File                                                                                    | Summary                         |
| ---                                                                                     | ---                             |
| [Dockerfile](https://github.com/syarahmadi/Techtrends/blob/master/Dockerfile)           | <code>► To be completed ...</code> |
| [docker_commands](https://github.com/syarahmadi/Techtrends/blob/master/docker_commands) | <code>► To be completed ...</code> |
| [Vagrantfile](https://github.com/syarahmadi/Techtrends/blob/master/Vagrantfile)         | <code>► To be completed ...</code> |

</details>

<details closed><summary>argocd</summary>

| File                                                                                                                     | Summary                         |
| ---                                                                                                                      | ---                             |
| [argocd-server-nodeport.yaml](https://github.com/syarahmadi/Techtrends/blob/master/argocd/argocd-server-nodeport.yaml)   | <code>► To be completed ...</code> |
| [helm-techtrends-prod.yaml](https://github.com/syarahmadi/Techtrends/blob/master/argocd/helm-techtrends-prod.yaml)       | <code>► To be completed ...</code> |
| [helm-techtrends-staging.yaml](https://github.com/syarahmadi/Techtrends/blob/master/argocd/helm-techtrends-staging.yaml) | <code>► To be completed ...</code> |

</details>

<details closed><summary>kubernetes</summary>

| File                                                                                             | Summary                         |
| ---                                                                                              | ---                             |
| [deploy.yaml](https://github.com/syarahmadi/Techtrends/blob/master/kubernetes/deploy.yaml)       | <code>► To be completed ...</code> |
| [service.yaml](https://github.com/syarahmadi/Techtrends/blob/master/kubernetes/service.yaml)     | <code>► To be completed ...</code> |
| [namespace.yaml](https://github.com/syarahmadi/Techtrends/blob/master/kubernetes/namespace.yaml) | <code>► To be completed ...</code> |

</details>

<details closed><summary>helm</summary>

| File                                                                                                 | Summary                         |
| ---                                                                                                  | ---                             |
| [Chart.yaml](https://github.com/syarahmadi/Techtrends/blob/master/helm/Chart.yaml)                   | <code>► To be completed ...</code> |
| [values-staging.yaml](https://github.com/syarahmadi/Techtrends/blob/master/helm/values-staging.yaml) | <code>► To be completed ...</code> |
| [values.yaml](https://github.com/syarahmadi/Techtrends/blob/master/helm/values.yaml)                 | <code>► To be completed ...</code> |
| [values-prod.yaml](https://github.com/syarahmadi/Techtrends/blob/master/helm/values-prod.yaml)       | <code>► To be completed ...</code> |

</details>

<details closed><summary>techtrends</summary>

| File                                                                                                 | Summary                         |
| ---                                                                                                  | ---                             |
| [requirements.txt](https://github.com/syarahmadi/Techtrends/blob/master/techtrends/requirements.txt) | <code>► To be completed ...</code> |
| [schema.sql](https://github.com/syarahmadi/Techtrends/blob/master/techtrends/schema.sql)             | <code>► To be completed ...</code> |
| [app.py](https://github.com/syarahmadi/Techtrends/blob/master/techtrends/app.py)                     | <code>► To be completed ...</code> |
| [init_db.py](https://github.com/syarahmadi/Techtrends/blob/master/techtrends/init_db.py)             | <code>► To be completed ...</code> |

</details>

<details closed><summary>.github.workflows</summary>

| File                                                                                                                        | Summary                         |
| ---                                                                                                                         | ---                             |
| [techtrends-dockerhub.yml](https://github.com/syarahmadi/Techtrends/blob/master/.github/workflows/techtrends-dockerhub.yml) | <code>► To be completed ...</code> |

</details>

<details closed><summary>helm.templates</summary>

| File                                                                                                 | Summary                         |
| ---                                                                                                  | ---                             |
| [deploy.yaml](https://github.com/syarahmadi/Techtrends/blob/master/helm/templates/deploy.yaml)       | <code>► To be completed ...</code> |
| [service.yaml](https://github.com/syarahmadi/Techtrends/blob/master/helm/templates/service.yaml)     | <code>► To be completed ...</code> |
| [namespace.yaml](https://github.com/syarahmadi/Techtrends/blob/master/helm/templates/namespace.yaml) | <code>► To be completed ...</code> |

</details>

<details closed><summary>techtrends.templates</summary>

| File                                                                                                 | Summary                         |
| ---                                                                                                  | ---                             |
| [post.html](https://github.com/syarahmadi/Techtrends/blob/master/techtrends/templates/post.html)     | <code>► To be completed ...</code> |
| [index.html](https://github.com/syarahmadi/Techtrends/blob/master/techtrends/templates/index.html)   | <code>► To be completed ...</code> |
| [about.html](https://github.com/syarahmadi/Techtrends/blob/master/techtrends/templates/about.html)   | <code>► To be completed ...</code> |
| [base.html](https://github.com/syarahmadi/Techtrends/blob/master/techtrends/templates/base.html)     | <code>► To be completed ...</code> |
| [create.html](https://github.com/syarahmadi/Techtrends/blob/master/techtrends/templates/create.html) | <code>► To be completed ...</code> |
| [404.html](https://github.com/syarahmadi/Techtrends/blob/master/techtrends/templates/404.html)       | <code>► To be completed ...</code> |

</details>


---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/syarahmadi/Techtrends/issues)**: Submit bugs found or log feature requests for the `Techtrends` project.
- **[Submit Pull Requests](https://github.com/syarahmadi/Techtrends/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/syarahmadi/Techtrends/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/syarahmadi/Techtrends
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
   <a href="https://github.com{/syarahmadi/Techtrends/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=syarahmadi/Techtrends">
   </a>
</p>
</details>

---

##  License

This project is protected under the [LICENSE](https://github.com/syarahmadi/Techtrends/blob/main/LICENSE) License.

