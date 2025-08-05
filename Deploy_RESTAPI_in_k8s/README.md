# 🚀 CRUD FastAPI - Kubernetes Deployment Guide

Deploy the **CRUD FastAPI** application and its dependencies on Kubernetes using:

- `ConfigMaps` for environment variables  
- `External Secrets Operator (ESO)` for managing secrets  
- **HashiCorp Vault** as the secrets backend  

---

## ✅ Prerequisites

* Minikube running (`minikube start`)
* `kubectl`, `helm`, and `vault` CLI installed and configured
* Source code cloned locally

---

## 🧱 1. Clone the Repository

```bash

cd Deploy_RESTAPI_in_k8s/manifests
```

---

## 🗂️ 2. Create Required Namespaces

Create the namespaces required for deployment:

```bash
kubectl create namespace crud-fastapi
kubectl create namespace vault
kubectl create namespace external-secrets
```

---

## 🔐 3. Deploy HashiCorp Vault on Minikube

### a) Add HashiCorp Helm repository and update

```bash
helm repo add hashicorp https://helm.releases.hashicorp.com
helm repo update
```

### b) Install Vault with custom values

```bash
helm install vault hashicorp/vault -n vault -f vault-values.yaml
```

### c) Verify Vault pod status

```bash
kubectl get pods -n vault
```

Look for the pod named `vault-0` in `Running` state.

---

## 🕵️‍♂️ 4. Access Vault UI/CLI (Optional)

Port-forward Vault service:

```bash
kubectl port-forward service/vault 8200:8200 -n vault
```

* Access Vault UI: [http://localhost:8200](http://localhost:8200)


Unseal Vault.

---

## 🔧 5. Vault + Kubernetes Auth Setup

### a) Login to Vault CLI

```bash
vault login
```

### b) Enable Kubernetes authentication method

```bash
vault auth enable kubernetes
```

### c) Configure Kubernetes auth method

```bash
vault write auth/kubernetes/config \
  token_reviewer_jwt=@/var/run/secrets/kubernetes.io/serviceaccount/token \
  kubernetes_host="https://kubernetes.default.svc" \
  kubernetes_ca_cert=@/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
```

### d) Create Vault policy `/tmp/eso-policy.hcl`

```hcl
path "secret/data/*" {
  capabilities = ["read"]
}
```

Apply the policy:

```bash
vault policy write eso-policy /tmp/eso-policy.hcl
```

### e) Create Kubernetes role for External Secrets Operator

```bash
vault write auth/kubernetes/role/eso \
  bound_service_account_names=external-secrets \
  bound_service_account_namespaces=external-secrets \
  policies=eso-policy \
  ttl=24h
```

---

## 🔁 6. Deploy External Secrets Operator (ESO)

```bash
helm repo add external-secrets https://charts.external-secrets.io
helm repo update

helm install external-secrets external-secrets/external-secrets \
  --namespace external-secrets \
  --create-namespace \
  --set affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[0].matchExpressions[0].key=type \
  --set affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[0].matchExpressions[0].operator=In \
  --set affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[0].matchExpressions[0].values[0]=dependent_services \
  --set installCRDs=true
```

---

## 🔗 7. Deploy ExternalSecret Resource

```bash
kubectl apply -f manifests/eso/external-secret.yml
```

---

## 🗃️ 8. Deploy PostgreSQL Database

```bash
kubectl apply -f manifests/database.yml
```

This manifest includes:

* Persistent volume claims
* Init container for DB migrations
* Secrets injected by ESO
* Internal service exposing the database

---

## 🚀 9. Deploy CRUD FastAPI Application

```bash
kubectl apply -f manifests/application.yml
```

This manifest includes:

* Namespace
* ConfigMap for environment variables
* Secrets injected by ESO
* Init container to ensure DB readiness
* Service exposing the REST API

---

## ✅ 10. Verify Deployment & Test API

Check pod statuses:

```bash
kubectl get pods -n crud-fastapi
```

Port-forward the application service:

```bash
kubectl port-forward svc/crud-fastapi-service 8000:80 -n crud-fastapi
```

Test API health endpoint:

```bash
curl http://localhost:8000/healthcheck/

```

Expect
{"status":"ok","message":"API is healthy!"}

---

## 🧹 Cleanup

```bash
kubectl delete namespace crud-fastapi
helm uninstall vault -n vault
helm uninstall external-secrets -n external-secrets
kubectl delete namespace vault external-secrets
```

---

## 📚 References

* [HashiCorp Vault Helm Chart](https://github.com/hashicorp/vault-helm)
* [External Secrets Operator](https://external-secrets.io/)
* [Kubernetes Documentation](https://kubernetes.io/docs/home/)

---
