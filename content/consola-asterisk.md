Title: La consola de asterisk
Date: 2008-13-04 10:20
Category: Asterisk, Debian, Linux

Ya se tiene el asterisk funcionando, solo queda probar entrar a la consola.

### Consola de asterisk

Desde root ejecutar asterisk -r.
```
jewel:~# asterisk -r
Asterisk 1.6.0-beta7.1, Copyright (C) 1999 - 2008 Digium, Inc. and others.
Created by Mark Spencer 
Asterisk comes with ABSOLUTELY NO WARRANTY; type 'core show warranty' for details.
This is free software, with components licensed under the GNU General Public
License version 2 and other licenses; you are welcome to redistribute it under
certain conditions. Type 'core show license' for details.
=========================================================================
Connected to Asterisk 1.6.0-beta7.1 currently running on jewel (pid = 3138)
jewel*CLI>

Se muestra la versión de asterisk que se está usando (en el ejemplo la versión beta7.1 de la 1.6.0). Luego el creador de asterisk y la licencia que usa; al final muestra el nombre del equipo y cli.

Para ver la lista de comandos se ejecuta help:
jewel*CLI> help
ael reload Reload AEL configuration
ael set debug {read|tokens|mac Enable AEL debugging flags
agent logoff Sets an agent offline
agent show Show status of agents
agent show online Show all online agents
agi dump html Dumps a list of AGI commands in HTML format
agi exec Add AGI command to a channel in Async AGI
agi set debug [on|off] Enable/Disable AGI debugging
agi show List AGI commands or specific help
cdr show status Display the CDR status
console active Sets/displays active console
console answer Answer an incoming console call
console autoanswer [on|off] Sets/displays autoanswer
console boost Sets/displays mic boost in dB
console dial Dial an extension on the console
console flash Flash a call on the console
console hangup Hangup a call on the console
console {mute|unmute} Disable/Enable mic input
console send text Send text to the remote device
console transfer Transfer a call to a different extension
console {device} Generic console command
core abort shutdown Cancel a running shutdown
core clear profile Clear profiling info
core restart gracefully Restart Asterisk gracefully
core restart now Restart Asterisk immediately
core restart when convenient Restart Asterisk at empty call volume
core set chanvar Set a channel variable
core set debug channel Enable/disable debugging on a channel
core set {debug|verbose} [off| Set level of debug/verbose chattiness
core set global Set global dialplan variable
core show applications [like|d Shows registered dialplan applications
core show application Describe a specific dialplan application
core show calls [uptime] Display information on calls
core show channels [concise|ve Display information on channels
core show channel Display information on a specific channel
core show channeltypes List available channel types
core show channeltype Give more details on that channel type
core show codecs [audio|video| Displays a list of codecs
core show codec Shows a specific codec
core show config mappings Display config mappings (file names to config engines)
core show file formats Displays file formats
core show file version [like] List versions of files used to build Asterisk
core show functions [like] Shows registered dialplan functions
core show function Describe a specific dialplan function
core show globals Show global dialplan variables
core show hints Show dialplan hints
core show hint Show dialplan hint
core show image formats Displays image formats
core show license Show the license(s) for this copy of Asterisk
core show profile Display profiling info
core show settings Show some core settings
core show switches Show alternative switches
core show sysinfo Show System Information
core show threads Show running threads
core show translation [recalc] Display translation matrix
core show uptime [seconds] Show uptime information
core show version Display version info
core show warranty Show the warranty (if any) for this copy of Asterisk
core stop gracefully Gracefully shut down Asterisk
core stop now Shut down Asterisk immediately
core stop when convenient Shut down Asterisk at empty call volume
database del Removes database key/value
database deltree Removes database keytree/values
database get Gets database value
database put Adds/updates database value
database show Shows database contents
database showkey Shows database contents
devstate change Change a custom device state
devstate list List currently known custom device states
dialplan add extension Add new extension into context
dialplan add ignorepat Add new ignore pattern
dialplan add include Include context in other context
dialplan reload Reload extensions and *only* extensions
dialplan remove extension Remove a specified extension
dialplan remove ignorepat Remove ignore pattern from context
dialplan remove include Remove a specified include from context
dialplan save Save dialplan
dialplan set extenpatternmatch Use the Old extension pattern matching algorithm.
dialplan set extenpatternmatch Use the New extension pattern matching algorithm.
dialplan show Show dialplan
dnsmgr refresh Performs an immediate refresh
dnsmgr reload Reloads the DNS manager configuration
dnsmgr status Display the DNS manager status
dundi flush [stats] Flush DUNDi cache
dundi lookup Lookup a number in DUNDi
dundi precache Precache a number in DUNDi
dundi query Query a DUNDi EID
dundi set debug {on|off} Enable/Disable DUNDi debugging
dundi show entityid Display Global Entity ID
dundi show mappings Show DUNDi mappings
dundi show peers [registered|i Show defined DUNDi peers
dundi show peer Show info on a specific DUNDi peer
dundi show precache Show DUNDi precache
dundi show requests Show DUNDi requests
dundi show trans Show active DUNDi transactions
dundi store history {on|off} Enable/Disable DUNDi historic records
feature show channels List status of feature channels
features reload Reloads configured features
features show Lists configured features
file convert Convert audio file
group show channels Display active channels with group(s)
help Display help list, or specific help on a command
http show status Display HTTP server status
iax2 provision Provision an IAX device
iax2 prune realtime Prune a cached realtime lookup
iax2 reload Reload IAX configuration
iax2 set debug {on|off} Enable/Disable IAX debugging
iax2 set debug jb {on|off} Enable/Disable IAX jitterbuffer debugging
iax2 set debug trunk {on|off} Enable/Disable IAX trunk debugging
iax2 set mtu Set the IAX systemwide trunking MTU
iax2 show cache Display IAX cached dialplan
iax2 show channels List active IAX channels
iax2 show firmware List available IAX firmware
iax2 show netstats List active IAX channel netstats
iax2 show peer Show details on specific IAX peer
iax2 show peers List defined IAX peers
iax2 show provisioning Display iax provisioning
iax2 show registry Display IAX registration status
iax2 show stats Display IAX statistics
iax2 show threads Display IAX helper thread info
iax2 show users [like] List defined IAX users
iax2 test losspct Set IAX2 incoming frame loss percentage
iax2 unregister Unregister (force expiration) an IAX2 peer from the registry
indication add Add the given indication to the country
indication remove Remove the given indication from the country
indication show Display a list of all countries/indications
jabber reload Reload Jabber configuration
jabber set debug {on|off} Enable/Disable Jabber debug
jabber show buddies Show buddy lists of our clients
jabber show connected Show state of clients and components
jabber test Shows roster, but is generally used for mog's debugging.
keys init Initialize RSA key passcodes
keys show Displays RSA key information
local show channels List status of local channels
logger mute Toggle logging output to a console
logger reload Reopens the log files
logger rotate Rotates and reopens the log files
logger show channels List configured log channels
manager debug [on|off] Show, enable, disable debugging of the manager code
manager reload Reload manager configurations
manager show command Show a manager interface command
manager show commands List manager interface commands
manager show connected List connected manager interface users
manager show eventq List manager interface queued events
manager show users List configured manager users
manager show user Display information on a specific manager user
meetme Execute a command on a conference or conferee
mgcp audit endpoint Audit specified MGCP endpoint
mgcp reload Reload MGCP configuration
mgcp set debug {on|off} Enable/Disable MGCP debugging
mgcp show endpoints List defined MGCP endpoints
minivm list accounts List defined mini-voicemail boxes
minivm list templates List message templates
minivm list zones List zone message formats
minivm reload Reload Mini-voicemail configuration
minivm show settings Show mini-voicemail general settings
minivm show stats Show some mini-voicemail statistics
mixmonitor [start|stop] Execute a MixMonitor command
mobile rfcomm Send commands to the rfcomm port for debugging
mobile search Search for Bluetooth Cell / Mobile devices
mobile show devices Show Bluetooth Cell / Mobile devices
module load Load a module by name
module reload Reload configuration
module show [like] List modules and info
module unload Unload a module by name
moh reload Reload MusicOnHold
moh show classes List MusicOnHold classes
moh show files List MusicOnHold file-based classes
no debug channel Disable debugging on channel(s)
ooh323 set debug [off] Enable/Disable OOH323 debugging
ooh323 show config Show details on global configuration of H.323 channel driver
ooh323 show peer Show details on specific OOH323 peer
ooh323 show peers Show defined OOH323 peers
ooh323 show user Show details on specific OOH323 user
ooh323 show users Show defined OOH323 users
originate Originate a call
parkedcalls show List currently parked calls
phoneprov show routes Show registered phoneprov http routes
pri debug span Enables PRI debugging on a span
pri intensive debug span Enables REALLY INTENSE PRI debugging
pri no debug span Disables PRI debugging on a span
pri set debug file Sends PRI debug output to the specified file
pri show debug Displays current PRI debug settings
pri show spans Displays PRI Information
pri show span Displays PRI Information
pri unset debug file Ends PRI debug output to file
queue add member Add a channel to a specified queue
queue remove member Removes a channel from a specified queue
queue rules reload Reload the rules defined in queuerules.conf
queue rules show Show the rules defined in queuerules.conf
queue set penalty Set penalty for a channel of a specified queue
queue show Show status of a specified queue
queue {pause|unpause} member Pause or unpause a queue member
realtime load Used to print out RealTime variables.
realtime mysql status Shows connection information for the MySQL RealTime driver
realtime update Used to update RealTime variables.
rpt debug level Enable app_rpt debuggin
rpt dump Dump app_rpt structs for debugging
rpt lstats Dump link statistics
rpt reload Reload app_rpt config
rpt restart Restart app_rpt
rpt stats Dump node statistics
rtcp set debug {on|off|ip} Enable/Disable RTCP debugging
rtcp set stats {on|off} Enable/Disable RTCP stats
rtp set debug {on|off|ip} Enable/Disable RTP debugging
say load [new|old] Set or show the say mode
sip notify Send a notify packet to a SIP peer
sip prune realtime [peer|user| Prune cached Realtime users/peers
sip reload Reload SIP configuration
sip set debug {on|off|ip|peer} Enable/Disable SIP debugging
sip set history {on|off} Enable/Disable SIP history
sip show {channels|subscriptio List active SIP channels/subscriptions
sip show channel Show detailed SIP channel info
sip show domains List our local SIP domains.
sip show history Show SIP dialog history
sip show inuse List all inuse/limits
sip show objects List all SIP object allocations
sip show peers List defined SIP peers
sip show peer Show details on specific SIP peer
sip show registry List SIP registration status
sip show settings Show SIP global settings
sip show tcp List TCP Connections
sip show users List defined SIP users
sip show user Show details on specific SIP user
sip unregister Unregister (force expiration) a SIP peer from the registery

skinny reset Reset Skinny device(s)
skinny set debug {on|off} Enable/Disable Skinny debugging
skinny show devices List defined Skinny devices
skinny show device List Skinny device information
skinny show lines List defined Skinny lines per device
skinny show line List Skinny line information
skinny show settings List global Skinny settings
sla show stations Show SLA Stations
sla show trunks Show SLA Trunks
soft hangup Request a hangup on a given channel
stun set debug {on|off} Enable/Disable STUN debugging
transcoder show Display Zaptel transcoder utilization.
udptl set debug {on|off|ip} Enable/Disable UDPTL debugging
ulimit Set or show process resource limits
unistim info Show UNISTIM info
unistim reload Reload UNISTIM configuration
unistim set debug {on|off} Toggle UNITSTIM debugging
unistim sp Send packet (for reverse engineering)
voicemail reload Reload voicemail configuration
voicemail show users List defined voicemail boxes
voicemail show zones List zone message formats
zap destroy channel Destroy a channel
zap restart Fully restart Zaptel channels
zap set dnd Set software gain on a channel
zap set hwgain Set hardware gain on a channel
zap set swgain Set software gain on a channel
zap show cadences List cadences
zap show channels [trunkgroup| Show active zapata channels
zap show channel Show information on a channel
zap show status Show all Zaptel cards status
zap show version Show the Zaptel version in use
```

