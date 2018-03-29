#!/user/bin/env python
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(host):
    dirs = [
        "/etc/alertmanager",
        "/etc/alertmanager/templates",
        "/var/lib/alertmanager"
    ]
    files = [
        "/usr/local/bin/alertmanager",
        "/usr/local/bin/amtool",
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
    sockets = [
      "tcp://127.0.0.1:9093",
      "tcp://127.0.0.1:6783"
    ]
    for s in sockets:
        assert host.socket(s).is_listening
