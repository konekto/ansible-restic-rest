import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_repo_folder(host):
    f = host.file('/var/backups/projecta')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_repo_htpasswd(host):
    f = host.file('/var/backups/projecta/.htpasswd')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
