# Homelab Network Equipment Guide - NetworkChuck Edition
## Build Your Dream Network Infrastructure (2025)

**Created:** November 23, 2025
**Companion Guide to:** [nas_rec.md](nas_rec.md)
**Budget Focus:** $200-$600 networking gear to complement your $500 NAS

---

## Executive Summary

Okay okay okay, let's GO! So you've got your NAS setup (whether it's that sweet TerraMaster F2-212 or the beastly UGREEN DXP2800 from the NAS guide), and now you need the networking gear to ACTUALLY unleash its full potential.

Here's the thing - you can have the most powerful NAS in the world, but if you're running it through a cheap router and basic switch, you're leaving MASSIVE performance on the table. We're talking about the difference between transferring files at 110 MB/s versus 280 MB/s. That's more than DOUBLE the speed!

Grab your coffee, because we're about to build a network infrastructure that would make any IT professional jealous. And the best part? We're doing it on a budget that won't make your wallet cry.

---

## Why Your Network Equipment ACTUALLY Matters

Before we dive into the shopping list, let me tell you WHY this stuff matters for your homelab:

### 1. **Speed is EVERYTHING**
- Your UGREEN DXP2800 has **2.5GbE networking** - but that means NOTHING if your switch only does gigabit
- A 2.5GbE network gives you 2.5x faster file transfers, Plex streaming, and backups
- This is the difference between waiting 10 minutes for a backup vs. 4 minutes

### 2. **VLANs = Security Superpowers**
- Isolate your sketchy IoT devices (looking at you, cheap Chinese cameras)
- Keep your guests from accessing your private files
- Segment your homelab services from your main network
- This is NetworkChuck 101 stuff - you NEED this

### 3. **Future-Proofing**
- Buy the right gear now, upgrade easily later
- Start with 1GbE, upgrade to 2.5GbE when you're ready
- Add more switches, APs, VLANs as your homelab grows

### 4. **Reliability**
- Consumer routers crash under heavy load
- Prosumer/business gear keeps running 24/7/365
- Your Plex server can't stream if the router reboots every week

---

## Your NAS Setup Quick Reference

Based on the [NAS Recommendations Guide](nas_rec.md), you likely have one of these setups:

| Option | NAS Model | Network Speed | RAM | What This Means for Networking |
|--------|-----------|---------------|-----|--------------------------------|
| **Budget** | TerraMaster F2-212 | 1GbE | 1GB | Gigabit switch is fine, but consider 2.5GbE for future |
| **Performance** | UGREEN DXP2800 | **2.5GbE** | 8GB | You NEED 2.5GbE to unlock full performance |
| **Alternative** | Synology DS223j | 1GbE | 1GB | Gigabit is adequate, focus budget on other areas |

**KEY INSIGHT:** If you went with the UGREEN DXP2800 (the performance beast), you're WASTING that 2.5GbE port if you don't have a 2.5GbE switch. Let's fix that!

---

## Essential Network Equipment for Homelabs

### The Three Pillars of Network Infrastructure

1. **Router/Gateway** - The brain of your network, handles routing, firewall, VPN
2. **Switch** - Connects all your wired devices together, handles VLANs
3. **Access Point** - Provides WiFi coverage (separate from router for best performance)

Let's break down each category with specific recommendations...

---

## Part 1: Routers & Gateways

### Budget Tier: Use What You Have (For Now)

**Cost: $0 (existing equipment)**

Here's the thing - most ISP-provided routers or cheap TP-Link/Netgear routers will work for basic homelab stuff. But here's what you're missing:
- Limited VLAN support (if any)
- Weak firewall rules
- Crashes under heavy torrent/Plex load
- No VPN server capability
- Consumer-grade unreliability

**When to upgrade:** When you want to run VPN servers, advanced firewall rules, or need rock-solid 24/7 reliability.

---

### Entry-Level Prosumer: TP-Link ER605 Omada Gateway

**Cost: ~$59.99**

**Specifications:**
- 5x Gigabit ports (1 WAN, 1 WAN/LAN, 3 LAN)
- Hardware VPN acceleration
- Managed via Omada Controller (free software)
- IPsec/OpenVPN/L2TP VPN support
- Advanced firewall rules
- Multi-WAN failover

**Pros:**
- INSANE value at $60
- Omada ecosystem is like UniFi but cheaper
- Excellent VLAN support
- Hardware VPN means fast VPN speeds
- Can handle gigabit WAN speeds with IDS/IPS enabled

**Cons:**
- Only gigabit ports (no 2.5GbE)
- Requires Omada Controller software (free, runs on Docker)
- Not as powerful as pfSense boxes

**Perfect for:** Budget-conscious users who want prosumer features without the prosumer price tag.

---

### Mid-Tier DIY: Mini PC Running pfSense/OPNsense

**Cost: ~$150-$250**

**Recommended Hardware Options:**

**Option A: ZimaBoard 432 (8GB version)**
- Intel Celeron N3450 quad-core
- 8GB RAM
- Dual 1GbE ports
- Cost: ~$159 (on sale)
- VPN Performance: 100Mbps OpenVPN, 400Mbps WireGuard
- Power: 6-10W (fanless, passive cooling)

**Option B: Protectli Vault FW2B**
- Intel Dual Core 64-bit processor
- 4GB RAM (upgradeable)
- Dual Intel NICs
- 32GB mSATA SSD
- Cost: ~$199
- Fanless design

**Option C: PC Engines APU2E4**
- AMD GX-412TC quad-core
- 4GB RAM
- Triple Intel NICs
- Cost: ~$170-$190
- Fanless, 6-10W power consumption
- Community favorite for pfSense

**Why pfSense/OPNsense:**
- Enterprise-grade firewall capabilities
- Unlimited VLANs
- VPN server/client (OpenVPN, WireGuard, IPsec)
- Traffic shaping and QoS
- IDS/IPS with Snort/Suricata
- Package ecosystem (Pi-hole alternative, etc.)
- Complete control over your network

**Cons:**
- Requires technical knowledge to set up
- More complex than plug-and-play routers
- Need to configure everything manually

**Perfect for:** Homelabbers who want maximum control and aren't afraid of CLI/web config.

---

### Premium Tier: UniFi Dream Machine SE

**Cost: ~$499 (official Ubiquiti store)**

**Specifications:**
- 10G SFP+ WAN port
- 2.5GbE RJ45 WAN/LAN port
- 8-port Gigabit PoE switch (built-in)
- 3.5 Gbps IPS/IDS routing
- 128GB built-in storage (for UniFi Protect NVR)
- Dual-WAN support
- UniFi Network Controller built-in
- 10G SFP+ uplink to other switches

**Pros:**
- All-in-one solution (router + switch + NVR)
- Beautiful UniFi interface
- Built-in PoE for cameras/APs
- 10G uplink ready for future expansion
- Best-in-class traffic analytics
- Rock-solid reliability

**Cons:**
- Expensive ($499)
- Locks you into UniFi ecosystem
- Overkill for small homelabs
- Takes up most of your budget

**Perfect for:** Users who want the absolute best all-in-one solution and plan to go deep into UniFi ecosystem (cameras, APs, switches).

**NOTE:** The UDM-SE is probably TOO MUCH for most homelab users unless you're also building a security camera system. Consider the cheaper UniFi Dream Router (~$199) if you want UniFi without breaking the bank.

---

## Part 2: Network Switches - The Heart of Your Network

This is where you'll spend most of your networking budget, and it's the MOST important decision for homelab performance.

### Understanding Switch Types

**Unmanaged Switches:**
- Plug and play, no configuration
- No VLAN support
- Perfect for simple setups
- Cheapest option

**Smart/Easy Managed Switches:**
- Web GUI configuration (no CLI)
- VLAN support (802.1Q)
- Basic QoS and traffic control
- Best value for homelabs

**Fully Managed Switches:**
- Full CLI + Web GUI
- Advanced features (LACP, spanning tree, etc.)
- Enterprise-grade capabilities
- More expensive

---

### Budget Gigabit Switches (1GbE)

#### **Best Value: TP-Link TL-SG108E (8-Port Easy Smart)**

**Cost: ~$29.99**

**Specifications:**
- 8x Gigabit ports
- VLAN support (802.1Q)
- QoS traffic prioritization
- IGMP snooping (important for Plex!)
- Port mirroring
- Desktop or wall-mount
- Fanless (silent operation)
- Metal chassis

**Why I love this switch:**
- Under $30 for managed features!
- Web GUI is simple and works great
- Perfect for learning VLANs
- Supports all the homelab projects you'll do
- Fanless means silent homelab

**Cons:**
- Web GUI only (no CLI)
- Limited compared to fully managed switches
- Only gigabit (not 2.5GbE)

**Perfect for:** Anyone with the TerraMaster F2-212 or Synology DS223j who wants VLAN support without spending much.

---

#### **Step-Up Option: TP-Link TL-SG2008 (8-Port Smart Managed)**

**Cost: ~$72.99**

**Specifications:**
- 8x Gigabit ports
- L2+ managed features
- Advanced VLAN configuration
- Link aggregation (LAG)
- Better QoS than TL-SG108E
- Loop prevention
- Better web interface

**Why upgrade to this:**
- More advanced features than TL-SG108E
- Better long-term investment
- Link aggregation for NAS (combine ports for more speed)
- Better suited for larger homelabs

**Perfect for:** Users who want more advanced features and plan to expand their homelab significantly.

---

### Premium Gigabit Option: Netgear GS308T

**Cost: ~$59.99**

**Specifications:**
- 8x Gigabit ports
- Fully managed features
- Excellent web GUI
- VLAN, QoS, IGMP snooping
- Very reliable hardware
- Fanless

**Why consider Netgear:**
- Better build quality than budget TP-Link
- More intuitive web interface
- Great community support
- Netgear's prosumer line is solid

---

### 2.5GbE Switches - The Sweet Spot for 2025

Here's where things get EXCITING! If you have the UGREEN DXP2800, you NEED one of these to unlock that 2.5GbE performance.

#### **Budget Champion: QNAP QSW-1105-5T (5-Port Unmanaged)**

**Cost: ~$108-$109**

**Specifications:**
- 5x 2.5GbE ports
- Unmanaged (plug and play)
- Backward compatible with 1GbE/100Mbps
- Fanless operation
- Desktop placement
- Compact metal chassis

**Performance:**
- Real-world speeds: 260-300 MB/s file transfers!
- Works with existing Cat5e/Cat6 cables (no rewiring needed)

**Why this is awesome:**
- Under $110 for 2.5GbE!
- Perfect for connecting: NAS, Desktop, Gaming PC, Server
- No fan = silent operation
- Plug and play simplicity

**Cons:**
- Only 5 ports (might need more later)
- Unmanaged (no VLANs)
- QNAP brand is hit-or-miss for some people

**Perfect for:** UGREEN DXP2800 owners who want maximum NAS performance on a budget and don't need VLANs on the 2.5GbE switch.

**Pro Tip:** You can use this for your "fast devices" (NAS, desktop, server) and use a separate cheap gigabit managed switch for everything else (IoT, cameras, etc.). This hybrid approach gives you speed WHERE IT MATTERS and VLANs where you need them.

---

#### **8-Port Budget Option: TRENDnet TEG-S380**

**Cost: ~$179**

**Specifications:**
- 8x 2.5GbE ports
- Unmanaged
- Backward compatible
- Fanless
- Metal desktop chassis

**Pros:**
- More ports than QNAP (8 vs 5)
- Still fanless and compact
- Good build quality

**Cons:**
- **WARNING:** Compatibility issues with Apple devices (M2 Mac minis, Apple TVs)
- **Does NOT pass VLAN-tagged traffic** (major limitation!)
- More expensive than QNAP per port

**Verdict:** Only buy this if you DON'T have Apple devices and DON'T need VLAN support on your 2.5GbE network. Otherwise, skip it.

---

#### **Best Overall 2.5GbE: TP-Link TL-SG108-M2 (8-Port Unmanaged)**

**Cost: ~$99-$129**

**Specifications:**
- 8x 2.5GbE ports
- Unmanaged (plug and play)
- Multi-gig support
- Wall-mountable
- Fanless
- Supports 100Mbps/1GbE/2.5GbE auto-negotiation

**Why this is THE ONE:**
- Best price per port for 2.5GbE
- TP-Link reliability
- No weird compatibility issues
- Perfect size for most homelabs
- Wall-mount option for rack setups

**Perfect for:** Anyone with 2.5GbE NAS who wants the best unmanaged 2.5GbE switch at the best price.

---

#### **Managed 2.5GbE Option: TP-Link TL-SG3210XP-M2**

**Cost: ~$379-$399**

**Specifications:**
- 8x 2.5GbE PoE++ ports (240W total)
- 2x 10G SFP+ uplinks
- Fully managed
- VLAN, QoS, ACLs
- PoE++ (60W per port)
- Rackmount or desktop

**This switch is INSANE:**
- Powers UniFi cameras/APs via PoE
- 2.5GbE for all your devices
- 10G uplinks for future expansion
- Full management features

**Cons:**
- Expensive ($379)
- Probably overkill unless you need PoE
- Fan-cooled (makes some noise)

**Perfect for:** Advanced users building serious homelabs with PoE cameras/APs who want 2.5GbE everywhere and 10G uplinks.

---

### 10GbE Switches - Future-Proofing (Advanced)

**Quick Take:** 10GbE is still pretty expensive in 2025, and most homelabs don't need it. 2.5GbE is the sweet spot. BUT if you're editing 4K video from a NAS or running heavy virtualization, consider these:

**Budget 10GbE Option: Zyxel XMG-108**
- Cost: ~$199
- 8x 2.5GbE + 1x 10G SFP+
- Unmanaged
- Fanless

This gives you mostly 2.5GbE with ONE 10G uplink for a NAS or server. Smart compromise.

---

## Part 3: WiFi Access Points

### Why Separate APs Are Better Than Router WiFi

Let me be clear: Your ISP router's WiFi SUCKS. Here's why:
- WiFi dies when router reboots
- Can't place it optimally (it's stuck where the cable comes in)
- Consumer WiFi is weak and unreliable
- Can't add more APs easily
- No proper VLAN support for guest networks

