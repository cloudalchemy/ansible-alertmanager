#!/user/bin/env python
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(host):
    dirs = [
        "/opt/alertmanager",
        "/etc/alertmanager",
        "/etc/alertmanager/templates",
        "/var/lib/alertmanager",
    ]
    files = [
        "/opt/alertmanager/alertmanager",
        "/etc/alertmanager/alertmanager.yml",
        "/etc/systemd/system/alertmanager.service"
    ]
    for directory in dirs:
        d = host.file(directory)
        assert d.is_directory
        assert d.exists
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_service(host):
    s = host.service("alertmanager")
    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    s = host.socket("tcp://127.0.0.1:9093")
    assert s.is_listening