Para ver los módulos instalados de asterisk se ejecuta module show:

```
jewel*CLI> module show
Module Description Use Count 
res_speech Generic Speech Recognition API 0 
res_smdi Simplified Message Desk Interface (SMDI) 0 
res_realtime Realtime Data Lookup/Rewrite 0 
res_phoneprov HTTP Phone Provisioning 0 
res_musiconhold Music On Hold Resource 0 
res_monitor Call Monitoring Resource 0 
res_limit Resource limits 0 
res_jabber AJI - Asterisk Jabber Interface 0 
res_indications Region-specific tones 0 
res_crypto Cryptographic Digital Signatures 0 
res_convert File format conversion CLI command 0 
res_config_sqlite Realtime SQLite configuration 0 
res_config_ldap LDAP realtime interface 0 
res_clioriginate Call origination from the CLI 0 
res_agi Asterisk Gateway Interface (AGI) 0 
res_ael_share share-able code for AEL 0 
res_adsi ADSI Resource 0 
pbx_spool Outgoing Spool Support 0 
pbx_realtime Realtime Switch 0 
pbx_lua Lua PBX Switch 0 
pbx_loopback Loopback Switch 0 
pbx_dundi Distributed Universal Number Discovery ( 0 
pbx_config Text Extension Configuration 0 
pbx_ael Asterisk Extension Language Compiler 0 
func_volume Technology independent volume control 0 
func_vmcount Indicator for whether a voice mailbox ha 0 
func_version Get Asterisk Version/Build Info 0 
func_uri URI encode/decode dialplan functions 0 
func_timeout Channel timeout dialplan functions 0 
func_sysinfo System information related functions 0 
func_strings String handling dialplan functions 0 
func_shell Returns the output of a shell command 0 
func_sha1 SHA-1 computation dialplan function 0 
func_realtime Read/Write/Store/Destroy values from a R 0 
func_rand Random number dialplan function 0 
func_module Checks if Asterisk module is loaded in m 0 
func_md5 MD5 digest dialplan functions 0 
func_math Mathematical dialplan function 0 
func_logic Logical dialplan functions 0 
func_lock Dialplan mutexes 0 
func_iconv Charset conversions 0 
func_groupcount Channel group dialplan functions 0 
func_global Variable dialplan functions 0 
func_extstate Gets an extension's state in the dialpla 0 
func_env Environment/filesystem dialplan function 0 
func_enum ENUM related dialplan functions 0 
func_dialplan Dialplan Context/Extension/Priority Chec 0 
func_dialgroup Dialgroup dialplan function 0 
func_devstate Gets or sets a device state in the dialp 0 
func_db Database (astdb) related dialplan functi 0 
func_cut Cut out information from a string 0 
func_channel Channel information dialplan function 0 
func_cdr Call Detail Record (CDR) dialplan functi 0 
func_callerid Caller ID related dialplan functions 0 
func_blacklist Look up Caller*ID name/number from black 0 
func_base64 base64 encode/decode dialplan functions 0 
format_wav_gsm Microsoft WAV format (Proprietary GSM) 0 
format_wav Microsoft WAV format (8000Hz Signed Line 0 
format_vox Dialogic VOX (ADPCM) File Format 0 
format_sln Raw Signed Linear Audio support (SLN) 0 
format_sln16 Raw Signed Linear 16KHz Audio support (S 0 
format_pcm Raw/Sun uLaw/ALaw 8KHz (PCM,PCMA,AU), G. 0 
format_ogg_vorbis OGG/Vorbis audio 0 
format_jpeg JPEG (Joint Picture Experts Group) Image 0 
format_ilbc Raw iLBC data 0 
format_h264 Raw H.264 data 0 
format_h263 Raw H.263 data 0 
format_gsm Raw GSM data 0 
format_g729 Raw G729 data 0 
format_g726 Raw G.726 (16/24/32/40kbps) data 0 
format_g723 G.723.1 Simple Timestamp File Format 0 
codec_zap Generic Zaptel Transcoder Codec Translat 0 
codec_ulaw mu-Law Coder/Decoder 0 
codec_speex Speex Coder/Decoder 0 
codec_resample SLIN Resampling Codec 0 
codec_lpc10 LPC10 2.4kbps Coder/Decoder 0 
codec_gsm GSM Coder/Decoder 0 
codec_g726 ITU G.726-32kbps G726 Transcoder 0 
codec_g722 ITU G.722-64kbps G722 Transcoder 0 
codec_a_mu A-law and Mulaw direct Coder/Decoder 0 
codec_alaw A-law Coder/Decoder 0 
codec_adpcm Adaptive Differential PCM Coder/Decoder 0 
chan_zap Zapata Telephony 0 
chan_unistim UNISTIM Protocol (USTM) 0 
chan_skinny Skinny Client Control Protocol (Skinny) 0 
chan_sip Session Initiation Protocol (SIP) 0 
chan_phone Linux Telephony API Support 0 
chan_oss OSS Console Channel Driver 0 
chan_mgcp Media Gateway Control Protocol (MGCP) 0 
chan_local Local Proxy Channel (Note: used internal 0 
chan_jingle Jingle Channel Driver 0 
chan_iax2 Inter Asterisk eXchange (Ver 2) 0 
chan_gtalk Gtalk Channel Driver 0 
chan_features Feature Proxy Channel 0 
chan_console Console Channel Driver 0 
chan_alsa ALSA Console Channel Driver 0 
chan_agent Agent Proxy Channel 0 
cdr_sqlite SQLite CDR Backend 0 
cdr_sqlite3_custom SQLite3 Custom CDR Module 0 
cdr_manager Asterisk Manager Interface CDR Backend 0 
cdr_custom Customizable Comma Separated Values CDR 0 
cdr_csv Comma Separated Values CDR Backend 0 
app_zapscan Scan Zap channels application 0 
app_zapras Zaptel ISDN Remote Access Server 0 
app_zapbarge Barge in on Zap channel application 0 
app_zapateller Block Telemarketers with Special Informa 0 
app_while While Loops and Conditional Execution 0 
app_waituntil Wait until specified time 0 
app_waitforsilence Wait For Silence 0 
app_waitforring Waits until first ring after time 0 
app_voicemail Comedian Mail (Voicemail System) 0 
app_verbose Send verbose output 0 
app_userevent Custom User Event Application 0 
app_url Send URL Applications 0 
app_transfer Transfers a caller to another extension 0 
app_test Interface Test Application 0 
app_talkdetect Playback with Talk Detection 0 
app_system Generic System() application 0 
app_stack Dialplan subroutines (Gosub, Return, etc 0 
app_speech_utils Dialplan Speech Applications 0 
app_softhangup Hangs up the requested channel 0 
app_sms SMS/PSTN handler 0 
app_skel Skeleton (sample) Application 0 
app_setcallerid Set CallerID Presentation Application 0 
app_sendtext Send Text Applications 0 
app_senddtmf Send DTMF digits Application 0 
app_sayunixtime Say time 0 
app_rpt Radio Repeater / Remote Base 0 
app_record Trivial Record Application 0 
app_readfile Stores output of file into a variable 0 
app_readexten Read and evaluate extension validity 0 
app_read Read Variable Application 0 
app_queue True Call Queueing 0 
app_privacy Require phone number to be entered, if n 0 
app_playback Sound File Playback Application 0 
app_pickupchan Channel Pickup Application 0 
app_parkandannounce Call Parking and Announce Application 0 
app_page Page Multiple Phones 0 
app_nbscat Silly NBS Stream Application 0 
app_mp3 Silly MP3 Application 0 
app_morsecode Morse code 0 
app_mixmonitor Mixed Audio Monitoring Application 0 
app_minivm Mini VoiceMail (A minimal Voicemail e-ma 0 
app_milliwatt Digital Milliwatt (mu-law) Test Applicat 0 
app_meetme MeetMe conference bridge 0 
app_macro Extension Macros 0 
app_jack JACK Interface 0 
app_ivrdemo IVR Demo Application 0 
app_image Image Transmission Application 0 
app_ices Encode and Stream via icecast and ices 0 
app_getcpeid Get ADSI CPE ID 0 
app_forkcdr Fork The CDR into 2 separate entities 0 
app_followme Find-Me/Follow-Me Application 0 
app_flash Flash channel application 0 
app_festival Simple Festival Interface 0 
app_externalivr External IVR Interface Application 0 
app_exec Executes dialplan applications 0 
app_echo Simple Echo Application 0 
app_dumpchan Dump Info About The Calling Channel 0 
app_disa DISA (Direct Inward System Access) Appli 0 
app_directory Extension Directory 0 
app_directed_pickup Directed Call Pickup Application 0 
app_dictate Virtual Dictation Machine 0 
app_dial Dialing Application 0 
app_db Database Access Functions 0 
app_controlplayback Control Playback Application 0 
app_chanspy Listen to the audio of an active channel 0 
app_channelredirect Redirects a given channel to a dialplan 0 
app_chanisavail Check channel availability 0 
app_cdr Tell Asterisk to not maintain a CDR for 0 
app_authenticate Authentication Application 0 
app_amd Answering Machine Detection Application 0 
app_alarmreceiver Alarm Receiver for Asterisk 0 
app_adsiprog Asterisk ADSI Programming Application 0 
res_config_mysql.so MySQL RealTime Configuration Driver 0 
chan_mobile.so Bluetooth Mobile Device Channel Driver 0 
format_mp3.so MP3 format [Any rate but 8000hz mono is 0 
test_skel.so Skeleton (sample) Test 0 
app_addon_sql_mysql.so Simple Mysql Interface 0 
chan_ooh323.so Objective Systems H323 Channel 0 
cdr_addon_mysql.so MySQL CDR Backend 0 
app_saycountpl.so Say polish counting words 0 
182 modules loaded
jewel*CLI> 
```

