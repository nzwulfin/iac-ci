import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_httpd_runing(host):
    httpd = host.service("httpd")
    assert httpd.is_running


def test_index_contents(host):
    index = host.file("/var/www/html/index.html")
    assert index.exists