Separate APs = professional setup = happy homelab.

---

### Budget WiFi 6 Option: TP-Link EAP225 (WiFi 5)

**Cost: ~$59.99**

**Wait, this is WiFi 5, not WiFi 6!**

Yeah, I know, but hear me out. The EAP225 is WiFi 5 (802.11ac), BUT:
- Supports up to 1350 Mbps
- Rock-solid reliability
- PoE powered
- Omada ecosystem integration
- Ceiling mounted (professional installation)
- Multiple SSIDs with VLAN support

**Why buy WiFi 5 in 2025?**
- Your phone/laptop won't max out WiFi 5 speeds anyway
- Save $40-60 vs WiFi 6
- Use the savings for better switches
- Still plenty fast for 4K Plex streaming

**Perfect for:** Budget-conscious users who want professional-grade WiFi without paying for WiFi 6 features they won't use.

---

### Entry WiFi 6: TP-Link EAP650

**Cost: ~$99-$119**

**Specifications:**
- WiFi 6 (802.11ax)
- AX3000 speeds (574 Mbps @ 2.4GHz + 2402 Mbps @ 5GHz)
- PoE powered
- Ceiling or wall mount
- Omada ecosystem
- MU-MIMO and OFDMA
- Multiple SSIDs with VLAN tagging

