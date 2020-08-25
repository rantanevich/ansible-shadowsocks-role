import os
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_shadowsocks_setting_file_exists(host):
    setting = host.file('/etc/shadowsocks/settings.json')

    assert setting.exists
    assert setting.is_file
    assert oct(setting.mode) == '0o600'


def test_shadowsocks_user(host):
    user = host.user('shadowsocks')

    assert user.exists
    assert user.shell == '/sbin/nologin'


def test_shadowsocks_running_and_enabled(host):
    service = host.service('shadowsocks')

    assert service.is_running
    assert service.is_enabled


def test_shadowsocks_sockets(host):
    tcp_socket = host.socket('tcp://0.0.0.0:8388')
    udp_socket = host.socket('udp://0.0.0.0:8388')

    assert tcp_socket.is_listening
    assert udp_socket.is_listening
