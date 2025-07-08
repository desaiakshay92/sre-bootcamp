# 🧱 3-Node Kubernetes Cluster with Minikube

This guide walks you through setting up a 3-node Kubernetes cluster using Minikube and assigning custom labels to each node for role-based scheduling.

---

## 📌 Prerequisites

Ensure the following tools are installed:

- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- A system with virtualization support (e.g., VirtualBox, Docker, Hyper-V)

---

## 🚀 Cluster Setup

### 1. Start the Minikube Cluster with 3 Nodes

- [Multinode-Cluster](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)

```bash
minikube start --nodes=3 -p multinode-cluster


2. Verify the Nodes

kubectl get nodes -o wide


3. 🏷️ Add Node Labels
Label each node based on its intended role:

kubectl label node multinode-cluster type=application
kubectl label node multinode-cluster-m02 type=database
kubectl label node multinode-cluster-m03 type=dependent_services

4. Confirm Label

kubectl get nodes --show-labels
