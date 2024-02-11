# KubeLinks

[![build docker image and release helm chart](https://github.com/kkirara/KubeLinks/actions/workflows/release.yml/badge.svg)](https://github.com/kkirara/KubeLinks/actions/workflows/release.yml)

KubeLinks provides a convenient web page with links to all urls presented in ingresses and istio gateways.

## Features
  * Showing all Istio gateway and Ingress objects with clickable URLs for HTTP and HTTPS, also merge same HTTP+HTTPS to one record
  * extra URLs to show on the page configurable in values if you want to add something useful
  * create your own URLs filters
  * customizable title
  * show/hide namespace
  
Look to [the values file](/charts/kubelinks/values.yaml)

![Screen](KubeLinksScreen.png)

## Install
  * [KubeLinks install on Kubernetes](https://kkirara.github.io/KubeLinks/)
