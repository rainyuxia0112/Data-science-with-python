# How to connect Spark with AWS S3
*  This readme is telling us how to connect Spark with AWS S3
## Get Started

- Preparation

* This duty needs to be done in python3.X environment and Java 8 

- Installation

```shell
source activate new_env # activate a new env
pip install pyspark 
```
* note: we need to install [java8 JDK](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) and [java](https://www.java.com/en/download/)

* note: after installing pyspark, we need to add 3 more jars in `pyspark/jars` file: `aws-java-sdk-1.7.4.jars`, `hadoop-aws-2.7.3.jars`, `jets3t-0.9.4.jars` [jars dowload](https://mvnrepository.com/). jars file are all in this website and take care of the version.

* note: if the java version is not version 8, please do the following things:

```shell
/usr/libexec/java_home -V  
```
* check the java version first, if there is no version 8, please download one first.
```shell
export JAVA_HOME=`/usr/libexec/java_home -v 1.8.0_121` 
# the version should be the version you download
* ```
OR
```shell
export JAVA_HOME=`/usr/libexec/java_home -v 1.8`
```
* after that, we will have:
```shell
java version "1.8.0_121"
Java(TM) SE Runtime Environment (build 1.8.0_121-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.121-b13, mixed mode)
```
* check the version again
```shell
java -version
```
- Connection to S3

see in html or jupiter notebook