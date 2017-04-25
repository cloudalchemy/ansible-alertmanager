# Ansible Role: alertmanager

An Ansible role that installs Prometheus Alertmanager server on Ubuntu-based machines with systemd.

## Requirements

All needed packages will be installed with this role.

## Role Variables

Available main variables are listed below, along with default values:
```yaml
alertmanager_version: 0.5.1
alertmanager_user: prometheus
alertmanager_group: prometheus

alertmanager_release_name: "alertmanager-{{ alertmanager_version }}.linux-amd64"

alertmanager_root_dir: /opt/prometheus/alertmanager
alertmanager_dist_dir: "{{ alertmanager_root_dir }}/dist"
alertmanager_bin_dir: "{{ alertmanager_root_dir }}/current"

alertmanager_config_dir: /etc/prometheus/alertmanager
alertmanager_templates_dir: "{{ alertmanager_config_dir }}/templates"
alertmanager_pid_path: /var/run/prometheus-alertmanager.pid
alertmanager_db_dir: /var/lib/prometheus/alertmanager
alertmanager_log_dir: /var/log/prometheus

alertmanager_listen_address: ':9093'
alertmanager_external_url: 'http://localhost:9093/'

alertmanager_templates_files: []

alertmanager_resolve_timeout: 5m
alertmanager_config_flags:
  'config.file': '{{ alertmanager_config_dir }}/alertmanager.yml'
  'storage.path': '{{ alertmanager_db_dir }}'
  'web.listen-address': '{{ alertmanager_listen_address }}'
  'web.external-url': '{{ alertmanager_external_url }}'```
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
