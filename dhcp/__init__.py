""" A DHCP implementation in Twisted """
__version__ = "0.1"

__all__ = [
    'packet',
    'service',
]

OPTS = [
    'pad',
    # Vendor Extension
    'subnet_mask',
    'time_offset',
    'router',
    'time_server',
    'name_server',
    'domain_name_server',
    'log_server',
    'cookie_server',
    'lpr_server',
    'impress_server',
    'resource_location_server',
    'host_name',
    'boot_file',
    'merit_dump_file',
    'domain_name',
    'swap_server',
    'root_path',
    'extensions_path',
    # IP layer parameters per host
    'ip_forwarding',
    'nonlocal_source_rooting',
    'policy_filter',
    'maximum_datagram_reassembly_size',
    'default_ip_time-to-live',
    'path_mtu_aging_timeout',
    'path_mtu_table',
    # IP layer parameters per interface
    'interface_mtu',
    'all_subnets_are_local',
    'broadcast_address',
    'perform_mask_discovery',
    'mask_supplier',
    'perform_router_discovery',
    'routeur_solicitation_address',
    'static_route',
    # link layer parameters per interface
    'trailer_encapsulation',
    'arp_cache_timeout',
    'ethernet_encapsulation',
    # TCP parameters
    'tcp_default_ttl',
    'tcp_keepalive_interval',
    'tcp_keepalive_garbage',
    # Applications and service parameters
    'nis_domain',
    'nis_servers',
    'ntp_servers',
    'vendor_specific',
    'nbns',
    'nbdd',
    'nd_node_type',
    'nb_scope',
    'x_window_system_font_server',
    'x_window_system_display_manager',
    # DHCP extensions
    'request_ip_address',
    'ip_address_lease_time',
    'overload',
    'dhcp_message_type',
    'server_identifier',
    'parameter_request_list',
    'message',
    'maximum_dhcp_message_size',
    'renewal_time_value',
    'rebinding_time_value',
    'vendor_class',
    'client_identifier',
    # adds from RFC 2132,2242
    'netware_ip_domain_name',
    'netware_ip_sub_options',
    'nis+_domain',
    'nis+_servers',
    'tftp_server_name',
    'bootfile_name',
    'mobile_ip_home_agent',
    'smtp_servers',
    'pop_servers',
    'nntp_servers',
    'default_www_server',
    'default_finger_server',
    'default_irc_server',
    'streettalk_server',
    'streettalk_directory_assistance_server',
    'user_class',
    'directory_agent',
    'service_scope',
    # 80
    'rapid_commit',
    'client_fqdn',
    'relay_agent',
    'internet_storage_name_service',
    '84',
    'nds_server',
    'nds_tree_name',
    'nds_context',
    '88',
    '89',

    #90
    'authentication',
    'client_last_transaction_time',
    'associated_ip', #RFC 4388
    'client_system', 'client_ndi', #RFC 3679
    'ldap',
    'unassigned',
    'uuid_guid', #RFC 3679
    'open_group_user_auth', #RFC 2485
    # 99->115 RFC3679
    'unassigned',
    'unassigned',
    'unassigned',
    'unassigned',
    'unassigned',
    'unassigned',
    'unassigned',
    'unassigned',
    'unassigned',
    'unassigned',
    'unassigned',
    'unassigned',
    'unassigned',
    'netinfo_address',
    'netinfo_tag',
    'url',
    'unassigned',
    #116
    'auto_config',
    'name_service_search',
    'subnet_selection',
    'domain_search',
    'sip_servers',
    'classless_static_route',
    'cablelabs_client_configuration',
    'geoconf',
    #124
    'vendor_class',
    'vendor_specific',
    '126',
    '127',
    '128',
    '129',
    '130',
    '131',
    '132',
    '133',
    '134',
    '135',
    '136',
    '137',
    '138',
    '139',
    '140',
    '141',
    '142',
    '143',
    '144',
    '145',
    '146',
    '147',
    '148',
    '149',
    '150',
    '151',
    '152',
    '153',
    '154',
    '155',
    '156',
    '157',
    '158',
    '159',
    '160',
    '161',
    '162',
    '163',
    '164',
    '165',
    '166',
    '167',
    '168',
    '169',
    '170',
    '171',
    '172',
    '173',
    '174',
    '175',
    '176',
    '177',
    '178',
    '179',
    '180',
    '181',
    '182',
    '183',
    '184',
    '185',
    '186',
    '187',
    '188',
    '189',
    '190',
    '191',
    '192',
    '193',
    '194',
    '195',
    '196',
    '197',
    '198',
    '199',
    '200',
    '201',
    '202',
    '203',
    '204',
    '205',
    '206',
    '207',
    '208',
    '209',
    '210',
    '211',
    '212',
    '213',
    '214',
    '215',
    '216',
    '217',
    '218',
    '219',
    '220',
    '221',
    '222',
    '223',
    '224',
    '225',
    '226',
    '227',
    '228',
    '229',
    '230',
    '231',
    '232',
    '233',
    '234',
    '235',
    '236',
    '237',
    '238',
    '239',
    '240',
    '241',
    '242',
    '243',
    '244',
    '245',
    '246',
    '247',
    '248',
    '249',
    '250',
    '251',
    '252',
    '253',
    '254',
    'end'
    ]
