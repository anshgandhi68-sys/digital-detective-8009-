# Mission 07 — Networking

## Goal

Learn the main networking ideas, look at the real network information on my Mac, and explain step by step what happens when I open a website.

## Task 7.1 — Key ideas

| Concept | What it is | Example from my life |
|---|---|---|
| **LAN** (Local Area Network) | A network that covers a small area, like one home, school or office | My MacBook, phone and smart TV all on our home Wi-Fi |
| **MAN** (Metropolitan Area Network) | A network across a city, linking many LANs | A city's cable broadband network, or a college with campuses across one city |
| **WAN** (Wide Area Network) | A network across countries or the whole world | The internet is the biggest WAN |
| **IP address** | The number that identifies a device on a network | My Mac's local address starts with `10.` (see 7.2) |
| **DNS** (Domain Name System) | Turns names like `example.com` into IP addresses | `nslookup example.com` → `104.20.23.154` |
| **Router** | Forwards data between networks; connects my LAN to the internet | My Wi-Fi router is the first hop in `traceroute` |
| **Protocol** | Agreed rules for how devices talk | HTTP/HTTPS for web pages, TCP/IP for moving the data, DNS for names |
| **Packet switching** | Data is split into small packets that can take different routes and get put back together at the end | `ping` sends 4 separate packets and times each one |
| **Client–server** | A client asks for something and a server answers | Safari (client) asks example.com's server for a page |

## Task 7.2 — My network, observed

### My device on the LAN

```text
$ ipconfig getifaddr en0
10.108.x.x                  # my Mac's private address on Wi-Fi (en0)

$ route -n get default
    gateway: 10.108.204.1   # my router
  interface: en0

$ scutil --dns | grep nameserver
  nameserver[0] : 8.8.8.8   # DNS servers my Mac asks
  nameserver[1] : 8.8.4.4
```

I hid the last part of my own address because this repo is public. `10.x.x.x` addresses are **private**: they only work inside my local network, and the router translates them for the internet.

### DNS lookup

```text
$ nslookup example.com
Non-authoritative answer:
Name:    example.com
Address: 172.66.147.243
Name:    example.com
Address: 104.20.23.154
```

`example.com` has **two** IP addresses. Big sites use several servers so that if one fails, the others keep working.

### Ping

```text
$ ping -c 4 example.com
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 11.411/22.723/55.169/18.735 ms
```

- 0% packet loss means every packet made it there and back.
- The fastest round trip was about **11 ms** and the slowest about **55 ms**. Each packet is sent separately, so they don't all take the same time (packet switching).

### Traceroute (the path my packets take)

```text
$ traceroute -m 6 example.com
 1  10.108.204.1        3.3 ms    <- my router (leaving my LAN)
 2  <my ISP>            5.4 ms    <- my internet provider
 3  *
 4  *                             <- routers that don't reply to traceroute
 5  *
 6  <my ISP>           73.3 ms
```

Hop 1 is my own router. After that the packets go into my internet provider's network and on towards the website. Some routers don't answer traceroute requests, which is why some lines show `*`.

### Talking to the web server

```text
$ curl -sI https://example.com
HTTP/2 200
content-type: text/html; charset=utf-8
server: cloudflare
```

`200` means "OK, here's the page". The `charset=utf-8` part is the same UTF-8 encoding from Mission 05.

## Task 7.3 — What happens when I open a website

When I type `https://example.com` into Safari and press Enter:

1. **Input:** Safari reads the address I typed.
2. **DNS lookup:** My Mac asks its DNS server (8.8.8.8), "what's the IP for example.com?" and gets back `104.20.23.154`. (If it looked it up recently, it uses the saved answer.)
3. **Through my LAN:** The request goes from my Mac over Wi-Fi to my router (`10.108.204.1`).
4. **Out to the WAN:** The router sends it to my internet provider, and from there it's passed from router to router across the internet towards the server.
5. **TCP connection:** My Mac and the server agree to start a reliable connection.
6. **TLS (the "S" in HTTPS):** They agree on encryption keys, so nobody in between can read or change the data.
7. **HTTP request:** Safari (the **client**) sends `GET /`, which means "please send me the homepage".
8. **HTTP response:** The **server** replies `200 OK` with the HTML.
9. **Packets:** The page arrives split into packets, and my Mac puts them back in the right order.
10. **Output:** Safari reads the HTML, fetches any images or styles it needs, and draws the page on my screen.

All of that usually takes less than a second.

```text
[My Mac] --Wi-Fi--> [Router] --> [ISP] --> ... internet routers ... --> [example.com server]
   ^                                                                         |
   +-------------------------- web page comes back --------------------------+
```

## Commands used

`ipconfig getifaddr en0`, `route -n get default`, `scutil --dns`, `nslookup`, `ping -c 4`, `traceroute -m 6`, `curl -sI`

## What I understood

Before this I just thought of "the internet" as one thing. Now I can see the layers: my Mac is on a small LAN, the router is the door out of it, and from there my data hops through many routers across a huge WAN until it reaches the server.

DNS was the part I hadn't thought about. Computers don't use names like `example.com` at all. Every visit starts with a lookup to turn the name into an IP address, and the commands showed that one name can even have two addresses.

Protocols are what make it all work. DNS, TCP, TLS and HTTP each do one job, and because every device follows the same rules, my Mac can talk to a server it has never seen before.

## Problems I ran into

- **Problem:** `traceroute` showed several lines of `*` and I thought the internet was broken.
  **Fix:** Some routers are set to ignore traceroute requests. The trace carried on after them, so the connection was fine.
- **Problem:** I wasn't sure it was safe to put my IP address in a public repo.
  **Fix:** My `10.x` address is private and only works on my LAN, but I still hid part of it, and left out my provider's details from the traceroute.

## Evidence

- Command output is copied into the code blocks above (private addresses partly hidden)
