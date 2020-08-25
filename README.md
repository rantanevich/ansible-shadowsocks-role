Ansible Role: Shadowsocks
=========

This ansible role installs shadowsocks-libev with v2ray-plugin.

Requirements
------------

None.

Role Variables
--------------

| Variable                 | Default       | Description |
| ------------------------ | ------------- | ----------- |
| `shadowsocks_install_path` | `/usr/local`    | path where software will be installed |
| `shadowsocks_temp_path`    | `/tmp`          | path where source code will be extracted during installation |`
| `shadowsocks_server_port`  | `8388`          | on which port it'll be worked  |
| `shadowsocks_password`     | `"secret"`      | password used for encryption |
| `shadowsocks_timeout`      | `300`           | timeout in seconds |
| `shadowsocks_method`       | `"aes-256-ctr"` | encryption method |
| `shadowsocks_nameserver`   | `"1.1.1.1"`     | dns server to use |
| `shadowsocks_service_user` | `shadowsocks`   | system user for run service |

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      become: yes

      roles:
        - rantanevich.shadowsocks

License
-------

MIT
