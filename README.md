# Ansible Role: alertmanager

An Ansible role that installs Prometheus Alertmanager server on Ubuntu-based machines with systemd.

## Requirements

All needed packages will be installed with this role.

## Role Variables

Available main variables are listed below, along with default values:
```yaml
prometheus_alertmanager_version: 0.3.0

prometheus_alertmanager_user: prometheus
prometheus_alertmanager_group: prometheus

prometheus_alertmanager_root_dir: /opt/prometheus/alertmanager
prometheus_alertmanager_templates_files: []
prometheus_alertmanager_resolve_timeout: 5m

prometheus_alertmanager_config_flags:
  'config.file': '{{ prometheus_alertmanager_config_dir }}/alertmanager.yml'
  'storage.path': '{{ prometheus_alertmanager_db_dir }}'
  'web.listen-address': '{{ prometheus_alertmanager_listen_address }}'
```
All variables you can see [here](defaults/main.yml).

## Dependencies

This role doesn't have dependencies.

## Example Playbook
deploy.yml file:
```yaml
- hosts: alertmanager
  roles:
    - { role: alertmanager }
```
