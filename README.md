<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Human-dialog-warning.svg/2000px-Human-dialog-warning.svg.png" alt="alert logo" title="alert" align="right" height="60" /></p>

# Ansible Role: alertmanager

[![Build Status](https://travis-ci.org/cloudalchemy/ansible-alertmanager.svg?branch=master)](https://travis-ci.org/cloudalchemy/ansible-alertmanager)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.alertmanager-blue.svg)](https://galaxy.ansible.com/cloudalchemy/alertmanager/)
[![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-alertmanager.svg)](https://github.com/cloudalchemy/ansible-alertmanager/tags)
[![IRC](https://img.shields.io/badge/chat-on%20freenode-blue.svg)](http://webchat.freenode.net/?channels=cloudalchemy)

## Description

Deploy and manage Prometheus [alertmanager](https://github.com/prometheus/alertmanager) service using ansible.

## Requirements

- Ansible >= 2.3

It would be nice to have prometheus installed somewhere

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `alertmanager_version` | 0.14.0 | Alermanager package version |
| `alertmanager_listen_address` | '0.0.0.0:9093' | Address on which alertmanager will be listening |
| `alertmanager_external_url` | 'http://localhost:9093/' | External address on which alertmanager is available. Useful when behind reverse proxy. Ex. example.org/alertmanager |
| `alertmanager_root_dir` | /opt/alertmanager | Path to directory with alertmanager and amtool binaries |
| `alertmanager_config_dir` | /etc/alertmanager | Path to directory with alertmanager configuration |
| `alertmanager_db_dir` | /var/lib/alertmanager | Path to directory with alertmanager database |
| `alertmanager_config_file` | 'alertmanager.yml.j2' | Variable used to provide custom alertmanager configuration file in form of ansible template |
| `alertmanager_config_flags_extra` | {} | Additional configuration flags passed to prometheus binary at startup |
| `alertmanager_resolve_timeout` | 3m | Time after which an alert is declared resolved |
| `alertmanager_smtp` | {} | SMTP (email) configuration |
| `alertmanager_slack_api_url` | "" | Slack webhook url |
| `alertmanager_pagerduty_url` | "" | Pagerduty webhook url |
| `alertmanager_opsgenie_api_host` | "" | Opsgenie webhook url |
| `alertmanager_hipchat_url` | "" | Hipchat webhook url |
| `alertmanager_hipchat_auth_token` | "" | Hipchat authentication token |
| `alertmanager_mesh` | {} | HA mesh network configuration |
| `alertmanager_receivers` | [] | A list of notification receivers. Configuration same as in [official docs](https://prometheus.io/docs/alerting/configuration/#<receiver>) |
| `alertmanager_inhibit_rules` | [] | List of inhibition rules. Same as in [official docs](https://prometheus.io/docs/alerting/configuration/#inhibit_rule) |
| `alertmanager_route` | {} | Alert routing. More in [official docs](https://prometheus.io/docs/alerting/configuration/#<route>) |
| `alertmanager_child_routes` | [] | List of child routes. |

## Example

### Playbook

```yaml
- hosts: all
  roles:
    - cloudalchemy.alertmanager
```

### Demo site

We provide demo site for full monitoring solution based on prometheus and grafana. Repository with code and links to running instances is [available on github](https://github.com/cloudalchemy/demo-site) and site is hosted on [DigitalOcean](https://digitalocean.com).

## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v2.x). You will have to install Docker on your system. See Get started for a Docker package suitable to for your system.
All packages you need to can be specified in one line:
```sh
pip install ansible 'ansible-lint>=3.4.15' 'molecule>2.13.0' docker 'testinfra>=1.7.0' jmespath
```
This should be similar to one listed in `.travis.yml` file in `install` section.
After installing test suit you can run test by running
```sh
molecule test --all
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/latest/).

## Travis CI

Combining molecule and travis CI allows us to test how new PRs will behave when used with multiple ansible versions and multiple operating systems. This also allows use to create test scenarios for different role configurations. As a result we have a quite large test matrix (42 parallel role executions in case of [ansible-prometheus](https://github.com/cloudalchemy/ansible-prometheus)) which will take more time than local testing, so please be patient.

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