OPT_TYPES = [
    'none',
    'ipv4',
    'ipv4',
    'ipv4+',
    'ipv4+',
    'ipv4+',
    'ipv4+',
    'ipv4+',
    'ipv4+',
    'ipv4+',
    'ipv4+',
    'ipv4+',
    'string',
    '16-bits',
    'string',
    'string',
    'ipv4',
    'string',
    'string',
    'bool',
    'bool',
    'ipv4+',
    '16-bits',
    'char',
    'ipv4',
    '16-bits',
    '16-bits',
    'bool',
    'ipv4',
    'bool',
    'bool',
    'bool',
    'ipv4',
    'ipv4+',
    'bool',
    '32-bits',
    'bool',
    'char',
    '32-bits',
    'bool',
    'string',
    'ipv4+',
    'ipv4+',
    'string',
    'ipv4+',
    'ipv4+',
    'char',
    'string',
    'ipv4+',
    'ipv4+',
    'ipv4',
    '32-bits',
    'char',
    'char',
    '32-bits',
    'char+',
    'string',
    '16-bits',
    '32-bits',
    '32-bits',
    'string',
    'identifier',
    'string',
    'RFC2242',
    'string',
    'ipv4+',
    'string',
    'string',
    'ipv4',
    'ipv4+',
    'ipv4+',
    'ipv4+',
    'ipv4+',
    'ipv4+',
    'ipv4+',
    'ipv4+',
    'ipv4+',
    'RFC3004',
    'RFC2610',
    'RFC2610',
    'null',
    'string',
    'RFC3046',
    'RFC4174',
    'Unassigned',
    'ipv4+',
    'RFC2241',
    'RFC2241',
    'Unassigned',
    'Unassigned',
    'RFC3118',
    'RFC4388',
    'ipv4+',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'string',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'char',
    'RFC2937',
    'ipv4',
    'RFC3397',
    'RFC3361',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned',
    'Unassigned'
]

# [offset, length, type]
FIELDS = {
    'op' : [0, 1, 'int'],
    'htype' : [1, 1, 'int'],
    'hlen' : [2, 1, 'int'],
    'hops' : [3, 1, 'int4'],
    'xid' : [4, 4, 'int2'],
    'secs' : [8, 2, 'int2'],
    'flags' : [10, 2, 'ipv4'],
    'ciaddr' : [12, 4, 'ipv4'],
    'yiaddr' : [16, 4, 'ipv4'],
    'siaddr' : [20, 4, 'ipv4'],
    'giaddr' : [24, 4, 'ipv4'],
    'chaddr' : [28, 16, 'hwmac'],
    'sname' : [44, 64, 'str'],
    'file' : [108, 128, 'str']
}

OP_VALUES = {
    '0' : 'ERROR_UNDEF',
    '1' : 'BOOTREQUEST' ,
    '2' : 'BOOTREPLY'
}

MESSAGE_TYPES = [
    'ERROR_UNDEF',
    'DHCP_DISCOVER',
    'DHCP_OFFER',
    'DHCP_REQUEST',
    'DHCP_DECLINE',
    'DHCP_ACK',
    'DHCP_NACK',
    'DHCP_RELEASE',
    'DHCP_INFORM'
]

MAGIC_COOKIE = [99, 130, 83, 99]

# fields_specs : {'option_code':fixed_length,minimum_length,multiple}
# if fixed_length == 0 : minimum_length and multiple apply
# else : forget minimum_length and multiple
# multiple : length MUST be a multiple of 'multiple'
FIELD_SPECS = {
    "ipv4":[4,0,1],
    "ipv4+":[0,4,4],
    "string":[0,0,1],
    "bool":[1,0,1],
    "char":[1,0,1],
    "16-bits":[2,0,1],
    "32-bits":[4,0,1],
    "identifier":[0,2,1],
    "RFC3397":[0,4,1],
    "none":[0,0,1],
    "char+":[0,1,1]
}