**Why upgrade to WiFi 6:**
- Better performance in congested areas
- More simultaneous device support
- Future-proofing for WiFi 6E devices
- Better battery life on client devices

**Perfect for:** Users who want true WiFi 6 in the budget-friendly Omada ecosystem.

---

### UniFi Option: U6 Lite

**Cost: ~$99 (official pricing), ~$114 (Europe)**

**Specifications:**
- WiFi 6 dual-band
- Up to 1.5 Gbps throughput
- 4 spatial streams
- Compact ceiling mount
- UniFi Network Controller
- PoE powered (802.3af)

**Why UniFi:**
- Best management interface
- Gorgeous controller UI
- Excellent mobile app
- Seamless roaming between APs
- Best-in-class traffic analytics

**Cons:**
- **2.4GHz is WiFi 4 (802.11n), NOT WiFi 6!**
- This is a weird limitation
- More expensive than Omada equivalents

**Verdict:** The U6 Lite is good, but TP-Link EAP650 offers better specs for similar money. Only get this if you're committed to UniFi ecosystem.

---

### Premium Pick: UniFi U6-Pro

**Cost: ~$149-$179**

**Specifications:**
- WiFi 6 dual-band (both bands WiFi 6!)
- Up to 4.8 Gbps throughput
- 4x4 MU-MIMO
- 2.5GbE uplink
- PoE+ powered

**Why this is worth it:**
- Truly flagship WiFi 6 performance
- 2.5GbE uplink (pairs perfectly with UGREEN DXP2800!)
- Both bands are WiFi 6
- Best UniFi AP for the money

**Perfect for:** Users going all-in on UniFi who want the best WiFi performance.

---

## Network Topology & VLAN Setup for Homelabs

Okay, grab another coffee because this is where it gets REALLY good. We're about to segment your network like a pro.

### Why VLANs Are Essential for Homelabs

**Security:**
- IoT devices are notoriously insecure (cheap cameras, smart bulbs, etc.)
- One compromised device could access your NAS/servers
- VLANs isolate devices into security zones

**Performance:**
- Broadcast traffic is contained per VLAN
- Better QoS control
- Reduces network congestion

**Organization:**
- Logical separation of devices
- Easier troubleshooting
- Professional network design

**Flexibility:**
- Add/change rules easily
- Test new services safely
- Guest WiFi that actually works

---

### Recommended VLAN Structure for Homelabs

Here's the VLAN structure I recommend (based on NetworkChuck's approach and homelab best practices):

#### **VLAN 1 - Management (Default)**
- **Purpose:** Switch/AP/router management
- **Devices:** Network equipment web interfaces only
- **Subnet:** 192.168.1.0/24
- **Why:** Keep management separate from user traffic

#### **VLAN 10 - Trusted Devices**
- **Purpose:** Your personal devices you trust
- **Devices:** Laptops, desktops, phones, tablets
- **Subnet:** 192.168.10.0/24
- **Firewall Rules:** Access to everything (NAS, servers, IoT, internet)

#### **VLAN 20 - Homelab Servers**
- **Purpose:** Your NAS, Docker host, VMs, game servers
- **Devices:** TerraMaster/UGREEN NAS, Proxmox servers, etc.
- **Subnet:** 192.168.20.0/24
- **Firewall Rules:**
  - Access TO: Internet, other VLANs (servers can initiate)
  - Access FROM: Only VLAN 10 and VLAN 40 (controlled access)
- **Why:** Servers accessible to trusted devices but protected from IoT

#### **VLAN 30 - IoT Devices**
- **Purpose:** Smart home devices, cameras, sensors
- **Devices:** IP cameras, smart lights, Alexa/Google Home, smart TVs
- **Subnet:** 192.168.30.0/24
- **Firewall Rules:**
  - Allow: DNS, internet access (outbound only)
  - Deny: Access to VLANs 10, 20, 40
  - Exception: VLAN 10 can access IoT (you control cameras, etc.)
- **Why:** IoT can't attack your NAS if compromised

