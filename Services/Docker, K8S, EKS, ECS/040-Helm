# Getting started with Helm

## Three Big Concepts

https://helm.sh/docs/intro/using_helm/#three-big-concepts

A **Chart** is a Helm package. It contains all of the resource definitions necessary to run an application, tool, or service inside of a Kubernetes cluster. Think of it like the Kubernetes equivalent of a Homebrew formula, an Apt dpkg, or a Yum RPM file.

A **Repository** is the place where charts can be collected and shared. It's like Perl's CPAN archive or the Fedora Package Database, but for Kubernetes packages.

A **Release** is an instance of a chart running in a Kubernetes cluster. One chart can often be installed many times into the same cluster. And each time it is installed, a new release is created. Consider a MySQL chart. If you want two databases running in your cluster, you can install that chart twice. Each one will have its own release, which will in turn have its own release name.

## Installing Helm

1. Get the latest version of Helm from https://github.com/helm/helm/releases.

1. Download the latest version and extract it.
    >wget https://get.helm.sh/helm-v3.7.1-linux-amd64.tar.gz
    >tar -zxvf helm-v3.7.1-linux-amd64.tar.gz
    >sudo mv linux-amd64/helm /usr/local/bin/helm

1. Add the Repo
    >helm repo add bitnami https://charts.bitnami.com/bitnami
    >helm repo update
    >helm search repo bitnami

1. Install MySQL onto K8S
    >helm install bitnami/mysql --generate-name

1. List all the releases.
    >helm list

1. Use the output from the above command to create a pod with MySQL Client and connect to the MySQL Server.

1. Uninstall MySQL
    >helm uninstall mysql-1612624192

# Further Reading

1. The purpose of Helm.
    - https://helm.sh/docs/topics/architecture/#the-purpose-of-helm

1. The chart file structure.
    - https://helm.sh/docs/topics/charts/#the-chart-file-structure

1. Create Your First Helm Chart
    - https://docs.bitnami.com/tutorials/create-your-first-helm-chart/

1. Customizing the chart before installing
    - https://helm.sh/docs/intro/using_helm/#customizing-the-chart-before-installing

1. Security in Helm
    - https://helm.sh/docs/topics/rbac/
