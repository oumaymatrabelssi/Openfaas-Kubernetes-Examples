# Deploy your first Openfaas Function 
Hello everyone :wave:  ! below are the steps I used to deploy my first Openfaas function on a local Kubernetes cluster, feel free to fellow the official documentation for doing this on [Kubernetes-openfaas](https://docs.openfaas.com/deployment/kubernetes/), or just copy paste the simplified commands below that I found really useful.
N.B : 
- Before you start just make sure you have Kubectl command installed on your machine. If not please refer to this tutorial: [Kubectl](feel%20free%20to%20follow%20it!%20or%20just%20copy%20paste%20the%20simplified%20commands%20below%20that%20I%20found%20really%20useful).
- All the commands below was tested on ubuntu 18.04.

## Install Openfaas 
 
Create a folder:
    
    > mkdir openfaas
    > cd openfaas
  
Clone the faas-netes repository, `faas-netes` is an OpenFaaS provider which enables Kubernetes for [OpenFaaS](https://github.com/openfaas/faas):
 
 

    > git clone https://github.com/openfaas/faas-netes 

Install the official CLI for openfaas, faas-cli can be used to build and deploy functions to [OpenFaaS](https://github.com/openfaas/faas):

    > curl -sL https://cli.openfaas.com | sh
    > faas-cli version
 Prepare Openfaas namespaces, this command will create two namespaces: openfaas and openfaas-fn
 

    > kubectl apply -f https://raw.githubusercontent.com/openfaas/faas-netes/master/namespaces.yml
    > kubectl get namespaces
  
  Deploy Openfaas pods:
  

    > helm repo add openfaas https://openfaas.github.io/faas-netes/
    > helm repo update 
    > helm upgrade openfaas --install openfaas/openfaas --namespace openfaas  --set functionNamespace=openfaas-fn --set generateBasicAuth=true 

:exclamation: Before that we continue, run the command below and make sure that all the pods status is **running** !
 

    > kubectl get pod -n openfaas

  

Now will create basic authentication secrets for openfaas that will help us to login to faas-cli later and deploy our function:

    > cd faas-netes
    > kubectl -n openfaas create secret generic basic-auth --from-literal=basic-auth-user=admin --from-literal=basic-auth-password="admin" 
    > cd ..   

  :raised_hand:  You can put any basic auth user and password, just remeber them well cause we will need them later! 

## Configure Openfaas

To configure openfaas you need run the commands below:

    > export OPENFAAS_URL=http://YOUR_IP_ADDRESS:31112
    > faas-cli login --password admin --gateway http://YOUR_IP_ADDRESS:31112

:exclamation: If you used an other basic auth password place it here to login successfully!

At this level, it will be better if you already have a valid account [ Docker](https://hub.docker.com/)  to prevent having issues while deploying your function.
If you already have one, run this command to login:

    docker login -u DOCKER_USER -p DOCKER_PASSWORD

 
 Now we are ready to deploy our first function ! :dancer: :dancer:

## Deploy a function
In this part, and to deploy a function, we will simply use the faas-cli tools provided by openfaas to easily create and deploy functions.
First, you need to know that openfaas provide a large variety of languages to use. In this example I will use Python3.

Create a new folder for your work:

    > mkdir -p functions
    > cd functions
    > faas-cli new insert_influx --lang python3

My function will simply create an influxdb table and insert some data on it! 
So to do so, we have to prepare our python environment and install the influxdb packages:

    > cd ./faas/template/python3
    > sudo nano Dockerfile 
  Than add the line below to the Dockerfile:
  

     RUN pip install influxdb
 
 Save the file, and now finally deploy our function
 

    > faas-cli up -f ./insert_influx.yml -g http://YOUR_IP_ADDRESS:31112

Navigate to http://YOUR_IP_ADDRESS:31112 and Invoke the insert_influx function et Voilà !

 

