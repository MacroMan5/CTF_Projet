#!/bin/bash
/usr/sbin/iptables-restore < /etc/iptables/rules.v4
/usr/sbin/sshd -D