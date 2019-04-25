# cloudformation-to-troposphere-convertor

[![codecov](https://codecov.io/gh/pyghassen/cloudformation-to-troposphere-convertor/branch/master/graph/badge.svg)](https://codecov.io/gh/pyghassen/cloudformation-to-troposphere-convertor)
[![Build Status](https://travis-ci.org/pyghassen/cloudformation-to-troposphere-convertor.svg?branch=master)](https://travis-ci.org/pyghassen/cloudformation-to-troposphere-convertor)

Purpose
========
A servrice that converts cloudformation file it to troposphere.

How to start
===============

0. Prerequisites:

   In order to run this project please make sure that the following packages are installed:

       - git
       - docker
       - docker-compose


 1. Clone the repository:

     `git clone git@github.com:pyghassen/cloudformation-to-troposphere-convertor.git`

  2. Run the tests:

     `docker-compose run test`
  
 3. Run the python linter:

     `docker-compose run lint`

 4. Run the convertor:

     ```bash
     docker-compose run convertor make run input=cloudformation_template_examples/template_experimental.json output=troposhphere_generated_files/toposhphere_template_experimental.json
    ```

 
