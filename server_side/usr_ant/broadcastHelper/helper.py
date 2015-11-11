from ..models import *
import json
import socket

def get_all_groups():
    return PeerGroup.objects.all()


def get_all_peers():
    peers = Peers.objects.all()
    return peers

def get_all_groups_for_peer(peer):
    groups = peer.group_set.all()
    return groups

def get_all_peers_in_group(group):
    peers = group.peers.all()
    return peers

def get_data(group):
    peernamelist = {}

    peers = group.peers.all()
    for eachpeer in peers:
        peernamelist[eachpeer.user.username] = (eachpeer.ip_addr, eachpeer.port)

    print peernamelist
    return peernamelist


def begin_broadcast():
    groups = get_all_groups()
    '''If there is no group exist do nothing'''
    if not groups:
        return

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for eachgroup in groups:
        peers = get_all_peers_in_group(eachgroup)
        '''continue to the next group if there is no peer'''
        if not peers:
            continue
        data = get_data(eachgroup)
        msg = json.dumps(data)

        for eachpeer in peers:
            udp_ip = eachpeer.ip_addr
            udp_port = eachpeer.port
            try:
                sock.sendto('Hello This is the server', (udp_ip, udp_port))
                sock.sendto(msg, (udp_ip, udp_port))
            except:
                print"sock error"
                continue





def debug_func():
    groups = PeerGroup.objects.all()
    peernamelist = {}
    peernamelist = get_data(groups)
    return peernamelist
