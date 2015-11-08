from ..models import *


'''
This function log in the peer object to the group object
'''
def login_peer_to_group(peer, group):
    group.peers.add(peer)
    group.save()



'''
This function log out the peer from the group object
'''
def logout_peer_from_group(peer, group):
    group.peers.remove(peer)
    group.save()



'''
This function log in the peer object to the group with the name of groupname
peer will not be logged in to the group if the name is empty
'''


def login_peer_to_group_with_name(peer, groupname):
    try:
        if(len(groupname)):
            group = PeerGroup.objects.get(groupname = groupname)
    except:
        group = PeerGroup(groupname = groupname);
        group.save()

    group.peers.add(peer)
    group.save()


'''
This function generates the json form to return to the new user
Input: groupname filled by the user
        this should be a valid groupname. e.g. exists in the database

Return: A json form containing the information of all user if groupname is
        not specified
        A json form containing the information of the user within the group
        if groupname is specified

'''
def get_response_for_new_user(groupname):
    peernamelist = {}
    if(len(groupname)):
        group = PeerGroup.objects.get(groupname = groupname)
        plist = group.peers.all()
    else:
        plist = Peer.peers.all()

    for individual in plist:
        print individual.user.username
        print individual.url
        peernamelist[individual.user.username] = individual.url
    print plist
    print peernamelist
    return peernamelist

'''
This function generates the json form to return to the old user
Input: peer object

Return: A json form containing the information of all the members of all the
        groups this peer is in
'''
def get_response_for_old_user(peer):

    peernamelist = {}
    #get all the group that contains the peer
    groups = peer.peergroup_set.all()

    if not groups:
        return {}
    else:
        for eachgroup in groups:
            groupmembers = {}
            peers = eachgroup.peers.all()
            for eachpeer in peers:
                groupmembers[eachpeer.user.username] = eachpeer.url
            peernamelist[eachgroup.groupname] = groupmembers

    print peernamelist
    return peernamelist
