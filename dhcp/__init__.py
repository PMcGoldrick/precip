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

OPT_TYPES= {
    "pad" : "none", # 0
    "subnet_mask" : "ipv4", # 1
    "time_offset" : "ipv4", # 2
    "router" : "ipv4+", # 3
    "time_server" : "ipv4+", # 4
    "name_server" : "ipv4+", # 5
    "domain_name_server" : "ipv4+", # 6
    "log_server" : "ipv4+", # 7
    "cookie_server" : "ipv4+", # 8
    "lpr_server" : "ipv4+", # 9
    "impress_server" : "ipv4+", # 10
    "resource_location_server" : "ipv4+", # 11
    "host_name" : "string", # 12
    "boot_file" : "16-bits", # 13
    "merit_dump_file" : "string", # 14
    "domain_name" : "string", # 15
    "swap_server" : "ipv4", # 16
    "root_path" : "string", # 17
    "extensions_path" : "string", # 18
    "ip_forwarding" : "bool", # 19
    "nonlocal_source_rooting" : "bool", # 20
    "policy_filter" : "ipv4+", # 21
    "maximum_datagram_reassembly_size" : "16-bits", # 22
    "default_ip_time-to-live" : "char", # 23
    "path_mtu_aging_timeout" : "ipv4", # 24
    "path_mtu_table" : "16-bits", # 25
    "interface_mtu" : "16-bits", # 26
    "all_subnets_are_local" : "bool", # 27
    "broadcast_address" : "ipv4", # 28
    "perform_mask_discovery" : "bool", # 29
    "mask_supplier" : "bool", # 30
    "perform_router_discovery" : "bool", # 31
    "routeur_solicitation_address" : "ipv4", # 32
    "static_route" : "ipv4+", # 33
    "trailer_encapsulation" : "bool", # 34
    "arp_cache_timeout" : "32-bits", # 35
    "ethernet_encapsulation" : "bool", # 36
    "tcp_default_ttl" : "char", # 37
    "tcp_keepalive_interval" : "32-bits", # 38
    "tcp_keepalive_garbage" : "bool", # 39
    "nis_domain" : "string", # 40
    "nis_servers" : "ipv4+", # 41
    "ntp_servers" : "ipv4+", # 42
    "vendor_specific" : "string", # 43
    "nbns" : "ipv4+", # 44
    "nbdd" : "ipv4+", # 45
    "nd_node_type" : "char", # 46
    "nb_scope" : "string", # 47
    "x_window_system_font_server" : "ipv4+", # 48
    "x_window_system_display_manager" : "ipv4+", # 49
    "request_ip_address" : "ipv4", # 50
    "ip_address_lease_time" : "32-bits", # 51
    "overload" : "char", # 52
    "dhcp_message_type" : "int", # 53
    "server_identifier" : "32-bits", # 54
    "parameter_request_list" : "char+", # 55
    "message" : "string", # 56
    "maximum_dhcp_message_size" : "16-bits", # 57
    "renewal_time_value" : "32-bits", # 58
    "rebinding_time_value" : "32-bits", # 59
    "vendor_class" : "string", # 60
    "client_identifier" : "identifier", # 61
    "netware_ip_domain_name" : "string", # 62
    "netware_ip_sub_options" : "RFC2242", # 63
    "nis+_domain" : "string", # 64
    "nis+_servers" : "ipv4+", # 65
    "tftp_server_name" : "string", # 66
    "bootfile_name" : "string", # 67
    "mobile_ip_home_agent" : "ipv4", # 68
    "smtp_servers" : "ipv4+", # 69
    "pop_servers" : "ipv4+", # 70
    "nntp_servers" : "ipv4+", # 71
    "default_www_server" : "ipv4+", # 72
    "default_finger_server" : "ipv4+", # 73
    "default_irc_server" : "ipv4+", # 74
    "streettalk_server" : "ipv4+", # 75
    "streettalk_directory_assistance_server" : "ipv4+", # 76
    "user_class" : "RFC3004", # 77
    "directory_agent" : "RFC2610", # 78
    "service_scope" : "RFC2610", # 79
    "rapid_commit" : "null", # 80
    "client_fqdn" : "string", # 81
    "relay_agent" : "RFC3046", # 82
    "internet_storage_name_service" : "RFC4174", # 83
    "84" : "Unassigned", # 84
    "nds_server" : "ipv4+", # 85
    "nds_tree_name" : "RFC2241", # 86
    "nds_context" : "RFC2241", # 87
    "88" : "Unassigned", # 88
    "89" : "Unassigned", # 89
    "authentication" : "RFC3118", # 90
    "client_last_transaction_time" : "RFC4388", # 91
    "associated_ip" : "ipv4+", # 92
    "client_system" : "Unassigned", # 93
    "client_ndi" : "Unassigned", # 94
    "ldap" : "Unassigned", # 95
    "unassigned" : "Unassigned", # 96
    "uuid_guid" : "Unassigned", # 97
    "open_group_user_auth" : "string", # 98
    "unassigned" : "Unassigned", # 96
    "unassigned" : "Unassigned", # 96
    "unassigned" : "Unassigned", # 96
    "unassigned" : "Unassigned", # 96
    "unassigned" : "Unassigned", # 96
    "unassigned" : "Unassigned", # 96
    "unassigned" : "Unassigned", # 96
    "unassigned" : "Unassigned", # 96
    "unassigned" : "Unassigned", # 96
    "unassigned" : "Unassigned", # 96
    "unassigned" : "Unassigned", # 96
    "unassigned" : "Unassigned", # 96
    "unassigned" : "Unassigned", # 96
    "netinfo_address" : "Unassigned", # 112
    "netinfo_tag" : "Unassigned", # 113
    "url" : "Unassigned", # 114
    "unassigned" : "Unassigned", # 96
    "auto_config" : "char", # 116
    "name_service_search" : "RFC2937", # 117
    "subnet_selection" : "ipv4", # 118
    "domain_search" : "RFC3397", # 119
    "sip_servers" : "RFC3361", # 120
    "classless_static_route" : "Unassigned", # 121
    "cablelabs_client_configuration" : "Unassigned", # 122
    "geoconf" : "Unassigned", # 123
    "vendor_class" : "string", # 60
    "vendor_specific" : "string", # 43
    "126" : "Unassigned", # 126
    "127" : "Unassigned", # 127
    "128" : "Unassigned", # 128
    "129" : "Unassigned", # 129
    "130" : "Unassigned", # 130
    "131" : "Unassigned", # 131
    "132" : "Unassigned", # 132
    "133" : "Unassigned", # 133
    "134" : "Unassigned", # 134
    "135" : "Unassigned", # 135
    "136" : "Unassigned", # 136
    "137" : "Unassigned", # 137
    "138" : "Unassigned", # 138
    "139" : "Unassigned", # 139
    "140" : "Unassigned", # 140
    "141" : "Unassigned", # 141
    "142" : "Unassigned", # 142
    "143" : "Unassigned", # 143
    "144" : "Unassigned", # 144
    "145" : "Unassigned", # 145
    "146" : "Unassigned", # 146
    "147" : "Unassigned", # 147
    "148" : "Unassigned", # 148
    "149" : "Unassigned", # 149
    "150" : "Unassigned", # 150
    "151" : "Unassigned", # 151
    "152" : "Unassigned", # 152
    "153" : "Unassigned", # 153
    "154" : "Unassigned", # 154
    "155" : "Unassigned", # 155
    "156" : "Unassigned", # 156
    "157" : "Unassigned", # 157
    "158" : "Unassigned", # 158
    "159" : "Unassigned", # 159
    "160" : "Unassigned", # 160
    "161" : "Unassigned", # 161
    "162" : "Unassigned", # 162
    "163" : "Unassigned", # 163
    "164" : "Unassigned", # 164
    "165" : "Unassigned", # 165
    "166" : "Unassigned", # 166
    "167" : "Unassigned", # 167
    "168" : "Unassigned", # 168
    "169" : "Unassigned", # 169
    "170" : "Unassigned", # 170
    "171" : "Unassigned", # 171
    "172" : "Unassigned", # 172
    "173" : "Unassigned", # 173
    "174" : "Unassigned", # 174
    "175" : "Unassigned", # 175
    "176" : "Unassigned", # 176
    "177" : "Unassigned", # 177
    "178" : "Unassigned", # 178
    "179" : "Unassigned", # 179
    "180" : "Unassigned", # 180
    "181" : "Unassigned", # 181
    "182" : "Unassigned", # 182
    "183" : "Unassigned", # 183
    "184" : "Unassigned", # 184
    "185" : "Unassigned", # 185
    "186" : "Unassigned", # 186
    "187" : "Unassigned", # 187
    "188" : "Unassigned", # 188
    "189" : "Unassigned", # 189
    "190" : "Unassigned", # 190
    "191" : "Unassigned", # 191
    "192" : "Unassigned", # 192
    "193" : "Unassigned", # 193
    "194" : "Unassigned", # 194
    "195" : "Unassigned", # 195
    "196" : "Unassigned", # 196
    "197" : "Unassigned", # 197
    "198" : "Unassigned", # 198
    "199" : "Unassigned", # 199
    "200" : "Unassigned", # 200
    "201" : "Unassigned", # 201
    "202" : "Unassigned", # 202
    "203" : "Unassigned", # 203
    "204" : "Unassigned", # 204
    "205" : "Unassigned", # 205
    "206" : "Unassigned", # 206
    "207" : "Unassigned", # 207
    "208" : "Unassigned", # 208
    "209" : "Unassigned", # 209
    "210" : "Unassigned", # 210
    "211" : "Unassigned", # 211
    "212" : "Unassigned", # 212
    "213" : "Unassigned", # 213
    "214" : "Unassigned", # 214
    "215" : "Unassigned", # 215
    "216" : "Unassigned", # 216
    "217" : "Unassigned", # 217
    "218" : "Unassigned", # 218
    "219" : "Unassigned", # 219
    "220" : "Unassigned", # 220
    "221" : "Unassigned", # 221
    "222" : "Unassigned", # 222
    "223" : "Unassigned", # 223
    "224" : "Unassigned", # 224
    "225" : "Unassigned", # 225
    "226" : "Unassigned", # 226
    "227" : "Unassigned", # 227
    "228" : "Unassigned", # 228
    "229" : "Unassigned", # 229
    "230" : "Unassigned", # 230
    "231" : "Unassigned", # 231
    "232" : "Unassigned", # 232
    "233" : "Unassigned", # 233
    "234" : "Unassigned", # 234
    "235" : "Unassigned", # 235
    "236" : "Unassigned", # 236
    "237" : "Unassigned", # 237
    "238" : "Unassigned", # 238
    "239" : "Unassigned", # 239
    "240" : "Unassigned", # 240
    "241" : "Unassigned", # 241
    "242" : "Unassigned", # 242
    "243" : "Unassigned", # 243
    "244" : "Unassigned", # 244
    "245" : "Unassigned", # 245
    "246" : "Unassigned", # 246
    "247" : "Unassigned", # 247
    "248" : "Unassigned", # 248
    "249" : "Unassigned", # 249
    "250" : "Unassigned", # 250
    "251" : "Unassigned", # 251
    "252" : "Unassigned", # 252
    "253" : "Unassigned", # 253
    "254" : "Unassigned", # 254
    "end" : "Unassigned", # 255
}

# [offset, length, type]
FIELDS = {
    'op' : [0, 1, 'int'],
    'htype' : [1, 1, 'int'],
    'hlen' : [2, 1, 'int'],
    'hops' : [3, 1, 'int'],
    'xid' : [4, 4, 'int2'],
    'secs' : [8, 2, 'int2'],
    'flags' : [10, 2, 'int2'],
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