#### **VLAN 40 - Guest Network**
- **Purpose:** Visitors, untrusted devices
- **Devices:** Friend's laptops/phones
- **Subnet:** 192.168.40.0/24
- **Firewall Rules:**
  - Allow: Internet access only
  - Deny: All RFC1918 private networks
  - AP Isolation: Enabled (guests can't see each other)
- **Why:** Guests get WiFi without accessing your stuff

#### **VLAN 50 - Security/VPN (Optional)**
- **Purpose:** VPN exit point, secure services
- **Devices:** VPN server, Pi-hole, reverse proxy
- **Subnet:** 192.168.50.0/24
- **Why:** Separate security services from main network

---

### Visual Network Topology

```
                     Internet
                        |
                [Router/Gateway]
              (pfSense/ER605/UDM)
                        |
                        |
          [Core Switch - VLAN Aware]
        (TP-Link SG108E or 2.5GbE Switch)
                        |
        +---------------+----------------+
        |               |                |
   [Servers]        [IoT SW]      [WiFi AP]
   VLAN 20          VLAN 30       Multi-SSID
        |               |                |
   +----+----+     +----+----+      +----+----+
   |         |     |         |      |         |
  NAS    Docker  Cameras   Bulbs  Main    Guest
         Host              WiFi    WiFi
                          VLAN10  VLAN40
```

---

### How to Configure VLANs on TP-Link TL-SG108E (Step-by-Step)

This is the most popular homelab switch, so here's the exact process:

#### **Step 1: Access the Switch**
1. Connect switch to PC via Ethernet
2. Download TP-Link Easy Smart Configuration Utility
3. Find switch IP (usually 192.168.0.1)
4. Login via web browser (admin/admin default)

#### **Step 2: Enable 802.1Q VLAN**
1. Go to **VLAN > 802.1Q VLAN**
2. Click **Enable**
3. Click **Apply**

#### **Step 3: Create VLANs**
1. Go to **VLAN > 802.1Q VLAN > VLAN Config**
2. Create each VLAN:
   - VLAN ID: 10, Name: "Trusted"
   - VLAN ID: 20, Name: "Servers"
   - VLAN ID: 30, Name: "IoT"
   - VLAN ID: 40, Name: "Guest"

#### **Step 4: Assign Ports to VLANs**

Example 8-port setup:
- **Port 1:** TRUNK (to router) - Tagged: 1,10,20,30,40
- **Port 2:** TRUNK (to WiFi AP) - Tagged: 1,10,30,40
- **Port 3:** NAS (VLAN 20) - Untagged: 20
- **Port 4:** Desktop (VLAN 10) - Untagged: 10
- **Port 5:** IoT Device (VLAN 30) - Untagged: 30
- **Port 6:** Server (VLAN 20) - Untagged: 20
- **Port 7:** Available
- **Port 8:** Management (VLAN 1) - Keep your connection!

#### **Step 5: Configure PVID (Important!)**
1. Go to **VLAN > 802.1Q VLAN > Port Config**
2. Set PVID for each port to match its VLAN:
   - Port 3: PVID 20
   - Port 4: PVID 10
   - Port 5: PVID 30
   - Etc.

#### **Step 6: Save Configuration**
1. Go to **System > Save Config**
2. Click **Save** (or changes disappear on reboot!)

#### **Step 7: Configure Router Firewall Rules**

On your pfSense/OPNsense/ER605, create these rules:

**VLAN 10 (Trusted):**
- Allow: All traffic

**VLAN 20 (Servers):**
- Allow: To internet
- Allow: From VLAN 10
- Deny: From VLAN 30, 40

**VLAN 30 (IoT):**
- Allow: To internet (HTTP/HTTPS/DNS only)
- Deny: To RFC1918 (all private IPs)
- Allow: From VLAN 10 (so you can manage IoT)

**VLAN 40 (Guest):**
- Allow: To internet only
- Deny: To RFC1918
- Enable AP isolation

---

### WiFi SSID to VLAN Mapping

Configure your access point to broadcast multiple SSIDs, each tagged to a VLAN:

- **SSID: "HomeNetwork"** → VLAN 10 (Trusted)
- **SSID: "HomeNetwork-Guest"** → VLAN 40 (Guest)
- **SSID: "IoT"** → VLAN 30 (IoT) - Hidden SSID for smart devices

On TP-Link Omada:
1. Go to **Settings > Wireless Networks**
2. Create SSID
3. Enable **VLAN**
4. Enter VLAN ID
5. Apply

---

## Complete Budget Build Configurations

Let me give you three complete setups at different price points...

### Configuration 1: Budget Gigabit Setup ($200 total)

**Best for:** TerraMaster F2-212 or Synology DS223j owners

| Component | Model | Cost | Notes |
|-----------|-------|------|-------|
| Router | TP-Link ER605 Omada | $59.99 | VPN, VLAN support |
| Switch | TP-Link TL-SG108E | $29.99 | 8-port managed, VLANs |
| Access Point | TP-Link EAP225 | $59.99 | WiFi 5, PoE, multiple SSIDs |
| Cables | Cat6 5-pack (3ft) | $15 | Quality cables matter |
| PoE Injector | TP-Link PoE Injector | $15 | Power the AP |
| **Total** | | **~$180** | Room for expansion! |

**What you get:**
- Full VLAN support
- Professional WiFi with guest network
- VPN server capability
- Gigabit speeds (perfect for 1GbE NAS)
- All Omada ecosystem (unified management)

**Setup complexity:** Medium (requires VLAN configuration)

---

### Configuration 2: Performance 2.5GbE Setup ($450 total)

**Best for:** UGREEN DXP2800 owners who want MAX PERFORMANCE

| Component | Model | Cost | Notes |
|-----------|-------|------|-------|
| Router | Mini PC + pfSense | $199 | Protectli FW2B |
| 2.5GbE Switch | TP-Link TL-SG108-M2 | $129 | 8x 2.5GbE unmanaged |
| Gigabit Switch | TP-Link TL-SG108E | $29.99 | For IoT/cameras |
| Access Point | TP-Link EAP650 | $119 | WiFi 6, VLANs |
| Cables | Cat6a 3-pack | $20 | 2.5GbE rated |
| PoE Injector | TP-Link PoE+ | $18 | WiFi 6 AP power |
| **Total** | | **~$515** | Premium performance |

**What you get:**
- 2.5GbE speeds to NAS (280+ MB/s transfers!)
- Separate managed gigabit for IoT/cameras
- Enterprise firewall (pfSense)
- WiFi 6 for future-proofing
- Maximum NAS performance

**Network layout:**
- 2.5GbE switch: NAS, Desktop, Gaming PC, Proxmox server
- Gigabit switch: IoT devices, cameras, printers (with VLANs)
- pfSense handles all VLAN routing and firewall

**Setup complexity:** High (pfSense configuration required)

---

### Configuration 3: UniFi Ecosystem ($600 total)

**Best for:** Users who want the prettiest UI and best management experience

| Component | Model | Cost | Notes |
|-----------|-------|------|-------|
| Router | UniFi Dream Router | $199 | All-in-one gateway |
| Switch | UniFi Flex Mini 2.5G | $49 | 5x 2.5GbE managed |
| Switch | UniFi Flex 5-port | $29 | Gigabit for IoT |
| Access Point | UniFi U6-Pro | $179 | WiFi 6, 2.5GbE uplink |
| Access Point | UniFi U6 Lite | $99 | Second floor coverage |
| Cables | Ubiquiti Cat6 | $25 | Official cables |
| **Total** | | **~$580** | Premium ecosystem |

**What you get:**
- Unified management (one app for everything)
- Beautiful interface
- 2.5GbE for NAS
- Excellent WiFi coverage (two APs)
- Professional-grade reliability

**Setup complexity:** Low (UniFi makes it easy)

**Why this is worth it:**
- Best mobile app management
- Automatic AP roaming
- Best traffic analytics
- Future expansion is seamless

---

## Integrating with Your NAS Setup

Let's talk specifics on how to connect your NAS for maximum performance:

### For TerraMaster F2-212 (1GbE)

**Basic Setup:**
```
[Router] → [TP-Link SG108E Switch] → [TerraMaster NAS]
                  ↓
            [Other Devices]
```

**Configuration:**
- NAS on VLAN 20 (Servers)
- Desktop on VLAN 10 (Trusted)
- Firewall allows VLAN 10 → VLAN 20 access

**Expected speeds:** 110-118 MB/s (full gigabit)

**Pro tip:** Enable jumbo frames on NAS and desktop for 5-10% speed boost:
- NAS: Settings → Network → MTU: 9000
- Desktop: Network adapter settings → MTU: 9000

---

### For UGREEN DXP2800 (2.5GbE)

**Optimal Setup:**
```
[pfSense Router] → [TP-Link 2.5GbE Switch] → [UGREEN DXP2800 NAS]
                          ↓                         ↓
                   [Gaming Desktop]        [Proxmox Server]
                   (2.5GbE NIC)            (2.5GbE NIC)
```

**Required:**
- 2.5GbE switch (TP-Link TL-SG108-M2 or QNAP QSW-1105-5T)
- Desktop/server with 2.5GbE NIC (or USB 3.0 2.5GbE adapter ~$30)
- Cat5e or better cables (Cat6/Cat6a recommended)

**Configuration:**
- NAS: Static IP on VLAN 20
- Desktop: VLAN 10
- 2.5GbE switch unmanaged (just plug in)
- VLANs handled by router

**Expected speeds:** 280-300 MB/s (full 2.5GbE!)

**How to verify you're getting 2.5GbE:**
1. Copy large file from NAS to desktop
2. Watch Task Manager (Windows) or Activity Monitor (Mac)
3. Should see 250-300 MB/s sustained

**If you're only getting 110 MB/s:**
- Check NIC is actually 2.5GbE (not gigabit)
- Verify switch is 2.5GbE
- Check cable is Cat5e minimum
- Disable VPN/antivirus during test

---

### Adding 2.5GbE to Existing Computers

**Desktop PCs:**
- **PCIe 2.5GbE Card:** $25-35
  - Example: ASUS XG-C100C, Realtek RTL8125
  - Plug into PCIe x1 slot
  - Instant 2.5GbE

**Laptops/Mini PCs:**
- **USB 3.0 2.5GbE Adapter:** $30-40
  - Example: Cable Matters USB-C 2.5GbE, TP-Link UE300
  - Plug into USB 3.0 (NOT USB 2.0!)
  - Good compatibility

**Note:** Some older USB 3.0 controllers can't handle full 2.5GbE speeds. Test before buying multiple adapters.

---

## NetworkChuck-Style Projects That Need Good Network Equipment

These are the projects you see on NetworkChuck's channel that REQUIRE proper networking:

### 1. Pi-hole Network-Wide Ad Blocking

**What it needs:**
- DNS server running in Docker
- **Network requirement:** All devices point to Pi-hole for DNS
- **Why good networking matters:**
  - Run Pi-hole on VLAN 50 (security)
  - All VLANs use it for DNS
  - Firewall rules allow DNS from all VLANs

**Setup with VLANs:**
- Pi-hole container on NAS (VLAN 20)
- DHCP gives Pi-hole IP as DNS server
- Works for all VLANs automatically

---

### 2. WireGuard VPN Server

**What it needs:**
- WireGuard container on NAS or router
- **Network requirement:** Port forwarding, split-tunnel routing
- **Why good networking matters:**
  - VPN clients connect to home network remotely
  - Access NAS, Plex, home automation from anywhere
  - pfSense/OPNsense make this EASY with GUI

**Best setup:**
- Run on pfSense/OPNsense router (not NAS)
- Hardware VPN acceleration = fast speeds
- Split tunnel: Route only home network traffic through VPN

---

### 3. Plex Media Server with Remote Access

**What it needs:**
- Plex running on NAS
- **Network requirement:** Port forwarding (32400), QoS for streaming
- **Why good networking matters:**
  - QoS prioritizes Plex traffic
  - VLANs isolate Plex from IoT
  - 2.5GbE = stream 4K locally without buffering

**Optimal config:**
- Plex on NAS (VLAN 20)
- Clients on VLAN 10
- QoS rule: Prioritize port 32400 traffic
- 2.5GbE for local 4K streaming

---

### 4. Home Assistant Smart Home Hub

**What it needs:**
- Home Assistant container
- **Network requirement:** Access to IoT VLAN, secure from internet
- **Why good networking matters:**
  - HA needs to control IoT devices (VLAN 30)
  - But shouldn't expose IoT to main network
  - Firewall rules: HA (VLAN 20) → IoT (VLAN 30), but not reverse

**Setup:**
- Home Assistant on NAS (VLAN 20)
- Firewall exception: VLAN 20 can access VLAN 30
- IoT devices controlled but isolated

---

### 5. Nextcloud Personal Cloud Storage

**What it needs:**
- Nextcloud container on NAS
- **Network requirement:** Reverse proxy, SSL certificate, remote access
- **Why good networking matters:**
  - Nginx Proxy Manager container handles SSL
  - Port 80/443 forwarding
  - VPN access alternative to exposing to internet

**Two approaches:**
1. **Public access:** Reverse proxy + SSL + Cloudflare
2. **VPN-only:** WireGuard → access Nextcloud internally

---

### 6. Game Servers (Minecraft, Valheim, etc.)

**What it needs:**
- Game server container on NAS/server
- **Network requirement:** Port forwarding, low latency
- **Why good networking matters:**
  - QoS prevents game lag
  - VLAN isolation protects main network
  - Friends connect without accessing NAS files

**Best practice:**
- Game server on VLAN 20
- Port forward ONLY game port (e.g., 25565 for Minecraft)
- QoS high priority for game traffic

---

### 7. Docker Portainer for Container Management

**What it needs:**
- Portainer container
- **Network requirement:** Web access on port 9000
- **Why good networking matters:**
  - Manage all containers from one dashboard
  - Accessible from VLAN 10 (trusted devices only)
  - Not exposed to IoT or guest networks

---

### 8. Network Monitoring with Grafana + Prometheus

**What it needs:**
- Grafana + Prometheus containers
- **Network requirement:** SNMP access to switches, routers
- **Why good networking matters:**
  - Monitor bandwidth usage per VLAN
  - Track network device health
  - Alert on issues

**This is COOL:**
- See which devices use most bandwidth
- Monitor NAS performance
- Get alerts when internet goes down

---

## Upgrade Paths & Future-Proofing

### Year 1: Foundation ($200-$300)

**Start here:**
- ISP router (free, existing)
- TP-Link TL-SG108E gigabit managed switch ($30)
- TP-Link EAP225 access point ($60)
- Basic VLAN setup

**What you can do:**
- Run Docker containers
- Set up Plex
- IoT segregation
- Guest WiFi

---

### Year 2: Performance Upgrade ($300-$400)

**Add these:**
- pfSense/OPNsense router ($150-$200)
- 2.5GbE switch for NAS/desktop ($109-$129)
- Keep gigabit switch for IoT

**What you gain:**
- Enterprise firewall
- VPN server
- 2.5x faster NAS speeds
- Advanced traffic shaping

---

### Year 3: Expansion ($200-$400)

**Expand with:**
- Second WiFi AP for coverage ($99-$179)
- Managed 2.5GbE PoE switch ($379)
- 10GbE NIC for main server ($80-$100)
- More advanced projects

**What you can do:**
- Whole-home WiFi coverage
- More Docker containers
- Proxmox cluster
- 10GbE backbone

---

### Future-Proofing Checklist

When buying TODAY, choose gear that supports:

**Protocols/Standards:**
- [ ] 802.1Q VLAN support (essential)
- [ ] Gigabit minimum, 2.5GbE preferred
- [ ] WiFi 6 for access points
- [ ] PoE (802.3af/at) for APs
- [ ] IPv6 support (it's coming, I promise)

**Hardware:**
- [ ] Fanless switches (run 24/7 silently)
- [ ] Metal chassis (better cooling, durability)
- [ ] Rackmount option (if you'll get a rack)
- [ ] SFP+ uplink ports (10G expansion)

**Ecosystem:**
- [ ] Active community support
- [ ] Regular firmware updates
- [ ] Good documentation
- [ ] Compatible with open-source software

---

## Common Mistakes to Avoid

Let me save you from the mistakes I see all the time:

### Mistake 1: Buying 2.5GbE Switch Without 2.5GbE Devices
**The Problem:** You buy a $129 2.5GbE switch but your NAS and desktop are gigabit.
**The Fix:** Upgrade devices FIRST, then upgrade switch.

### Mistake 2: Ignoring Cable Quality
**The Problem:** Using 20-year-old Cat5 cables, wondering why 2.5GbE doesn't work.
**The Fix:** Buy Cat6/Cat6a cables. They're $2 each. Don't skimp.

### Mistake 3: Forgetting PoE for Access Points
**The Problem:** Buy AP, realize it needs PoE, don't have PoE switch.
**The Fix:** Budget $15-20 for PoE injector OR buy PoE switch from start.

### Mistake 4: Locking Into One Ecosystem Too Early
**The Problem:** Buy one UniFi AP, feel forced to buy all UniFi gear.
**The Fix:** Start with open standards (TP-Link Omada, Ubiquiti, or standalone gear).

### Mistake 5: Not Saving Switch Configurations
**The Problem:** Spend 2 hours configuring VLANs, switch reboots, all gone.
**The Fix:** ALWAYS save config to flash/NVRAM after changes!

### Mistake 6: Configuring VLANs While Connected to Port You're Changing
**The Problem:** Change port 5 to VLAN 30, you're connected on port 5, lose access.
**The Fix:** Always leave port 8 (or last port) on VLAN 1 for management.

### Mistake 7: No Firewall Rules Between VLANs
**The Problem:** Create VLANs but all devices can still talk to each other.
**The Fix:** Configure firewall rules on router. VLANs alone don't block traffic!

---

## Recommended Retailers & Where to Buy

### United States

**Best for everything:**
- **B&H Photo Video** - No tax (outside NY), great customer service
- **Amazon** - Fast shipping, easy returns, Prime deals
- **Newegg** - Good tech selection, frequent sales

**Best for networking:**
- **Micro Center** - In-store pickup, excellent selection (limited locations)
- **ui.com** - Official Ubiquiti store (UniFi gear)
- **TP-Link Store** - Direct from manufacturer

**Best for cables:**
- **Monoprice** - Cheap, quality cables
- **Cable Matters** - Good balance of price/quality

### Shopping Tips

**When to buy:**
- **Black Friday** (late November) - 20-40% off switches/APs
- **Prime Day** (July) - 15-30% off networking
- **Back to School** (August) - Good deals on TP-Link

**Price alerts:**
- Use CamelCamelCamel for Amazon tracking
- Set alerts at 20% below current price
- Don't wait too long - some deals are rare

---

## Detailed Product Comparison Tables

### Router/Gateway Comparison

| Model | Type | WAN Speed | VPN | VLANs | Price | Best For |
|-------|------|-----------|-----|-------|-------|----------|
| ISP Router | Consumer | 1Gbps | No | Limited | $0 | Starting out |
| TP-Link ER605 | Prosumer | 1Gbps | Yes (HW accel) | Unlimited | $59.99 | Budget VLAN setup |
| PC Engines APU2E4 | DIY | 1Gbps | Yes | Unlimited | $179 | pfSense enthusiasts |
| Protectli FW2B | DIY | 1Gbps | Yes | Unlimited | $199 | Serious homelab |
| UniFi Dream Router | All-in-one | 1Gbps | Yes | Unlimited | $199 | UniFi ecosystem entry |
| UniFi Dream Machine SE | Premium | 10Gbps | Yes | Unlimited | $499 | Professional setup |

### Switch Comparison (Gigabit)

| Model | Ports | Managed | VLAN | PoE | Fan | Price | Best For |
|-------|-------|---------|------|-----|-----|-------|----------|
| TP-Link TL-SG105 | 5 | No | No | No | No | $19.99 | Basic expansion |
| TP-Link TL-SG108E | 8 | Smart | Yes | No | No | $29.99 | Budget VLAN |
| Netgear GS308T | 8 | Full | Yes | No | No | $59.99 | Better features |
| TP-Link TL-SG2008 | 8 | Smart+ | Yes | No | No | $72.99 | Advanced homelab |

### Switch Comparison (2.5GbE)

| Model | Ports | Speed | Managed | VLAN | PoE | SFP+ | Price | Best For |
|-------|-------|-------|---------|------|-----|------|-------|----------|
| QNAP QSW-1105-5T | 5 | 2.5GbE | No | No | No | No | $108 | Budget 2.5GbE |
| TP-Link TL-SG108-M2 | 8 | 2.5GbE | No | No | No | No | $129 | Best value 2.5GbE |
| TRENDnet TEG-S380 | 8 | 2.5GbE | No | No | No | No | $179 | More ports |
| Zyxel XMG-108 | 8+1 | 2.5GbE + 10G | No | No | No | Yes (1) | $199 | 10G uplink |
| TP-Link SG3210XP-M2 | 8+2 | 2.5GbE + 10G | Yes | Yes | Yes | Yes (2) | $379 | Premium managed |

### Access Point Comparison

| Model | WiFi | Speed | PoE | VLAN SSIDs | Management | Price | Best For |
|-------|------|-------|-----|------------|------------|-------|----------|
| TP-Link EAP225 | WiFi 5 | 1350Mbps | Yes | Yes | Omada | $59.99 | Budget professional |
| TP-Link EAP650 | WiFi 6 | 3000Mbps | Yes | Yes | Omada | $119 | WiFi 6 value |
| UniFi U6 Lite | WiFi 6* | 1500Mbps | Yes | Yes | UniFi | $99 | UniFi entry |
| UniFi U6-Pro | WiFi 6 | 4800Mbps | Yes | Yes | UniFi | $179 | Premium WiFi 6 |

*2.4GHz is WiFi 4 only

---

## Maintenance & Management

### Weekly Tasks (5 minutes)

- [ ] Check router uptime (should be weeks/months)
- [ ] Verify internet speed (speedtest.net)
- [ ] Check for firmware updates (but don't apply yet)

### Monthly Tasks (30 minutes)

- [ ] Review DHCP leases (unknown devices?)
- [ ] Check switch port utilization
- [ ] Backup router/switch configurations
- [ ] Review firewall logs for blocks
- [ ] Update firmware if critical patches

### Quarterly Tasks (1-2 hours)

- [ ] Full network documentation review
- [ ] Test backup configuration restore
- [ ] Review and optimize firewall rules
- [ ] Check for new firmware features
- [ ] Verify VLAN isolation still working

### Annual Tasks (3-4 hours)

- [ ] Full network audit
- [ ] Replace any failing hardware
- [ ] Document all changes from past year
- [ ] Consider upgrade path for next year
- [ ] Test disaster recovery procedures

---

## Troubleshooting Common Issues

### Problem: Can't Access Devices on Different VLANs

**Symptoms:** Desktop (VLAN 10) can't reach NAS (VLAN 20)

**Cause:** Missing firewall rules or incorrect VLAN tagging

**Fix:**
1. Verify firewall rules allow VLAN 10 → VLAN 20
2. Check PVID is set correctly on switch ports
3. Verify trunk port has both VLANs tagged
4. Test with firewall rules disabled (temporarily!)

---

### Problem: 2.5GbE Not Working (Only Getting Gigabit Speeds)

**Symptoms:** Transfer speeds stuck at 110-120 MB/s instead of 250-300 MB/s

**Cause:** One device in chain is only gigabit

**Checklist:**
- [ ] NIC is actually 2.5GbE (check device manager/specs)
- [ ] Switch is 2.5GbE model
- [ ] Cable is Cat5e or better
- [ ] Both source and destination are 2.5GbE
- [ ] No gigabit device in middle (check switch cascade)

**How to verify link speed:**
- Windows: Device Manager → Network Adapter → Properties → Link Speed
- Mac: Option+Click WiFi icon → shows connection speed
- Linux: `ethtool eth0` → Speed

---

### Problem: VLANs Work Wired, Not Working on WiFi

**Symptoms:** VLAN segregation works on switch but not WiFi

**Cause:** Access point not configured for VLAN tagging

**Fix:**
1. Access point MUST support multiple SSIDs with VLAN tags
2. Configure each SSID with VLAN ID
3. Trunk port from switch to AP must have all VLANs tagged
4. Some consumer APs don't support this (need Omada/UniFi)

---

### Problem: Switch Losing Configuration on Reboot

**Symptoms:** VLANs work, reboot switch, back to defaults

**Cause:** Configuration not saved to non-volatile memory

**Fix:**
- TP-Link: System → Save Config → Save
- Look for "Save to Startup Config" or similar
- Some switches auto-save, others don't

---

### Problem: Slow WiFi Speeds Despite Good Signal

**Symptoms:** -40dBm signal but only 50Mbps speed

**Common causes:**
- WiFi channel congestion (use WiFi analyzer app)
- AP on 2.4GHz instead of 5GHz
- Client device WiFi limitation
- Too many clients on one AP

**Fixes:**
- Change WiFi channel (1, 6, or 11 for 2.4GHz)
- Force clients to 5GHz band
- Add second AP for capacity
- Enable band steering on AP

---

## Final Recommendations Summary

### If You Have TerraMaster F2-212 or Synology DS223j (1GbE NAS):

**Minimum Setup ($110):**
- TP-Link TL-SG108E ($30) - managed gigabit switch
- TP-Link EAP225 ($60) - professional WiFi
- Keep existing router for now

**Recommended Setup ($230):**
- TP-Link ER605 ($60) - prosumer router
- TP-Link TL-SG108E ($30) - managed switch
- TP-Link EAP650 ($119) - WiFi 6 AP
- PoE injector ($18)

**Why:** Your NAS is gigabit, so focus budget on good management (VLANs) and WiFi 6.

---

### If You Have UGREEN DXP2800 (2.5GbE NAS):

**Minimum Setup ($237):**
- QNAP QSW-1105-5T ($108) - 2.5GbE switch
- TP-Link TL-SG108E ($30) - gigabit for IoT
- TP-Link EAP650 ($119) - WiFi 6

**Recommended Setup ($515):**
- Protectli FW2B + pfSense ($199) - enterprise router
- TP-Link TL-SG108-M2 ($129) - 8-port 2.5GbE
- TP-Link TL-SG108E ($30) - gigabit for IoT
- TP-Link EAP650 ($119) - WiFi 6
- PoE injector ($18)
- Quality Cat6a cables ($20)

**Why:** Unlock that 2.5GbE performance! The UGREEN is capable of 280+ MB/s, don't bottleneck it with gigabit switches.

---

### If You Want the Best Management Experience:

**UniFi Setup ($580):**
- UniFi Dream Router ($199)
- UniFi Flex Mini 2.5G ($49)
- UniFi U6-Pro ($179)
- Additional U6 Lite ($99) for coverage
- Cables ($25)

**Why:** Best UI, mobile app, traffic analytics, and seamless ecosystem.

---

## My Top Pick for Most People

If I had to choose ONE setup for 80% of homelab users:

**The Balanced Build ($260)**

- **Router:** TP-Link ER605 Omada - $59.99
- **2.5GbE Switch:** QNAP QSW-1105-5T - $108
- **Gigabit Switch:** TP-Link TL-SG108E - $29.99
- **Access Point:** TP-Link EAP225 - $59.99
- **PoE Injector:** TP-Link - $15

**Why this is perfect:**
- 2.5GbE for devices that need it (NAS, desktop)
- Managed gigabit for IoT with VLANs
- Professional WiFi with guest network
- VPN server capability
- Omada ecosystem (unified management)
- Leaves budget for 2.5GbE NIC upgrade ($30)

**What you can run:**
- All NetworkChuck projects
- Full VLAN segmentation
- Fast NAS access
- Professional WiFi
- VPN server

---

## Next Steps - Your Action Plan

Here's exactly what to do RIGHT NOW:

### Step 1: Assess Your Current Setup (15 minutes)
- [ ] What router do you have? (ISP provided or purchased?)
- [ ] What switch do you have? (Managed or unmanaged?)
- [ ] How many devices need wired connections?
- [ ] What's your NAS network speed? (1GbE or 2.5GbE?)
- [ ] Do you need WiFi upgrade? (Current coverage good enough?)

### Step 2: Set Your Budget (5 minutes)
- [ ] Minimum: $100-$200
- [ ] Recommended: $200-$400
- [ ] Premium: $400-$600+

### Step 3: Choose Your Configuration (10 minutes)
Pick one of the builds from this guide based on:
- Your NAS specs (from nas_rec.md)
- Your budget
- Your technical comfort level

### Step 4: Buy the Gear (1-2 weeks)
- [ ] Set price alerts on Amazon/B&H
- [ ] Wait for deals (Black Friday is NOW!)
- [ ] Buy in phases if needed (router first, then switches, then APs)

### Step 5: Install and Configure (4-8 hours)
- [ ] Physical installation (easy)
- [ ] Basic configuration (medium)
- [ ] VLAN setup (medium-hard)
- [ ] Firewall rules (hard)
- [ ] Testing (easy but important)

### Step 6: Deploy NetworkChuck Projects (ongoing)
- [ ] Pi-hole ad blocking
- [ ] Plex media server
- [ ] WireGuard VPN
- [ ] Home Assistant
- [ ] Docker containers
- [ ] And MANY more!

---

## Learning Resources

### YouTube Channels
- **NetworkChuck** - The GOAT for homelab projects
- **Craft Computing** - Excellent server/networking content
- **Lawrence Systems** - Deep dives on pfSense, networking
- **TechnoTim** - Kubernetes, Docker, homelabs
- **Hardware Haven** - NAS reviews, networking

### Websites & Forums
- **r/homelab** (Reddit) - Amazing community
- **r/pfSense** (Reddit) - pfSense help
- **ServeTheHome** - Enterprise gear reviews
- **HomeTechHacker** - Practical guides
- **Home Network Guy** - Configuration tutorials

### Documentation
- **pfSense Docs** - pfsense.org/docs
- **TP-Link Omada** - omada.tp-link.com
- **UniFi Help** - help.ui.com
- **Netgate Docs** - docs.netgate.com

---

## Conclusion

Look, here's the thing - networking is the FOUNDATION of your homelab. You can have the most powerful NAS, the best server, the coolest containers, but if your network is trash, EVERYTHING runs like trash.

Invest in good networking gear. Start small if you need to, but start with QUALITY. A $30 managed switch teaches you VLANs. A $60 router gives you VPN. A $100 access point gives you professional WiFi.

And the best part? This gear will last you YEARS. I'm talking 5-7 years of reliable service. That $260 balanced build? That's $3.70 per month over 6 years. Your COFFEE costs more than that!

So grab your coffee, pick a configuration from this guide, and let's BUILD something awesome. Your homelab is waiting. Let's GO!

---

## Sources & References

### Network Equipment Research
- [A cheap 2.5GbE managed switch was one of the best home networking upgrades I've made](https://www.xda-developers.com/cheap-2-5-gbe-managed-switch-best-home-networking-upgrades/)
- [The Ultimate Cheap Fanless 2.5GbE Switch Buyers Guide](https://www.servethehome.com/the-ultimate-cheap-2-5gbe-switch-mega-round-up-buyers-guide-qnap-netgear-hasivo-mokerlink-trendnet-zyxel-tp-link/)
- [Best Network Switches for Homelabs (2025 Guide)](https://subnetsavy.com/wp-content/uploads/articles/best-network-switches-homelab-2025.html)
- [Best 2.5Gb Switches to Use in 2025 - WunderTech](https://www.wundertech.net/which-2-5gb-switch-should-you-use/)
- [Ultimate Guide to Building a 2.5GbE Home Lab Network in 2025](https://www.virtualizationhowto.com/2025/04/ultimate-guide-to-building-a-2-5gbe-home-lab-network-in-2025/)
- [How I Chose the Best Managed Network Switch for My Home Lab](https://linuxblog.io/best-managed-switch-home-lab/)

### Router & Gateway Research
- [7 Great Choices for OPNsense Hardware](https://hometechhacker.com/great-choices-for-opnsense-hardware/)
- [OPNsense Hardware Recommendations (2025)](https://homenetworkguy.com/review/opnsense-hardware-recommendations/)
- [11 Great Choices for pfSense Hardware](https://hometechhacker.com/11-great-choices-for-pfsense-hardware/)
- [Best pfSense Hardware for Home/SOHO/Business](https://www.zenarmor.com/docs/network-security-tutorials/best-pfsense-hardware-for-home-soho-business)
- [How to Build a Low-Cost Lab Network with Ubiquiti UniFi (2025 Guide)](https://subnetsavy.com/wp-content/uploads/articles/unifi-homelab-network-guide.html)

### Access Point Research
- [Best Homelab Networking Ecosystem](https://www.virtualizationhowto.com/2025/02/best-homelab-networking-ecosystem/)
- [Ubiquiti U6-Pro vs. TP-Link EAP670 WiFi 6 Access Points](https://aceperipherals.com/blogs/news/ubiquiti-u6-pro-vs-tp-link-eap670-top-ax5400-wifi-6-access-points-compared)
- [UniFi Wi-Fi Access Point Buyers Guide](https://evanmccann.net/blog/2021/1/unifi-ap-guide)

### VLAN Configuration
- [Home Lab Networking 101: VLANs, Subnets, and Segmentation for Beginners](https://www.virtualizationhowto.com/2025/10/home-lab-networking-101-vlans-subnets-and-segmentation-for-beginners/)
- [VLANs and Traffic Segmentation for Your Homelab](https://excalibursheath.com/guide/2025/06/15/vlans-traffic-segmentation.html)
- [How to Configure VLANs on a TP-Link Managed Switch](https://homenetworkguy.com/how-to/configure-vlans-tp-link-switch/)
- [How to configure 802.1Q VLAN on TP-Link Smart and Managed Switches](https://www.tp-link.com/us/support/faq/2149/)
- [VLANs for the Homelab: A beginner's guide to segmenting networks](https://liore.com/vlans-for-the-homelab-a-beginners-guide-to-segmenting-networks/)

### Pricing & Product Info
- [QNAP QSW-1105-5T 2.5GbE Switch Hardware Review](https://nascompares.com/2020/11/04/qnap-qsw-1105-5t-2-5gbe-switch-hardware-review/amp/)
- [TRENDnet TEG-S380 8-port 2.5GbE Switch Review](https://www.servethehome.com/trendnet-teg-s380-8-port-2-5gbe-switch-review/2/)
- [Amazon - Network Equipment](https://www.amazon.com)
- [Ubiquiti Store - Official](https://store.ui.com)
- [B&H Photo Video](https://www.bhphotovideo.com)

---

**Document Version:** 1.0
**Last Updated:** November 23, 2025
**Companion Document:** [nas_rec.md](nas_rec.md)
**Next Review:** February 2026 (post-Black Friday updates)

**Created with:** NetworkChuck energy and way too much coffee ☕