Al final se muestra la cantidad de módulos cargados.

Para ver los canales que se están usando se ejecuta:

```
jewel*CLI> sip show channels
Peer User/ANR Call ID Format Hold Last Message 
0 active SIP dialogs
```

Actualmente como no se tiene configurado completamente el asterisk no se muestra canal alguno.


Para listar los usuarios sip definidos se tiene el comando sip show users:

```
jewel*CLI> sip show users
Username Secret Accountcode Def.Context ACL NAT 
jewel*CLI>
```

Devuelve el nombre de usuario la clave, el cual contexto se encuentra, la lista de acceso y si usa NAT

Muestra el estatus de la interfaz zapata

```
jewel*CLI> zap show status
Description Alarms IRQ bpviol CRC4 Fra Codi Options LBO
ZTDUMMY/1 (source: HRtimer) 1 UNCONFI 0 0 0 CAS Unk YEL 0 db (CSU)/0-133 feet (DSX-1)
```

Para ver los buzones de voz:

```
jewel*CLI> voicemail show users
Context Mbox User Zone NewMsg
default general New User 0
default 1234 Example Mailbox 0
other 1234 Company2 User 0
3 voicemail users configured.
```

Para buscar dispositivos moviles se ejecuta:

```
jewel*CLI> mobile search
Address Name Usable Type Port
00:19:2C:2C:29:33 Motorola A1200 No Headset 0
```

Hay muchos comandos para la consola de asterisk y en futuros post se mostrarán

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC) 
usando la billetera digital de tu preferencia a la siguiente 
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./imagenes/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)