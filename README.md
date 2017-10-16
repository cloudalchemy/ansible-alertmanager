<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Human-dialog-warning.svg/2000px-Human-dialog-warning.svg.png" alt="alert logo" title="alert" align="right" height="60" /></p>

Ansible Role: alertmanager
==========================

[![Build Status](https://travis-ci.org/SoInteractive/ansible-alertmanager.svg?branch=master)](https://travis-ci.org/SoInteractive/ansible-alertmanager) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-SoInteractive.alertmanager-blue.svg)](https://galaxy.ansible.com/SoInteractive/alertmanager/) [![GitHub tag](https://img.shields.io/github/tag/sointeractive/ansible-alertmanager.svg)](https://github.com/SoInteractive/ansible-alertmanager/tags) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Deploy Prometheus Alertmanager service

Requirements
------------

It would be nice to have prometheus installed somewhere

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.alertmanager
```

Role Variables
--------------

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.
