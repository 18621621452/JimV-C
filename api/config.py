#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Blueprint, g
from flask import request
import jimit as ji
import json

from models import Config
from models import Rules
from models import Utils


__author__ = 'James Iter'
__date__ = '2017/3/21'
__contact__ = 'james.iter.cn@gmail.com'
__copyright__ = '(c) 2017 by James Iter.'


blueprint = Blueprint(
    'api_config',
    __name__,
    url_prefix='/api/config'
)


@Utils.dumps2response
def r_create():

    args_rules = [
        Rules.JIMV_EDITION.value,
        Rules.STORAGE_MODE.value,
        Rules.DFS_VOLUME.value,
        Rules.STORAGE_PATH.value,
        Rules.VM_NETWORK.value,
        Rules.VM_MANAGE_NETWORK.value,
        Rules.START_IP.value,
        Rules.END_IP.value,
        Rules.START_VNC_PORT.value,
        Rules.NETMASK.value,
        Rules.GATEWAY.value,
        Rules.DNS1.value,
        Rules.DNS2.value
    ]

    config = Config()
    config.id = 1
    config.jimv_edition = int(request.json.get('jimv_edition', 0))
    config.storage_mode = int(request.json.get('storage_mode', 0))
    config.dfs_volume = request.json.get('dfs_volume', '')
    config.storage_path = request.json.get('storage_path')
    config.vm_network = request.json.get('vm_network')
    config.vm_manage_network = request.json.get('vm_manage_network')
    config.start_ip = request.json.get('start_ip')
    config.end_ip = request.json.get('end_ip')
    config.start_vnc_port = int(request.json.get('start_vnc_port'))
    config.netmask = request.json.get('netmask')
    config.gateway = request.json.get('gateway')
    config.dns1 = request.json.get('dns1')
    config.dns2 = request.json.get('dns2')

    try:
        ji.Check.previewing(args_rules, config.__dict__)

        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)

        if config.exist():
            ret['state'] = ji.Common.exchange_state(40901)
            return ret

        config.check_ip()
        config.generate_available_ip2set()
        config.generate_available_vnc_port()
        config.create()
        config.update_global_config()

        config.id = 1
        config.get()
        ret['data'] = config.__dict__
        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
def r_update():

    config = Config()

    args_rules = [
    ]

    if 'jimv_edition' in request.json:
        args_rules.append(
            Rules.JIMV_EDITION.value,
        )

    if 'storage_mode' in request.json:
        args_rules.append(
            Rules.STORAGE_MODE.value,
        )

    if 'dfs_volume' in request.json:
        args_rules.append(
            Rules.DFS_VOLUME.value,
        )

    if 'storage_path' in request.json:
        args_rules.append(
            Rules.STORAGE_PATH.value,
        )

    if 'vm_network' in request.json:
        args_rules.append(
            Rules.VM_NETWORK.value,
        )

    if 'vm_manage_network' in request.json:
        args_rules.append(
            Rules.VM_MANAGE_NETWORK.value,
        )

    if 'start_ip' in request.json:
        args_rules.append(
            Rules.START_IP.value,
        )

    if 'end_ip' in request.json:
        args_rules.append(
            Rules.END_IP.value,
        )

    if 'start_vnc_port' in request.json:
        args_rules.append(
            Rules.START_VNC_PORT.value,
        )

    if 'netmask' in request.json:
        args_rules.append(
            Rules.NETMASK.value,
        )

    if 'gateway' in request.json:
        args_rules.append(
            Rules.GATEWAY.value,
        )

    if 'dns1' in request.json:
        args_rules.append(
            Rules.DNS1.value,
        )

    if 'dns2' in request.json:
        args_rules.append(
            Rules.DNS2.value,
        )

    if args_rules.__len__() < 1:
        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        return ret

    try:
        config.id = 1
        ji.Check.previewing(args_rules, request.json)
        config.get()

        config.jimv_edition = request.json.get('jimv_edition', config.jimv_edition)
        config.storage_mode = request.json.get('storage_mode', config.storage_mode)
        config.dfs_volume = request.json.get('dfs_volume', config.dfs_volume)
        config.storage_path = request.json.get('storage_path', config.storage_path)
        config.vm_network = request.json.get('vm_network', config.vm_network)
        config.vm_manage_network = request.json.get('vm_manage_network', config.vm_manage_network)
        config.start_ip = request.json.get('start_ip', config.start_ip)
        config.end_ip = request.json.get('end_ip', config.end_ip)
        config.start_vnc_port = request.json.get('start_vnc_port', config.start_vnc_port)
        config.netmask = request.json.get('netmask', config.netmask)
        config.gateway = request.json.get('gateway', config.gateway)
        config.dns1 = request.json.get('dns1', config.dns1)
        config.dns2 = request.json.get('dns2', config.dns2)

        config.check_ip()
        config.generate_available_ip2set()
        config.generate_available_vnc_port()
        config.update()
        config.update_global_config()

        config.get()

        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = config.__dict__
        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)


@Utils.dumps2response
def r_get():

    config = Config()

    try:
        config.id = 1
        config.get()

        ret = dict()
        ret['state'] = ji.Common.exchange_state(20000)
        ret['data'] = config.__dict__
        return ret
    except ji.PreviewingError, e:
        return json.loads(e.message)

